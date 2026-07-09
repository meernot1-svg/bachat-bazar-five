#!/usr/bin/env python3
"""Update data.ts with unique images for products that had duplicates."""
import re

# Read current data.ts
with open('/home/z/my-project/src/lib/data.ts', 'r') as f:
    content = f.read()

# Image mappings: product_id -> list of 3 image URLs
image_updates = {
    9: [
        'https://admin.yourmart.pk/storage/uploads/inventory/products/media/5_1750942955.jpg',
        'https://admin.yourmart.pk/storage/uploads/inventory/products/media/1_1750942955.jpg',
        'https://admin.yourmart.pk/storage/uploads/inventory/products/media/3_1750942955.jpg',
    ],
    11: [
        'https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(62)_1781613673.webp',
        'https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(63)_1781613673.webp',
        'https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(64)_1781613673.webp',
    ],
    12: [
        'https://admin.yourmart.pk/storage/uploads/inventory/products/media/Yourmartproducts(15)_1780911799.webp',
        'https://admin.yourmart.pk/storage/uploads/inventory/products/media/Yourmartproducts(17)_1780911799.webp',
        'https://admin.yourmart.pk/storage/uploads/inventory/products/media/Yourmartproducts(19)_1780911799.webp',
    ],
    22: [
        'https://admin.yourmart.pk/storage/uploads/inventory/products/media/Yourmartproducts(89)_1781006535.webp',
        'https://admin.yourmart.pk/storage/uploads/inventory/products/media/Yourmartproducts(90)_1781006535.webp',
        'https://admin.yourmart.pk/storage/uploads/inventory/products/media/Yourmartproducts(91)_1781006535.webp',
    ],
    23: [
        'https://admin.yourmart.pk/storage/uploads/inventory/products/media/yourmartproduct(35)_1783345950.webp',
        'https://admin.yourmart.pk/storage/uploads/inventory/products/media/yourmartproduct(36)_1783345950.webp',
        'https://admin.yourmart.pk/storage/uploads/inventory/products/media/yourmartproduct(37)_1783345950.webp',
    ],
    24: [
        'https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(5)_1779442626.webp',
        'https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(3)_1779442626.webp',
        'https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(6)_1779442626.webp',
    ],
    26: [
        'https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(34)_1782724541.webp',
        'https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(35)_1782724541.webp',
        'https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(37)_1782724541.webp',
    ],
    33: [
        'https://admin.yourmart.pk/storage/uploads/inventory/products/media/Yourmartproducts(72)_1780997100.webp',
        'https://admin.yourmart.pk/storage/uploads/inventory/products/media/Yourmartproducts(70)_1780997100.webp',
        'https://admin.yourmart.pk/storage/uploads/inventory/products/media/Yourmartproducts(73)_1780997100.webp',
    ],
    35: [
        'https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(10)_1781679519.webp',
        'https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(9)_1781679519.webp',
        'https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(11)_1781679519.webp',
    ],
    36: [
        'https://admin.yourmart.pk/storage/uploads/inventory/products/media/Yourmartproducts(52)_1780920553.webp',
        'https://admin.yourmart.pk/storage/uploads/inventory/products/media/Yourmartproducts(49)_1780920553.webp',
        'https://admin.yourmart.pk/storage/uploads/inventory/products/media/Yourmartproducts(53)_1780920553.webp',
    ],
    37: [
        'https://admin.yourmart.pk/storage/uploads/inventory/products/media/yourmartproduct(43)_1783346944.webp',
        'https://admin.yourmart.pk/storage/uploads/inventory/products/media/yourmartproduct(41)_1783346944.webp',
        'https://admin.yourmart.pk/storage/uploads/inventory/products/media/yourmartproduct(44)_1783346944.webp',
    ],
    38: [
        'https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(17)_1779446889.webp',
        'https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(14)_1779446889.webp',
        'https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(16)_1779446889.webp',
    ],
    44: [
        'https://admin.yourmart.pk/storage/uploads/inventory/products/media/yourmartproduct(19)_1783340117.webp',
        'https://admin.yourmart.pk/storage/uploads/inventory/products/media/yourmartproduct(16)_1783340117.webp',
        'https://admin.yourmart.pk/storage/uploads/inventory/products/media/yourmartproduct(18)_1783340117.webp',
    ],
    45: [
        'https://admin.yourmart.pk/storage/uploads/inventory/products/media/yourmartproduct(56)_1783403862.webp',
        'https://admin.yourmart.pk/storage/uploads/inventory/products/media/yourmartproduct(57)_1783403862.webp',
        'https://admin.yourmart.pk/storage/uploads/inventory/products/media/yourmartproduct(59)_1783403862.webp',
    ],
    47: [
        'https://admin.yourmart.pk/storage/uploads/inventory/products/media/Yourmartproducts(2)_1780909493.webp',
        'https://admin.yourmart.pk/storage/uploads/inventory/products/media/Yourmartproducts(3)_1780909493.webp',
        'https://admin.yourmart.pk/storage/uploads/inventory/products/media/Yourmartproducts(5)_1780909493.webp',
    ],
    50: [
        'https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(12)_1781767720.webp',
        'https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(13)_1781767720.webp',
        'https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(16)_1781767720.webp',
    ],
}

updated = 0
for pid, images in image_updates.items():
    # Find the P(id, line in data.ts and replace its image array
    # Pattern: P(id,'name',...,['img1','img2','img3'],{...})
    
    # Find the line starting with P(pid,
    # The image array is the 10th parameter (after id, name, brand, cat, price, old, rating, reviews, stock)
    
    # Use regex to find and replace the image array for this product
    # Match: P(pid, ... ['url1','url2','url3'] ...
    # Replace the image array with new URLs
    
    # Build the new image array string
    new_img_str = '[' + ','.join(f"'{url}'" for url in images) + ']'
    
    # Find the P(pid, pattern and locate the image array
    # The image array comes after 9 commas (id, name, brand, cat, price, old, rating, reviews, stock)
    pattern = rf"(P\({pid},)([^[]*)(\[[^\]]*\])"
    
    match = re.search(pattern, content)
    if match:
        old_img_str = match.group(3)
        new_line = match.group(1) + match.group(2) + new_img_str
        content = content.replace(match.group(0), new_line, 1)
        updated += 1
        print(f"Updated P{pid}: replaced {old_img_str[:60]}... -> {new_img_str[:60]}...")
    else:
        print(f"WARNING: Could not find P{pid} pattern")

print(f"\nTotal updated: {updated} products")

# Write back
with open('/home/z/my-project/src/lib/data.ts', 'w') as f:
    f.write(content)

print("data.ts updated successfully!")