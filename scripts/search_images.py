#!/usr/bin/env python3
"""Search product images for each category and save URL mappings."""
import subprocess, json, re, os, time

OUT_DIR = "/home/z/my-project/img_results"
os.makedirs(OUT_DIR, exist_ok=True)

CATEGORIES = [
    ("beauty", "beauty skincare makeup cosmetics products", 15),
    ("beauty2", "hair straightener cream serum face mask", 10),
    ("kitchen", "kitchen cookware pots pans utensils cooking", 15),
    ("electronics", "electronic gadgets phone accessories tech devices", 15),
    ("home-lifestyle", "home decor LED lights lamps room accessories", 15),
    ("kids-babies", "kids toys baby products children educational toy", 15),
    ("appliances", "home appliances drill machine fan household gadgets", 12),
    ("sports-fitness", "sports fitness equipment gym exercise massage", 12),
    ("womens-fashion", "women fashion clothing dresses pakistani lawn", 12),
    ("mens-fashion", "men fashion clothing shirts pants kurta shalwar", 12),
    ("bedding", "bedding bedsheets pillows blankets comforter set", 10),
    ("islamic", "islamic products prayer mat quran decor muslim", 10),
    ("watches-bags", "watches bags jewellery luxury accessories wallet", 12),
    ("stationery", "stationery office supplies pens notebooks school", 10),
    ("fragrance", "perfume fragrance bottles men women scent", 10),
    ("car-accessories", "car accessories auto parts cleaning tools", 10),
    ("mobile-accessories", "mobile phone holder case stand charger accessories", 10),
    ("hair-care", "hair care shampoo conditioner hair tools oil", 10),
    ("pet-care", "pet care dog cat food accessories toys", 10),
    ("womens-shoes", "women shoes heels sandals sneakers khussa", 8),
    ("grocery", "grocery food snacks pakistani dry fruits", 8),
]

def search_images(query, count):
    """Run image search and return list of URLs."""
    try:
        result = subprocess.run(
            ["z-ai", "image-search", "-q", query, "--count", str(count), "--no-rank"],
            capture_output=True, text=True, timeout=150
        )
        output = result.stdout
        if not output.strip():
            output = result.stderr
        # Extract JSON from output
        start = output.index('{')
        end = output.rindex('}') + 1
        data = json.loads(output[start:end])
        if data.get("success") and data.get("results"):
            return [r["original_url"] for r in data["results"]]
    except Exception as e:
        print(f"  Error: {e}")
    return []

def main():
    all_images = {}
    for cat_id, query, count in CATEGORIES:
        print(f"Searching: {cat_id} ({count})...")
        urls = search_images(query, count)
        all_images[cat_id] = urls
        print(f"  Got {len(urls)} images")
        time.sleep(4)  # Rate limit
    
    # Merge beauty + beauty2
    if "beauty" in all_images and "beauty2" in all_images:
        all_images["beauty"].extend(all_images["beauty2"])
        del all_images["beauty2"]
    
    # Save combined results
    with open(os.path.join(OUT_DIR, "all_images.json"), "w") as f:
        json.dump(all_images, f, indent=2)
    
    total = sum(len(v) for v in all_images.values())
    print(f"\nTotal: {total} images across {len(all_images)} categories")
    for cat, urls in all_images.items():
        print(f"  {cat}: {len(urls)}")

if __name__ == "__main__":
    main()