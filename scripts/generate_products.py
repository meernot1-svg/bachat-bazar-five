#!/usr/bin/env python3
"""Generate new data.ts PRODUCTS array with real images from markaz.app and yourmart.pk"""

# Helper to create markaz image URLs (product-1, product-2, product-3)
def mk(prefix):
    """Generate 3 markaz full-size image URLs from thumbnail prefix"""
    base = f"https://static.markaz.app/pakistan/products/{prefix}-product"
    return [f"{base}-{i}.webp" for i in range(1, 4)]

def mk_content(prefix):
    """For content.public.markaz.app URLs"""
    base = f"https://content.public.markaz.app/markazimagevideo/public/products/{prefix}-product"
    return [f"{base}-{i}.jpg" for i in range(1, 4)]

def mk_gen(prefix_id):
    """For GenerativeMedia URLs - only 1 image available"""
    url = f"https://static.markaz.app/GenerativeMedia/Pakistan/thumbnails/pakistan_{prefix_id}.png"
    return [url, url, url]

def ym(img_url):
    """yourmart image - use same for all 3"""
    return [img_url, img_url, img_url]

def p(id, name, brand, cat, price, old, rating, reviews, imgs, source, **opts):
    """Generate a P() call string"""
    trending = opts.get('trending', False)
    featured = opts.get('featured', False)
    bestseller = opts.get('bestseller', False)
    is_new = opts.get('is_new', False)
    badge = opts.get('badge', '')
    desc = opts.get('desc', f'{name} by {brand}. Available at Bachat Bazar with fast delivery across Pakistan.')
    features = opts.get('features', ['Genuine product','Fast delivery','7-day returns','Quality guaranteed'])
    specs = opts.get('specs', {'Brand': brand, 'Category': cat})

    img_str = ','.join(f"'{i}'" for i in imgs)
    
    opts_parts = []
    if trending: opts_parts.append('trending:true')
    if featured: opts_parts.append('featured:true')
    if bestseller: opts_parts.append('bestSeller:true')
    if is_new: opts_parts.append('isNew:true')
    if badge: opts_parts.append(f"badge:'{badge}'")
    if desc != f'{name} by {brand}. Available at Bachat Bazar with fast delivery across Pakistan.':
        desc_escaped = desc.replace("'", "\\'")
        opts_parts.append(f"description:'{desc_escaped}'")
    if features != ['Genuine product','Fast delivery','7-day returns','Quality guaranteed']:
        feats_str = ','.join(f"'{f}'" for f in features)
        opts_parts.append(f"features:[{feats_str}]")
    if specs != {'Brand': brand, 'Category': cat}:
        specs_str = ','.join(f"'{k}':'{v}'" for k, v in specs.items())
        opts_parts.append(f"specs:{{{specs_str}}}")

    opts_str = ','.join(opts_parts)
    if opts_str:
        opts_str = ',' + opts_str

    name_escaped = name.replace("'", "\\'")
    source_str = f" // Source: {source}"
    
    return f"P({id},'{name_escaped}','{brand}','{cat}',{price},{old},{rating},{reviews},{30 if cat=='womens-fashion' else 40},[{img_str}]{opts_str}),{source_str}"

products = []

# ============================================================
# GADGETS & ELECTRONICS (12 products)
# ============================================================

products.append(p(1, 'Air31 TWS Transparent Earbuds Bluetooth 5.3', 'Markaz', 'electronics', 1220, 1470, 4.5, 78,
    mk('1172-86-481404'), 'markaz.app/shop/product/air31-tws-transparent-earbuds-bluetooth-5-3/481404',
    trending=True, desc='Transparent design TWS earbuds with Bluetooth 5.3. Touch controls, deep bass, 30-hour battery with case. IPX5 water resistant.',
    features=['Bluetooth 5.3', 'Transparent Design', 'Touch Controls', '30H Battery', 'IPX5 Waterproof', 'Charging Case'],
    specs={'Brand': 'Markaz', 'Bluetooth': '5.3', 'Battery': '30H with case', 'Driver': '13mm', 'Waterproof': 'IPX5'}))

products.append(p(2, 'Black Over-Ear Headphones ABS Lightweight', 'Markaz', 'electronics', 1629, 1979, 4.3, 55,
    mk('1518-86-627089'), 'markaz.app/shop/product/black-over-ear-headphones-abs-plastic-lightweight-comfortable/627089',
    trending=True, desc='Lightweight over-ear headphones with deep bass. ABS plastic construction, comfortable padded ear cups. Wired 3.5mm jack.',
    features=['Over-Ear Design', 'Deep Bass', 'Lightweight ABS', 'Padded Ear Cups', '3.5mm Jack', 'Foldable'],
    specs={'Brand': 'Markaz', 'Type': 'Over-Ear Headphones', 'Driver': '40mm', 'Cable': '1.2m 3.5mm', 'Weight': '180g'}))

products.append(p(3, 'Smartwatch Multicolor Metal Silicone Band', 'Markaz', 'electronics', 2054, 2404, 4.4, 92,
    mk('1172-87-608084'), 'markaz.app/shop/product/smartwatch-multicolor-metal-silicone-band-long-battery/608084',
    trending=True, featured=True, desc='Smart fitness watch with heart rate monitor, step counter, and sleep tracking. Long battery life, IP68 waterproof.',
    features=['Heart Rate Monitor', 'Step Counter', 'Sleep Tracking', 'IP68 Waterproof', 'Long Battery', 'Multi-Sport Modes'],
    specs={'Brand': 'Markaz', 'Display': '1.69 inch IPS', 'Battery': '7 days', 'Waterproof': 'IP68', 'Connectivity': 'Bluetooth 5.0'}))

