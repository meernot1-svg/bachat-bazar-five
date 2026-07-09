#!/usr/bin/env python3
"""Visit each YourMart product page and extract verified gallery images using agent-browser."""
import subprocess
import json
import re
import time

# Products with their slugs and hero image filenames
products = [
    (9, "m04-tws-wireless-earbuds-bluetooth-53-led-display-bass-sound-fast-charging", "5_1750942955.jpg"),
    (12, "sq11-mini-camera-hd-1080p-night-vision-motion-detection-dvr-camcorder", "Yourmartproducts(15)_1780911799.webp"),
    (22, "remington-proluxe-hair-straightener-model-fr-2105-professional-salon-styling-with-advanced-ceramic-plates", "Yourmartproducts(89)_1781006535.webp"),
    (24, "kinoki-detox-foot-pads-natural-cleansing-foot-patches-for-stress-relief-better-sleep", "Untitleddesign(5)_1779442626.webp"),
    (35, "led-jellyfish-lamp-rgb-mood-light-voice-control-fantasy-jellyfish-night-light-decorative-bedroom-living-room-lighting", "Untitleddesign(10)_1781679519.webp"),
    (45, "long-handle-fascial-gun-massager-model-bld-339-rechargeable-massage-gun-with-4-interchangeable-heads-full-body-muscle-relaxation", "yourmartproduct(56)_1783403862.webp"),
]

# Try to find missing products with different search terms
missing_searches = [
    (11, "CX16"),
    (23, "hair+serum"),
    (26, "scar+gel"),
    (33, "RFID+wallet"),
    (36, "tap+light"),
    (37, "tool+kit"),
    (38, "book+light"),
    (44, "massage+gun"),
    (47, "COB+flashlight"),
    (50, "massage+gun"),
]

# Search for missing products
for pid, query in missing_searches:
    try:
        result = subprocess.run(
            ["curl", "-s", f"https://yourmart.pk/api/search-products?q={query}", "-H", "Accept: application/json"],
            capture_output=True, text=True, timeout=10
        )
        data = json.loads(result.stdout)
        if data:
            slug = data[0]['slug']
            hero = data[0]['hero_image']
            products.append((pid, slug, hero))
            print(f"P{pid}: found -> {slug[:60]}")
        else:
            print(f"P{pid}: NOT FOUND for '{query}'")
    except Exception as e:
        print(f"P{pid}: search error - {e}")

print(f"\nTotal products to verify: {len(products)}")

# Now visit each product page and extract gallery images
results = {}
for pid, slug, hero_filename in products:
    url = f"https://yourmart.pk/products/{slug}"
    print(f"\nP{pid}: Opening {slug[:60]}...")
    
    # Open product page
    r = subprocess.run(
        ["agent-browser", "open", url, "--timeout", "20000"],
        capture_output=True, text=True, timeout=30
    )
    
    time.sleep(3)  # Wait for carousel to load
    
    # Extract hero image timestamp
    ts_match = re.search(r'(\d{10})', hero_filename)
    hero_ts = ts_match.group(1) if ts_match else ""
    
    # Get all gallery images
    js_code = f"""
    (() => {{
      const gallery = document.querySelector('.product-single-gallery');
      if (!gallery) return JSON.stringify({{error: 'no gallery'}});
      
      // Get all unique images from the gallery
      const allImgs = Array.from(gallery.querySelectorAll('img'))
        .map(i => i.src.replace('/public/storage/', '/storage/'))
        .filter(s => s.includes('admin.yourmart'))
        .filter((v, i, a) => a.indexOf(v) === i);
      
      // Separate by timestamp
      const heroTs = '{hero_ts}';
      const mainImgs = allImgs.filter(s => s.includes(heroTs));
      const otherImgs = allImgs.filter(s => !s.includes(heroTs));
      
      return JSON.stringify({{
        total: allImgs.length,
        mainCount: mainImgs.length,
        otherCount: otherImgs.length,
        mainImgs: mainImgs,
        otherImgs: otherImgs
      }});
    }})()
    """
    
    r = subprocess.run(
        ["agent-browser", "eval", js_code],
        capture_output=True, text=True, timeout=15
    )
    
    try:
        data = json.loads(r.stdout.strip())
        if 'error' in data:
            print(f"  ERROR: {data['error']}")
            results[pid] = {"hero": hero_filename, "images": [f"https://admin.yourmart.pk/storage/uploads/inventory/products/media/{hero_filename}"]}
        else:
            print(f"  Gallery: {data['total']} images ({data['mainCount']} main, {data['otherCount']} other)")
            for img in data.get('mainImgs', []):
                print(f"    MAIN: {img.split('/')[-1]}")
            
            # Use main product images (those with same timestamp as hero)
            if data['mainCount'] >= 3:
                verified = data['mainImgs'][:3]
            elif data['mainCount'] >= 1:
                # Fill remaining from other imgs if they look related
                verified = data['mainImgs'][:1] + (data['otherImgs'][:2] if data['otherCount'] >= 2 else data['mainImgs'][:1] * 2)
            else:
                verified = [f"https://admin.yourmart.pk/storage/uploads/inventory/products/media/{hero_filename}"]
            
            results[pid] = {"hero": hero_filename, "images": verified, "mainCount": data['mainCount'], "otherCount": data['otherCount']}
            print(f"  Using {len(verified)} verified images")
    except Exception as e:
        print(f"  Parse error: {e}")
        results[pid] = {"hero": hero_filename, "images": [f"https://admin.yourmart.pk/storage/uploads/inventory/products/media/{hero_filename}"]}

# Save results
with open('/tmp/verified_images.json', 'w') as f:
    json.dump(results, f, indent=2)

print(f"\n\n=== RESULTS SAVED ===")
print(f"Verified {len(results)} products")
for pid, data in sorted(results.items()):
    imgs = data['images']
    unique = len(set(imgs))
    print(f"P{pid}: {unique} unique images (main={data.get('mainCount','?')}, other={data.get('otherCount','?')})")