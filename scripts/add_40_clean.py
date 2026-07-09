import json, re

DATA_FILE = "/home/z/my-project/src/lib/data.ts"
with open("/home/z/my-project/img_results/all_images.json") as f:
    ci = json.load(f)

def g3(c, o):
    p = ci.get(c, ci.get("electronics", []))
    if not p: p = ["https://picsum.photos/seed/x/800/800"]
    return [p[(o + i) % len(p)] for i in range(3)]

with open(DATA_FILE) as f:
    ct = f.read()

m = re.search(r'(export const PRODUCTS: Product\[\] = \[)(.*?)(\];)', ct, re.DOTALL)
if not m:
    print("ERROR")
    exit(1)

N = [
    "Rechargeable Eyebrow Trimmer", "Eyebrow Trimmer Pink Glitter",
    "A9 1080P WiFi Security Camera", "Premium Wireless Earbuds Bluetooth 5.3",
    "Bluetooth Earbuds Noise Cancellation", "Mini Massager Gun Portable",
    "Handheld Fan USB Rechargeable", "LED Flashlight USB-C Zoomable",
    "Phone Screen Magnifier HD", "Mini Air Cooler 3-Speed",
    "LED Table Lamp Touch", "Zafarani Freckle Cream Serum",
    "Whitening Zafarani Cream Set of 2", "Brightening Facial Kit Rice Extract",
    "Hair Curler Straightener 5-in-1", "Makeup Skincare Bundle 3-in-1",
    "Premium Skincare Set 5-in-1", "Wellice Onion Shampoo",
    "Teeth Whitening Toothpaste", "Iconic London Highlighter",
    "Apple Shape Manicure Kit 8 Pcs", "Bridal Makeup Kit 19-in-1",
    "Makeup Set 16-in-1", "Floral Perfume Janan Zarar",
    "Colorful Charm Bracelet", "Mens Ring Set of 3",
    "Heart Love Watch Women", "Skeleton Chronograph Watch",
    "RALEX Gold Plated Watch", "Croc Leather Wallet Men",
    "PU Leather Crossbody Bag", "Crossbody Bag Rose Gold Chain",
    "Manual Food Chopper", "Nano Tape Reusable",
    "Quilted Microwave Cover", "Vibrant Wall Stickers",
    "Back Bath Scrubber Belt", "Dri-Fit Track Suit 2pc",
    "Printed Polyester T-Shirt", "Knitted Zip Cardigan",
]

B = ["YourMart"] * 40
B[17] = "Wellice"
B[19] = "Iconic London"
B[23] = "Janan Zarar"
B[28] = "RALEX"

P = [1050,1100,1400,1300,980,3000,1000,650,600,2750,700,900,1250,900,3450,1350,2200,640,720,550,900,2600,1850,900,1400,580,680,2800,1500,620,1200,1450,900,490,550,460,530,1200,590,3700]
O = [1200,1300,1650,1550,1200,3500,1200,800,750,3200,850,1100,1500,1100,4000,1600,2600,800,900,700,1100,3100,2200,1100,1700,700,850,3300,1800,800,1450,1700,1100,600,700,580,650,1450,750,4200]
R = [5.0,5.0,5.0,5.0,5.0,5.0,4.3,5.0,5.0,3.9,5.0,4.9,5.0,5.0,5.0,5.0,5.0,5.0,4.6,5.0,4.2,5.0,5.0,4.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,4.8]
V = [24,18,42,85,120,55,38,30,65,28,45,180,95,72,88,110,65,200,90,35,75,95,60,150,42,55,38,48,62,80,45,32,130,200,55,85,40,95,110,35]
S = [35,30,25,50,60,20,40,45,35,15,30,50,40,35,20,45,25,60,55,20,40,18,25,30,40,25,15,20,35,20,18,40,60,35,50,25,30,50,15]
C = {
    1:"electronics", 2:"electronics", 3:"electronics", 4:"electronics", 5:"electronics",
    6:"sports-fitness", 7:"electronics", 8:"electronics", 9:"electronics", 10:"home-lifestyle",
    11:"home-lifestyle", 12:"beauty", 13:"beauty", 14:"beauty", 15:"beauty",
    16:"beauty", 17:"beauty", 18:"beauty", 19:"beauty", 20:"beauty",
    21:"beauty", 22:"beauty", 23:"beauty", 24:"fragrance", 25:"watches-bags",
    26:"watches-bags", 27:"watches-bags", 28:"watches-bags", 29:"watches-bags", 30:"watches-bags",
    31:"watches-bags", 32:"watches-bags", 33:"kitchen", 34:"home-lifestyle",
    35:"kitchen", 36:"home-lifestyle", 37:"home-lifestyle", 38:"mens-fashion",
    39:"mens-fashion", 40:"mens-fashion",
}

L = []
for i in range(40):
    p = i + 1
    im = g3(C[p], p * 2)
    is_ = ",".join(f"'{u}'" for u in im)
    tg = "trending:true" if (p <= 11 or p >= 25) else "featured:true,bestSeller:true"
    L.append(
        f"  P({p},'{N[i]}','{B[i]}','{C[p]}',"
        f"{P[i]},{O[i]},{R[i]},{V[i]},{S[i]},"
        f"['{is_}'],{{{tg}}}),"
    )

new_ct = ct[: m.start(1)] + "\n".join(L) + "\n" + ct[m.end(2):]
with open(DATA_FILE, "w") as f:
    f.write(new_ct)
print(f"OK {len(L)} products added")