products.append(p(4, 'BX-502 AirBuds ENC Wireless Earbuds', 'Markaz', 'electronics', 3540, 3990, 4.6, 65,
    mk_content('1657-86-561715'), 'markaz.app/shop/product/bx-502-airbuds-enc/561715',
    trending=True, desc='Premium TWS earbuds with Environmental Noise Cancellation. Crystal clear calls, deep bass, compact charging case.',
    features=['ENC Noise Cancellation', 'Clear HD Calls', 'Deep Bass', 'Touch Controls', 'Compact Case', 'Fast Charging'],
    specs={'Brand': 'Markaz', 'ANC': 'ENC', 'Bluetooth': '5.2', 'Battery': '28H total', 'Charging': 'USB-C'}))

products.append(p(5, 'Rechargeable LED Torch Light Black Red ABS', 'Markaz', 'electronics', 879, 1029, 4.7, 110,
    mk('1172-116-649022'), 'markaz.app/shop/product/rechargeable-led-torch-light-black-red-abs/649022',
    trending=True, desc='Rechargeable LED torch with zoomable focus. 4 modes: High, Low, SOS, Strobe. USB-C charging, ABS body.',
    features=['USB-C Rechargeable', 'Zoomable Focus', '4 Light Modes', 'ABS Body', 'LED Bulb', 'Water Resistant'],
    specs={'Brand': 'Markaz', 'Power': 'XML-T6 LED', 'Charging': 'USB-C', 'Modes': 'High/Low/SOS/Strobe', 'Material': 'ABS Plastic'}))

products.append(p(6, 'Rechargeable Crystal Table Lamp Touch Control', 'Markaz', 'home-lifestyle', 1670, 1920, 4.8, 88,
    mk('1172-116-496647'), 'markaz.app/shop/product/rechargeable-crystal-table-lamp-with-touch-control/496647',
    trending=True, desc='Elegant crystal table lamp with touch control. 3 color temperatures, stepless dimming. USB rechargeable, perfect for bedside.',
    features=['Touch Control', '3 Color Temperatures', 'Stepless Dimming', 'Crystal Design', 'USB Rechargeable', 'Eye-Caring LED'],
    specs={'Brand': 'Markaz', 'LED': 'Eye-Caring', 'Colors': 'Warm/Neutral/White', 'Battery': '2000mAh', 'Control': 'Touch'}))

products.append(p(7, 'Smart Bluetooth Headset M11 Mini Compact', 'Markaz', 'electronics', 800, 950, 4.2, 45,
    mk('578-86-387899'), 'markaz.app/shop/product/smart-bluetooth-headset-m11-mini-compact-comfortable-small-and-durable/387899',
    trending=True, desc='Ultra-compact mini Bluetooth headset. Single ear design for calls, lightweight and comfortable. Long battery life.',
    features=['Mini Compact Design', 'Single Ear', 'Bluetooth 5.0', 'Long Battery', 'Comfortable Fit', 'Clear Calls'],
    specs={'Brand': 'Markaz', 'Bluetooth': '5.0', 'Battery': '6H talk time', 'Weight': '8g', 'Charging': 'USB-C'}))

products.append(p(8, 'BX-202 Power Bank 10000mAh', 'Markaz', 'electronics', 4310, 4660, 4.5, 72,
    mk_content('1657-91-584926'), 'markaz.app/shop/product/bx-202-power-bank/584926',
    trending=True, desc='10000mAh power bank with dual USB output. Fast charging, LED indicator, compact design. Charges 2 devices simultaneously.',
    features=['10000mAh Capacity', 'Dual USB Output', 'Fast Charging', 'LED Indicator', 'Compact Design', 'Safety Protection'],
    specs={'Brand': 'Markaz', 'Capacity': '10000mAh', 'Output': 'Dual USB', 'Input': 'USB-C', 'Weight': '220g'}))

products.append(p(9, 'M04 TWS Wireless Earbuds Bluetooth 5.3', 'YourMart', 'electronics', 1050, 1200, 4.4, 95,
    ym('https://admin.yourmart.pk/storage/uploads/inventory/products/media/5_1750942955.jpg'),
    'yourmart.pk/products/m04-tws-wireless-earbuds-bluetooth-53-led-display-bass-sound-fast-charging',
    trending=True, desc='TWS wireless earbuds with Bluetooth 5.3, LED display, and deep bass sound. Fast charging, comfortable in-ear design.',
    features=['Bluetooth 5.3', 'LED Display', 'Deep Bass', 'Fast Charging', 'Comfortable Fit', 'Charging Case'],
    specs={'Brand': 'YourMart', 'Bluetooth': '5.3', 'Display': 'LED', 'Battery': '25H total', 'Driver': '13mm', 'Charging': 'USB-C'}))

products.append(p(10, 'Air 39 Transparent Bluetooth Earbuds ENC', 'YourMart', 'electronics', 825, 975, 4.3, 68,
    ym("https://admin.yourmart.pk/storage/uploads/inventory/products/media/Product'sPictures(19)_1776770521.webp"),
    'yourmart.pk/products/air-39-transparent-bluetooth-earbuds-super-bass-enc-noise-reduction-hd-calling-bluetooth-53',
    trending=True, desc='Transparent design Bluetooth 5.3 earbuds with ENC noise reduction. Super bass, HD calling, LED battery display.',
    features=['ENC Noise Reduction', 'Transparent Design', 'Super Bass', 'HD Calling', 'LED Display', 'Bluetooth 5.3'],
    specs={'Brand': 'YourMart', 'Bluetooth': '5.3', 'ANC': 'ENC', 'Battery': '24H total', 'Waterproof': 'IPX5'}))

