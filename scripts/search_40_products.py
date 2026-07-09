#!/usr/bin/env python3
"""
Search 3 accurate images for each of the 40 products.
Saves progress incrementally. Run multiple times until all done.
"""
import subprocess, json, os, time, sys

PROGRESS_FILE = "/home/z/my-project/img_results/new_products_images.json"

PRODUCTS = [
    # (id, name, search_query)
    # Gadgets & Electronics
    (1, "Rechargeable Eyebrow Trimmer w/ Cleaning Brushes", "rechargeable eyebrow trimmer electric face"),
    (2, "Rechargeable Eyebrow Trimmer Pink Glitter", "rechargeable eyebrow trimmer pink women"),
    (3, "A9 1080P WiFi Mini Security Camera Night Vision", "mini wifi security camera 1080p night vision"),
    (4, "Premium Wireless Earbuds Bluetooth 5.3", "wireless earbuds bluetooth 5.3 premium"),
    (5, "Wireless Bluetooth 5.3 Earbuds Noise Cancellation", "wireless earbuds noise cancelling bluetooth"),
    (6, "Mini Massager Gun", "mini massage gun portable handheld"),
    (7, "Mini Handheld Fan USB Rechargeable", "mini handheld fan USB rechargeable portable"),
    (8, "Rechargeable LED Flashlight USB-C", "rechargeable LED flashlight USB-C tactical"),
    (9, "Video Amplifying Screen Phone Magnifier", "phone screen magnifier amplifier HD"),
    (10, "Mini Air Cooler 3-Speed Perfume", "mini portable air cooler 3 speed USB"),
    (11, "Table Lamp LED Desk Lamp", "LED table lamp desk modern"),
    # Beauty & Care
    (12, "Zafarani Freckle Cream Glutathione Serum", "glutathione serum skin whitening cream"),
    (13, "Whitening Zafarani Cream Set of 2", "whitening face cream set skincare"),
    (14, "Whitening Brightening Facial Kit Rice Extract", "rice extract facial kit whitening skincare"),
    (15, "5-in-1 Hair Curler and Straightener", "hair curler straightener 5 in 1"),
    (16, "3-in-1 Makeup and Skincare Bundle", "makeup skincare bundle set cosmetic"),
    (17, "5-in-1 Premium Skincare Set", "premium skincare set beauty box"),
    (18, "Wellice Onion Anti-Hair Loss Shampoo", "onion shampoo anti hair loss wellice"),
    (19, "Nano Hydroxyapatite Teeth Whitening Toothpaste", "teeth whitening toothpaste nano hydroxyapatite"),
    (20, "Iconic London Highlighter 3 Shades", "Iconic London highlighter shimmer palette"),
    (21, "8 Pcs Apple Shape Manicure Kit", "apple shape manicure kit nail tools"),
    (22, "19-in-1 Bridal Makeup Kit", "bridal makeup kit 19 pieces cosmetic set"),
    (23, "16-in-1 Makeup Set", "makeup set 16 pieces palette cosmetic"),
    (24, "Unisex Floral Perfume Pack Janan Zarar", "floral perfume unisex fragrance set"),
    # Fashion Accessories
    (25, "Colorful Charm Bracelet", "colorful charm bracelet women jewelry"),
    (26, "Turkish-Inspired Mens Ring Set of 3", "men ring set stainless steel Turkish"),
    (27, "Stainless Steel Heart Love Watch", "heart shape watch women stainless steel"),
    (28, "Black Skeleton Chronograph Watch Men", "skeleton chronograph watch men black"),
    (29, "RALEX Gold Plated Watch Men", "gold plated watch men luxury RALEX"),
    (30, "Premium Croc Embossed Leather Wallet", "crocodile leather wallet men premium"),
    (31, "Mustard PU Leather Crossbody Bag", "PU leather crossbody bag mustard yellow"),
    (32, "Green Crossbody Bag Rose Gold Chain", "green crossbody bag rose gold chain"),
    # Home & Practical
    (33, "Manual Food Chopper", "manual food chopper vegetable cutter kitchen"),
    (34, "Nano Tape Reusable Home Organization", "nano tape reusable adhesive home"),
    (35, "Quilted Microwave Cover", "quilted microwave cover kitchen"),
    (36, "Vibrant Wall Stickers Room Decor", "wall stickers room decor vibrant"),
    (37, "Silicone Back Bath Scrubber Belt", "silicone back scrubber belt bath shower"),
    # Apparel
    (38, "Mens Dri-Fit Track Suit 2pc", "men dri-fit track suit sportswear"),
    (39, "Unisex Printed Polyester T-Shirt", "printed polyester t-shirt unisex casual"),
    (40, "Mens Knitted Zip-Up Cardigan", "men knitted zip cardigan sweater"),
]

def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE) as f:
            return json.load(f)
    return {}

def save_progress(p):
    with open(PROGRESS_FILE, 'w') as f:
        json.dump(p, f, indent=2)

def search_images(query, count=3):
    try:
        result = subprocess.run(
            ["z-ai", "image-search", "-q", query, "--count", str(count), "--no-rank"],
            capture_output=True, text=True, timeout=120
        )
        output = result.stdout or result.stderr
        if '{' not in output:
            return []
        start = output.index('{')
        end = output.rindex('}') + 1
        data = json.loads(output[start:end])
        if data.get("success") and data.get("results"):
            return [r["original_url"] for r in data["results"]]
    except:
        pass
    return []

def main():
    progress = load_progress()
    
    # Find products that need images
    todo = []
    for pid, name, query in PRODUCTS:
        key = str(pid)
        if key not in progress or not progress[key]:
            todo.append((pid, name, query))
    
    done_count = sum(1 for v in progress.values() if v)
    print(f"Need images: {len(todo)}/40 | Already done: {done_count}", flush=True)
    
    for i, (pid, name, query) in enumerate(todo):
        print(f"[{i+1}/{len(todo)}] P{pid}: {query[:45]}", end=" ", flush=True)
        urls = search_images(query, 3)
        if urls:
            progress[str(pid)] = urls
            print(f"OK ({len(urls)})", flush=True)
        else:
            progress[str(pid)] = []
            print("FAIL - retrying in 8s...", flush=True)
            time.sleep(8)
            # Retry once
            urls = search_images(query, 3)
            if urls:
                progress[str(pid)] = urls
                print(f"  RETRY OK ({len(urls)})", flush=True)
            else:
                print(f"  RETRY FAIL", flush=True)
        
        if (i + 1) % 3 == 0:
            save_progress(progress)
        
        time.sleep(4)
    
    save_progress(progress)
    
    done = sum(1 for v in progress.values() if v)
    failed = sum(1 for v in progress.values() if not v)
    print(f"\nDone! {done}/40 with images, {failed} failed")
    
    # Show failed ones for retry
    if failed:
        print("Failed products:")
        for pid, name, _ in PRODUCTS:
            if not progress.get(str(pid)):
                print(f"  P{pid}: {name}")

if __name__ == "__main__":
    main()