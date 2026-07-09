#!/usr/bin/env python3
"""Combine all category products, deduplicate, select 100 diverse low-cost products."""
import json
import re
import random

random.seed(42)

def load_raw(path):
    raw = open(path).read().strip()
    if raw.startswith('"') and raw.endswith('"'):
        raw = json.loads(raw)
    return json.loads(raw)

# Load all categories
categories = {
    'tech': load_raw('/home/z/my-project/scripts/tech_raw.json'),
    'home': load_raw('/home/z/my-project/scripts/home_raw.json'),
    'beauty': load_raw('/home/z/my-project/scripts/beauty_raw.json'),
    'mens': load_raw('/home/z/my-project/scripts/mens_raw.json'),
    'kids': load_raw('/home/z/my-project/scripts/kids_raw.json'),
    'women': load_raw('/home/z/my-project/scripts/women_raw.json'),
}

# Combine with category tags
all_products = []
seen_ids = set()
for cat, products in categories.items():
    for p in products:
        if p['id'] in seen_ids:
            continue
        seen_ids.add(p['id'])
        p['cat'] = cat
        all_products.append(p)

print(f"Total unique products: {len(all_products)}")

# Filter: low cost 200-3000 PKR, valid image base
valid = []
for p in all_products:
    if not (200 <= p['p'] <= 3000):
        continue
    if not p['b'] or 'markaz.app' not in p['b']:
        continue
    # Skip products with very long names (likely duplicate listings)
    if len(p['n']) > 100:
        p['n'] = p['n'][:100]
    valid.append(p)

print(f"Valid low-cost products: {len(valid)}")

# Deduplicate by similar names
def normalize(name):
    return re.sub(r'[^a-z0-9]', '', name.lower())

seen_names = set()
unique = []
for p in valid:
    norm = normalize(p['n'])
    # Check if too similar to existing
    is_dup = False
    for sn in seen_names:
        if norm in sn or sn in norm:
            is_dup = True
            break
        # Check word overlap
        words1 = set(norm.split())
        words2 = set(sn.split())
        if len(words1) > 3 and len(words2) > 3:
            overlap = len(words1 & words2) / min(len(words1), len(words2))
            if overlap > 0.7:
                is_dup = True
                break
    if not is_dup:
        seen_names.add(norm)
        unique.append(p)

print(f"After dedup: {len(unique)}")

# Map categories to Bachat Bazar categories
cat_map = {
    'tech': 'electronics',
    'home': 'home-lifestyle',
    'beauty': 'beauty',
    'mens': 'mens-fashion',
    'kids': 'kids',
    'women': 'womens-fashion',
}

# Categorize products into groups for diversity
groups = {
    'electronics': [],
    'beauty': [],
    'home-lifestyle': [],
    'mens-fashion': [],
    'womens-fashion': [],
    'kids': [],
}

for p in unique:
    bb_cat = cat_map.get(p['cat'], 'home-lifestyle')
    # Sub-categorize beauty products
    n = p['n'].lower()
    if 'perfume' in n or 'fragrance' in n:
        bb_cat = 'beauty'
    elif 'ring' in n or 'earring' in n or 'bracelet' in n or 'necklace' in n or 'jewelry' in n or 'pendant' in n:
        bb_cat = 'beauty'
    elif 'watch' in n:
        bb_cat = 'electronics'
    elif 'bag' in n or 'wallet' in n:
        bb_cat = 'fashion-accessories'
    elif 'shoe' in n or 'heel' in n or 'sneaker' in n:
        bb_cat = 'fashion-accessories'
    elif 'shirt' in n or 'trouser' in n or 'kurta' in n or 'suit' in n or 'pajama' in n:
        if p['cat'] == 'mens':
            bb_cat = 'mens-fashion'
        elif p['cat'] == 'women':
            bb_cat = 'womens-fashion'
        else:
            bb_cat = 'apparel'
    elif 'cream' in n or 'lipstick' in n or 'shampoo' in n or 'lotion' in n or 'face wash' in n or 'blush' in n or 'makeup' in n or 'hair' in n or 'eye cream' in n or 'skin' in n or 'whitening' in n:
        bb_cat = 'beauty'
    elif 'led' in n or 'light' in n or 'fan' in n or 'charger' in n or 'cable' in n or 'earbuds' in n or 'headphone' in n or 'speaker' in n or 'torch' in n or 'flashlight' in n:
        bb_cat = 'electronics'
    elif 'cover' in n or 'mat' in n or 'organizer' in n or 'storage' in n or 'kitchen' in n or 'cutter' in n or 'tissue' in n:
        bb_cat = 'home-lifestyle'
    
    if bb_cat not in groups:
        groups[bb_cat] = []
    groups[bb_cat].append(p)