products.append(p(11, 'CX16 Magnetic Mobile Cooling Fan RGB', 'YourMart', 'electronics', 2250, 2500, 4.6, 55,
    ym('https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(62)_1781613673.webp'),
    'yourmart.pk/products/cx16-magnetic-mobile-cooling-fan-semiconductor-phone-cooler-with-rgb-lights-fast-cooling-gaming-radiator-for-android-iphone',
    trending=True, isNew=True, desc='Magnetic phone cooling fan with RGB lights. Semiconductor cooling technology, fast heat dissipation for gaming. Works with all phones.',
    features=['Magnetic Attachment', 'Semiconductor Cooling', 'RGB Lights', 'Fast Cooling', 'Universal Fit', 'Low Noise'],
    specs={'Brand': 'CX16', 'Power': '15W', 'Cooling': 'Semiconductor', 'RGB': 'Yes', 'Compatibility': 'All Smartphones'}))

products.append(p(12, 'SQ11 Mini Camera HD 1080P Night Vision', 'YourMart', 'electronics', 1500, 1700, 4.4, 82,
    ym('https://admin.yourmart.pk/storage/uploads/inventory/products/media/Yourmartproducts(15)_1780911799.webp'),
    'yourmart.pk/products/sq11-mini-camera-hd-1080p-night-vision-motion-detection-dvr-camcorder',
    trending=True, desc='Mini portable 1080P HD camera with night vision. Motion detection, loop recording, compact body. Perfect for security.',
    features=['1080P Full HD', 'Night Vision', 'Motion Detection', 'Loop Recording', 'Mini Compact', 'USB Charging'],
    specs={'Brand': 'SQ11', 'Resolution': '1080P', 'Night Vision': 'Yes', 'Storage': 'MicroSD up to 32GB', 'Battery': 'Built-in Li-ion'}))

# ============================================================
# BEAUTY & CARE (14 products)
# ============================================================

products.append(p(13, '19 in 1 Makeup Kit for Pakistani Brides', 'Markaz', 'beauty', 2579, 3029, 4.7, 120,
    mk_gen('644275'), 'markaz.app/shop/product/19-in-1-makeup-kit-for-pakistani-brides-party-goers/644275',
    trending=True, bestseller=True, desc='Complete 19-piece bridal makeup kit with foundations, lipsticks, eyeshadows, brushes. Premium quality in gift box.',
    features=['19 Pieces Complete', 'Bridal Special', 'Foundation + Lipstick + Eyeshadow', 'Brushes Included', 'Premium Quality', 'Gift Box'],
    specs={'Brand': 'Markaz', 'Pieces': '19', 'Occasion': 'Bridal/Party', 'Quality': 'Premium', 'Packaging': 'Gift Box'}))

products.append(p(14, 'Ultimate Makeup Kit 20 Items for Women', 'Markaz', 'beauty', 2220, 2570, 4.6, 95,
    mk_gen('581802'), 'markaz.app/shop/product/ultimate-makeup-kit-20-items-for-women/581802',
    trending=True, bestseller=True, desc='Complete 20-item professional makeup kit. Everything you need for daily wear to party looks in one premium case.',
    features=['20 Items Complete', 'Professional Quality', 'Daily + Party Looks', 'All-in-One Case', 'Premium Brushes', 'Color Palettes'],
    specs={'Brand': 'Markaz', 'Items': '20', 'Type': 'Professional Kit', 'Includes': 'Palettes + Brushes + Tools', 'Quality': 'Premium'}))

products.append(p(15, '16-in-1 Makeup Set for Flawless Wear', 'Markaz', 'beauty', 1750, 2050, 4.5, 88,
    mk_gen('630536'), 'markaz.app/shop/product/16-in-1-makeup-set-for-flawless-long-lasting-wear/630536',
    trending=True, desc='Professional 16-in-1 makeup set with color palettes, brushes, and tools. Long-lasting wear, complete daily and occasion solution.',
    features=['16 Pieces', 'Long-Lasting Formula', 'Color Palettes', 'Brushes Included', 'Compact Case', 'Multi-Use'],
    specs={'Brand': 'Markaz', 'Pieces': '16', 'Type': 'Professional Set', 'Longevity': '8+ hours', 'Quality': 'Premium'}))

products.append(p(16, '4-in-1 Makeup Kit for Brides Daily Wear', 'Markaz', 'beauty', 2060, 2410, 4.4, 72,
    mk('1304-287-555838'), 'markaz.app/shop/product/4-in-1-makeup-kit-for-pakistani-brides-daily-wear/555838',
    trending=True, desc='Compact 4-in-1 makeup kit perfect for brides and daily wear. Foundation, powder, lipstick, and eyeshadow in portable case.',
    features=['4-in-1 Compact', 'Bridal + Daily', 'Portable Case', 'Foundation + Powder + Lipstick + Eyeshadow', 'Mirror Included', 'Travel Friendly'],
    specs={'Brand': 'Markaz', 'Pieces': '4', 'Type': 'Compact Kit', 'Includes': 'Mirror', 'Design': 'Portable'}))

products.append(p(17, 'Whitening Zafarani Cream Set of 2', 'Markaz', 'beauty', 1230, 1430, 4.8, 180,
    mk('1718-77-669889'), 'markaz.app/shop/product/whitening-zafarani-cream-set-of-2-for-all-skin-types/669889',
    trending=True, bestseller=True, featured=True, desc='Pack of 2 Zafarani whitening creams with glutathione. Vitamin C formula for skin brightening and dark spot removal.',
    features=['Set of 2 Creams', 'Glutathione Formula', 'Skin Whitening', 'Dark Spot Removal', 'Vitamin C', 'All Skin Types'],
    specs={'Brand': 'Zafarani', 'Quantity': '2 pieces', 'Size': '30g each', 'Key Ingredient': 'Glutathione + Vitamin C', 'Skin Type': 'All types'}))

