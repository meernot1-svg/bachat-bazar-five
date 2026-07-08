#!/usr/bin/env python3
"""
Search product-specific images for each product by name.
Processes in chunks, saves progress incrementally.
"""
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
            # Extract key search terms from product name
            # Take first 8-10 meaningful words, remove model numbers
            words = name.split()
            # Remove words that are just model numbers (alphanumeric codes)
            search_terms = []
            for w in words:
                # Skip pure model numbers like FT-905, BLD-339, FR-2105
                if re.match(r'^[A-Z]{1,3}-?\d{2,5}$', w):
                    continue
                if w.lower() in ('with', 'for', 'and', 'the', 'pcs', 'set', 'kit', 'of', 'in', 'to', '&'):
                    continue
                search_terms.append(w)
                if len(search_terms) >= 6:
                    break
            query = ' '.join(search_terms)
            if not query:
                query = name.split(' with ')[0].split(' for ')[0].split(' - ')[0][:50]
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
        start = output.index('{')
        end = output.rindex('}') + 1
        data = json.loads(output[start:end])
        if data.get("success") and data.get("results"):
            return [r["original_url"] for r in data["results"]]
    except Exception as e:
        print(f"  ERR: {e}", flush=True)
    return []

def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE) as f:
            return json.load(f)
    return {}

def save_progress(progress):
    with open(PROGRESS_FILE, 'w') as f:
        json.dump(progress, f, indent=2)

def main():
    products = extract_products()
    print(f"Total products: {len(products)}", flush=True)
    
    progress = load_progress()
    done_count = len(progress)
    print(f"Already done: {done_count}", flush=True)
    
    # Process only remaining products
    remaining = [(pid, name, query) for pid, name, query in products if str(pid) not in progress]
    print(f"Remaining: {len(remaining)}", flush=True)
    
    batch_num = 0
    for i, (pid, name, query) in enumerate(remaining):
        print(f"[{done_count + i + 1}/{len(products)}] P{pid}: {query[:50]}...", flush=True)
        urls = search_images(query, 3)
        
        if urls:
            progress[str(pid)] = urls
            print(f"  Got {len(urls)} images", flush=True)
        else:
            progress[str(pid)] = []
            print(f"  NO RESULTS", flush=True)
        
        # Save progress every 5 products
        if (i + 1) % 5 == 0:
            save_progress(progress)
            print(f"  [Progress saved: {len(progress)}/{len(products)}]", flush=True)
        
        time.sleep(3)  # Rate limit
    
    # Final save
    save_progress(progress)
    
    success = sum(1 for v in progress.values() if v)
    print(f"\nDone! {success}/{len(products)} products have images")
    
    # Show summary
    missing = [pid for pid, urls in progress.items() if not urls]
    if missing:
        print(f"Missing images for {len(missing)} products: {missing[:20]}...")

if __name__ == "__main__":
    main()