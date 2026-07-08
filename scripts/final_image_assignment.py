#!/usr/bin/env python3
"""
Final image assignment:
1. Use product-specific images where available (56 products)
2. Smart keyword-based assignment from category image pools for the rest
3. Update data.ts with all images
"""
import json, re, os

DATA_FILE = "/home/z/my-project/src/lib/data.ts"
PROGRESS_FILE = "/home/z/my-project/img_results/product_images_progress.json"
CAT_IMAGES_FILE = "/home/z/my-project/img_results/all_images.json"

# Load data
with open(PROGRESS_FILE) as f:
    product_imgs = json.load(f)
with open(CAT_IMAGES_FILE) as f:
    cat_imgs = json.load(f)

# Flatten all category images into a pool with category tags
all_pool = []  # [(url, category, query_used)]
for cat, urls in cat_imgs.items():
    for url in urls:
        all_pool.append((url, cat))

print(f"Category image pool: {len(all_pool)} images across {len(cat_imgs)} categories")
print(f"Product-specific images: {sum(1 for v in product_imgs.values() if v)} products")

# Keyword to category/image source mapping for smart assignment
KEYWORD_MAP = {
    # Beauty & Skincare
    'straightener': ['beauty', 'beauty2', 'hair-care'],
    'hair': ['beauty', 'beauty2', 'hair-care'],
    'cream': ['beauty', 'beauty2'],
    'facial': ['beauty', 'beauty2'],
    'skin': ['beauty', 'beauty2'],
    'skincare': ['beauty', 'beauty2'],
    'makeup': ['beauty', 'beauty2'],
    'whitening': ['beauty', 'beauty2'],
    'serum': ['beauty', 'beauty2'],
    'nail': ['beauty', 'beauty2'],
    'perfume': ['fragrance', 'beauty'],
    'fragrance': ['fragrance', 'beauty'],
    'scent': ['fragrance'],
    'kajal': ['beauty', 'beauty2'],
    'lipstick': ['beauty', 'beauty2'],
    'foundation': ['beauty', 'beauty2'],
    'mask': ['beauty', 'beauty2'],
    'suction': ['beauty', 'beauty2'],
    'exfoliating': ['beauty', 'beauty2'],
    'derma': ['beauty', 'beauty2'],
    'zafarani': ['beauty', 'beauty2'],
    'keratin': ['beauty', 'beauty2', 'hair-care'],
    'shampoo': ['hair-care', 'beauty'],
    'conditioner': ['hair-care', 'beauty'],
    'oil': ['hair-care', 'beauty'],
    
    # Kitchen
    'chopper': ['kitchen'],
    'sauce': ['kitchen'],
    'bottle': ['kitchen', 'grocery'],
    'peeler': ['kitchen'],
    'knife': ['kitchen'],
    'cooking': ['kitchen'],
    'pot': ['kitchen'],
    'pan': ['kitchen'],
    'utensil': ['kitchen'],
    'storage': ['kitchen', 'home-lifestyle'],
    'container': ['kitchen'],
    'press': ['kitchen'],
    'blender': ['kitchen'],
    'jug': ['kitchen'],
    'glass': ['kitchen'],
    'tissue': ['kitchen', 'grocery'],
    'kitchen': ['kitchen'],
    
    # Electronics & Mobile
    'phone': ['mobile-accessories', 'electronics'],
    'mobile': ['mobile-accessories', 'electronics'],
    'cooler': ['electronics', 'appliances'],
    'fan': ['electronics', 'appliances'],
    'camera': ['electronics'],
    'camera': ['electronics'],
    'charger': ['electronics', 'mobile-accessories'],
    'cable': ['electronics', 'mobile-accessories'],
    'earbuds': ['electronics'],
    'speaker': ['electronics'],
    'power': ['electronics'],
    'disconnector': ['electronics'],
    'led': ['home-lifestyle', 'electronics'],
    'lamp': ['home-lifestyle'],
    'light': ['home-lifestyle'],
    'projector': ['home-lifestyle', 'electronics'],
    
    # Appliances
    'drill': ['appliances'],
    'tool': ['appliances', 'home-lifestyle'],
    'wrench': ['appliances', 'home-lifestyle'],
    'socket': ['appliances', 'home-lifestyle'],
    'repair': ['appliances', 'home-lifestyle'],
    'iron': ['appliances'],
    'sewing': ['appliances'],
    'heater': ['appliances'],
    
    # Sports & Fitness
    'massager': ['sports-fitness'],
    'massage': ['sports-fitness'],
    'fascial': ['sports-fitness'],
    'gun': ['sports-fitness', 'kids-babies'],
    'exercise': ['sports-fitness'],
    'yoga': ['sports-fitness'],
    'dumbbell': ['sports-fitness'],
    'gym': ['sports-fitness'],
    'fitness': ['sports-fitness'],
    'waist': ['sports-fitness'],
    'slimming': ['sports-fitness'],
    'abdominal': ['sports-fitness'],
    
    # Fashion
    'lawn': ['womens-fashion'],
    'kurta': ['mens-fashion', 'womens-fashion'],
    'embroidered': ['womens-fashion'],
    'print': ['womens-fashion', 'mens-fashion'],
    'dress': ['womens-fashion'],
    'shirt': ['mens-fashion'],
    'pants': ['mens-fashion'],
    'trouser': ['mens-fashion'],
    'shoes': ['womens-shoes', 'mens-fashion'],
    'heel': ['womens-shoes'],
    'sneaker': ['womens-shoes'],
    'sandal': ['womens-shoes'],
    'khussa': ['womens-shoes'],
    'cotton': ['womens-fashion', 'mens-fashion', 'bedding'],
    'silk': ['bedding', 'womens-fashion'],
    'synthetic': ['mens-fashion'],
    'leather': ['mens-fashion', 'watches-bags'],
    'track': ['mens-fashion'],
    'jeans': ['mens-fashion'],
    'waistcoat': ['mens-fashion'],
    'coat': ['mens-fashion'],
    
    # Home & Lifestyle
    'sand art': ['home-lifestyle'],
    'jellyfish': ['home-lifestyle'],
    'ripple': ['home-lifestyle'],
    'aurora': ['home-lifestyle'],
    'cube': ['home-lifestyle'],
    'night light': ['home-lifestyle'],
    'tap light': ['home-lifestyle'],
    'remote control': ['home-lifestyle', 'electronics'],
    'ocean': ['home-lifestyle'],
    'wave': ['home-lifestyle'],
    'decor': ['home-lifestyle'],
    'frame': ['home-lifestyle'],
    'organizer': ['home-lifestyle', 'stationery'],
    'shelf': ['home-lifestyle'],
    'clock': ['home-lifestyle', 'watches-bags'],
    
    # Bedding
    'bedsheet': ['bedding'],
    'bed sheet': ['bedding'],
    'pillow': ['bedding'],
    'blanket': ['bedding'],
    'comforter': ['bedding'],
    'quilt': ['bedding'],
    'bed': ['bedding'],
    'mattress': ['bedding'],
    'fitted': ['bedding'],
    'flat': ['bedding'],
    
    # Islamic
    'prayer': ['islamic'],
    'quran': ['islamic'],
    'islamic': ['islamic'],
    'muslim': ['islamic'],
    'tasbih': ['islamic'],
    'surah': ['islamic'],
    'ayat': ['islamic'],
    'hijab': ['islamic', 'womens-fashion'],
    'cap': ['islamic', 'mens-fashion'],
    
    # Watches & Bags
    'watch': ['watches-bags'],
    'bag': ['watches-bags'],
    'wallet': ['watches-bags'],
    'handbag': ['watches-bags'],
    'ring': ['watches-bags'],
    'bracelet': ['watches-bags'],
    'jewelry': ['watches-bags'],
    'jewellery': ['watches-bags'],
    
    # Kids & Babies
    'toy': ['kids-babies'],
    'baby': ['kids-babies'],
    'kids': ['kids-babies'],
    'children': ['kids-babies'],
    'bubble': ['kids-babies'],
    'unicorn': ['kids-babies'],
    'pop-it': ['kids-babies'],
    'writing': ['kids-babies', 'stationery'],
    'lcd': ['kids-babies', 'electronics'],
    'musical': ['kids-babies'],
    'catapult': ['kids-babies'],
    'aircraft': ['kids-babies'],
    'foam': ['kids-babies'],
    
    # Car
    'car': ['car-accessories'],
    'auto': ['car-accessories'],
    'seat': ['car-accessories'],
    'vacuum': ['car-accessories'],
    'dash': ['car-accessories'],
    
    # Pet
    'dog': ['pet-care'],
    'cat food': ['pet-care'],
    'pet': ['pet-care'],
    
    # Stationery
    'pen': ['stationery'],
    'notebook': ['stationery'],
    'board': ['stationery', 'home-lifestyle'],
    'acrylic': ['stationery', 'home-lifestyle'],
    
    # Grocery
    'food': ['grocery'],
    'snack': ['grocery'],
    'dry fruit': ['grocery'],
    'nut': ['grocery'],
    'honey': ['grocery'],
    'tea': ['grocery'],
    'biscuit': ['grocery'],
}

