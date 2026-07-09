#!/usr/bin/env python3
"""Search accurate images for all 40 products using z-ai image-search CLI."""
import json
import subprocess
import time
import sys
import os

# All 40 products with their names for image search
products = [
    (1, "Rechargeable Eyebrow Trimmer Electric Face Hair Remover"),
    (2, "Pink Glitter Rechargeable Eyebrow Trimmer Women"),
    (3, "Mini 1080P WiFi Security Camera Night Vision"),
    (4, "Wireless Bluetooth Earbuds TWS 5.3"),
    (5, "Bluetooth 5.3 Earbuds Active Noise Cancelling"),
    (6, "Mini Massage Gun Portable Deep Tissue"),
    (7, "Mini Handheld Fan USB Rechargeable Portable"),
    (8, "Rechargeable LED Flashlight USB-C Zoomable Tactical"),
    (9, "Phone Screen Magnifier HD 3D Acrylic Lens"),
    (10, "Mini Air Cooler Portable USB 3-Speed"),
    (11, "LED Table Lamp Touch Control Desk Lamp"),
    (12, "Zafarani Freckle Cream Glutathione Skin Whitening"),
    (13, "Zafarani Whitening Cream Vitamin C Glutathione"),
    (14, "Rice Extract Whitening Facial Kit Korean Beauty"),
    (15, "5-in-1 Hair Curler Straightener Ceramic"),
    (16, "Makeup and Skincare Bundle Set"),
    (17, "Premium 5-step Korean Skincare Set"),
    (18, "Wellice Onion Shampoo Anti Hair Loss Biotin"),
    (19, "Nano Hydroxyapatite Teeth Whitening Toothpaste"),
    (20, "Iconic London Highlighter Palette Shimmer"),
    (21, "Apple Shape Manicure Kit 8 Pcs Stainless Steel"),
    (22, "Bridal Makeup Kit 19 Pieces Complete Set"),
    (23, "Professional 16-in-1 Makeup Set Color Palettes"),
    (24, "Janan Zarar Unisex Floral Perfume"),
    (25, "Colorful Charm Bracelet Women Crystal"),
    (26, "Turkish Ottoman Men Ring Set Stainless Steel"),
    (27, "Heart Shape Dial Watch Women Stainless Steel Mesh"),
    (28, "Black Skeleton Chronograph Watch Men Mechanical"),
    (29, "Gold Plated Luxury Watch Men Leather Strap"),
    (30, "Croc Embossed Leather Wallet Men RFID Blocking"),
    (31, "Mustard Yellow PU Leather Crossbody Bag"),
    (32, "Green Crossbody Bag Rose Gold Chain"),
    (33, "Manual Food Chopper Vegetable Cutter Pull String"),
    (34, "Nano Tape Reusable Magic Adhesive Washable"),
    (35, "Quilted Cotton Microwave Cover Dust Protection"),
    (36, "Colorful Wall Stickers Room Decor Vinyl Waterproof"),
    (37, "Silicone Back Bath Scrubber Belt Extended Handle"),
    (38, "Mens Dri-Fit Track Suit 2 Piece Set"),
    (39, "Unisex Printed Polyester T-Shirt Casual"),
    (40, "Mens Knitted Zip-Up Cardigan Sweater Winter"),
]

results = {}
output_file = "/home/z/my-project/scripts/accurate_images_40.json"

# Load existing results if any
if os.path.exists(output_file):
    with open(output_file) as f:
        results = json.load(f)
    print(f"Loaded {len(results)} existing results")

start_idx = 0
for i, (pid, query) in enumerate(products):
    if str(pid) in results:
        print(f"[{pid}] SKIP - already have {len(results[str(pid)])} images")
        continue
    
    if i < start_idx:
        continue
    
    print(f"\n[{pid}/{len(products)}] Searching: {query}")
    
    try:
        result = subprocess.run(
            ["z-ai", "image-search", "-q", query, "--count", "3", "--no-rank", "--gl", "us"],
            capture_output=True, text=True, timeout=120
        )
        
        if result.returncode == 0:
            data = json.loads(result.stdout)
            if data.get("success") and data.get("results"):
                urls = [r["original_url"] for r in data["results"][:3]]
                results[str(pid)] = urls
                print(f"  -> Found {len(urls)} images")
                for u in urls:
                    print(f"     {u}")
            else:
                print(f"  -> No results (success={data.get('success')})")
                results[str(pid)] = []
        else:
            print(f"  -> CLI error: {result.stderr[:100]}")
            results[str(pid)] = []
    except subprocess.TimeoutExpired:
        print(f"  -> TIMEOUT")
        results[str(pid)] = []
    except Exception as e:
        print(f"  -> Error: {e}")
        results[str(pid)] = []
    
    # Save progress after each search
    with open(output_file, "w") as f:
        json.dump(results, f, indent=2)
    
    # Rate limit delay
    time.sleep(4)

print(f"\n=== DONE ===")
print(f"Total products with images: {sum(1 for v in results.values() if v)}/{len(products)}")
print(f"Results saved to: {output_file}")