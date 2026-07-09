#!/usr/bin/env python3
"""Use agent-browser to extract images for remaining products."""
import json
import subprocess
import re

# Products to check: (pid, search_query, hero_timestamp)
products_to_check = [
    (10, "Air+39", "1776770521"),
    (21, "Remington+Keratin", "1781011609"),
    (25, "Meow+Club+Wax", "1779534225"),
    (46, "LED+Night+Light+Motion+Sensor", "1781681829"),
    (48, "TurboFan+Cooling+Fan", "1779191754"),
    (49, "Mosquito+Swatter+USB", "1778490824"),
]

# Also check Markaz GenerativeMedia products
markaz_products = [
    (13, "19+in+1+makeup+kit+bridal", "644275"),
    (14, "ultimate+makeup+kit+20+items", "581802"),
    (15, "16+in+1+makeup+set", "630536"),
]

for pid, query, ts in products_to_check:
    print(f"\n=== Checking P{pid} (ts: {ts}) ===")
    
    # Step 1: Find product URL via search
    search_url = f"https://yourmart.pk/all-products?like={query}"
    result = subprocess.run(
        ["agent-browser", "open", search_url, "--timeout", "15000"],
        capture_output=True, text=True, timeout=30
    )
    
    # Step 2: Get product link
    result = subprocess.run(
        ["agent-browser", "eval", 
         "Array.from(document.querySelectorAll('a')).filter(a => a.href.includes('products/')).map(a => a.href)[0] || 'NONE'"],
        capture_output=True, text=True, timeout=15
    )
    product_url = result.stdout.strip().strip('"').strip("'")
    
    if product_url == "NONE" or not product_url.startswith("http"):
        print(f"  Product not found for query: {query}")
        continue
    
    print(f"  Found: {product_url}")
    
    # Step 3: Open product page
    subprocess.run(
        ["agent-browser", "open", product_url, "--timeout", "15000"],
        capture_output=True, text=True, timeout=30
    )
    
    # Step 4: Extract all images with matching timestamp
    js_code = f"""
    Array.from(document.querySelectorAll('img'))
        .map(i => i.src.replace('/public/storage/', '/storage/'))
        .filter(s => s.includes('admin.yourmart') && s.includes('{ts}'))
        .filter((v,i,a) => a.indexOf(v) === i)
    """
    result = subprocess.run(
        ["agent-browser", "eval", js_code],
        capture_output=True, text=True, timeout=15
    )
    
    # Parse the JSON array
    try:
        output = result.stdout.strip()
        images = json.loads(output)
        print(f"  Found {len(images)} images:")
        for img in images:
            print(f"    {img.split('/')[-1]}")
    except:
        print(f"  Could not parse: {result.stdout[:200]}")

# Close browser
subprocess.run(["agent-browser", "close"], capture_output=True, text=True, timeout=10)
print("\n=== DONE ===")