products.append(p(18, 'Premium Zafarani Whitening Cream', 'Markaz', 'beauty', 1079, 1279, 4.7, 150,
    mk('700-77-669812'), 'markaz.app/shop/product/premium-zafarani-whitening-cream-for-all-skin-types/669812',
    trending=True, featured=True, desc='Premium Zafarani whitening cream with glutathione for skin brightening. Removes freckles and pigmentation naturally.',
    features=['Glutathione Formula', 'Freckle Removal', 'Dark Spot Treatment', 'Natural Ingredients', 'Visible in 2 Weeks', 'All Skin Types'],
    specs={'Brand': 'Zafarani', 'Type': 'Whitening Cream', 'Key Ingredient': 'Glutathione', 'Size': '30g', 'Skin Type': 'All types'}))

products.append(p(19, '3-in-1 Makeup and Skincare Bundle', 'Markaz', 'beauty', 1319, 1569, 4.6, 135,
    mk('1004-287-618049'), 'markaz.app/shop/product/3-in-1-makeup-skincare-bundle-for-all-skin-types/618049',
    trending=True, bestseller=True, desc='Complete 3-in-1 makeup and skincare bundle. Foundation, lipstick set, and skincare essentials in premium gift case.',
    features=['3-in-1 Bundle', 'Makeup + Skincare', 'Gift Ready Case', 'Premium Quality', 'All Essentials', 'Compact'],
    specs={'Brand': 'Markaz', 'Type': 'Bundle Set', 'Pieces': '3-in-1', 'Gift': 'Premium Case', 'Quality': 'Premium'}))

products.append(p(20, '5-in-1 Premium Skincare Set', 'Markaz', 'beauty', 2169, 2519, 4.8, 110,
    mk('1183-287-647460'), 'markaz.app/shop/product/5-in-1-premium-skincare-set-for-pakistani-skin/647460',
    trending=True, featured=True, desc='Premium 5-step Korean skincare routine. Cleanser, toner, serum, moisturizer, and SPF sunscreen in travel sizes.',
    features=['5-Step Routine', 'Korean Formula', 'Cleanser + Toner + Serum + Moisturizer + SPF', 'Travel Size', 'Premium Ingredients', 'All Skin Types'],
    specs={'Brand': 'Markaz', 'Steps': '5', 'Formula': 'Korean', 'SPF': 'Included', 'Size': 'Travel', 'Skin Type': 'All'}))

products.append(p(21, 'Remington Keratin Therapy Pro Straightener', 'Remington', 'beauty', 1800, 2050, 4.7, 65,
    ym('https://admin.yourmart.pk/storage/uploads/inventory/products/media/Yourmartproducts-2026-06-09T182545.999_1781011609.webp'),
    'yourmart.pk/products/remington-keratin-therapy-pro-straightener-model-fr-531-up-to-57-more-protection',
    trending=True, featured=True, desc='Remington Keratin Therapy Pro hair straightener FR-531. Up to 57% more keratin protection, ceramic plates, fast heat-up.',
    features=['Keratin Therapy', '57% More Protection', 'Ceramic Plates', 'Fast Heat-up to 230C', 'Auto Shut-off', '360 Swivel Cord'],
    specs={'Brand': 'Remington', 'Model': 'FR-531', 'Plates': 'Ceramic Coated', 'Temp': 'Up to 230C', 'Heat-up': '30 seconds'}))

products.append(p(22, 'Remington PROLUXE Hair Straightener FR-2105', 'Remington', 'beauty', 2350, 2650, 4.8, 48,
    ym('https://admin.yourmart.pk/storage/uploads/inventory/products/media/Yourmartproducts(89)_1781006535.webp'),
    'yourmart.pk/products/remington-proluxe-hair-straightener-model-fr-2105-professional-salon-styling-with-advanced-ceramic-plates',
    trending=True, featured=True, desc='Remington PROLUXE professional salon straightener. Advanced ceramic plates, intelligent heat control for salon finish at home.',
    features=['PROLUXE Technology', 'Advanced Ceramic', 'Intelligent Heat', 'Salon Quality', 'Float Plates', 'Premium Finish'],
    specs={'Brand': 'Remington', 'Model': 'FR-2105', 'Plates': 'Advanced Ceramic', 'Temp': '150-230C', 'Heat-up': '15 seconds'}))

products.append(p(23, 'Roots Hair Treatment Serum 50ml', 'Herbiotics', 'beauty', 380, 480, 4.3, 92,
    ym('https://admin.yourmart.pk/storage/uploads/inventory/products/media/yourmartproduct(35)_1783345950.webp'),
    'yourmart.pk/products/roots-hair-treatment-serum-nourishing-hair-growth-serum-for-men-women-smooth-shiny-frizz-free-hair-50ml',
    trending=True, desc='Nourishing hair growth serum for men and women. Promotes smooth, shiny, frizz-free hair. Contains root-strengthening ingredients.',
    features=['Hair Growth Formula', 'Frizz Control', 'Smooth & Shiny', 'For Men & Women', '50ml Bottle', 'Root Strengthening'],
    specs={'Brand': 'Herbiotics', 'Size': '50ml', 'Type': 'Hair Serum', 'Benefit': 'Growth + Anti-Frizz', 'Gender': 'Unisex'}))

products.append(p(24, 'Kinoki Detox Foot Pads Natural Cleansing', 'Kinoki', 'beauty', 475, 575, 4.1, 68,
    ym('https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(5)_1779442626.webp'),
    'yourmart.pk/products/kinoki-detox-foot-pads-natural-cleansing-foot-patches-for-stress-relief-better-sleep',
    trending=True, desc='Natural cleansing detox foot pads for stress relief and better sleep. Apply before bed, wake up feeling refreshed. 10 pads per pack.',
    features=['Natural Detox', 'Stress Relief', 'Better Sleep', 'Easy to Use', '10 Pads Per Pack', 'Safe & Gentle'],
    specs={'Brand': 'Kinoki', 'Pads': '10 per pack', 'Type': 'Detox Foot Pads', 'Use': 'Overnight', 'Natural': 'Yes'}))

