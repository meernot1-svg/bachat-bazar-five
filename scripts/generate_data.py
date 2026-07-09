#!/usr/bin/env python3
"""Generate data.ts PRODUCTS array from final_100.json"""
import json
import re

products = json.load(open('/home/z/my-project/scripts/final_100.json'))

# Map our categories to Bachat Bazar category IDs used in the site
cat_map = {
    'electronics': 'electronics',
    'beauty': 'beauty',
    'home-lifestyle': 'home-lifestyle',
    'fashion-accessories': 'fashion-accessories',
    'mens-fashion': 'mens-fashion',
    'womens-fashion': 'womens-fashion',
    'kids-mother': 'kids-mother',
}

lines = []
lines.append('// Product catalog — 100 products from markaz.app with verified accurate images')
lines.append('export const PRODUCTS: Product[] = [')

for p in products:
    pid = p['id']
    name = p['name'].replace("'", "\\'").replace('"', '\\"')
    brand = 'Markaz'
    cat = cat_map.get(p['category'], 'home-lifestyle')
    price = p['price']
    old = p['oldPrice']
    rating = p['rating']
    reviews = p['reviews']
    stock = p['stock']
    
    # Images as array
    imgs = ', '.join(f"'{img}'" for img in p['images'])
    
    # Build options
    trending = 'true' if pid <= 50 else 'false'
    is_new = 'true' if pid <= 20 else 'false'
    
    # Generate description from name
    desc_words = name.split()
    if len(desc_words) > 6:
        short_name = ' '.join(desc_words[:6])
    else:
        short_name = name
    
    desc = f"Premium quality {short_name}. Sourced from top brands, available at Bachat Bazar with fast delivery across Pakistan. Cash on delivery available."
    desc = desc.replace("'", "\\'")
    
    # Features based on category
    if cat == 'electronics':
        features = "['High Quality','Durable Build','Fast Delivery','Value for Money','7-Day Returns']"
    elif cat == 'beauty':
        features = "['Genuine Product','Safe Ingredients','Fast Delivery','Great Value','7-Day Returns']"
    elif cat in ('mens-fashion', 'womens-fashion', 'fashion-accessories'):
        features = "['Premium Quality','Trendy Design','Comfortable Fit','Fast Delivery','7-Day Returns']"
    elif cat == 'kids-mother':
        features = "['Child Safe','High Quality','Durable Material','Fast Delivery','7-Day Returns']"
    else:
        features = "['Premium Quality','Practical Design','Durable','Fast Delivery','7-Day Returns']"
    
    # Specs
    specs = f"{{'Brand':'{brand}','Category':'{cat}','SKU':'BB-{str(pid).zfill(4)}'}}"
    
    line = f"P({pid},'{name}','{brand}','{cat}',{price},{old},{rating},{reviews},{stock},[{imgs}],{{trending:{trending},isNew:{is_new},description:'{desc}',features:{features},specs:{specs}}}),"
    lines.append(line)

lines.append('')
lines.append('// Total: 100 products with verified accurate images from markaz.app')
lines.append('];')

output = '\n'.join(lines)

# Read current data.ts
with open('/home/z/my-project/src/lib/data.ts', 'r') as f:
    content = f.read()

# Replace the empty PRODUCTS array
import re
pattern = r"// Product catalog\s*\nexport const PRODUCTS: Product\[\] = \[\s*\];"
replacement = output

new_content = re.sub(pattern, replacement, content)

with open('/home/z/my-project/src/lib/data.ts', 'w') as f:
    f.write(new_content)

print(f"Generated {len(products)} products in data.ts")
print(f"File size: {len(new_content)} bytes")