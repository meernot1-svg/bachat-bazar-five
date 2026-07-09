#!/bin/bash
# Search for accurate product images for 25 products with duplicate images
# Each search gets 3 unique images with --no-rank for speed

OUTDIR="/home/z/my-project/scripts/img-results"
mkdir -p "$OUTDIR"

search() {
  local id=$1
  local query="$2"
  local outfile="$OUTDIR/p${id}.json"
  
  if [ -f "$outfile" ]; then
    echo "P${id}: already exists, skipping"
    return
  fi
  
  echo "P${id}: Searching for '$query'..."
  z-ai image-search -q "$query" -c 3 --no-rank -o "$outfile" 2>/dev/null
  local count=$(python3 -c "import json; d=json.load(open('$outfile')); print(len(d.get('results',[])))" 2>/dev/null || echo "0")
  echo "P${id}: Got $count images"
  
  # Rate limit: wait 5 seconds between calls
  sleep 5
}

# Electronics products with duplicate images
search 9 "M04 TWS wireless earbuds Bluetooth 5.3 white charging case"
search 10 "Air 39 transparent Bluetooth earbuds ENC noise cancellation"
search 11 "CX16 magnetic phone cooling fan RGB semiconductor"
search 12 "SQ11 mini camera HD 1080P night vision portable"
search 47 "COB LED flashlight mini rechargeable metal penlight"
search 48 "TurboFan rechargeable mini handheld cooling fan portable"

# Beauty products with duplicate images
search 13 "19 in 1 complete makeup kit bridal Pakistani"
search 14 "ultimate makeup kit 20 items women professional"
search 15 "16 in 1 makeup set flawless wear palette"
search 21 "Remington Keratin Therapy Pro hair straightener FR-531"
search 22 "Remington PROLUXE hair straightener FR-2105 ceramic"
search 23 "hair growth serum 50ml nourishing treatment"
search 24 "Kinoki detox foot pads natural cleansing patches"
search 25 "painless body wax powder orange formula"
search 26 "scar removal gel stretch marks treatment 30ml"

# Fashion accessories with duplicate images
search 33 "RFID blocking passport wallet PU leather travel"

# Home & Practical products with duplicate images
search 35 "LED jellyfish lamp RGB mood light aquatic decorative"
search 36 "LED tap lights remote control wireless pack of 3"
search 37 "12 in 1 home tool kit multi-purpose repair box"
search 38 "mini book light clip LED reading lamp rechargeable"
search 46 "LED night light motion sensor rechargeable magnetic"
search 49 "electric mosquito swatter USB rechargeable LED"

# Sports & Fitness with duplicate images
search 44 "massage gun rechargeable 5 heads deep tissue portable"
search 45 "long handle fascial gun massager full body"
search 50 "deep tissue muscle massage gun 4 heads portable"

echo "=== DONE ==="
echo "Results saved to $OUTDIR/"