products.append(p(25, 'Meow Club Painless Body Wax Powder 10-Min', 'Meow Club', 'beauty', 410, 510, 4.4, 55,
    ym('https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(54)_1779534225.webp'),
    'yourmart.pk/products/meow-club-10-min-painless-body-wax-powder-with-spoon-orange-hair-removal-wax-for-smooth-skin',
    trending=True, isNew=True, desc='Quick 10-minute painless body wax powder. Orange formula with included application spoon. Smooth hair removal for all skin types.',
    features=['Painless Waxing', '10-Min Fast', 'Orange Formula', 'Application Spoon Included', 'Smooth Skin', 'All Skin Types'],
    specs={'Brand': 'Meow Club', 'Type': 'Wax Powder', 'Flavor': 'Orange', 'Time': '10 minutes', 'Includes': 'Spoon'}))

products.append(p(26, 'TIMILK Scarvanisher Scar Gel 30g', 'TIMILK', 'beauty', 310, 410, 4.2, 42,
    ym('https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(34)_1782724541.webp'),
    'yourmart.pk/products/timilk-scarvanisher-scar-gel-30g-advanced-scar-stretch-marks-removal-cream-fast-absorbing-skin-repair-gel',
    trending=True, isNew=True, desc='Advanced scar and stretch marks removal gel. Fast-absorbing skin repair formula. Reduces appearance of scars in weeks.',
    features=['Scar Removal', 'Stretch Marks Treatment', 'Fast Absorbing', 'Skin Repair', '30g Tube', 'Visible Results'],
    specs={'Brand': 'TIMILK', 'Size': '30g', 'Type': 'Scar Gel', 'Absorption': 'Fast', 'Results': '2-4 weeks'}))

# ============================================================
# FASHION ACCESSORIES (7 products)
# ============================================================

products.append(p(27, 'Matte Grey Carbon Fiber Watch for Men', 'Markaz', 'watches-bags', 1710, 1960, 4.5, 65,
    mk('1885-132-710013'), 'markaz.app/shop/product/matte-grey-carbon-fiber-watch-for-men/710013',
    trending=True, desc='Stylish matte grey carbon fiber dial watch for men. Stainless steel band, Japanese quartz movement. Premium casual and formal wear.',
    features=['Carbon Fiber Dial', 'Stainless Steel Band', 'Japanese Quartz', 'Matte Grey Finish', 'Date Display', 'Water Resistant'],
    specs={'Brand': 'Markaz', 'Dial': 'Carbon Fiber 42mm', 'Movement': 'Japanese Quartz', 'Band': 'Stainless Steel', 'Water Resistant': '3ATM'}))

products.append(p(28, 'POEDAGAR Luxury Mens Quartz Wristwatch', 'POEDAGAR', 'watches-bags', 4680, 5130, 4.6, 52,
    mk('1885-132-738699'), 'markaz.app/shop/product/poedagar-luxury-mens-quartz-wristwatch/738699',
    trending=True, featured=True, desc='POEDAGAR luxury wristwatch for men. Premium stainless steel case and band, elegant dial design. Gift box included.',
    features:['Luxury Design', 'Stainless Steel', 'Japanese Quartz', 'Gift Box', 'Premium Finish', 'Elegant Dial'],
    specs={'Brand': 'POEDAGAR', 'Case': 'Stainless Steel', 'Movement': 'Japanese Quartz', 'Band': 'Stainless Steel', 'Dial': '44mm'}))

products.append(p(29, 'Two-Tone Gold Silver Pakistani Mens Watch', 'Markaz', 'watches-bags', 4200, 4600, 4.4, 48,
    mk('1885-132-677622'), 'markaz.app/shop/product/two-tone-gold-silver-pakistani-mens-watch-quartz-stainless-steel/681770',
    trending=True, desc='Two-tone gold and silver stainless steel watch. Quartz movement, date display, premium Pakistani design. Perfect for gifting.',
    features=['Two-Tone Gold & Silver', 'Stainless Steel', 'Quartz Movement', 'Date Display', 'Premium Design', 'Gift Ready'],
    specs={'Brand': 'Markaz', 'Color': 'Gold & Silver', 'Movement': 'Quartz', 'Case': 'Stainless Steel', 'Dial': '42mm'}))

products.append(p(30, 'Rado DiaStar Scratchproof Watch', 'Rado', 'watches-bags', 2080, 2330, 4.7, 38,
    mk('1885-132-713590'), 'markaz.app/shop/product/rado-diastar-scratchproof-watch-with-stainless-steel-band/713590',
    trending=True, featured=True, desc='Rado DiaStar scratchproof watch with stainless steel band. Swiss-inspired design, sapphire crystal, premium quality.',
    features=['Scratchproof', 'Stainless Steel Band', 'Sapphire Crystal', 'Premium Design', 'Swiss Inspired', 'Durable'],
    specs={'Brand': 'Rado', 'Model': 'DiaStar', 'Crystal': 'Sapphire', 'Band': 'Stainless Steel', 'Water Resistant': '3ATM'}))

products.append(p(31, 'Crystal Time Watch Rose Gold Dial Unisex', 'Crystal Time', 'watches-bags', 4799, 5249, 4.5, 42,
    mk('1885-132-680148'), 'markaz.app/shop/product/crystal-time-watch-for-men-women-stainless-steel-rose-gold-dial/680711',
    trending=True, desc='Elegant unisex watch with rose gold dial. Stainless steel case and band, crystal embellishments. Suitable for men and women.',
    features=['Rose Gold Dial', 'Unisex Design', 'Crystal Embellishments', 'Stainless Steel', 'Elegant & Versatile', 'Premium Quality'],
    specs={'Brand': 'Crystal Time', 'Dial': 'Rose Gold 38mm', 'Movement': 'Quartz', 'Band': 'Stainless Steel', 'Gender': 'Unisex'}))

