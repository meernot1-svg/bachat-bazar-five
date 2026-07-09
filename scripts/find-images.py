#!/usr/bin/env python3
"""Find additional YourMart product images by checking timestamp-based variants."""
import re
import subprocess
import json
import sys

BASE = "https://admin.yourmart.pk/storage/uploads/inventory/products/media"

def check_url(url):
    """Check if URL exists (returns True if 200)."""
    try:
        result = subprocess.run(
            ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", url],
            capture_output=True, text=True, timeout=10
        )
        return result.stdout.strip() == "200"
    except:
        return False

def find_images_for_product(image_url):
    """Given a hero image URL, find all related images with the same timestamp."""
    # Extract filename
    filename = image_url.split("/")[-1]
    
    # Extract timestamp (10-digit number)
    ts_match = re.search(r'(\d{10})', filename)
    if not ts_match:
        return [image_url]
    ts = ts_match.group(1)
    
    # Determine extension
    ext_match = re.search(r'\.(jpg|jpeg|webp|png)$', filename, re.IGNORECASE)
    ext = ext_match.group(1) if ext_match else "jpg"
    
    # Try different patterns
    found = []
    
    # Pattern 1: numbered_{timestamp}.{ext} - check 1-10
    for num in range(1, 11):
        url = f"{BASE}/{num}_{ts}.{ext}"
        if check_url(url):
            found.append(url)
    
    # Pattern 2: check for both extensions
    other_ext = "webp" if ext == "jpg" else "jpg"
    for num in range(1, 11):
        url = f"{BASE}/{num}_{ts}.{other_ext}"
        if check_url(url):
            found.append(url)
    
    # Pattern 3: prefix(N)_{timestamp}.{ext} - check sequential
    prefix_match = re.match(r'^(.+?)\((\d+)\)(_\d+\.\w+)$', filename)
    if prefix_match:
        prefix = prefix_match.group(1)
        num = int(prefix_match.group(2))
        suffix = prefix_match.group(3)
        
        for n in range(max(1, num - 3), num + 8):
            if n == num:
                continue
            url = f"{BASE}/{prefix}({n}){suffix}"
            if check_url(url):
                found.append(url)
    
    # Pattern 4: prefix_{timestamp}.{ext} without numbers in prefix
    if not prefix_match:
        # Check if filename has a descriptive prefix before timestamp
        simple_match = re.match(r'^(.+?)_(\d{10})\.\w+$', filename)
        if simple_match:
            prefix = simple_match.group(1)
            # Try adding sequential numbers
            for n in range(1, 10):
                url = f"{BASE}/{prefix}({n})_{ts}.{ext}"
                if check_url(url):
                    found.append(url)
                url = f"{BASE}/{prefix}_{n}_{ts}.{ext}"
                if check_url(url):
                    found.append(url)
    
    # Add original
    found.append(image_url)
    
    # Deduplicate while preserving order
    seen = set()
    unique = []
    for url in found:
        if url not in seen:
            seen.add(url)
            unique.append(url)
    
    return unique

# Define all YourMart products that need image fixes
products = {
    9: "5_1750942955.jpg",
    10: "ProductsPictures(19)_1776770521.webp",
    11: "Untitleddesign(62)_1781613673.webp",
    12: "Yourmartproducts(15)_1780911799.webp",
    21: "Yourmartproducts-2026-06-09T182545.999_1781011609.webp",
    22: "Yourmartproducts(89)_1781006535.webp",
    23: "yourmartproduct(35)_1783345950.webp",
    24: "Untitleddesign(5)_1779442626.webp",
    25: "Untitleddesign(54)_1779534225.webp",
    26: "Untitleddesign(34)_1782724541.webp",
    33: "Yourmartproducts(72)_1780997100.webp",
    35: "Untitleddesign(10)_1781679519.webp",
    36: "Yourmartproducts(52)_1780920553.webp",
    37: "yourmartproduct(43)_1783346944.webp",
    38: "Untitleddesign(17)_1779446889.webp",
    44: "yourmartproduct(19)_1783340117.webp",
    45: "yourmartproduct(56)_1783403862.webp",
    46: "Untitleddesign(16)_1781681829.webp",
    47: "Yourmartproducts(2)_1780909493.webp",
    48: "ProductsPictures(70)_1779191754.webp",
    49: "ProductsPictures(58)_1778490824.webp",
    50: "Untitleddesign(12)_1781767720.webp",
}

results = {}
for pid, filename in products.items():
    url = f"{BASE}/{filename}"
    print(f"P{pid}: Checking {filename}...", file=sys.stderr)
    images = find_images_for_product(url)
    results[pid] = images[:5]  # Keep up to 5
    print(f"P{pid}: Found {len(results[pid])} images", file=sys.stderr)

print(json.dumps(results, indent=2))