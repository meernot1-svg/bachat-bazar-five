#!/usr/bin/env python3
"""
Add 40 products to data.ts with:
- Correct names, increased prices (+100-200 PKR)
- 3 images per product from existing image pool (smart keyword matched)
- Proper categories, ratings, descriptions
- Source URL field
"""
import json, re, os

DATA_FILE = "/home/z/my-project/src/lib/data.ts"
CAT_IMAGES = "/home/z/my-project/img_results/all_images.json"
PROD_IMAGES = "/home/z/my-project/img_results/product_images_progress.json"

with open(CAT_IMAGES) as f:
    cat_imgs = json.load(f)
with open(PROD_IMAGES) as f:
    prod_imgs = json.load(f)

# Collect all available images with their source category
all_pool = []
for cat, urls in cat_imgs.items():
    for url in urls:
        all_pool.append((url, cat))

def get_images_for_product(name, category, count=3):
    """Smart keyword-based image selection."""
    name_lower = name.lower()
    
    # Keyword scoring for categories
    KEYWORDS = {
        'electronics': ['earbuds','bluetooth','earphone','headphone','speaker','camera','flashlight','magnifier','phone','charger','cable'],
        'beauty': ['cream','serum','freckle','whitening','facial','skincare','highlighter','makeup','manicure','bridal','perfume','fragrance','shampoo','toothpaste','teeth'],
        'hair-care': ['hair','curler','straightener','shampoo'],
        'watches-bags': ['bracelet','ring','watch','wallet','bag','crossbody'],
        'home-lifestyle': ['chopper','tape','cover','sticker','scrubber','lamp','cooler','table','fan'],
        'mens-fashion': ['track suit','cardigan','t-shirt','shirt'],
        'sports-fitness': ['massager','massage'],
    }
    
    # Score categories
    scores = {}
    for cat, keywords in KEYWORDS.items():
        for kw in keywords:
            if kw in name_lower:
                scores[cat] = scores.get(cat, 0) + 1
    
    scores[category] = scores.get(category, 0) + 0.5
    
    # Get images from top scoring categories
    sorted_cats = sorted(scores.keys(), key=lambda c: scores[c], reverse=True)
    pool = []
    for cat in sorted_cats:
        if cat in cat_imgs:
            for url in cat_imgs[cat]:
                if url not in pool:
                    pool.append(url)
        if len(pool) >= count * 2:
            break
    
    if not pool:
        pool = cat_imgs.get(category, cat_imgs.get('electronics', []))
    
    # Select evenly spaced images for variety
    if pool:
        step = max(1, len(pool) // count)
        return [pool[i * step % len(pool)] for i in range(count)]
    return [f"https://picsum.photos/seed/{name[:10]}/800/800"] * count

# Define all 40 products with INCREASED prices
PRODUCTS = [
    # Gadgets & Electronics
    {"id":1, "name":"Rechargeable Eyebrow Trimmer w/ Cleaning Brushes", "brand":"YourMart", "cat":"electronics", "price":1050, "old":1200, "rating":5.0, "reviews":24, "stock":35, "source":"https://yourmart.pk", "desc":"Electric rechargeable eyebrow trimmer with cleaning brushes. USB rechargeable, painless precise trimming. Includes multiple heads for eyebrows, facial hair, and nose hair. LED indicator, compact design.", "features":["USB Rechargeable","Painless trimming","Multiple heads included","LED indicator","Cleaning brushes included"], "specs":{"Brand":"YourMart","Type":"Eyebrow Trimmer","Power":"USB Rechargeable","Heads":"3 interchangeable","Use":"Face, Eyebrows, Nose"}},
    {"id":2, "name":"Rechargeable Eyebrow Trimmer Pink Glitter", "brand":"YourMart", "cat":"electronics", "price":1100, "old":1300, "rating":5.0, "reviews":18, "stock":30, "source":"https://yourmart.pk", "desc":"Stylish pink glitter rechargeable eyebrow trimmer for women. USB-C fast charging, LED display, ergonomic grip. Safe and painless facial hair removal.", "features":["Pink glitter design","USB-C charging","LED display","Ergonomic grip","Safe & painless"], "specs":{"Brand":"YourMart","Color":"Pink Glitter","Charging":"USB-C","Battery":"Built-in Li-ion"}},
    {"id":3, "name":"A9 1080P WiFi Mini Security Camera Night Vision", "brand":"YourMart", "cat":"electronics", "price":1400, "old":1650, "rating":5.0, "reviews":42, "stock":25, "source":"https://yourmart.pk", "desc":"Compact 1080P HD WiFi security camera with night vision. Motion detection, two-way audio, mobile app control. Perfect for home and office security.", "features":["1080P Full HD","WiFi Connected","Night Vision IR","Motion Detection","Two-way Audio","Mobile App Control"], "specs":{"Brand":"YourMart","Resolution":"1080P HD","Connectivity":"WiFi","Night Vision":"Yes","Audio":"Two-way","Power":"USB"}},
    {"id":4, "name":"Premium Wireless Earbuds Bluetooth 5.3", "brand":"YourMart", "cat":"electronics", "price":1300, "old":1550, "rating":5.0, "reviews":85, "stock":50, "source":"https://yourmart.pk", "desc":"Premium TWS wireless earbuds with Bluetooth 5.3. Touch controls, bass boost, noise isolation. Long battery life with charging case.", "features":["Bluetooth 5.3","Touch Controls","Bass Boost","Noise Isolation","Long Battery","Charging Case"], "specs":{"Brand":"YourMart","Bluetooth":"5.3","Battery":"35H with case","Charging":"USB-C","Driver":"13mm","Waterproof":"IPX5"}},
    {"id":5, "name":"Wireless Bluetooth 5.3 Earbuds Noise Cancellation", "brand":"YourMart", "cat":"electronics", "price":980, "old":1200, "rating":5.0, "reviews":120, "stock":60, "source":"https://yourmart.pk", "desc":"Bluetooth 5.3 wireless earbuds with active noise cancellation. Deep bass, clear calls, comfortable fit. LED battery display on case.", "features":["Active Noise Cancellation","Bluetooth 5.3","LED Display","Deep Bass","Clear Calls","Comfortable Fit"], "specs":{"Brand":"YourMart","ANC":"Yes","Bluetooth":"5.3","Display":"LED","Battery":"30H total","Driver":"12mm"}},
    {"id":6, "name":"Mini Massager Gun Portable", "brand":"YourMart", "cat":"sports-fitness", "price":3000, "old":3500, "rating":5.0, "reviews":55, "stock":20, "source":"https://yourmart.pk", "desc":"Compact mini massage gun for deep tissue muscle relief. 4 massage heads, multiple speed levels. Rechargeable battery, ultra-quiet motor.", "features":["4 Massage Heads","Multiple Speeds","Rechargeable","Ultra-Quiet","Portable Design","Deep Tissue"], "specs":{"Brand":"YourMart","Speeds":"6 levels","Heads":"4 interchangeable","Battery":"Rechargeable Li-ion","Noise":"<45dB","Weight":"350g"}},
    {"id":7, "name":"Mini Handheld Fan USB Rechargeable", "brand":"YourMart", "cat":"electronics", "price":1000, "old":1200, "rating":4.3, "reviews":38, "stock":40, "source":"https://yourmart.pk", "desc":"Portable mini handheld fan with USB rechargeable battery. 3 speed settings, 180-degree rotation. Perfect for outdoor activities and travel.", "features":["USB Rechargeable","3 Speed Settings","180° Rotation","Portable","Quiet Motor","LED Indicator"], "specs":{"Brand":"YourMart","Speeds":"3 levels","Battery":"2000mAh","Charging":"USB","Rotation":"180°","Weight":"150g"}},
    {"id":8, "name":"Rechargeable LED Flashlight USB-C", "brand":"YourMart", "cat":"electronics", "price":650, "old":800, "rating":5.0, "reviews":30, "stock":45, "source":"https://yourmart.pk", "desc":"High-power LED rechargeable flashlight with USB-C charging. Zoomable focus, multiple modes (high/low/SOS). Aircraft-grade aluminum body, waterproof.", "features":["USB-C Charging","Zoomable Focus","Multiple Modes","Waterproof","Aluminum Body","High Power LED"], "specs":{"Brand":"YourMart","Power":"LED","Charging":"USB-C","Modes":"High/Low/SOS/Strobe","Material":"Aluminum Alloy","Waterproof":"IPX4"}},
    {"id":9, "name":"Phone Screen Magnifier Video Amplifier", "brand":"YourMart", "cat":"electronics", "price":600, "old":750, "rating":5.0, "reviews":65, "stock":35, "source":"https://yourmart.pk", "desc":"HD phone screen magnifier with 3D zoom lens. Enlarges phone screen 2-4x for movies and videos. Foldable design, no battery needed.", "features":["3D HD Lens","2-4x Magnification","Foldable Design","No Battery Needed","Universal Compatibility","Eye Protection"], "specs":{"Brand":"YourMart","Magnification":"2-4x","Lens":"Acrylic HD","Compatibility":"All smartphones","Design":"Foldable portable","Screen":"12 inch"}},
    {"id":10, "name":"Mini Air Cooler 3-Speed with Perfume", "brand":"YourMart", "cat":"home-lifestyle", "price":2750, "old":3200, "rating":3.9, "reviews":28, "stock":15, "source":"https://yourmart.pk", "desc":"Portable mini air cooler with 3-speed fan and perfume/diffuser feature. USB powered, add ice for extra cooling. Perfect for personal use.", "features":["3 Speed Settings","Perfume/Diffuser","USB Powered","Ice Compatible","LED Lights","Portable Design"], "specs":{"Brand":"YourMart","Speeds":"3 levels","Power":"USB/Adapter","Water Tank":"500ml","Features":"Perfume diffuser","Size":"Compact"}},
    {"id":11, "name":"LED Table Lamp Desk Lamp Touch Control", "brand":"YourMart", "cat":"home-lifestyle", "price":700, "old":850, "rating":5.0, "reviews":45, "stock":30, "source":"https://yourmart.pk", "desc":"Modern LED desk lamp with touch control. 3 color temperatures, adjustable brightness. Eye-caring LED, USB charging port. Foldable design.", "features":["Touch Control","3 Color Temperatures","Adjustable Brightness","Eye-Caring LED","USB Charging Port","Foldable Design"], "specs":{"Brand":"YourMart","LED":"Eye-Caring","Colors":"3 temperatures","Power":"USB","Control":"Touch","Material":"ABS + Metal"}},

    # Beauty & Care
    {"id":12, "name":"Zafarani Freckle Cream Glutathione Serum", "brand":"YourMart", "cat":"beauty", "price":900, "old":1100, "rating":4.9, "reviews":180, "stock":50, "source":"https://yourmart.pk", "desc":"Zafarani freckle cream with glutathione serum for skin whitening. Removes dark spots, freckles, and pigmentation. Natural ingredients, suitable for all skin types.", "features":["Glutathione Serum","Freckle Removal","Dark Spot Treatment","Natural Ingredients","All Skin Types","Fast Results"], "specs":{"Brand":"YourMart","Type":"Freckle Cream","Key Ingredient":"Glutathione","Size":"30g","Skin Type":"All types","Results":"2-4 weeks"}},
    {"id":13, "name":"Whitening Zafarani Cream Set of 2", "brand":"YourMart", "cat":"beauty", "price":1250, "old":1500, "rating":5.0, "reviews":95, "stock":40, "source":"https://yourmart.pk", "desc":"Pack of 2 Zafarani whitening creams for skin brightening and spot removal. Visible results in 2 weeks. Natural formula with vitamin C and glutathione.", "features":["Set of 2","Skin Whitening","Spot Removal","Vitamin C","Glutathione","Natural Formula"], "specs":{"Brand":"YourMart","Quantity":"2 pieces","Size":"30g each","Key Ingredients":"Vitamin C, Glutathione","Results":"2 weeks","Skin Type":"All"}},
    {"id":14, "name":"Whitening Brightening Facial Kit Rice Extract", "brand":"YourMart", "cat":"beauty", "price":900, "old":1100, "rating":5.0, "reviews":72, "stock":35, "source":"https://yourmart.pk", "desc":"Complete facial kit with rice extract for skin whitening and brightening. Includes cleanser, scrub, mask, and serum. Korean beauty formula.", "features":["Rice Extract","Complete Kit","Skin Whitening","Brightening","Korean Formula","4-Step System"], "specs":{"Brand":"YourMart","Type":"Facial Kit","Key Ingredient":"Rice Extract","Steps":"4 steps","Origin":"Korean Formula","Skin Type":"All"}},
    {"id":15, "name":"5-in-1 Hair Curler and Straightener", "brand":"YourMart", "cat":"beauty", "price":3450, "old":4000, "rating":5.0, "reviews":88, "stock":20, "source":"https://yourmart.pk", "desc":"Professional 5-in-1 hair styling tool. Curl, straighten, crimp, and wave. Ceramic plates, fast heat-up, adjustable temperature.", "features":["5-in-1 Styling","Ceramic Plates","Fast Heat-up","Adjustable Temp","Auto Shut-off","360° Swivel Cord"], "specs":{"Brand":"YourMart","Functions":"5 in 1","Plates":"Ceramic","Temp Range":"130-230°C","Heat-up":"30 seconds","Cord":"360° Swivel 2m"}},
    {"id":16, "name":"3-in-1 Makeup and Skincare Bundle", "brand":"YourMart", "cat":"beauty", "price":1350, "old":1600, "rating":5.0, "reviews":110, "stock":45, "source":"https://yourmart.pk", "desc":"Complete 3-in-1 makeup and skincare bundle. Includes foundation, lipstick set, and skincare essentials. Perfect gift set for women.", "features":["3-in-1 Bundle","Makeup + Skincare","Gift Ready","Premium Quality","All Essentials Included","Compact Case"], "specs":{"Brand":"YourMart","Type":"Makeup Bundle","Pieces":"3-in-1","Gift":"Yes","Quality":"Premium","Case":"Included"}},
    {"id":17, "name":"5-in-1 Premium Skincare Set", "brand":"YourMart", "cat":"beauty", "price":2200, "old":2600, "rating":5.0, "reviews":65, "stock":25, "source":"https://yourmart.pk", "desc":"Premium 5-in-1 skincare routine set. Cleanser, toner, serum, moisturizer, and sunscreen. Korean beauty formulation for radiant skin.", "features":["5-in-1 Routine","Korean Formula","Complete Skincare","Cleanser + Toner + Serum + Moisturizer + SPF","Premium Ingredients","All Skin Types"], "specs":{"Brand":"YourMart","Steps":"5 steps","Origin":"Korean Formula","Skin Type":"All","SPF":"Included","Size":"Travel Size"}},
    {"id":18, "name":"Wellice Onion Anti-Hair Loss Shampoo", "brand":"Wellice", "cat":"beauty", "price":640, "old":800, "rating":4.6, "reviews":200, "stock":60, "source":"https://yourmart.pk", "desc":"Wellice onion shampoo for anti-hair loss and hair growth. Enriched with onion extract and biotin. Strengthens hair roots, reduces hair fall.", "features":["Onion Extract","Anti-Hair Loss","Biotin Enriched","Strengthens Roots","Reduces Hair Fall","Sulfate Free"], "specs":{"Brand":"Wellice","Size":"400ml","Key Ingredient":"Onion Extract","Additional":"Biotin","Sulfate Free":"Yes","Hair Type":"All"}},
    {"id":19, "name":"Nano Hydroxyapatite Teeth Whitening Toothpaste", "brand":"YourMart", "cat":"beauty", "price":720, "old":900, "rating":5.0, "reviews":90, "stock":55, "source":"https://yourmart.pk", "desc":"Professional teeth whitening toothpaste with nano hydroxyapatite. Removes stains, strengthens enamel, freshens breath. Safe for daily use.", "features":["Nano Hydroxyapatite","Teeth Whitening","Enamel Strength","Stain Removal","Fresh Breath","Daily Use Safe"], "specs":{"Brand":"YourMart","Key Ingredient":"Nano Hydroxyapatite","Size":"100g","Whitening":"Professional Grade","Safe":"Daily Use","Flavor":"Mint"}},
    {"id":20, "name":"Iconic London Highlighter 3 Shades", "brand":"Iconic London", "cat":"beauty", "price":550, "old":700, "rating":4.2, "reviews":35, "stock":20, "source":"https://www.markaz.app/shop", "desc":"Iconic London highlighter palette with 3 stunning shades. Illuminating shimmer for face and body. Long-lasting, buildable formula.", "features":["3 Shades","Illuminating Shimmer","Face & Body","Long-Lasting","Buildable","Premium Formula"], "specs":{"Brand":"Iconic London","Shades":"3","Finish":"Shimmer","Longevity":"Long-lasting","Use":"Face & Body","Size":"Compact"}},
    {"id":21, "name":"8 Pcs Apple Shape Manicure Kit", "brand":"YourMart", "cat":"beauty", "price":900, "old":1100, "rating":5.0, "reviews":75, "stock":40, "source":"https://yourmart.pk", "desc":"Apple-shaped 8-piece manicure and pedicure kit. Includes nail clipper, file, cuticle pusher, tweezers, and more. Cute compact design.", "features":["8 Essential Tools","Apple Shape Design","Nail Clipper & File","Cuticle Pusher","Tweezers Included","Compact Case"], "specs":{"Brand":"YourMart","Pieces":"8","Design":"Apple Shape","Material":"Stainless Steel","Case":"Compact","Use":"Manicure & Pedicure"}},
    {"id":22, "name":"19-in-1 Bridal Makeup Kit Complete Set", "brand":"YourMart", "cat":"beauty", "price":2600, "old":3100, "rating":5.0, "reviews":95, "stock":18, "source":"https://yourmart.pk", "desc":"Complete 19-in-1 bridal makeup kit with all essentials. Includes foundations, lipsticks, eyeshadows, brushes, and more. Premium quality for perfect bridal look.", "features":["19 Pieces Complete","Bridal Special","Foundation + Lipstick + Eyeshadow","Brushes Included","Premium Quality","Gift Box Packaging"], "specs":{"Brand":"YourMart","Pieces":"19","Occasion":"Bridal","Quality":"Premium","Packaging":"Gift Box","Includes":"Brushes"}},
    {"id":23, "name":"16-in-1 Makeup Set Professional", "brand":"YourMart", "cat":"beauty", "price":1850, "old":2200, "rating":4.0, "reviews":60, "source":"https://yourmart.pk", "desc":"Professional 16-in-1 makeup set with palettes, brushes, and tools. Complete makeup solution for daily use and special occasions.", "features":["16 Pieces","Professional Quality","Color Palettes","Brushes Included","Multi-Use","Compact Design"], "specs":{"Brand":"YourMart","Pieces":"16","Type":"Professional Set","Includes":"Palettes + Brushes","Quality":"Professional","Case":"Included"}},
    {"id":24, "name":"Unisex Floral Perfume Pack Janan Zarar", "brand":"Janan Zarar", "cat":"beauty", "price":900, "old":1100, "rating":5.0, "reviews":150, "stock":35, "source":"https://yourmart.pk", "desc":"Janan Zarar unisex floral perfume pack. Long-lasting fragrance with premium notes. Perfect for daily wear and gifting.", "features":["Unisex Floral","Long-Lasting","Premium Notes","Daily Wear","Gift Ready","Pack of 1"], "specs":{"Brand":"Janan Zarar","Type":"Eau de Parfum","Scent":"Floral","Longevity":"8+ hours","Gender":"Unisex","Size":"50ml"}},

    # Fashion Accessories
    {"id":25, "name":"Colorful Charm Bracelet Women", "brand":"YourMart", "cat":"watches-bags", "price":1400, "old":1700, "rating":5.0, "reviews":42, "stock":30, "source":"https://www.markaz.app/shop", "desc":"Stunning colorful charm bracelet for women. Premium alloy with crystal charms. Adjustable size, tarnish-resistant, perfect for gifting.", "features":["Colorful Charms","Crystal Stones","Adjustable Size","Tarnish Resistant","Premium Alloy","Gift Ready"], "specs":{"Brand":"YourMart","Type":"Charm Bracelet","Material":"Alloy + Crystal","Adjustable":"Yes","Color":"Multi-color","Gender":"Women"}},
    {"id":26, "name":"Turkish-Inspired Mens Ring Set of 3", "brand":"YourMart", "cat":"watches-bags", "price":580, "old":700, "rating":5.0, "reviews":55, "stock":40, "source":"https://www.markaz.app/shop", "desc":"Set of 3 Turkish-inspired men's rings. Stainless steel with premium finish. Various Ottoman-inspired designs, comfortable fit.", "features":["Set of 3 Rings","Turkish Design","Stainless Steel","Premium Finish","Comfortable Fit","Ottoman Inspired"], "specs":{"Brand":"YourMart","Quantity":"3 pieces","Material":"Stainless Steel","Style":"Turkish/Ottoman","Finish":"Premium","Sizes":"Adjustable"}},
    {"id":27, "name":"Stainless Steel Heart Love Watch Women", "brand":"YourMart", "cat":"watches-bags", "price":680, "old":850, "rating":5.0, "reviews":38, "stock":25, "source":"https://www.markaz.app/shop", "desc":"Elegant stainless steel heart-shaped love watch for women. Quartz movement, adjustable band. Beautiful heart dial design, perfect gift.", "features":["Heart Shape Design","Stainless Steel","Quartz Movement","Adjustable Band","Elegant Look","Gift Perfect"], "specs":{"Brand":"YourMart","Dial":"Heart Shape","Movement":"Quartz","Material":"Stainless Steel","Band":"Adjustable","Water Resistant":"Yes"}},
    {"id":28, "name":"Black Skeleton Chronograph Watch Men", "brand":"YourMart", "cat":"watches-bags", "price":2800, "old":3300, "rating":5.0, "reviews":48, "stock":15, "source":"https://www.markaz.app/shop", "desc":"Premium black skeleton chronograph watch for men. See-through dial, stainless steel band. Japanese movement, luminous hands.", "features":["Skeleton Dial","Chronograph","Stainless Steel Band","Japanese Movement","Luminous Hands","See-Through Design"], "specs":{"Brand":"YourMart","Dial":"Skeleton","Movement":"Japanese Quartz","Band":"Stainless Steel","Chronograph":"Yes","Water Resistant":"3ATM"}},
    {"id":29, "name":"RALEX Gold Plated Watch Men Luxury", "brand":"RALEX", "cat":"watches-bags", "price":1500, "old":1800, "rating":5.0, "reviews":62, "stock":20, "source":"https://www.markaz.app/shop", "desc":"RALEX luxury gold plated watch for men. Premium finish, leather strap. Elegant design suitable for formal and casual wear.", "features":["Gold Plated","RALEX Brand","Leather Strap","Luxury Design","Japanese Movement","Formal & Casual"], "specs":{"Brand":"RALEX","Plating":"Gold","Strap":"Genuine Leather","Movement":"Japanese Quartz","Dial":"Premium","Style":"Luxury"}},
    {"id":30, "name":"Premium Croc Embossed Leather Wallet Men", "brand":"YourMart", "cat":"watches-bags", "price":620, "old":800, "rating":5.0, "reviews":80, "stock":35, "source":"https://www.markaz.app/shop", "desc":"Premium crocodile embossed genuine leather wallet for men. Multiple card slots, RFID blocking. Slim design, gift box included.", "features":["Croc Embossed","Genuine Leather","RFID Blocking","Multiple Card Slots","Slim Design","Gift Box"], "specs":{"Brand":"YourMart","Material":"Genuine Leather","Pattern":"Croc Embossed","RFID":"Blocking","Card Slots":"8+","Size":"Slim Bifold"}},
    {"id":31, "name":"Mustard PU Leather Crossbody Bag", "brand":"YourMart", "cat":"watches-bags", "price":1200, "old":1450, "rating":5.0, "reviews":45, "stock":20, "source":"https://www.markaz.app/shop", "desc":"Stylish mustard yellow PU leather crossbody bag. Adjustable strap, multiple compartments. Perfect for daily use and casual outings.", "features":["Mustard Yellow","PU Leather","Crossbody Style","Adjustable Strap","Multiple Pockets","Compact Design"], "specs":{"Brand":"YourMart","Color":"Mustard Yellow","Material":"PU Leather","Style":"Crossbody","Strap":"Adjustable","Compartments":"3+"}},
    {"id":32, "name":"Green Crossbody Bag Rose Gold Chain", "brand":"YourMart", "cat":"watches-bags", "price":1450, "old":1700, "rating":4.6, "reviews":32, "stock":18, "source":"https://www.markaz.app/shop", "desc":"Elegant green crossbody bag with rose gold chain strap. Premium PU leather, spacious interior. Perfect for parties and formal occasions.", "features":["Green Color","Rose Gold Chain","Premium PU Leather","Spacious Interior","Elegant Design","Party Ready"], "specs":{"Brand":"YourMart","Color":"Green","Chain":"Rose Gold","Material":"Premium PU Leather","Style":"Crossbody","Occasion":"Party/Formal"}},

    # Home & Practical
    {"id":33, "name":"Manual Food Chopper Vegetable Cutter", "brand":"YourMart", "cat":"kitchen", "price":900, "old":1100, "rating":5.0, "reviews":130, "stock":40, "source":"https://www.markaz.app/shop", "desc":"Manual food chopper for quick vegetable and fruit cutting. Sharp stainless steel blades, BPA-free container. Pull-string mechanism, easy to clean.", "features":["Manual Operation","Stainless Steel Blades","BPA-Free Container","Pull String","Easy to Clean","Compact Design"], "specs":{"Brand":"YourMart","Type":"Manual Chopper","Blades":"Stainless Steel","Capacity":"900ml","Material":"BPA-Free PP","Dishwasher Safe":"Yes"}},
    {"id":34, "name":"Nano Tape Reusable Home Organization", "brand":"YourMart", "cat":"home-lifestyle", "price":490, "old":600, "rating":5.0, "reviews":200, "stock":60, "source":"https://www.markaz.app/shop", "desc":"Reusable nano magic tape for home organization. Strong adhesion, leaves no residue. Works on walls, glass, tiles. Washable and reusable.", "features":["Reusable","Strong Adhesion","No Residue","Multi-Surface","Washable","Transparent"], "specs":{"Brand":"YourMart","Type":"Nano Tape","Adhesion":"Strong","Reusable":"Yes","Washable":"Yes","Size":"3m x 3cm"}},
    {"id":35, "name":"Quilted Microwave Cover", "brand":"YourMart", "cat":"kitchen", "price":550, "old":700, "rating":4.3, "reviews":55, "stock":35, "source":"https://www.markaz.app/shop", "desc":"Quilted cotton microwave cover with beautiful print. Protects microwave from dust and splatters. Machine washable, easy to fit.", "features":["Quilted Cotton","Dust Protection","Splash Guard","Machine Washable","Easy Fit","Beautiful Print"], "specs":{"Brand":"YourMart","Material":"Quilted Cotton","Size":"Standard Microwave","Washable":"Machine Wash","Design":"Printed","Protection":"Dust + Splash"}},
    {"id":36, "name":"Vibrant Wall Stickers Room Decor", "brand":"YourMart", "cat":"home-lifestyle", "price":460, "old":580, "rating":5.0, "reviews":85, "stock":50, "source":"https://www.markaz.app/shop", "desc":"Vibrant and colorful wall stickers for room decoration. Self-adhesive, waterproof, removable. Multiple designs available for living room, bedroom, and kids room.", "features":["Self-Adhesive","Waterproof","Removable","Multiple Designs","Easy to Apply","Vibrant Colors"], "specs":{"Brand":"YourMart","Type":"Wall Sticker","Material":"Vinyl","Waterproof":"Yes","Removable":"Yes","Application":"Smooth Surfaces"}},
    {"id":37, "name":"Silicone Back Bath Scrubber Belt", "brand":"YourMart", "cat":"home-lifestyle", "price":530, "old":650, "rating":4.0, "reviews":40, "source":"https://www.markaz.app/shop", "desc":"Silicone back scrubber belt for easy bath cleaning. Extended handle reaches all areas. Soft silicone bristles, comfortable grip, hangable design.", "features":["Silicone Bristles","Extended Handle","Comfortable Grip","Hangable","Easy to Clean","Gentle on Skin"], "specs":{"Brand":"YourMart","Material":"Silicone","Handle":"Extended","Bristles":"Soft Silicone","Design":"Ergonomic","Storage":"Hangable"}},

    # Apparel
    {"id":38, "name":"Mens Dri-Fit Track Suit 2pc", "brand":"YourMart", "cat":"mens-fashion", "price":1200, "old":1450, "rating":5.0, "reviews":95, "stock":30, "source":"https://www.markaz.app/shop", "desc":"Men's premium dri-fit track suit in 2 pieces. Quick-dry fabric, comfortable fit. Available in multiple colors, perfect for gym and casual wear.", "features":["Dri-Fit Fabric","2 Piece Set","Quick Dry","Comfortable Fit","Multiple Colors","Gym & Casual"], "specs":{"Brand":"YourMart","Type":"Track Suit","Pieces":"2 (Jacket + Pants)","Fabric":"Dri-Fit Polyester","Fit":"Regular","Sizes":"M, L, XL, XXL"}},
    {"id":39, "name":"Unisex Printed Polyester T-Shirt", "brand":"YourMart", "cat":"mens-fashion", "price":590, "old":750, "rating":5.0, "reviews":110, "stock":50, "source":"https://www.markaz.app/shop", "desc":"Premium printed polyester t-shirt, unisex design. Soft fabric, durable print. Available in multiple prints and colors, casual everyday wear.", "features":["Unisex Design","Premium Print","Soft Fabric","Durable Print","Multiple Options","Casual Wear"], "specs":{"Brand":"YourMart","Material":"Polyester","Print":"Premium DTF","Fit":"Regular","Sizes":"S, M, L, XL, XXL","Care":"Machine Wash"}},
    {"id":40, "name":"Mens Knitted Zip-Up Cardigan Sweater", "brand":"YourMart", "cat":"mens-fashion", "price":3700, "old":4200, "rating":4.8, "reviews":35, "source":"https://www.markaz.app/shop", "desc":"Premium men's knitted zip-up cardigan. Soft warm fabric, full zip front. Perfect for winter, casual and semi-formal occasions.", "features":["Knitted Fabric","Full Zip","Soft & Warm","Premium Quality","Winter Essential","Versatile Style"], "specs":{"Brand":"YourMart","Type":"Cardigan","Material":"Knitted Acrylic Blend","Closure":"Full Zip","Fit":"Regular","Season":"Winter"}},
]

# Generate P() calls
lines = []
lines.append("")
lines.append("// ══════════ Trending Products from YourMart.pk & Markaz.app ══════════")
lines.append("")

for p in PRODUCTS:
    imgs = get_images_for_product(p['name'], p['cat'], 3)
    img_str = ",".join(f"'{u}'" for u in imgs)
    
    tags = []
    if p['id'] <= 11: tags.append("trending:true")
    if p['id'] >= 12 and p['id'] <= 24: tags.append("featured:true,bestSeller:true")
    if p['id'] >= 38: tags.append("trending:true")
    
    opts_parts = []
    if tags: opts_parts.append(tags[0])
    
    desc = p['desc'].replace("'", "\\'")
    feats = ",".join(f"'{f}'" for f in p['features'])
    specs = ",".join(f"'{k}':'{v}'" for k,v in p['specs'].items())
    
    opts = "{" + ",".join([f"description:'{desc}'",f"features:[{feats}]",f"specs:{{{specs}}}",f"trending:true"]) + "}"
    
    line = f"  P({p['id']},'{p['name']}','{p['brand']}','{p['cat']}',{p['price']},{p['old']},{p['rating']},{p['reviews']},{p['stock']},['{img_str}'],{opts}),"
    lines.append(line)

product_code = "\n".join(lines)

# Update data.ts
with open(DATA_FILE) as f:
    content = f.read()

# Find the empty PRODUCTS array and replace
old = "export const PRODUCTS: Product[] = [\n  // Products cleared — add new products via Admin Panel\n];"
new = "export const PRODUCTS: Product[] = [" + product_code + "\n];"

if old in content:
    content = content.replace(old, new)
    with open(DATA_FILE, 'w') as f:
        f.write(content)
    print(f"SUCCESS: Added {len(PRODUCTS)} products to data.ts")
else:
    print("ERROR: Could not find empty PRODUCTS array marker")
    print("Looking for alternative...")
    # Try to find and replace
    import re
    m = re.search(r'export const PRODUCTS: Product\[\] = \[\s*//[^\]]*\];', content, re.DOTALL)
    if m:
        content = content[:m.start()] + "export const PRODUCTS: Product[] = [" + product_code + "\n];" + content[m.end():]
        with open(DATA_FILE, 'w') as f:
            f.write(content)
        print(f"SUCCESS (regex): Added {len(PRODUCTS)} products")
    else:
        print("FALLBACK: Could not auto-replace, showing insertion point")
        idx = content.index("export const PRODUCTS")
        print(f"Found at char {idx}")