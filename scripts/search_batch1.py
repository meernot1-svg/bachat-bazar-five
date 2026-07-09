#!/usr/bin/env python3
"""Search accurate images for products 1-10."""
import json, subprocess, time, os

products = [
    (1, "Rechargeable Eyebrow Trimmer Electric Face Hair Remover"),
    (2, "Pink Glitter Rechargeable Eyebrow Trimmer Women"),
    (3, "Mini 1080P WiFi Security Camera Night Vision"),
    (4, "Wireless Bluetooth Earbuds TWS 5.3 White"),
    (5, "Bluetooth 5.3 Earbuds Active Noise Cancelling Black"),
    (6, "Mini Massage Gun Portable Deep Tissue Muscle"),
    (7, "Mini Handheld Fan USB Rechargeable Portable"),
    (8, "Rechargeable LED Flashlight USB-C Zoomable Tactical"),
    (9, "Phone Screen Magnifier HD 3D Acrylic Lens"),
    (10, "Mini Portable Air Cooler USB 3-Speed Fan"),
]

results = {}
output_file = "/home/z/my-project/scripts/accurate_images_40.json"
if os.path.exists(output_file):
    with open(output_file) as f:
        results = json.load(f)

for pid, query in products:
    if str(pid) in results and results[str(pid)]:
        print(f"[{pid}] SKIP - already have images")
        continue
    print(f"\n[{pid}] Searching: {query}")
    try:
        r = subprocess.run(
            ["z-ai", "image-search", "-q", query, "--count", "3", "--no-rank", "--gl", "us"],
            capture_output=True, text=True, timeout=120
        )
        if r.returncode == 0:
            data = json.loads(r.stdout)
            if data.get("success") and data.get("results"):
                urls = [x["original_url"] for x in data["results"][:3]]
                results[str(pid)] = urls
                print(f"  -> Found {len(urls)} images")
            else:
                print(f"  -> No results")
                results[str(pid)] = []
        else:
            print(f"  -> Error")
            results[str(pid)] = []
    except Exception as e:
        print(f"  -> {e}")
        results[str(pid)] = []
    with open(output_file, "w") as f:
        json.dump(results, f, indent=2)
    time.sleep(4)

print(f"\nDone batch 1. Total: {sum(1 for v in results.values() if v)}/10")