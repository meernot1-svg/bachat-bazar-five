#!/usr/bin/env python3
"""Verify all 100 products' images and fix missing ones."""
import json
import urllib.request
import concurrent.futures

def check_url(url):
    try:
        req = urllib.request.Request(url, method='HEAD')
        req.add_header('User-Agent', 'Mozilla/5.0')
        resp = urllib.request.urlopen(req, timeout=8)
        return resp.status == 200
    except:
        return False

def find_working_images(base, ext, max_n=6):
    """Find up to 3 working images for a product."""
    working = []
    for n in range(1, max_n + 1):
        url = f"{base}-product-{n}{ext}"
        if check_url(url):
            working.append(url)
            if len(working) == 3:
                break
    return working

products = json.load(open('/home/z/my-project/scripts/final_100.json'))

print(f"Verifying {len(products)} products' images...")
fixed = 0
broken = 0

for p in products:
    current = p['images']
    # Check which ones work
    working = []
    for url in current:
        if check_url(url):
            working.append(url)
    
    if len(working) >= 3:
        continue  # All good
    
    # Need to find more images
    base = current[0].rsplit('-product-', 1)[0]
    ext = current[0].rsplit('.', 1)[1]
    all_working = find_working_images(base, ext)
    
    if len(all_working) >= 3:
        p['images'] = all_working[:3]
        fixed += 1
        print(f"  Fixed: {p['name'][:50]} ({len(working)}->3)")
    else:
        broken += 1
        # Use whatever we have, duplicate last if needed
        while len(p['images']) < 3:
            p['images'].append(p['images'][-1])
        print(f"  WARNING: {p['name'][:50]} only has {len(all_working)} images")

print(f"\nFixed: {fixed}, Broken: {broken}")

# Save fixed data
with open('/home/z/my-project/scripts/final_100.json', 'w') as f:
    json.dump(products, f, indent=2, ensure_ascii=False)

print("Saved updated final_100.json")