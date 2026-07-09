/* ============================================================
   Bachat Bazar — Data Layer
   Catalog based on Naheed.pk products & categories
   Prices in PKR
   Pakistani-themed color scheme & proper product images
   ============================================================ */

// Direct image URL builder - uses reliable product image sources
// Handles: data URLs (data:...), full URLs (https://...), local paths (/uploads/...), Unsplash IDs
export const U = (id: string, w = 1200) => {
  if (typeof id !== 'string' || !id) return `https://picsum.photos/seed/placeholder/${w}/${w}`;
  if (/^data:/i.test(id)) return id;
  if (/^https?:\/\//.test(id)) return id;
  if (/^\//.test(id)) return id;
  return `https://images.unsplash.com/photo-${id}?w=${w}&q=90&auto=format&fit=crop&dpr=1`;
};

// Helper: resolve image src — same logic as U() for inline use
export const resolveImg = (src: string, w = 800) => {
  if (!src) return '';
  if (/^data:/i.test(src)) return src;
  if (/^https?:\/\//.test(src)) return src;
  if (/^\//.test(src)) return src;
  return U(src, w);
};

export interface Category {
  id: string;
  name: string;
  icon: string;
  color: string;
  img: string;
}

export interface Product {
  id: number;
  name: string;
  brand: string;
  category: string;
  price: number;
  oldPrice: number;
  rating: number;
  reviews: number;
  stock: number;
  sku: string;
  images: string[];
  imageId: string;
  badge: string;
  isNew: boolean;
  trending: boolean;
  bestSeller: boolean;
  featured: boolean;
  description: string;
  features: string[];
  specs: Record<string, string>;
  video: string | null;
  related: number[];
  reviewList: Review[];
}

export interface Coupon {
  code: string;
  type: 'percent' | 'flat' | 'ship';
  value: number;
  label: string;
  min: number;
}

export interface Testimonial {
  name: string;
  role: string;
  avatar: string;
  rating: number;
  text: string;
}


export interface Review {
  id: number;
  name: string;
  avatar: string;
  rating: number;
  date: string;
  text: string;
  verified: boolean;
  helpful: number;
}

export interface BlogPost {
  id: number;
  title: string;
  img: string;
  date: string;
  author: string;
  excerpt: string;
}

export interface HeroSlide {
  title: string;
  sub: string;
  cta: string;
  route: string;
  img: string;
  grad: string;
  bg: string;
}

export interface ShippingMethod {
  id: string;
  name: string;
  desc: string;
  cost: number;
}

export interface Payment {
  id: string;
  name: string;
  icon: string;
}

export interface BannerData {
  id: string;
  title: string;
  subtitle: string;
  cta: string;
  ctaLink: string;
  image: string;
  gradient: string;
  active: boolean;
  order: number;
}

export interface SaleData {
  id: string;
  name: string;
  description: string;
  discountPercent: number;
  startDate: string;
  endDate: string;
  categoryId: string;
  active: boolean;
  bannerColor: string;
}

// Category images - each with a correct, category-appropriate Unsplash photo
export const CATEGORIES: Category[] = [
  { id:'beauty', name:'Health & Beauty', icon:'Sparkles', color:'from-emerald-600 to-teal-500', img:'https://sfile.chatglm.cn/images-ppt/4d50fcc75fcf.webp' },
  { id:'grocery', name:'Grocery & Pet Care', icon:'ShoppingCart', color:'from-amber-500 to-orange-500', img:'https://sfile.chatglm.cn/images-ppt/09e7de5b8143.jpg' },
  { id:'appliances', name:'TV & Home Appliances', icon:'Tv', color:'from-sky-600 to-blue-500', img:'https://sfile.chatglm.cn/images-ppt/bb87b7e9c7dd.jpg' },
  { id:'electronics', name:'Phones & Computers', icon:'Smartphone', color:'from-violet-600 to-purple-500', img:'https://sfile.chatglm.cn/images-ppt/45556987266b.jpg' },
  { id:'mens-fashion', name:"Men's Fashion", icon:'Shirt', color:'from-slate-600 to-zinc-700', img:'https://sfile.chatglm.cn/images-ppt/ed375a74ca61.jpg' },
  { id:'home-lifestyle', name:'Home & Lifestyle', icon:'Sofa', color:'from-rose-500 to-pink-500', img:'https://sfile.chatglm.cn/images-ppt/ee579b8769c2.jpg' },
  { id:'watches-bags', name:'Watches, Bags & Jewellery', icon:'Watch', color:'from-yellow-500 to-amber-600', img:'https://sfile.chatglm.cn/images-ppt/6b298c3eed38.webp' },
  { id:'kids-babies', name:'Kids & Babies', icon:'Baby', color:'from-pink-400 to-rose-500', img:'https://sfile.chatglm.cn/images-ppt/97001ab87050.png' },
  { id:'womens-fashion', name:"Women's Fashion", icon:'Shirt', color:'from-fuchsia-500 to-purple-500', img:'https://sfile.chatglm.cn/images-ppt/533f5876173a.jpg' },
  { id:'kitchen', name:'Kitchen & Dining', icon:'ChefHat', color:'from-orange-400 to-red-500', img:'https://sfile.chatglm.cn/images-ppt/85cd41ea7377.jpg' },
  { id:'sports-fitness', name:'Sports & Fitness', icon:'Dumbbell', color:'from-green-500 to-emerald-600', img:'https://sfile.chatglm.cn/images-ppt/8561b977f03c.jpg' },
  { id:'islamic', name:'Islamic Products', icon:'Moon', color:'from-teal-600 to-cyan-600', img:'https://sfile.chatglm.cn/images-ppt/987d8a5e23b0.jpg' },
  { id:'mobile-accessories', name:'Mobile Accessories', icon:'Smartphone', color:'from-indigo-500 to-blue-600', img:'https://sfile.chatglm.cn/images-ppt/fdc24d44c91e.jpg' },
  { id:'hair-care', name:'Hair Care', icon:'Scissors', color:'from-pink-500 to-rose-600', img:'https://sfile.chatglm.cn/images-ppt/9d66f225ecde.jpg' },
  { id:'bedding', name:'Bedding & Bedsheets', icon:'Bed', color:'from-purple-500 to-violet-600', img:'https://sfile.chatglm.cn/images-ppt/8e378d5c7946.jpg' },
  { id:'car-accessories', name:'Car Accessories', icon:'Car', color:'from-gray-600 to-slate-700', img:'https://sfile.chatglm.cn/images-ppt/d8a5041d4a13.jpg' },
  { id:'stationery', name:'Stationery & School', icon:'PenTool', color:'from-cyan-500 to-teal-600', img:'https://sfile.chatglm.cn/images-ppt/6863a218c457.jpg' },
  { id:'womens-shoes', name:"Women's Shoes", icon:'Footprints', color:'from-fuchsia-600 to-pink-600', img:'https://sfile.chatglm.cn/images-ppt/8912b24542fc.jpg' },
  { id:'fragrance', name:'Perfumes & Fragrances', icon:'SprayCan', color:'from-amber-600 to-yellow-600', img:'https://sfile.chatglm.cn/images-ppt/6ed6d593c8ca.png' },
  { id:'pet-care', name:'Pet Care', icon:'PawPrint', color:'from-lime-500 to-green-600', img:'https://sfile.chatglm.cn/images-ppt/a1a3c4ab7042.jpg' },
];

export const BRANDS = ['YourMart','J Premium','Remington','CX16','Memo','Herbiotics','SQ11','Markaz','Sapphire','Rukh','Zarar','Janan','Zafarani','MILANO','M25','Kinscoter','Haier','Dawlance','PEL','Anker','Baseus','JBL','Xiaomi','Audionic','Conatural','Medicam','Garnier','Nivea','Khaadi','Alkaram','Bonanza','Digital Quran Co','ProFit','MegaBuild','Barbie','SpeedRacer','Bonanza Satrangi','Ideas','Gul Ahmed','Sana Safinaz','Interwood','Roadster','Shell','Petpat','Furry Friends','Camlin','Dollar Stationery'];

// Generate realistic fake reviews for products
function generateReviews(productId: number, avgRating: number, reviewCount: number): Review[] {
  const reviewers = [
    { name: 'Ayesha Khan', avatar: '1494790108377-be9c29b29330' },
    { name: 'Bilal Ahmed', avatar: '1500648767791-00dcc994a43e' },
    { name: 'Fatima Ali', avatar: '1438761681033-6461ffad8d80' },
    { name: 'Usman Malik', avatar: '1507003211169-0a1dd7228f2d' },
    { name: 'Sana Noor', avatar: '1494790108377-be9c29b29330' },
    { name: 'Ahmed Raza', avatar: '1500648767791-00dcc994a43e' },
    { name: 'Zainab Hussain', avatar: '1438761681033-6461ffad8d80' },
    { name: 'Kamran Siddiqui', avatar: '1507003211169-0a1dd7228f2d' },
    { name: 'Hira Bashir', avatar: '1494790108377-be9c29b29330' },
    { name: 'Tariq Mehmood', avatar: '1500648767791-00dcc994a43e' },
    { name: 'Nadia Sharif', avatar: '1438761681033-6461ffad8d80' },
    { name: 'Farhan Qureshi', avatar: '1507003211169-0a1dd7228f2d' },
    { name: 'Amna Tariq', avatar: '1494790108377-be9c29b29330' },
    { name: 'Imran Akhtar', avatar: '1500648767791-00dcc994a43e' },
    { name: 'Sadia Wahid', avatar: '1438761681033-6461ffad8d80' },
  ];
  const positiveComments = [
    'Mashallah! Best quality product I have received. Delivery was fast and packaging was excellent. Will order again InshaAllah.',
    'Very good product for the price. Exactly as shown in pictures. Bachat Bazar never disappoints me.',
    'Ordered this for my family and everyone loves it. Quality is premium and delivery was on time. Highly recommended!',
    'Amazing value for money! The quality exceeded my expectations. Will definitely recommend to friends and family.',
    'Second time ordering from Bachat Bazar. Product is genuine and works perfectly. COD option is very convenient.',
    'Just received my order and I am very happy with the quality. Packaging was secure and delivery was quick.',
    'Great product at an affordable price. The build quality is much better than what I expected. Five stars!',
    'My wife loved this product! Quality is top-notch and it arrived before the expected date. Thank you Bachat Bazar.',
    'This is exactly what I was looking for. Works great and the price is unbeatable. Will order more soon.',
    'Outstanding product! Been using it for 2 weeks now and it performs exactly as described. No complaints at all.',
    'Very satisfied with my purchase. The product quality is excellent and delivery was super fast to Lahore.',
    'Good product overall. A bit different from the picture but quality is fine for this price range.',
    'Finally found a reliable store for online shopping in Pakistan. Product is genuine and well-packed.',
    'Bought this as a gift and the recipient was very happy. Good quality and beautiful packaging.',
    'Quick delivery to Karachi! Product is exactly as described. Will be a repeat customer for sure.',
  ];
  const mixedComments = [
    'Product is okay. Quality could be better but for this price it is acceptable. Delivery was on time.',
    'Decent product. Not exactly like the picture but works fine. Shipping was fast which is a plus.',
    'Average quality for the price. Functionality is good but the material could be improved. Still worth buying.',
    'Product works as described but finishing could be better. Overall satisfied with the purchase.',
  ];

  const numReviews = Math.min(Math.max(3, Math.floor(reviewCount * 0.15)), 8);
  const reviews: Review[] = [];
  const months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];

  for (let i = 0; i < numReviews; i++) {
    const reviewer = reviewers[(productId * 7 + i * 3) % reviewers.length];
    const isPositive = i < numReviews - 1 || avgRating >= 4.0;
    const comments = isPositive ? positiveComments : mixedComments;
    const commentIdx = (productId * 11 + i * 5) % comments.length;
    const ratingVariance = isPositive ? [4,5] : [3,4];
    const reviewRating = ratingVariance[(productId + i) % ratingVariance.length];
    const monthIdx = (productId + i * 2) % 12;
    const day = ((productId * 3 + i * 7) % 28) + 1;

    reviews.push({
      id: i + 1,
      name: reviewer.name,
      avatar: reviewer.avatar,
      rating: reviewRating,
      date: `${months[monthIdx]} ${day}, 2026`,
      text: comments[commentIdx],
      verified: (productId + i) % 3 !== 0,
      helpful: (productId * 3 + i * 7) % 25,
    });
  }
  return reviews;
}

function P(id: number, name: string, brand: string, cat: string, price: number, old: number, rating: number, reviews: number, stock: number, img: string | string[], opts: Partial<Product> = {}): Product {
  const imgArr = Array.isArray(img) ? img : [img];
  return {
    id, name, brand, category: cat,
    price: Math.round(price), oldPrice: Math.round(old || 0), rating, reviews, stock,
    sku: `BB-${String(id).padStart(4,'0')}`,
    images: imgArr.map((i: string) => U(i, 1200)),
    imageId: imgArr[0],
    badge: opts.badge || (old && old>price ? Math.round((1-price/old)*100)+'% OFF' : ''),
    isNew: opts.isNew || false,
    trending: opts.trending || false,
    bestSeller: opts.bestSeller || false,
    featured: opts.featured || false,
    description: opts.description || `${name} by ${brand}. Available at Bachat Bazar with fast delivery across Pakistan. 7-day return policy.`,
    features: opts.features || ['Genuine product','Fast delivery','7-day returns','Quality guaranteed'],
    specs: opts.specs || { 'Brand':brand, 'Category':cat, 'SKU':`BB-${String(id).padStart(4,'0')}` },
    video: opts.video || null,
    related: opts.related || [],
    reviewList: opts.reviewList || generateReviews(id, rating, reviews)
  };
}

// Product catalog
export const PRODUCTS: Product[] = [
P(1,'Air31 TWS Transparent Earbuds Bluetooth 5.3','Markaz','electronics',1220,1470,4.5,78,40,['https://static.markaz.app/pakistan/products/1172-86-481404-product-1.webp','https://static.markaz.app/pakistan/products/1172-86-481404-product-2.webp','https://static.markaz.app/pakistan/products/1172-86-481404-product-3.webp'],{trending:true,description:'Transparent design TWS earbuds with Bluetooth 5.3. Touch controls, deep bass, 30-hour battery with case. IPX5 water resistant.',features:['Bluetooth 5.3','Transparent Design','Touch Controls','30H Battery','IPX5 Waterproof','Charging Case'],specs:{'Brand':'Markaz','Bluetooth':'5.3','Battery':'30H with case','Driver':'13mm','Waterproof':'IPX5'}}),
P(2,'Black Over-Ear Headphones ABS Lightweight','Markaz','electronics',1629,1979,4.3,55,35,['https://static.markaz.app/pakistan/products/1518-86-627089-product-1.webp','https://static.markaz.app/pakistan/products/1518-86-627089-product-2.webp','https://static.markaz.app/pakistan/products/1518-86-627089-product-3.webp'],{trending:true,description:'Lightweight over-ear headphones with deep bass. ABS plastic, comfortable padded ear cups, 3.5mm jack.',features:['Over-Ear Design','Deep Bass','Lightweight ABS','Padded Ear Cups','3.5mm Jack','Foldable'],specs:{'Brand':'Markaz','Type':'Over-Ear','Driver':'40mm','Cable':'1.2m 3.5mm','Weight':'180g'}}),
P(3,'Smartwatch Multicolor Metal Silicone Band','Markaz','electronics',2054,2404,4.4,92,25,['https://static.markaz.app/pakistan/products/1172-87-608084-product-1.webp','https://static.markaz.app/pakistan/products/1172-87-608084-product-2.webp','https://static.markaz.app/pakistan/products/1172-87-608084-product-3.webp'],{trending:true,featured:true,description:'Smart fitness watch with heart rate, step counter, sleep tracking. Long battery life, IP68 waterproof.',features:['Heart Rate Monitor','Step Counter','Sleep Tracking','IP68 Waterproof','Long Battery','Multi-Sport'],specs:{'Brand':'Markaz','Display':'1.69 inch IPS','Battery':'7 days','Waterproof':'IP68','Bluetooth':'5.0'}}),
P(4,'BX-502 AirBuds ENC Wireless Earbuds','Markaz','electronics',3540,3990,4.6,65,20,['https://content.public.markaz.app/markazimagevideo/public/products/1657-86-561715-product-1.jpg','https://content.public.markaz.app/markazimagevideo/public/products/1657-86-561715-product-2.jpg','https://content.public.markaz.app/markazimagevideo/public/products/1657-86-561715-product-3.jpg'],{trending:true,description:'Premium TWS earbuds with Environmental Noise Cancellation. Crystal clear calls, deep bass, compact case.',features:['ENC Noise Cancellation','Clear HD Calls','Deep Bass','Touch Controls','Compact Case','Fast Charging'],specs:{'Brand':'Markaz','ANC':'ENC','Bluetooth':'5.2','Battery':'28H total','Charging':'USB-C'}}),
P(5,'Rechargeable LED Torch Light USB-C Zoomable','Markaz','electronics',879,1029,4.7,110,45,['https://static.markaz.app/pakistan/products/1172-116-649022-product-1.webp','https://static.markaz.app/pakistan/products/1172-116-649022-product-2.webp','https://static.markaz.app/pakistan/products/1172-116-649022-product-3.webp'],{trending:true,description:'Rechargeable LED torch with zoomable focus. 4 modes: High, Low, SOS, Strobe. USB-C charging, ABS body.',features:['USB-C Rechargeable','Zoomable Focus','4 Light Modes','ABS Body','LED Bulb','Water Resistant'],specs:{'Brand':'Markaz','Power':'XML-T6 LED','Charging':'USB-C','Modes':'4 modes','Material':'ABS Plastic'}}),
P(6,'Rechargeable Crystal Table Lamp Touch Control','Markaz','home-lifestyle',1670,1920,4.8,88,30,['https://static.markaz.app/pakistan/products/1172-116-496647-product-1.webp','https://static.markaz.app/pakistan/products/1172-116-496647-product-2.webp','https://static.markaz.app/pakistan/products/1172-116-496647-product-3.webp'],{trending:true,description:'Elegant crystal table lamp with touch control. 3 color temperatures, stepless dimming. USB rechargeable.',features:['Touch Control','3 Color Temperatures','Stepless Dimming','Crystal Design','USB Rechargeable','Eye-Caring LED'],specs:{'Brand':'Markaz','LED':'Eye-Caring','Colors':'3 temps','Battery':'2000mAh','Control':'Touch'}}),
P(7,'Smart Bluetooth Headset M11 Mini Compact','Markaz','electronics',800,950,4.2,45,40,['https://static.markaz.app/pakistan/products/578-86-387899-product-1.webp','https://static.markaz.app/pakistan/products/578-86-387899-product-2.webp','https://static.markaz.app/pakistan/products/578-86-387899-product-3.webp'],{trending:true,description:'Ultra-compact mini Bluetooth headset. Single ear design, lightweight, long battery. Clear calls.',features:['Mini Compact Design','Single Ear','Bluetooth 5.0','Long Battery','Comfortable Fit','Clear Calls'],specs:{'Brand':'Markaz','Bluetooth':'5.0','Battery':'6H talk','Weight':'8g','Charging':'USB-C'}}),
P(8,'BX-202 Power Bank 10000mAh','Markaz','electronics',4310,4660,4.5,72,20,['https://content.public.markaz.app/markazimagevideo/public/products/1657-91-584926-product-1.jpg','https://content.public.markaz.app/markazimagevideo/public/products/1657-91-584926-product-2.jpg','https://content.public.markaz.app/markazimagevideo/public/products/1657-91-584926-product-3.jpg'],{trending:true,description:'10000mAh power bank with dual USB output. Fast charging, LED indicator, compact design.',features:['10000mAh Capacity','Dual USB Output','Fast Charging','LED Indicator','Compact Design','Safety Protection'],specs:{'Brand':'Markaz','Capacity':'10000mAh','Output':'Dual USB','Input':'USB-C','Weight':'220g'}}),
P(9,'M04 TWS Wireless Earbuds Bluetooth 5.3','YourMart','electronics',1050,1200,4.4,95,50,['https://admin.yourmart.pk/storage/uploads/inventory/products/media/5_1750942955.jpg','https://admin.yourmart.pk/storage/uploads/inventory/products/media/1_1750942955.jpg','https://admin.yourmart.pk/storage/uploads/inventory/products/media/3_1750942955.jpg'],{trending:true,description:'TWS wireless earbuds with Bluetooth 5.3, LED display, deep bass sound. Fast charging.',features:['Bluetooth 5.3','LED Display','Deep Bass','Fast Charging','Comfortable Fit','Charging Case'],specs:{'Brand':'YourMart','Bluetooth':'5.3','Display':'LED','Battery':'25H total','Driver':'13mm','Charging':'USB-C'}}),
P(10,'Air 39 Transparent Bluetooth Earbuds ENC','YourMart','electronics',825,975,4.3,68,45,['https://admin.yourmart.pk/storage/uploads/inventory/products/media/ProductsPictures(19)_1776770521.webp','https://admin.yourmart.pk/storage/uploads/inventory/products/media/ProductsPictures(19)_1776770521.webp','https://admin.yourmart.pk/storage/uploads/inventory/products/media/ProductsPictures(19)_1776770521.webp'],{trending:true,description:'Transparent design Bluetooth 5.3 earbuds with ENC noise reduction. Super bass, HD calling.',features:['ENC Noise Reduction','Transparent Design','Super Bass','HD Calling','LED Display','Bluetooth 5.3'],specs:{'Brand':'YourMart','Bluetooth':'5.3','ANC':'ENC','Battery':'24H total','Waterproof':'IPX5'}}),
P(11,'CX16 Magnetic Mobile Cooling Fan RGB','YourMart','electronics',2250,2500,4.6,55,25,['https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(62)_1781613673.webp','https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(63)_1781613673.webp','https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(64)_1781613673.webp'],{trending:true,isNew:true,description:'Magnetic phone cooling fan with RGB lights. Semiconductor cooling for gaming. Works with all phones.',features:['Magnetic Attachment','Semiconductor Cooling','RGB Lights','Fast Cooling','Universal Fit','Low Noise'],specs:{'Brand':'CX16','Power':'15W','Cooling':'Semiconductor','RGB':'Yes','Compatibility':'All Smartphones'}}),
P(12,'SQ11 Mini Camera HD 1080P Night Vision','YourMart','electronics',1500,1700,4.4,82,35,['https://admin.yourmart.pk/storage/uploads/inventory/products/media/Yourmartproducts(15)_1780911799.webp','https://admin.yourmart.pk/storage/uploads/inventory/products/media/Yourmartproducts(17)_1780911799.webp','https://admin.yourmart.pk/storage/uploads/inventory/products/media/Yourmartproducts(19)_1780911799.webp'],{trending:true,description:'Mini portable 1080P HD camera with night vision. Motion detection, loop recording, compact body.',features:['1080P Full HD','Night Vision','Motion Detection','Loop Recording','Mini Compact','USB Charging'],specs:{'Brand':'SQ11','Resolution':'1080P','Night Vision':'Yes','Storage':'MicroSD 32GB','Battery':'Built-in'}}),
P(13,'19 in 1 Makeup Kit for Pakistani Brides','Markaz','beauty',2579,3029,4.7,120,18,['https://static.markaz.app/GenerativeMedia/Pakistan/thumbnails/pakistan_644275.png','https://static.markaz.app/GenerativeMedia/Pakistan/thumbnails/pakistan_644275.png','https://static.markaz.app/GenerativeMedia/Pakistan/thumbnails/pakistan_644275.png'],{trending:true,bestSeller:true,description:'Complete 19-piece bridal makeup kit with foundations, lipsticks, eyeshadows, brushes. Premium gift box.',features:['19 Pieces Complete','Bridal Special','Foundation + Lipstick + Eyeshadow','Brushes Included','Premium Quality','Gift Box'],specs:{'Brand':'Markaz','Pieces':'19','Occasion':'Bridal/Party','Packaging':'Gift Box'}}),
P(14,'Ultimate Makeup Kit 20 Items for Women','Markaz','beauty',2220,2570,4.6,95,25,['https://static.markaz.app/GenerativeMedia/Pakistan/thumbnails/pakistan_581802.png','https://static.markaz.app/GenerativeMedia/Pakistan/thumbnails/pakistan_581802.png','https://static.markaz.app/GenerativeMedia/Pakistan/thumbnails/pakistan_581802.png'],{trending:true,bestSeller:true,description:'Complete 20-item professional makeup kit. Daily wear to party looks in one premium case.',features:['20 Items Complete','Professional Quality','Daily + Party Looks','All-in-One Case','Premium Brushes','Color Palettes'],specs:{'Brand':'Markaz','Items':'20','Type':'Professional Kit','Quality':'Premium'}}),
P(15,'16-in-1 Makeup Set for Flawless Wear','Markaz','beauty',1750,2050,4.5,88,25,['https://static.markaz.app/GenerativeMedia/Pakistan/thumbnails/pakistan_630536.png','https://static.markaz.app/GenerativeMedia/Pakistan/thumbnails/pakistan_630536.png','https://static.markaz.app/GenerativeMedia/Pakistan/thumbnails/pakistan_630536.png'],{trending:true,description:'Professional 16-in-1 makeup set with color palettes, brushes, and tools. Long-lasting wear.',features:['16 Pieces','Long-Lasting Formula','Color Palettes','Brushes Included','Compact Case','Multi-Use'],specs:{'Brand':'Markaz','Pieces':'16','Type':'Professional Set','Longevity':'8+ hours'}}),
P(16,'4-in-1 Makeup Kit for Brides Daily Wear','Markaz','beauty',2060,2410,4.4,72,30,['https://static.markaz.app/pakistan/products/1304-287-555838-product-1.webp','https://static.markaz.app/pakistan/products/1304-287-555838-product-2.webp','https://static.markaz.app/pakistan/products/1304-287-555838-product-3.webp'],{trending:true,description:'Compact 4-in-1 makeup kit for brides and daily wear. Foundation, powder, lipstick, eyeshadow.',features:['4-in-1 Compact','Bridal + Daily','Portable Case','Mirror Included','Travel Friendly','All-in-One'],specs:{'Brand':'Markaz','Pieces':'4','Type':'Compact Kit','Includes':'Mirror'}}),
P(17,'Whitening Zafarani Cream Set of 2','Markaz','beauty',1230,1430,4.8,180,50,['https://static.markaz.app/pakistan/products/1718-77-669889-product-1.webp','https://static.markaz.app/pakistan/products/1718-77-669889-product-2.webp','https://static.markaz.app/pakistan/products/1718-77-669889-product-3.webp'],{trending:true,bestSeller:true,featured:true,description:'Pack of 2 Zafarani whitening creams with glutathione. Vitamin C formula for brightening skin.',features:['Set of 2 Creams','Glutathione Formula','Skin Whitening','Dark Spot Removal','Vitamin C','All Skin Types'],specs:{'Brand':'Zafarani','Quantity':'2 pieces','Size':'30g each','Key Ingredient':'Glutathione + Vitamin C'}}),
P(18,'Premium Zafarani Whitening Cream','Markaz','beauty',1079,1279,4.7,150,45,['https://static.markaz.app/pakistan/products/700-77-669812-product-1.webp','https://static.markaz.app/pakistan/products/700-77-669812-product-2.webp','https://static.markaz.app/pakistan/products/700-77-669812-product-3.webp'],{trending:true,featured:true,description:'Premium Zafarani whitening cream with glutathione. Removes freckles and pigmentation naturally.',features:['Glutathione Formula','Freckle Removal','Dark Spot Treatment','Natural Ingredients','Visible in 2 Weeks','All Skin Types'],specs:{'Brand':'Zafarani','Type':'Whitening Cream','Key Ingredient':'Glutathione','Size':'30g'}}),
P(19,'3-in-1 Makeup and Skincare Bundle','Markaz','beauty',1319,1569,4.6,135,45,['https://static.markaz.app/pakistan/products/1004-287-618049-product-1.webp','https://static.markaz.app/pakistan/products/1004-287-618049-product-2.webp','https://static.markaz.app/pakistan/products/1004-287-618049-product-3.webp'],{trending:true,bestSeller:true,description:'Complete 3-in-1 makeup and skincare bundle. Foundation, lipstick set, skincare essentials.',features:['3-in-1 Bundle','Makeup + Skincare','Gift Ready Case','Premium Quality','All Essentials','Compact'],specs:{'Brand':'Markaz','Type':'Bundle Set','Pieces':'3-in-1','Gift':'Premium Case'}}),
P(20,'5-in-1 Premium Skincare Set','Markaz','beauty',2169,2519,4.8,110,25,['https://static.markaz.app/pakistan/products/1183-287-647460-product-1.webp','https://static.markaz.app/pakistan/products/1183-287-647460-product-2.webp','https://static.markaz.app/pakistan/products/1183-287-647460-product-3.webp'],{trending:true,featured:true,description:'Premium 5-step Korean skincare routine. Cleanser, toner, serum, moisturizer, SPF sunscreen.',features:['5-Step Routine','Korean Formula','Cleanser + Toner + Serum + Moisturizer + SPF','Travel Size','Premium Ingredients'],specs:{'Brand':'Markaz','Steps':'5','Formula':'Korean','SPF':'Included','Size':'Travel'}}),
P(21,'Remington Keratin Therapy Pro Straightener','Remington','beauty',1800,2050,4.7,65,20,['https://admin.yourmart.pk/storage/uploads/inventory/products/media/Yourmartproducts-2026-06-09T182545.999_1781011609.webp','https://admin.yourmart.pk/storage/uploads/inventory/products/media/Yourmartproducts-2026-06-09T182545.999_1781011609.webp','https://admin.yourmart.pk/storage/uploads/inventory/products/media/Yourmartproducts-2026-06-09T182545.999_1781011609.webp'],{trending:true,featured:true,description:'Remington Keratin Therapy Pro hair straightener FR-531. Up to 57% more keratin protection, ceramic plates.',features:['Keratin Therapy','57% More Protection','Ceramic Plates','Fast Heat-up 230C','Auto Shut-off','360 Swivel Cord'],specs:{'Brand':'Remington','Model':'FR-531','Plates':'Ceramic Coated','Temp':'Up to 230C','Heat-up':'30 seconds'}}),
P(22,'Remington PROLUXE Hair Straightener FR-2105','Remington','beauty',2350,2650,4.8,48,15,['https://admin.yourmart.pk/storage/uploads/inventory/products/media/Yourmartproducts(89)_1781006535.webp','https://admin.yourmart.pk/storage/uploads/inventory/products/media/Yourmartproducts(90)_1781006535.webp','https://admin.yourmart.pk/storage/uploads/inventory/products/media/Yourmartproducts(91)_1781006535.webp'],{trending:true,featured:true,description:'Remington PROLUXE professional salon straightener. Advanced ceramic plates, intelligent heat control.',features:['PROLUXE Technology','Advanced Ceramic','Intelligent Heat','Salon Quality','Float Plates','Premium Finish'],specs:{'Brand':'Remington','Model':'FR-2105','Plates':'Advanced Ceramic','Temp':'150-230C','Heat-up':'15 seconds'}}),
P(23,'Roots Hair Treatment Serum 50ml','Herbiotics','beauty',380,480,4.3,92,60,['https://admin.yourmart.pk/storage/uploads/inventory/products/media/yourmartproduct(35)_1783345950.webp','https://admin.yourmart.pk/storage/uploads/inventory/products/media/yourmartproduct(35)_1783345950.webp','https://admin.yourmart.pk/storage/uploads/inventory/products/media/yourmartproduct(35)_1783345950.webp'],{trending:true,description:'Nourishing hair growth serum for men and women. Promotes smooth, shiny, frizz-free hair.',features:['Hair Growth Formula','Frizz Control','Smooth and Shiny','For Men and Women','50ml Bottle','Root Strengthening'],specs:{'Brand':'Herbiotics','Size':'50ml','Type':'Hair Serum','Benefit':'Growth + Anti-Frizz','Gender':'Unisex'}}),
P(24,'Kinoki Detox Foot Pads Natural Cleansing','Kinoki','beauty',475,575,4.1,68,50,['https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(5)_1779442626.webp','https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(2)_1779442626.webp','https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(3)_1779442626.webp'],{trending:true,description:'Natural cleansing detox foot pads for stress relief and better sleep. 10 pads per pack.',features:['Natural Detox','Stress Relief','Better Sleep','Easy to Use','10 Pads Per Pack','Safe and Gentle'],specs:{'Brand':'Kinoki','Pads':'10 per pack','Type':'Detox Foot Pads','Use':'Overnight','Natural':'Yes'}}),
P(25,'Meow Club Painless Body Wax Powder','Meow Club','beauty',410,510,4.4,55,40,['https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(54)_1779534225.webp','https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(54)_1779534225.webp','https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(54)_1779534225.webp'],{trending:true,isNew:true,description:'Quick 10-minute painless body wax powder. Orange formula with application spoon included.',features:['Painless Waxing','10-Min Fast','Orange Formula','Spoon Included','Smooth Skin','All Skin Types'],specs:{'Brand':'Meow Club','Type':'Wax Powder','Flavor':'Orange','Time':'10 minutes'}}),
P(26,'TIMILK Scarvanisher Scar Gel 30g','TIMILK','beauty',310,410,4.2,42,40,['https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(34)_1782724541.webp','https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(34)_1782724541.webp','https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(34)_1782724541.webp'],{trending:true,isNew:true,description:'Advanced scar and stretch marks removal gel. Fast-absorbing skin repair formula.',features:['Scar Removal','Stretch Marks Treatment','Fast Absorbing','Skin Repair','30g Tube','Visible Results'],specs:{'Brand':'TIMILK','Size':'30g','Type':'Scar Gel','Absorption':'Fast','Results':'2-4 weeks'}}),
P(27,'Matte Grey Carbon Fiber Watch for Men','Markaz','watches-bags',1710,1960,4.5,65,25,['https://static.markaz.app/pakistan/products/1885-132-710013-product-1.webp','https://static.markaz.app/pakistan/products/1885-132-710013-product-2.webp','https://static.markaz.app/pakistan/products/1885-132-710013-product-3.webp'],{trending:true,description:'Stylish matte grey carbon fiber dial watch. Stainless steel band, Japanese quartz movement.',features:['Carbon Fiber Dial','Stainless Steel Band','Japanese Quartz','Matte Grey Finish','Date Display','Water Resistant'],specs:{'Brand':'Markaz','Dial':'Carbon Fiber 42mm','Movement':'Japanese Quartz','Band':'Stainless Steel','Water Resistant':'3ATM'}}),
P(28,'POEDAGAR Luxury Mens Quartz Wristwatch','POEDAGAR','watches-bags',4680,5130,4.6,52,15,['https://static.markaz.app/pakistan/products/1885-132-738699-product-1.webp','https://static.markaz.app/pakistan/products/1885-132-738699-product-2.webp','https://static.markaz.app/pakistan/products/1885-132-738699-product-3.webp'],{trending:true,featured:true,description:'POEDAGAR luxury wristwatch for men. Premium stainless steel case and band, elegant dial. Gift box.',features:['Luxury Design','Stainless Steel','Japanese Quartz','Gift Box','Premium Finish','Elegant Dial'],specs:{'Brand':'POEDAGAR','Case':'Stainless Steel','Movement':'Japanese Quartz','Band':'Stainless Steel','Dial':'44mm'}}),
P(29,'Two-Tone Gold Silver Pakistani Mens Watch','Markaz','watches-bags',4200,4600,4.4,48,20,['https://static.markaz.app/pakistan/products/1885-132-677622-product-1.webp','https://static.markaz.app/pakistan/products/1885-132-677622-product-2.webp','https://static.markaz.app/pakistan/products/1885-132-677622-product-3.webp'],{trending:true,description:'Two-tone gold and silver stainless steel watch. Quartz movement, date display, premium design.',features:['Two-Tone Gold and Silver','Stainless Steel','Quartz Movement','Date Display','Premium Design','Gift Ready'],specs:{'Brand':'Markaz','Color':'Gold and Silver','Movement':'Quartz','Case':'Stainless Steel','Dial':'42mm'}}),
P(30,'Rado DiaStar Scratchproof Watch','Rado','watches-bags',2080,2330,4.7,38,15,['https://static.markaz.app/pakistan/products/1885-132-713590-product-1.webp','https://static.markaz.app/pakistan/products/1885-132-713590-product-2.webp','https://static.markaz.app/pakistan/products/1885-132-713590-product-3.webp'],{trending:true,featured:true,description:'Rado DiaStar scratchproof watch with stainless steel band. Sapphire crystal, premium quality.',features:['Scratchproof','Stainless Steel Band','Sapphire Crystal','Premium Design','Swiss Inspired','Durable'],specs:{'Brand':'Rado','Model':'DiaStar','Crystal':'Sapphire','Band':'Stainless Steel','Water Resistant':'3ATM'}}),
P(31,'Crystal Time Watch Rose Gold Dial Unisex','Crystal Time','watches-bags',4799,5249,4.5,42,18,['https://static.markaz.app/pakistan/products/1885-132-680148-product-1.webp','https://static.markaz.app/pakistan/products/1885-132-680148-product-2.webp','https://static.markaz.app/pakistan/products/1885-132-680148-product-3.webp'],{trending:true,description:'Elegant unisex watch with rose gold dial. Stainless steel, crystal embellishments.',features:['Rose Gold Dial','Unisex Design','Crystal Embellishments','Stainless Steel','Elegant and Versatile','Premium Quality'],specs:{'Brand':'Crystal Time','Dial':'Rose Gold 38mm','Movement':'Quartz','Band':'Stainless Steel','Gender':'Unisex'}}),
P(32,'Womens Rexine Printed Shoulder Bag','Markaz','watches-bags',1179,1379,4.3,55,30,['https://static.markaz.app/pakistan/products/2768-37-741041-product-1.webp','https://static.markaz.app/pakistan/products/2768-37-741041-product-2.webp','https://static.markaz.app/pakistan/products/2768-37-741041-product-3.webp'],{trending:true,description:'Stylish printed shoulder bag for women. Premium rexine, spacious interior, multiple compartments.',features:['Printed Design','Premium Rexine','Spacious Interior','Multiple Compartments','Shoulder Strap','Daily Use'],specs:{'Brand':'Markaz','Material':'Rexine','Type':'Shoulder Bag','Strap':'Adjustable','Compartments':'3+','Closure':'Zip'}}),
P(33,'RFID Blocking Passport Wallet PU Leather','YourMart','watches-bags',725,875,4.4,75,35,['https://admin.yourmart.pk/storage/uploads/inventory/products/media/Yourmartproducts(72)_1780997100.webp','https://admin.yourmart.pk/storage/uploads/inventory/products/media/Yourmartproducts(72)_1780997100.webp','https://admin.yourmart.pk/storage/uploads/inventory/products/media/Yourmartproducts(72)_1780997100.webp'],{trending:true,description:'RFID blocking passport wallet with PU leather. Travel document holder with card slots.',features:['RFID Blocking','PU Leather','Passport Slot','Card Pockets','Cash Compartment','Travel Ready'],specs:{'Brand':'YourMart','Material':'PU Leather','RFID':'Yes','Passport':'1 slot','Cards':'6+ slots','Type':'Bifold'}}),
P(34,'Rechargeable Green Desk Fan Foldable Design','Markaz','home-lifestyle',1479,1729,4.6,95,30,['https://static.markaz.app/pakistan/products/943-121-619086-product-1.webp','https://static.markaz.app/pakistan/products/943-121-619086-product-2.webp','https://static.markaz.app/pakistan/products/943-121-619086-product-3.webp'],{trending:true,bestSeller:true,description:'Rechargeable desk fan with base and foldable design. 3-speed, USB charging, quiet motor.',features:['Rechargeable Battery','Foldable Design','3 Speed Settings','USB Charging','Quiet Motor','Desk Base'],specs:{'Brand':'Markaz','Power':'USB Rechargeable','Speeds':'3 levels','Battery':'2000mAh','Noise':'Low','Design':'Foldable'}}),
P(35,'LED Jellyfish Lamp RGB Mood Light','YourMart','home-lifestyle',2000,2300,4.5,48,20,['https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(10)_1781679519.webp','https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(9)_1781679519.webp','https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(11)_1781679519.webp'],{trending:true,isNew:true,description:'Fantasy jellyfish lamp with RGB mood lighting and voice control. Mesmerizing aquatic effect.',features:['RGB Mood Light','Voice Control','Jellyfish Effect','USB Powered','Decorative','Calming Ambiance'],specs:{'Brand':'YourMart','Type':'Jellyfish Lamp','Control':'Voice + Button','Colors':'RGB','Power':'USB 5V'}}),
P(36,'Pack of 3 LED Remote Control Tap Lights','YourMart','home-lifestyle',1030,1230,4.6,82,40,['https://admin.yourmart.pk/storage/uploads/inventory/products/media/Yourmartproducts(52)_1780920553.webp','https://admin.yourmart.pk/storage/uploads/inventory/products/media/Yourmartproducts(52)_1780920553.webp','https://admin.yourmart.pk/storage/uploads/inventory/products/media/Yourmartproducts(52)_1780920553.webp'],{trending:true,description:'Pack of 3 wireless LED tap lights with remote. Self-adhesive for cabinets and wardrobes.',features:['Pack of 3','Remote Control','Self-Adhesive','Wireless','Battery Operated','Multi-Location'],specs:{'Brand':'YourMart','Quantity':'3 pieces','Control':'Remote + Tap','Power':'Battery AAA','Adhesive':'Self-Adhesive','LED':'Bright White'}}),
P(37,'12-in-1 Home Tool Kit Multi-Purpose','YourMart','home-lifestyle',1800,2050,4.5,65,30,['https://admin.yourmart.pk/storage/uploads/inventory/products/media/yourmartproduct(43)_1783346944.webp','https://admin.yourmart.pk/storage/uploads/inventory/products/media/yourmartproduct(43)_1783346944.webp','https://admin.yourmart.pk/storage/uploads/inventory/products/media/yourmartproduct(43)_1783346944.webp'],{trending:true,description:'12-in-1 multi-purpose home repair tool kit. Durable storage box, essential tools for household repairs.',features:['12 Essential Tools','Durable Storage Box','Multi-Purpose','Home Repairs','DIY Friendly','Compact Design'],specs:{'Brand':'YourMart','Pieces':'12','Type':'Home Tool Kit','Storage':'Durable Box','Material':'Steel + ABS'}}),
P(38,'Mini Book Light with Clip LED Reading Lamp','YourMart','home-lifestyle',480,580,4.3,58,45,['https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(17)_1779446889.webp','https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(17)_1779446889.webp','https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(17)_1779446889.webp'],{trending:true,description:'Portable mini LED book light with clip. Eye protection, USB rechargeable, 3 brightness levels.',features:['Clip-On Design','Eye Protection LED','USB Rechargeable','Portable','Flexible Neck','3 Brightness Levels'],specs:{'Brand':'YourMart','LED':'Eye Protection','Power':'USB Rechargeable','Brightness':'3 Levels','Clip':'Strong Grip','Weight':'45g'}}),
P(39,'Navy Monarch 3 Piece Lawn Embroidered Dress','Markaz','womens-fashion',8129,8579,4.7,35,15,['https://content.public.markaz.app/markazimagevideo/public/products/2587-10-734039-product-1.jpg','https://content.public.markaz.app/markazimagevideo/public/products/2587-10-734039-product-2.jpg','https://content.public.markaz.app/markazimagevideo/public/products/2587-10-734039-product-3.jpg'],{trending:true,featured:true,description:'Elegant navy blue 3-piece lawn cotton embroidered dress. Premium fabric with intricate embroidery.',features:['3 Piece Set','Lawn Cotton','Embroidered','Navy Blue','Premium Fabric','Unstitched'],specs:{'Brand':'Markaz','Pieces':'3 Shirt + Dupatta + Trouser','Fabric':'Lawn Cotton','Embroidery':'Intricate','Color':'Navy Blue','Type':'Unstitched'}}),
P(40,'Red Printed Kurta Pajama Set for Women','Markaz','womens-fashion',1975,2225,4.4,52,30,['https://static.markaz.app/pakistan/products/322-3-722152-product-1.webp','https://static.markaz.app/pakistan/products/322-3-722152-product-2.webp','https://static.markaz.app/pakistan/products/322-3-722152-product-3.webp'],{trending:true,description:'Beautiful red printed kurta pajama set for women. Comfortable cotton fabric, elegant print.',features:['Red Printed','Cotton Fabric','2 Piece Set','Comfortable Fit','Elegant Design','Everyday Wear'],specs:{'Brand':'Markaz','Pieces':'2 Kurta + Pajama','Fabric':'Cotton','Color':'Red','Print':'Floral','Fit':'Regular'}}),
P(41,'Blue Embroidered Cotton Lawn 3Pcs Set','Markaz','womens-fashion',2980,3330,4.5,42,20,['https://static.markaz.app/pakistan/products/2381-10-723748-product-1.webp','https://static.markaz.app/pakistan/products/2381-10-723748-product-2.webp','https://static.markaz.app/pakistan/products/2381-10-723748-product-3.webp'],{trending:true,description:'Blue embroidered cotton lawn 3-piece suit. Beautiful embroidery on premium lawn fabric.',features:['3 Piece Set','Cotton Lawn','Embroidered','Blue Color','Premium Quality','Unstitched'],specs:{'Brand':'Markaz','Pieces':'3 Shirt + Dupatta + Trouser','Fabric':'Cotton Lawn','Embroidery':'Traditional','Color':'Blue','Type':'Unstitched'}}),
P(42,'Smartwatch Red Blue Lightweight Fitness Tracker','Markaz','electronics',1850,2100,4.4,78,25,['https://static.markaz.app/pakistan/products/1172-87-606860-product-1.webp','https://static.markaz.app/pakistan/products/1172-87-606860-product-2.webp','https://static.markaz.app/pakistan/products/1172-87-606860-product-3.webp'],{trending:true,isNew:true,description:'Lightweight fitness tracker smartwatch in red and blue. Heart rate, SpO2, step counter, 7-day battery.',features:['Heart Rate Monitor','SpO2 Tracking','Step Counter','Sleep Tracking','7-Day Battery','IP68 Waterproof'],specs:{'Brand':'Markaz','Display':'1.69 inch','Battery':'7 days','Waterproof':'IP68','Sensors':'HR + SpO2'}}),
P(43,'Premium Camping Light 4 Modes Stepless','Markaz','home-lifestyle',2629,2979,4.5,38,15,['https://static.markaz.app/pakistan/products/1518-116-627128-product-1.webp','https://static.markaz.app/pakistan/products/1518-116-627128-product-2.webp','https://static.markaz.app/pakistan/products/1518-116-627128-product-3.webp'],{trending:true,description:'Premium camping light with 4 modes and stepless brightness. USB rechargeable, durable build.',features:['4 Light Modes','Stepless Dimming','USB Rechargeable','Durable Build','Hook Design','Water Resistant'],specs:{'Brand':'Markaz','Modes':'4 + Stepless','Power':'USB Rechargeable','Battery':'2000mAh','Use':'Camping/Outdoor'}}),
P(44,'Five Head Massage Gun Rechargeable 9 Heads','YourMart','sports-fitness',2650,3000,4.6,72,20,['https://admin.yourmart.pk/storage/uploads/inventory/products/media/yourmartproduct(19)_1783340117.webp','https://admin.yourmart.pk/storage/uploads/inventory/products/media/yourmartproduct(19)_1783340117.webp','https://admin.yourmart.pk/storage/uploads/inventory/products/media/yourmartproduct(19)_1783340117.webp'],{trending:true,description:'Powerful 5-head massage gun with 9 interchangeable heads. 6 speed levels, deep tissue relief.',features:['5 Massage Heads','6 Speed Levels','Deep Tissue Relief','Rechargeable','Quiet Motor','Portable'],specs:{'Brand':'YourMart','Heads':'9 interchangeable','Speeds':'6 levels','Battery':'2500mAh','Noise':'Less than 45dB','Weight':'600g'}}),
P(45,'Long Handle Fascial Gun Massager','YourMart','sports-fitness',3000,3350,4.5,55,18,['https://admin.yourmart.pk/storage/uploads/inventory/products/media/yourmartproduct(56)_1783403862.webp','https://admin.yourmart.pk/storage/uploads/inventory/products/media/yourmartproduct(57)_1783403862.webp','https://admin.yourmart.pk/storage/uploads/inventory/products/media/yourmartproduct(58)_1783403862.webp'],{trending:true,description:'Long handle fascial gun for full body muscle relaxation. Extended reach for back massage.',features:['Long Handle Design','Extended Reach','4 Massage Heads','Full Body Relief','Rechargeable','Ergonomic Grip'],specs:{'Brand':'YourMart','Handle':'Extended Long','Heads':'4 interchangeable','Battery':'2000mAh','Speeds':'6 levels','Weight':'850g'}}),
P(46,'LED Night Light Motion Sensor Rechargeable','YourMart','home-lifestyle',1525,1775,4.5,65,30,['https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(16)_1781681829.webp','https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(16)_1781681829.webp','https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(16)_1781681829.webp'],{trending:true,isNew:true,description:'Wireless LED night light with motion sensor. Rechargeable, dimmable, magnetic mount.',features:['Motion Sensor','Rechargeable','Dimmable','Magnetic Mount','Wireless','Indoor/Outdoor'],specs:{'Brand':'YourMart','Sensor':'Motion PIR','Power':'USB Rechargeable','Brightness':'Dimmable','Mount':'Magnetic','LED':'28 SMD'}}),
P(47,'Metal COB Flashlight Torch Mini Rechargeable','YourMart','electronics',510,660,4.6,95,50,['https://admin.yourmart.pk/storage/uploads/inventory/products/media/Yourmartproducts(2)_1780909493.webp','https://admin.yourmart.pk/storage/uploads/inventory/products/media/Yourmartproducts(1)_1780909493.webp','https://admin.yourmart.pk/storage/uploads/inventory/products/media/Yourmartproducts(3)_1780909493.webp'],{trending:true,description:'Mini metal COB LED flashlight torch. Rechargeable, waterproof, penlight design.',features:['COB LED','Mini Metal Body','Rechargeable','Waterproof','Penlight Design','Emergency Light'],specs:{'Brand':'YourMart','LED':'COB','Material':'Metal Alloy','Charging':'USB','Waterproof':'IPX4','Size':'Pen Size'}}),
P(48,'TurboFan Rechargeable Mini Cooling Fan','YourMart','electronics',925,1075,4.3,48,40,['https://admin.yourmart.pk/storage/uploads/inventory/products/media/ProductsPictures(70)_1779191754.webp','https://admin.yourmart.pk/storage/uploads/inventory/products/media/ProductsPictures(70)_1779191754.webp','https://admin.yourmart.pk/storage/uploads/inventory/products/media/ProductsPictures(70)_1779191754.webp'],{trending:true,description:'TurboFan rechargeable mini cooling fan. 3 speed modes, powerful airflow, USB charging.',features:['Turbo Power','3 Speed Modes','USB Rechargeable','Portable Handheld','Powerful Airflow','Quiet Motor'],specs:{'Brand':'TurboFan','Speeds':'3 levels','Power':'USB Rechargeable','Battery':'1500mAh','Weight':'130g','Design':'Handheld'}}),
P(49,'Portable Mini Mosquito Swatter USB Rechargeable','YourMart','home-lifestyle',650,800,4.2,55,35,['https://admin.yourmart.pk/storage/uploads/inventory/products/media/ProductsPictures(58)_1778490824.webp','https://admin.yourmart.pk/storage/uploads/inventory/products/media/ProductsPictures(58)_1778490824.webp','https://admin.yourmart.pk/storage/uploads/inventory/products/media/ProductsPictures(58)_1778490824.webp'],{trending:true,description:'Portable electric mosquito swatter with LED night light. USB rechargeable, 3-layer safety mesh.',features:['Electric Bug Zapper','LED Night Light','USB Rechargeable','3-Layer Safety Mesh','Portable','Effective'],specs:{'Brand':'YourMart','Power':'USB Rechargeable','Mesh':'3-Layer Safety','Battery':'1200mAh','LED':'Built-in Night Light','Weight':'200g'}}),
P(50,'Deep Tissue Muscle Massage Gun 4 Heads','YourMart','sports-fitness',1650,1900,4.4,62,25,['https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(12)_1781767720.webp','https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(12)_1781767720.webp','https://admin.yourmart.pk/storage/uploads/inventory/products/media/Untitleddesign(12)_1781767720.webp'],{trending:true,description:'Deep tissue massage gun for muscle relaxation. 6 speed levels, 4 massage heads, ultra-quiet.',features:['Deep Tissue Massage','6 Speed Levels','4 Massage Heads','Ultra-Quiet','Portable','USB-C Charging'],specs:{'Brand':'YourMart','Speeds':'6 levels','Heads':'4 interchangeable','Battery':'2000mAh','Noise':'Less than 45dB','Weight':'350g'}}),

// Total: 50 products
];

// Build related ids by same category
PRODUCTS.forEach(p => {
  if (!p.related.length) p.related = PRODUCTS.filter(x => x.category === p.category && x.id !== p.id).slice(0,4).map(x=>x.id);
});

export const COUPONS: Coupon[] = [
  { code:'WELCOME10', type:'percent', value:10, label:'10% off your first order', min:0 },
  { code:'SAVE15', type:'percent', value:15, label:'15% off orders over Rs 10,000', min:10000 },
  { code:'FLAT500', type:'flat', value:500, label:'Rs 500 off orders over Rs 5,000', min:5000 },
  { code:'FREESHIP', type:'ship', value:0, label:'Free shipping on any order', min:0 },
  { code:'EID25', type:'percent', value:25, label:'25% off orders over Rs 50,000', min:50000 },
];

export const TESTIMONIALS: Testimonial[] = [
  { name:'Ayesha Khan', role:'Verified Buyer', avatar:'1494790108377-be9c29b29330', rating:5, text:'Best online shopping experience in Pakistan! Fast delivery and genuine products every time.' },
  { name:'Bilal Ahmed', role:'Verified Buyer', avatar:'1500648767791-00dcc994a43e', rating:5, text:'Bachat Bazar has everything I need at great prices. The Cash on Delivery option is so convenient!' },
  { name:'Fatima Ali', role:'Verified Buyer', avatar:'1438761681033-6461ffad8d80', rating:4, text:'Love the variety of products. Quality is excellent and prices are very reasonable compared to other stores.' },
  { name:'Usman Malik', role:'Verified Buyer', avatar:'1507003211169-0a1dd7228f2d', rating:5, text:'Ordered groceries and they arrived the same day. Amazing service and the website is so easy to use!' },
];

export const BLOGS: BlogPost[] = [
  { id:1, title:'10 Best Beauty Products for Glowing Skin', img:'1596462502278-27bfdc403348', date:'Jul 1, 2026', author:'Beauty Desk', excerpt:'Discover the top skincare picks that will give you that radiant glow this season.' },
  { id:2, title:'Smart Home Appliances That Save Time', img:'1556909114-f6e7ad7d3136', date:'Jun 25, 2026', author:'Home Team', excerpt:'Upgrade your kitchen with these time-saving appliances that make cooking a breeze.' },
  { id:3, title:'Men\'s Fashion Trends for 2026', img:'1483985988355-763728e1935b', date:'Jun 18, 2026', author:'Fashion Edit', excerpt:'Stay stylish with the latest fashion trends for men this year.' },
  { id:4, title:'Best Phone Accessories Under Rs 5,000', img:'1505740420928-5e560c06d30e', date:'Jun 10, 2026', author:'Tech Desk', excerpt:'From earbuds to chargers, here are the best accessories that won\'t break the bank.' },
];

// Pakistani-themed hero slides - controlled by admin banners
export const HERO_SLIDES: HeroSlide[] = [
  { title:'Eid Mubarak Sale!', sub:'Up to 30% off on Health & Beauty essentials', cta:'Shop Now', route:'#/shop?category=beauty', img:'1596462502278-27bfdc403348', grad:'from-[#006233] to-[#00A651]', bg:'bg-gradient-to-br from-[#004D25] via-[#006233] to-[#00A651]' },
  { title:'Ramzan Kitchen Deals', sub:'Premium appliances at unbeatable prices', cta:'Shop Appliances', route:'#/shop?category=appliances', img:'1556909114-f6e7ad7d3136', grad:'from-[#004D25] to-[#006233]', bg:'bg-gradient-to-br from-[#002510] via-[#004D25] to-[#006233]' },
  { title:'Latest Phones & Gadgets', sub:'Smartphones, earbuds & accessories', cta:'Shop Electronics', route:'#/shop?category=electronics', img:'1511707171634-5f897ff02aa9', grad:'from-[#0C2340] to-[#1A4D8F]', bg:'bg-gradient-to-br from-[#0C2340] via-[#1A4D8F] to-[#2E6BC6]' },
  { title:'Bachat ka Vaade!', sub:'Best prices on Fashion, Home & more', cta:'Shop All', route:'#/shop', img:'1483985988355-763728e1935b', grad:'from-[#8B1A1A] to-[#C41E3A]', bg:'bg-gradient-to-br from-[#5C1010] via-[#8B1A1A] to-[#C41E3A]' },
];

// Default banners for admin management - these control the hero slider AND banner cards
export const DEFAULT_BANNERS: BannerData[] = [
  { id:'b1', title:'Eid Collection 2026', subtitle:'Exclusive deals on Fashion & Beauty', cta:'Explore Now', ctaLink:'#/shop?category=beauty', image:'1596462502278-27bfdc403348', gradient:'from-[#006233] to-[#C5A028]', active:true, order:1 },
  { id:'b2', title:'Mega Sale Weekend', subtitle:'Flat 20% off on all Electronics', cta:'Shop Electronics', ctaLink:'#/shop?category=electronics', image:'1511707171634-5f897ff02aa9', gradient:'from-[#1A4D8F] to-[#00A651]', active:true, order:2 },
  { id:'b3', title:'Free Delivery Nationwide', subtitle:'On orders above Rs 25,000', cta:'Start Shopping', ctaLink:'#/shop', image:'', gradient:'from-[#8B1A1A] to-[#C41E3A]', active:true, order:3 },
];

// Default sales for admin management
export const DEFAULT_SALES: SaleData[] = [
  { id:'s1', name:'Eid Mubarak Sale', description:'25% off on all beauty products', discountPercent:25, startDate:'2026-06-25', endDate:'2026-07-15', categoryId:'beauty', active:true, bannerColor:'#006233' },
  { id:'s2', name:'Tech Week', description:'15% off on electronics', discountPercent:15, startDate:'2026-07-01', endDate:'2026-07-10', categoryId:'electronics', active:true, bannerColor:'#1A4D8F' },
  { id:'s3', name:'Ramzan Special', description:'20% off on groceries', discountPercent:20, startDate:'2026-07-05', endDate:'2026-07-20', categoryId:'grocery', active:true, bannerColor:'#C5A028' },
];

export const SHIPPING_METHODS: ShippingMethod[] = [
  { id:'standard', name:'Standard Shipping', desc:'3-5 business days', cost:0 },
  { id:'express', name:'Express Shipping', desc:'1-2 business days', cost:250 },
  { id:'overnight', name:'Overnight Delivery', desc:'Next business day', cost:500 },
];

export const PAYMENTS: Payment[] = [
  { id:'card', name:'Credit / Debit Card', icon:'CreditCard' },
  { id:'jazzcash', name:'JazzCash', icon:'Wallet' },
  { id:'easypaisa', name:'EasyPaisa', icon:'Wallet' },
  { id:'bank', name:'Bank Transfer', icon:'Building2' },
  { id:'cod', name:'Cash on Delivery', icon:'Banknote' },
];
