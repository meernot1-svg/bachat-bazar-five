#!/usr/bin/env python3
"""Update product images in data.ts using regex approach."""
import json, re

DATA_FILE = "/home/z/my-project/src/lib/data.ts"
IMAGES_FILE = "/home/z/my-project/img_results/all_images.json"

with open(IMAGES_FILE) as f:
    cat_images = json.load(f)

with open(DATA_FILE) as f:
    lines = f.readlines()

# First pass: extract product id -> category mapping
product_cats = {}
for line in lines:
    m = re.match(r"\s*P\((\d+),'[^']*','[^']*','([^']+)'", line)
    if m:
        product_cats[int(m.group(1))] = m.group(2)

print(f"Found {len(product_cats)} products")

# Build category -> product ids mapping
from collections import defaultdict
cat_pids = defaultdict(list)
for pid, cat in product_cats.items():
    cat_pids[cat].append(pid)

# Build pid -> [img1, img2, img3] mapping
def get_pool(cat):
    return cat_images.get(cat, cat_images.get("home-lifestyle", []))

pid_images = {}
for cat, pids in cat_pids.items():
    pool = get_pool(cat)
    if not pool:
        pool = [f"https://picsum.photos/seed/{cat}{i}/800/800" for i in range(10)]
    n = len(pool)
    for idx, pid in enumerate(pids):
        i1 = idx % n
        i2 = (idx * 2 + 1) % n
        i3 = (idx * 3 + 2) % n
        imgs = list(dict.fromkeys([pool[i1], pool[i2], pool[i3]]))
        while len(imgs) < 3:
            imgs.append(pool[(idx + len(imgs)) % n])
        pid_images[pid] = imgs[:3]

print(f"Built image map for {len(pid_images)} products")

# Second pass: replace image arrays in P() calls
updated = 0
new_lines = []
for line in lines:
    m = re.match(r"(\s*P\((\d+),[^[]*)(\[[^\]]*\])", line)
    if m:
        prefix = m.group(1)
        pid = int(m.group(2))
        old_imgs = m.group(3)
        suffix = line[m.end():]
        
        if pid in pid_images:
            imgs = pid_images[pid]
            new_img_str = "[" + ",".join(f"'{u}'" for u in imgs) + "]"
            new_line = prefix + new_img_str + suffix
            new_lines.append(new_line)
            updated += 1
        else:
            new_lines.append(line)
    else:
        new_lines.append(line)

print(f"Updated {updated} products")

with open(DATA_FILE, 'w') as f:
    f.writelines(new_lines)

# Verify
with open(DATA_FILE) as f:
    content = f.read()
for pid in [1, 5, 10, 50, 100, 200]:
    for line in content.split('\n'):
        if re.match(rf"\s*P\({pid},", line):
            imgs = re.search(r'\[([^\]]{20,200})\]', line)
            if imgs:
                print(f"  P{pid}: {imgs.group(0)[:120]}")
            break