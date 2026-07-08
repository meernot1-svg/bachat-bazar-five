#!/usr/bin/env python3
"""Search product images with simpler queries and longer delays for remaining products."""
import subprocess, json, re, os, time, sys

DATA_FILE = "/home/z/my-project/src/lib/data.ts"
PROGRESS_FILE = "/home/z/my-project/img_results/product_images_progress.json"

def extract_products():
    with open(DATA_FILE) as f:
        content = f.read()
    products = []
    for line in content.split('\n'):
        m = re.match(r"\s*P\((\d+),'([^']+)'", line)
        if m:
            pid = int(m.group(1))
            name = m.group(2)
            # Simple query: first 3-4 meaningful words only
            words = []
            for w in name.split():
                if re.match(r'^[A-Z]{1,3}-?\d', w): continue
                if w.lower() in ('with','for','and','the','pcs','set','kit','of','in','to','&','pack','piece','pieces','all','new','best','premium','high','quality','free','fast','original','genuine'): continue
                if len(w) < 3: continue
                words.append(w)
                if len(words) >= 3: break
            query = ' '.join(words) if words else name.split(' with ')[0][:40]
            products.append((pid, name, query))
    return products

def search_images(query, count=3):
    try:
        result = subprocess.run(
            ["z-ai", "image-search", "-q", query, "--count", str(count), "--no-rank"],
            capture_output=True, text=True, timeout=120
        )
        output = result.stdout
        if not output.strip():
            output = result.stderr
        if '{' not in output:
            return []
        start = output.index('{')
        end = output.rindex('}') + 1
        data = json.loads(output[start:end])
        if data.get("success") and data.get("results"):
            return [r["original_url"] for r in data["results"]]
    except Exception as e:
        pass
    return []

def main():
    products = extract_products()
    progress = json.load(open(PROGRESS_FILE)) if os.path.exists(PROGRESS_FILE) else {}
    
    # Find products that need images (either missing or failed)
    todo = []
    for pid, name, query in products:
        key = str(pid)
        if key not in progress or not progress[key]:
            todo.append((pid, name, query))
    
    print(f"Need images for {len(todo)} products (of {len(products)} total)", flush=True)
    print(f"Already have: {sum(1 for v in progress.values() if v)}", flush=True)
    
    for i, (pid, name, query) in enumerate(todo):
        print(f"[{i+1}/{len(todo)}] P{pid}: {query[:50]}", end=" ", flush=True)
        urls = search_images(query, 3)
        
        if urls:
            progress[str(pid)] = urls
            print(f"OK ({len(urls)})", flush=True)
        else:
            progress[str(pid)] = []
            print("FAIL", flush=True)
        
        if (i + 1) % 3 == 0:
            with open(PROGRESS_FILE, 'w') as f:
                json.dump(progress, f)
        
        time.sleep(5)
    
    with open(PROGRESS_FILE, 'w') as f:
        json.dump(progress, f)
    
    success = sum(1 for v in progress.values() if v)
    print(f"\nDone! {success}/{len(products)} products have images")

if __name__ == "__main__":
    main()