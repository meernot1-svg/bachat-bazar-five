#!/usr/bin/env python3
"""Select 100 products using ONLY static.markaz.app CDN (reliable 3 images)."""
import json
import re
import random
import urllib.request

random.seed(42)

def load_raw(path):
    raw = open(path).read().strip()
    if raw.startswith('"') and raw.endswith('"'):
        raw = json.loads(raw)
    return json.loads(raw)

categories = {
    'tech': load_raw('/home/z/my-project/scripts/tech_raw.json'),
    'home': load_raw('/home/z/my-project/scripts/home_raw.json'),
    'beauty': load_raw('/home/z/my-project/scripts/beauty_raw.json'),
    'mens': load_raw('/home/z/my-project/scripts/mens_raw.json'),
    'kids': load_raw('/home/z/my-project/scripts/kids_raw.json'),
    'women': load_raw('/home/z/my-project/scripts/women_raw.json'),
}

# Combine, deduplicate by ID
all_products = []
seen_ids = set()
for cat, products in categories.items():
    for p in products:
        if p['id'] in seen_ids:
            continue
        seen_ids.add(p['id'])
        p['cat'] = cat
        all_products.append(p)

# Filter: only static.markaz.app CDN, low cost, valid
valid = []
for p in all_products:
    if not (200 <= p['p'] <= 3000):
        continue
    if 'static.markaz.app' not in p['b']:
        continue  # ONLY static CDN
    if len(p['n']) > 100:
        p['n'] = p['n'][:100]
    valid.append(p)

print(f"Static CDN low-cost products: {len(valid)}")

# Deduplicate by name similarity
def normalize(name):
    return re.sub(r'[^a-z0c0-9]', '', name.lower())

seen_names = set()
unique = []
for p in valid:
    norm = normalize(p['n'])
    is_dup = False
    for sn in seen_names:
        if norm in sn or sn in norm:
            is_dup = True
            break
        words1 = set(norm.split())
        words2 = set(sn.split())
        if len(words1) > 3 and len(words2) > 3:
            overlap = len(words1 & words2) / min(len(words1), len(words2))
            if overlap > 0.65:
                is_dup = True
                break
    if not is_dup:
        seen_names.add(norm)
        unique.append(p)

print(f"After dedup: {len(unique)}")

# Categorize
def categorize(p):
    n = p['n'].lower()
    if any(w in n for w in ['earbuds','headphone','earphone','speaker','charger','cable','torch','flashlight','led','fan','watch','power bank','powerbank','adapter','mouse','keyboard','lighter','clock','timer']):
        return 'electronics'
    if any(w in n for w in ['cream','lipstick','shampoo','lotion','face wash','blush','makeup','hair straight','hair dry','perfume','fragrance','eye cream','skin','whitening','ring','earring','bracelet','necklace','jewelry','pendant','lip gloss','deodorant','sunscreen','face mask']):
        return 'beauty'
    if any(w in n for w in ['bag','wallet','shoe','heel','sneaker','cap','belt','scarf','sunglass']):
        return 'fashion-accessories'
    if any(w in n for w in ['shirt','trouser','kurta','suit','pajama','shawl','hijab','niqab','abaya','dupatta','night suit','t-shirt','jersey','underwear','sock']):
        if p['cat'] in ('mens',):
            return 'mens-fashion'
        elif p['cat'] in ('women',):
            return 'womens-fashion'
        return 'apparel'
    if any(w in n for w in ['kids','baby','toy','puzzle','rc car','balloon','swaddle','rattle']):
        return 'kids-mother'
    return 'home-lifestyle'

groups = {}
for p in unique:
    cat = categorize(p)
    groups.setdefault(cat, []).append(p)

for g, items in sorted(groups.items()):
    print(f"  {g}: {len(items)}")

# Verify all images work before selecting
def check_url(url):
    try:
        req = urllib.request.Request(url, method='HEAD')
        req.add_header('User-Agent', 'Mozilla/5.0')
        resp = urllib.request.urlopen(req, timeout=5)
        return resp.status == 200
    except:
        return False

# Verify all products have 3 working images
print("\nVerifying image URLs...")
verified_products = []
for p in unique:
    img1 = p['b'] + '-product-1' + p['e']
    img2 = p['b'] + '-product-2' + p['e']
    img3 = p['b'] + '-product-3' + p['e']
    
    if check_url(img1) and check_url(img2) and check_url(img3):
        verified_products.append(p)
    else:
        # Try to find 3 working
        working = []
        for n in range(1, 7):
            url = f"{p['b']}-product-{n}{p['e']}"
            if check_url(url):
                working.append(url)
            if len(working) == 3:
                break
        if len(working) >= 3:
            p['_verified_imgs'] = working[:3]
            verified_products.append(p)
        else:
            print(f"  SKIP: {p['n'][:50]} ({len(working)} images)")

print(f"Products with 3+ verified images: {len(verified_products)}")

# Re-categorize verified products
vgroups = {}
for p in verified_products:
    cat = categorize(p)
    vgroups.setdefault(cat, []).append(p)

for g, items in sorted(vgroups.items()):
    print(f"  {g}: {len(items)}")

# Select 100 with good distribution
target_dist = {
    'electronics': 22,
    'beauty': 22,
    'home-lifestyle': 18,
    'fashion-accessories': 10,
    'mens-fashion': 10,
    'womens-fashion': 10,
    'kids-mother': 8,
}

selected = []
for cat, count in target_dist.items():
    items = vgroups.get(cat, [])
    items.sort(key=lambda x: x['p'])
    if len(items) <= count:
        selected.extend(items)
    else:
        step = len(items) / count
        picked = set()
        result = []
        for i in range(count):
            idx = int(i * step)
            if idx not in picked:
                picked.add(idx)
                result.append(items[idx])
        # Fill remaining
        remaining = [(i, x) for i, x in enumerate(items) if i not in picked]
        random.shuffle(remaining)
        for i, x in remaining:
            if len(result) >= count:
                break
            result.append(x)
        selected.extend(result[:count])

print(f"\nSelected: {len(selected)}")

# Build final product data
final = []
for i, p in enumerate(selected, 1):
    cat = categorize(p)
    markup = random.randint(100, 200)
    new_price = p['p'] + markup
    old_price = int(new_price * random.uniform(1.15, 1.30))
    rating = round(4.0 + random.random() * 0.8, 1)
    reviews = random.randint(15, 120)
    stock = random.randint(10, 80)
    
    if '_verified_imgs' in p:
        images = p['_verified_imgs']
    else:
        images = [
            p['b'] + '-product-1' + p['e'],
            p['b'] + '-product-2' + p['e'],
            p['b'] + '-product-3' + p['e'],
        ]
    
    final.append({
        'id': i,
        'name': p['n'],
        'brand': 'Markaz',
        'category': cat,
        'price': new_price,
        'oldPrice': old_price,
        'rating': rating,
        'reviews': reviews,
        'stock': stock,
        'images': images,
        'source_id': p['id'],
        'source_price': p['p'],
    })

with open('/home/z/my-project/scripts/final_100.json', 'w') as f:
    json.dump(final, f, indent=2, ensure_ascii=False)

from collections import Counter
cats = Counter(p['category'] for p in final)
print("\nFinal category distribution:")
for c, n in cats.most_common():
    print(f"  {c}: {n}")

print(f"\nPrice range: {min(p['price'] for p in final)}-{max(p['price'] for p in final)} PKR")
print("Done!")