def get_smart_images(name, category, count=3):
    """Get images based on product name keywords."""
    name_lower = name.lower()
    
    # Score each category based on keyword matches
    cat_scores = {}
    for keyword, cats in KEYWORD_MAP.items():
        if keyword in name_lower:
            for cat in cats:
                cat_scores[cat] = cat_scores.get(cat, 0) + 1
    
    # Also add the product's own category with a base score
    cat_scores[category] = cat_scores.get(category, 0) + 0.5
    
    if cat_scores:
        # Sort categories by score (highest first)
        sorted_cats = sorted(cat_scores.keys(), key=lambda c: cat_scores[c], reverse=True)
        
        # Collect images from top-matching categories
        all_urls = []
        for cat in sorted_cats:
            if cat in cat_imgs:
                for url in cat_imgs[cat]:
                    if url not in all_urls:
                        all_urls.append(url)
            if len(all_urls) >= count * 2:
                break
        
        if all_urls:
            # Return evenly spaced images from the pool
            step = max(1, len(all_urls) // count)
            return [all_urls[i * step % len(all_urls)] for i in range(count)]
    
    # Fallback: use category images
    pool = cat_imgs.get(category, cat_imgs.get('home-lifestyle', []))
    if pool:
        return [pool[i % len(pool)] for i in range(count)]
    
    return [f"https://picsum.photos/seed/prod{i}/800/800" for i in range(count)]

# Read data.ts
with open(DATA_FILE) as f:
    lines = f.readlines()

# Extract products
products = {}
for line in lines:
    m = re.match(r"\s*P\((\d+),'([^']+)'[^']*'([^']+)'", line)
    if m:
        products[int(m.group(1))] = (m.group(2), m.group(3))

# Build final image mapping
final_images = {}
used_product_specific = 0
used_smart = 0

for pid in sorted(products.keys()):
    key = str(pid)
    name, cat = products[pid]
    
    if key in product_imgs and product_imgs[key]:
        # Use product-specific images
        final_images[pid] = product_imgs[key]
        used_product_specific += 1
    else:
        # Use smart keyword-based assignment
        imgs = get_smart_images(name, cat, 3)
        final_images[pid] = imgs
        used_smart += 1

print(f"\nFinal assignment:")
print(f"  Product-specific: {used_product_specific}")
print(f"  Smart category: {used_smart}")

# Update data.ts
updated = 0
new_lines = []
for line in lines:
    m = re.match(r"(\s*P\((\d+),[^[]*)(\[[^\]]*\])", line)
    if m:
        prefix = m.group(1)
        pid = int(m.group(2))
        suffix = line[m.end():]
        
        if pid in final_images:
            imgs = final_images[pid]
            new_img_str = "[" + ",".join(f"'{u}'" for u in imgs) + "]"
            new_line = prefix + new_img_str + suffix
            new_lines.append(new_line)
            updated += 1
        else:
            new_lines.append(line)
    else:
        new_lines.append(line)

print(f"Updated {updated} product image arrays in data.ts")

with open(DATA_FILE, 'w') as f:
    f.writelines(new_lines)

# Verify a few
with open(DATA_FILE) as f:
    content = f.read()
print("\nSample products:")
for pid in [1, 5, 30, 80, 120, 200]:
    for line in content.split('\n'):
        if re.match(rf"\s*P\({pid},", line):
            name_match = re.search(r"P\(\d+,'([^']+)'", line)
            img_match = re.search(r"\['([^']+)'", line)
            if name_match and img_match:
                print(f"  P{pid}: {name_match.group(1)[:45]}... → {img_match.group(1)[:70]}...")
            break