products.append(p(32, 'Womens Rexine Printed Shoulder Bag', 'Markaz', 'watches-bags', 1179, 1379, 4.3, 55,
    mk('2768-37-741041'), 'markaz.app/shop/product/womens-rexine-printed-shoulder-bag/741388',
    trending=True, desc='Stylish printed shoulder bag for women. Premium rexine material, spacious interior with multiple compartments. Perfect for daily use.',
    features=['Printed Design', 'Premium Rexine', 'Spacious Interior', 'Multiple Compartments', 'Shoulder Strap', 'Daily Use'],
    specs={'Brand': 'Markaz', 'Material': 'Rexine', 'Type': 'Shoulder Bag', 'Strap': 'Adjustable', 'Compartments': '3+', 'Closure': 'Zip'}))

products.append(p(33, 'RFID Blocking Passport Wallet PU Leather', 'YourMart', 'watches-bags', 725, 875, 4.4, 75,
    ym('https://admin.yourmart.pk/storage/uploads/inventory/products/media/Yourmartproducts(72)_1780997100.webp'),
    'yourmart.pk/products/rfid-blocking-passport-wallet-pu-leather-travel-document-holder-with-card-cash-pockets-random-color',
    trending=True, desc='RFID blocking passport wallet with PU leather. Travel document holder with card slots and cash pocket. Protects from digital theft.',
    features=['RFID Blocking', 'PU Leather', 'Passport Slot', 'Card Pockets', 'Cash Compartment', 'Travel Ready'],
    specs={'Brand': 'YourMart', 'Material': 'PU Leather', 'RFID': 'Yes', 'Passport': '1 slot', 'Cards': '6+ slots', 'Type': 'Bifold Wallet'}))

# ============================================================
# HOME & PRACTICAL (5 products)
# ============================================================

products.append(p(34, 'Rechargeable Green Desk Fan with Foldable Design', 'Markaz', 'home-lifestyle', 1479, 1729, 4.6, 95,
    mk('943-121-619086'), 'markaz.app/shop/product/rechargeable-green-desk-fan-with-base-foldable-design/619086',
    trending=True, bestseller=True, desc='Rechargeable desk fan with base and foldable design. 3-speed settings, USB charging, quiet motor. Perfect for office and home.',
    features:['Rechargeable Battery', 'Foldable Design', '3 Speed Settings', 'USB Charging', 'Quiet Motor', 'Desk Base'],
    specs={'Brand': 'Markaz', 'Power': 'USB Rechargeable', 'Speeds': '3 levels', 'Battery': '2000mAh', 'Noise': 'Low', 'Design': 'Foldable'}))

products.append(p(35, 'LED Jellyfish Lamp RGB Mood Light Voice Control', 'YourMart', 'home-lifestyle', 2000, 2300, 4.5, 48,
    ym('https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(10)_1781679519.webp'),
    'yourmart.pk/products/led-jellyfish-lamp-rgb-mood-light-voice-control-fantasy-jellyfish-night-light-decorative-bedroom-living-room-lighting',
    trending=True, isNew=True, desc='Fantasy jellyfish lamp with RGB mood lighting and voice control. Creates mesmerizing aquatic effect. Perfect for bedroom and living room.',
    features=['RGB Mood Light', 'Voice Control', 'Jellyfish Effect', 'USB Powered', 'Decorative', 'Calming Ambiance'],
    specs={'Brand': 'YourMart', 'Type': 'Jellyfish Lamp', 'Control': 'Voice + Button', 'Colors': 'RGB', 'Power': 'USB 5V', 'Use': 'Bedroom/Living Room'}))

products.append(p(36, 'Pack of 3 LED Remote Control Tap Lights', 'YourMart', 'home-lifestyle', 1030, 1230, 4.6, 82,
    ym('https://admin.yourmart.pk/storage/uploads/inventory/products/media/Yourmartproducts(52)_1780920553.webp'),
    'yourmart.pk/products/pack-of-3-led-remote-control-tap-lights-self-adhesive-cabinet-wardrobe-kitchen-lights',
    trending=True, desc='Pack of 3 wireless LED tap lights with remote control. Self-adhesive for cabinets, wardrobes, and kitchen. Battery operated.',
    features=['Pack of 3', 'Remote Control', 'Self-Adhesive', 'Wireless', 'Battery Operated', 'Multi-Location Use'],
    specs={'Brand': 'YourMart', 'Quantity': '3 pieces', 'Control': 'Remote + Tap', 'Power': 'Battery (AAA)', 'Adhesive': 'Self-Adhesive', 'LED': 'Bright White'}))

products.append(p(37, '12-in-1 Home Tool Kit Multi-Purpose', 'YourMart', 'home-lifestyle', 1800, 2050, 4.5, 65,
    ym('https://admin.yourmart.pk/storage/uploads/inventory/products/media/yourmartproduct(43)_1783346944.webp'),
    'yourmart.pk/products/12-in-1-home-tool-kit-multi-purpose-household-repair-tool-set-hardware-toolkit-with-durable-storage-box',
    trending=True, desc='12-in-1 multi-purpose home repair tool kit. Durable storage box, essential tools for household repairs. Perfect for every home.',
    features=['12 Essential Tools', 'Durable Storage Box', 'Multi-Purpose', 'Home Repairs', 'DIY Friendly', 'Compact Design'],
    specs={'Brand': 'YourMart', 'Pieces': '12', 'Type': 'Home Tool Kit', 'Storage': 'Durable Box', 'Use': 'Household Repairs', 'Material': 'Steel + ABS'}))

