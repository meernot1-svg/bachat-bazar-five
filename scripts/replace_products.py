#!/usr/bin/env python3
"""Replace PRODUCTS array in data.ts with new product entries"""
import re

# Read the new products
with open('/home/z/my-project/scripts/products_new.txt') as f:
    new_products = f.read().strip()

# Read the original data.ts
with open('/home/z/my-project/src/lib/data.ts') as f:
    content = f.read()

# Find and replace the PRODUCTS array
# Pattern: from "P(1," to the closing "];"
start_marker = "export const PRODUCTS: Product[] = [\n"
end_marker = "\n];"

start_idx = content.index(start_marker) + len(start_marker)
end_idx = content.index(end_marker, start_idx)

new_content = content[:start_idx] + new_products + "\n" + content[end_idx+1:]

with open('/home/z/my-project/src/lib/data.ts', 'w') as f:
    f.write(new_content)

print("SUCCESS: PRODUCTS array replaced with 50 new products")