for g, items in groups.items():
    print(f"  {g}: {len(items)}")

# Select 100 products with good distribution
# Target: electronics=25, beauty=25, home=20, mens-fashion=10, womens-fashion=10, kids=10
target = {
    'electronics': 25,
    'beauty': 25,
    'home-lifestyle': 20,
    'mens-fashion': 10,
    'womens-fashion': 10,
    'fashion-accessories': 5,
    'kids': 5,
}

selected = []
for cat, count in target.items():
    items = groups.get(cat, [])
    # Sort by price (prefer variety in prices)
    items.sort(key=lambda x: x['p'])
    # Pick evenly from price ranges
    if len(items) <= count:
        selected.extend(items)
    else:
        # Pick from different price ranges
        step = len(items) / count
        picked = []
        for i in range(count):
            idx = int(i * step)
            if idx < len(items) and items[idx] not in picked:
                picked.append(items[idx])
        # Fill remaining with random
        remaining = [x for x in items if x not in picked]
        random.shuffle(remaining)
        while len(picked) < count and remaining:
            picked.append(remaining.pop())
        selected.extend(picked[:count])

print(f"\nSelected: {len(selected)} products")

# Verify image URLs work for a few samples
import subprocess
import urllib.request

def check_url(url):
    try:
        req = urllib.request.Request(url, method='HEAD')
        req.add_header('User-Agent', 'Mozilla/5.0')
        resp = urllib.request.urlopen(req, timeout=5)
        return resp.status == 200
    except:
        return False

print("\nVerifying sample image URLs...")
verified = 0
for p in selected[:10]:
    img1 = p['b'] + '-product-1' + p['e']
    img2 = p['b'] + '-product-2' + p['e']
    img3 = p['b'] + '-product-3' + p['e']
    ok1 = check_url(img1)
    ok2 = check_url(img2)
    ok3 = check_url(img3)
    status = "✓" if (ok1 and ok2 and ok3) else "✗"
    if ok1 and ok2 and ok3:
        verified += 1
    print(f"  {status} {p['n'][:45]:45s} | {ok1} {ok2} {ok3}")

print(f"\nVerified {verified}/10 samples have all 3 images working")

# Save final selection
final = []
for i, p in enumerate(selected, 1):
    bb_cat = 'home-lifestyle'  # default
    for cat, items in groups.items():
        if p in items:
            bb_cat = cat
            break
    
    # Map to Bachat Bazar category IDs
    cat_id_map = {
        'electronics': 'electronics',
        'beauty': 'beauty',
        'home-lifestyle': 'home-lifestyle',
        'mens-fashion': 'mens-fashion',
        'womens-fashion': 'womens-fashion',
        'fashion-accessories': 'fashion-accessories',
        'kids': 'kids-mother',
    }
    
    # Increase price by 100-200 PKR
    markup = random.randint(100, 200)
    new_price = p['p'] + markup
    old_price = int(new_price * 1.25)
    
    # Rating 4.0-4.8
    rating = round(4.0 + random.random() * 0.8, 1)
    reviews = random.randint(15, 120)
    stock = random.randint(10, 80)
    
    img1 = p['b'] + '-product-1' + p['e']
    img2 = p['b'] + '-product-2' + p['e']
    img3 = p['b'] + '-product-3' + p['e']
    
    final.append({
        'id': i,
        'name': p['n'],
        'brand': 'Markaz',
        'category': cat_id_map.get(bb_cat, 'home-lifestyle'),
        'price': new_price,
        'oldPrice': old_price,
        'rating': rating,
        'reviews': reviews,
        'stock': stock,
        'images': [img1, img2, img3],
        'source': p['id'],
    })

with open('/home/z/my-project/scripts/final_100.json', 'w') as f:
    json.dump(final, f, indent=2, ensure_ascii=False)

print(f"\nSaved {len(final)} products to final_100.json")

# Print distribution
from collections import Counter
cats = Counter(p['category'] for p in final)
print("\nCategory distribution:")
for c, n in cats.most_common():
    print(f"  {c}: {n}")