products.append(p(38, 'Mini Book Light with Clip LED Reading Lamp', 'YourMart', 'home-lifestyle', 480, 580, 4.3, 58,
    ym('https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(17)_1779446889.webp'),
    'yourmart.pk/products/mini-book-light-with-clip-portable-led-reading-lamp-with-eye-protection-random-color',
    trending=True, desc='Portable mini LED book light with clip. Eye protection technology, USB rechargeable. Perfect for reading in bed without disturbing others.',
    features=['Clip-On Design', 'Eye Protection LED', 'USB Rechargeable', 'Portable', 'Flexible Neck', '3 Brightness Levels'],
    specs={'Brand': 'YourMart', 'LED': 'Eye Protection', 'Power': 'USB Rechargeable', 'Brightness': '3 Levels', 'Clip': 'Strong Grip', 'Weight': '45g'}))

# ============================================================
# APPAREL (3 products)
# ============================================================

products.append(p(39, 'Navy Monarch 3 Piece Lawn Cotton Embroidered Dress', 'Markaz', 'womens-fashion', 8129, 8579, 4.7, 35,
    mk_content('2587-10-734039'), 'markaz.app/shop/product/navy-monarch-3-piece-lawn-cotton-embroidered-dress/734039',
    trending=True, featured=True, desc='Elegant navy blue 3-piece lawn cotton embroidered dress. Premium fabric with intricate embroidery. Includes shirt, dupatta, and trouser.',
    features=['3 Piece Set', 'Lawn Cotton', 'Embroidered', 'Navy Blue', 'Premium Fabric', 'Unstitched'],
    specs={'Brand': 'Markaz', 'Pieces': '3 (Shirt + Dupatta + Trouser)', 'Fabric': 'Lawn Cotton', 'Embroidery': 'Intricate', 'Color': 'Navy Blue', 'Type': 'Unstitched'}))

products.append(p(40, 'Red Printed Kurta Pajama Set for Women', 'Markaz', 'womens-fashion', 1975, 2225, 4.4, 52,
    mk('322-3-722152'), 'markaz.app/shop/product/red-printed-kurta-pajama-set-for-women/722152',
    trending=True, desc='Beautiful red printed kurta pajama set for women. Comfortable cotton fabric, elegant print. 2-piece set with kurta and pajama.',
    features=['Red Printed', 'Cotton Fabric', '2 Piece Set', 'Comfortable Fit', 'Elegant Design', 'Everyday Wear'],
    specs={'Brand': 'Markaz', 'Pieces': '2 (Kurta + Pajama)', 'Fabric': 'Cotton', 'Color': 'Red', 'Print': 'Floral', 'Fit': 'Regular'}))

products.append(p(41, 'Blue Embroidered Cotton Lawn 3Pcs Set', 'Markaz', 'womens-fashion', 2980, 3330, 4.5, 42,
    mk('2381-10-723748'), 'markaz.app/shop/product/blue-embroidered-cotton-lawn-3pcs-set/723748',
    trending=True, desc='Blue embroidered cotton lawn 3-piece suit. Beautiful embroidery on premium lawn fabric. Includes shirt, dupatta, and trouser.',
    features=['3 Piece Set', 'Cotton Lawn', 'Embroidered', 'Blue Color', 'Premium Quality', 'Unstitched'],
    specs={'Brand': 'Markaz', 'Pieces': '3 (Shirt + Dupatta + Trouser)', 'Fabric': 'Cotton Lawn', 'Embroidery': 'Traditional', 'Color': 'Blue', 'Type': 'Unstitched'}))

# ============================================================
# ADDITIONAL DISCOVERED PRODUCTS (9 products)
# ============================================================

products.append(p(42, 'Smartwatch Red Blue Lightweight Fitness Tracker', 'Markaz', 'electronics', 1850, 2100, 4.4, 78,
    mk('1172-87-606860'), 'markaz.app/shop/product/smartwatch-red-blue-lightweight-fitness-tracker/606860',
    trending=True, isNew=True, desc='Lightweight fitness tracker smartwatch in red and blue. Heart rate, blood oxygen, step counter, sleep tracking. 7-day battery.',
    features=['Heart Rate Monitor', 'SpO2 Tracking', 'Step Counter', 'Sleep Tracking', '7-Day Battery', 'IP68 Waterproof'],
    specs={'Brand': 'Markaz', 'Display': '1.69 inch', 'Battery': '7 days', 'Waterproof': 'IP68', 'Sensors': 'HR + SpO2'}))

products.append(p(43, 'Premium Quality Camping Light 4 Modes', 'Markaz', 'home-lifestyle', 2629, 2979, 4.5, 38,
    mk('1518-116-627128'), 'markaz.app/shop/product/premium-quality-camping-light-with-4-modes-stepless-control/627128',
    trending=True, desc='Premium camping light with 4 modes and stepless brightness control. USB rechargeable, durable build. Perfect for outdoor adventures.',
    features=['4 Light Modes', 'Stepless Dimming', 'USB Rechargeable', 'Durable Build', 'Hook Design', 'Water Resistant'],
    specs={'Brand': 'Markaz', 'Modes': '4 + Stepless', 'Power': 'USB Rechargeable', 'Battery': '2000mAh', 'Use': 'Camping/Outdoor'}))

products.append(p(44, 'Five Head Massage Gun Rechargeable 9 Heads', 'YourMart', 'sports-fitness', 2650, 3000, 4.6, 72,
    ym('https://admin.yourmart.pk/storage/uploads/inventory/products/media/yourmartproduct(19)_1783340117.webp'),
    'yourmart.pk/products/five-head-massage-gun-rechargeable-deep-tissue-muscle-massager-9-massage-heads-6-speed-levels-model-bld-780-random-color',
    trending=True, desc='Powerful 5-head massage gun with 9 interchangeable massage heads. 6 speed levels, deep tissue muscle relief. Rechargeable battery.',
    features=['5 Massage Heads', '6 Speed Levels', 'Deep Tissue Relief', 'Rechargeable', 'Quiet Motor', 'Portable'],
    specs={'Brand': 'YourMart', 'Heads': '9 interchangeable', 'Speeds': '6 levels', 'Battery': '2500mAh', 'Noise': '<45dB', 'Weight': '600g'}))

