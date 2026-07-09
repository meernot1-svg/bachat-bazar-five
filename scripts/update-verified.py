#!/usr/bin/env python3
"""Update data.ts with VERIFIED images from actual product pages."""
import re

with open('src/lib/data.ts', 'r') as f:
    content = f.read()

# Verified images from actual product page galleries (same timestamp = same product)
verified = {
    9: [
        "https://admin.yourmart.pk/storage/uploads/inventory/products/media/5_1750942955.jpg",
        "https://admin.yourmart.pk/storage/uploads/inventory/products/media/1_1750942955.jpg",
        "https://admin.yourmart.pk/storage/uploads/inventory/products/media/3_1750942955.jpg",
    ],
    11: [
        "https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(62)_1781613673.webp",
        "https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(63)_1781613673.webp",
        "https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(64)_1781613673.webp",
    ],
    12: [
        "https://admin.yourmart.pk/storage/uploads/inventory/products/media/Yourmartproducts(15)_1780911799.webp",
        "https://admin.yourmart.pk/storage/uploads/inventory/products/media/Yourmartproducts(17)_1780911799.webp",
        "https://admin.yourmart.pk/storage/uploads/inventory/products/media/Yourmartproducts(19)_1780911799.webp",
    ],
    22: [
        "https://admin.yourmart.pk/storage/uploads/inventory/products/media/Yourmartproducts(89)_1781006535.webp",
        "https://admin.yourmart.pk/storage/uploads/inventory/products/media/Yourmartproducts(90)_1781006535.webp",
        "https://admin.yourmart.pk/storage/uploads/inventory/products/media/Yourmartproducts(91)_1781006535.webp",
    ],
    24: [
        "https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(5)_1779442626.webp",
        "https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(2)_1779442626.webp",
        "https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(3)_1779442626.webp",
    ],
    35: [
        "https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(10)_1781679519.webp",
        "https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(9)_1781679519.webp",
        "https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(11)_1781679519.webp",
    ],
    45: [
        "https://admin.yourmart.pk/storage/uploads/inventory/products/media/yourmartproduct(56)_1783403862.webp",
        "https://admin.yourmart.pk/storage/uploads/inventory/products/media/yourmartproduct(57)_1783403862.webp",
        "https://admin.yourmart.pk/storage/uploads/inventory/products/media/yourmartproduct(58)_1783403862.webp",
    ],
    47: [
        "https://admin.yourmart.pk/storage/uploads/inventory/products/media/Yourmartproducts(2)_1780909493.webp",
        "https://admin.yourmart.pk/storage/uploads/inventory/products/media/Yourmartproducts(1)_1780909493.webp",
        "https://admin.yourmart.pk/storage/uploads/inventory/products/media/Yourmartproducts(3)_1780909493.webp",
    ],
}

updated = 0
for pid, images in verified.items():
    new_img_str = '[' + ','.join(f"'{url}'" for url in images) + ']'
    pattern = rf"(P\({pid},[^\[]*)(\[[^\]]+\])"
    match = re.search(pattern, content)
    if match:
        content = content.replace(match.group(0), match.group(1) + new_img_str, 1)
        updated += 1
        print(f"P{pid}: updated with {len(set(images))} unique VERIFIED images")

print(f"\nUpdated {updated} products with verified gallery images")
print("Remaining products keep their accurate hero image only")

with open('src/lib/data.ts', 'w') as f:
    f.write(content)