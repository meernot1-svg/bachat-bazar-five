#!/usr/bin/env python3
"""Search images for the most important products (featured/trending/bestSeller)."""
import subprocess, json, re, os, time

DATA_FILE = "/home/z/my-project/src/lib/data.ts"
PROGRESS_FILE = "/home/z/my-project/img_results/product_images_progress.json"

def search_images(query, count=3):
    try:
        result = subprocess.run(
            ["z-ai", "image-search", "-q", query, "--count", str(count), "--no-rank"],
            capture_output=True, text=True, timeout=120
        )
        output = result.stdout or result.stderr
        if '{' not in output: return []
        start = output.index('{')
        end = output.rindex('}') + 1
        data = json.loads(output[start:end])
        if data.get("success") and data.get("results"):
            return [r["original_url"] for r in data["results"]]
    except: pass
    return []

# Load progress
progress = json.load(open(PROGRESS_FILE)) if os.path.exists(PROGRESS_FILE) else {}

# Find important products that need images
with open(DATA_FILE) as f:
    content = f.read()

todo = []
for line in content.split('\n'):
    m = re.match(r"\s*P\((\d+),'([^']+)'", line)
    if not m: continue
    pid = int(m.group(1))
    name = m.group(2)
    # Only target featured/trending/bestSeller
    if not any(t in line for t in ['featured:true', 'trending:true', 'bestSeller:true']): continue
    # Skip if already has images
    if str(pid) in progress and progress[str(pid)]: continue
    
    # Build simple query
    words = []
    for w in name.split():
        if re.match(r'^[A-Z]{1,3}-?\d', w): continue
        if w.lower() in ('with','for','and','the','pcs','set','of','in','to','&','pack','piece','pieces','all','new','best','premium','high','quality','free','fast','original','genuine','non','plus','size','ml','kg','cm','inch','pack','pro','max','mini','large','small','medium','double','single','multi','wide','long','short','black','white','red','blue','green','pink','gold','grey','brown','silver','purple','yellow','men','women','kids','baby','boys','girls'): continue
        if len(w) < 3: continue
        words.append(w)
        if len(words) >= 4: break
    query = ' '.join(words) if words else name[:40]
    todo.append((pid, name, query))

print(f"Important products needing images: {len(todo)}", flush=True)

for i, (pid, name, query) in enumerate(todo):
    print(f"[{i+1}/{len(todo)}] P{pid}: {query[:50]}", end=" ", flush=True)
    urls = search_images(query, 3)
    if urls:
        progress[str(pid)] = urls
        print(f"OK ({len(urls)})", flush=True)
    else:
        print("FAIL", flush=True)
    
    if (i + 1) % 5 == 0:
        with open(PROGRESS_FILE, 'w') as f:
            json.dump(progress, f)
    time.sleep(4)

with open(PROGRESS_FILE, 'w') as f:
    json.dump(progress, f)

print(f"\nDone! Total with images: {sum(1 for v in progress.values() if v)}")

# Now re-run the final assignment to update data.ts
print("\nRunning final assignment...")
exec(open('/home/z/my-project/scripts/final_image_assignment.py').read())