products.append(p(45, 'Long Handle Fascial Gun Massager', 'YourMart', 'sports-fitness', 3000, 3350, 4.5, 55,
    ym('https://admin.yourmart.pk/storage/uploads/inventory/products/media/yourmartproduct(56)_1783403862.webp'),
    'yourmart.pk/products/long-handle-fascial-gun-massager-model-bld-339-rechargeable-massage-gun-with-4-interchangeable-heads-full-body-muscle-relaxation',
    trending=True, desc='Long handle fascial gun massager for full body muscle relaxation. Extended reach for back massage. 4 heads, multiple speeds.',
    features=['Long Handle Design', 'Extended Reach', '4 Massage Heads', 'Full Body Relief', 'Rechargeable', 'Ergonomic Grip'],
    specs={'Brand': 'YourMart', 'Handle': 'Extended Long', 'Heads': '4 interchangeable', 'Battery': '2000mAh', 'Speeds': '6 levels', 'Weight': '850g'}))

products.append(p(46, 'LED Night Light Motion Sensor Rechargeable', 'YourMart', 'home-lifestyle', 1525, 1775, 4.5, 65,
    ym('https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(16)_1781681829.webp'),
    'yourmart.pk/products/led-night-light-with-motion-sensor-rechargeable-wireless-wall-lamp-dimmable-smart-night-light-magnetic-indoor-outdoor-wall-light',
    trending=True, isNew=True, desc='Wireless LED night light with motion sensor. Rechargeable, dimmable, magnetic mount. Indoor and outdoor use.',
    features=['Motion Sensor', 'Rechargeable', 'Dimmable', 'Magnetic Mount', 'Wireless', 'Indoor/Outdoor'],
    specs={'Brand': 'YourMart', 'Sensor': 'Motion/PIR', 'Power': 'USB Rechargeable', 'Brightness': 'Dimmable', 'Mount': 'Magnetic', 'LED': '28 SMD'}))

products.append(p(47, 'Metal COB Flashlight Torch Mini Rechargeable', 'YourMart', 'electronics', 510, 660, 4.6, 95,
    ym('https://admin.yourmart.pk/storage/uploads/inventory/products/media/Yourmartproducts(2)_1780909493.webp'),
    'yourmart.pk/products/metal-cob-flashlight-torch-mini-rechargeable-led-work-light-waterproof-emergency-penlight',
    trending=True, desc='Mini metal COB LED flashlight torch. Rechargeable, waterproof, penlight design. High brightness work light for emergencies.',
    features=['COB LED', 'Mini Metal Body', 'Rechargeable', 'Waterproof', 'Penlight Design', 'Emergency Light'],
    specs={'Brand': 'YourMart', 'LED': 'COB', 'Material': 'Metal Alloy', 'Charging': 'USB', 'Waterproof': 'IPX4', 'Size': 'Pen Size'}))

products.append(p(48, 'TurboFan Rechargeable Mini Cooling Fan 3-Speed', 'YourMart', 'electronics', 925, 1075, 4.3, 48,
    ym("https://admin.yourmart.pk/storage/uploads/inventory/products/media/Product'sPictures(70)_1779191754.webp"),
    'yourmart.pk/products/turbofan-rechargeable-mini-cooling-fan-portable-handheld-usb-turbo-fan-with-3-speed-modes-random-color',
    trending=True, desc='TurboFan rechargeable mini cooling fan. 3 speed modes, powerful airflow, USB charging. Portable handheld design for summer.',
    features=['Turbo Power', '3 Speed Modes', 'USB Rechargeable', 'Portable Handheld', 'Powerful Airflow', 'Quiet Motor'],
    specs={'Brand': 'TurboFan', 'Speeds': '3 levels', 'Power': 'USB Rechargeable', 'Battery': '1500mAh', 'Weight': '130g', 'Design': 'Handheld'}))

products.append(p(49, 'Portable Mini Mosquito Swatter USB Rechargeable', 'YourMart', 'home-lifestyle', 650, 800, 4.2, 55,
    ym("https://admin.yourmart.pk/storage/uploads/inventory/products/media/Product'sPictures(58)_1778490824.webp"),
    'yourmart.pk/products/portable-mini-mosquito-swatter-usb-rechargeable-electric-bug-zapper-with-led-night-light-random-color',
    trending=True, desc='Portable electric mosquito swatter with LED night light. USB rechargeable, 3-layer safety mesh. Effective bug zapper for home.',
    features=['Electric Bug Zapper', 'LED Night Light', 'USB Rechargeable', '3-Layer Safety Mesh', 'Portable', 'Effective'],
    specs={'Brand': 'YourMart', 'Power': 'USB Rechargeable', 'Mesh': '3-Layer Safety', 'Battery': '1200mAh', 'LED': 'Built-in Night Light', 'Weight': '200g'}))

products.append(p(50, 'Deep Tissue Muscle Massage Gun 4 Heads', 'YourMart', 'sports-fitness', 1650, 1900, 4.4, 62,
    ym('https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(12)_1781767720.webp'),
    'yourmart.pk/products/deep-tissue-muscle-massage-gun-fascia-relaxation-massage-gun-with-6-speed-levels-4-massage-heads-random-color',
    trending=True, desc='Deep tissue massage gun for muscle relaxation and pain relief. 6 speed levels, 4 massage heads. Ultra-quiet, portable design.',
    features=['Deep Tissue Massage', '6 Speed Levels', '4 Massage Heads', 'Ultra-Quiet', 'Portable', 'USB-C Charging'],
    specs={'Brand': 'YourMart', 'Speeds': '6 levels', 'Heads': '4 interchangeable', 'Battery': '2000mAh', 'Noise': '<45dB', 'Weight': '350g'}))

# Generate the output
output = []
for prod in products:
    output.append(prod)

result = '\n'.join(output)
print(result)
print(f'\n// Total: {len(products)} products')