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
P(1,'Rechargeable Eyebrow Trimmer w/ Cleaning Brushes','YourMart','electronics',1050,1200,5.0,24,35,['https://sfile.chatglm.cn/images-ppt/75f28e44f0a6.webp','https://sfile.chatglm.cn/images-ppt/75f28e44f0a6.webp','https://sfile.chatglm.cn/images-ppt/75f28e44f0a6.webp'],{trending:true,description:'Electric rechargeable eyebrow trimmer with cleaning brushes. USB rechargeable, painless precise trimming for face and body hair. LED indicator, compact travel-friendly design.',features:['USB Rechargeable','Painless trimming','3 interchangeable heads','LED indicator','Cleaning brushes included','Compact design'],specs:{'Brand':'YourMart','Type':'Eyebrow Trimmer','Power':'USB Rechargeable','Heads':'3 interchangeable','Use':'Face, Eyebrows, Nose'}}),
P(2,'Rechargeable Eyebrow Trimmer Pink Glitter','YourMart','electronics',1100,1300,5.0,18,30,['https://sfile.chatglm.cn/images-ppt/9107e4f7ff16.jpg','https://sfile.chatglm.cn/images-ppt/9107e4f7ff16.jpg','https://sfile.chatglm.cn/images-ppt/9107e4f7ff16.jpg'],{trending:true,description:'Stylish pink glitter rechargeable eyebrow trimmer for women. USB-C fast charging, LED display, ergonomic grip for easy handling.',features:['Pink glitter design','USB-C fast charging','LED display','Ergonomic grip','Safe and painless','Compact'],specs:{'Brand':'YourMart','Color':'Pink','Charging':'USB-C','Battery':'Built-in Li-ion'}}),
P(3,'A9 1080P WiFi Mini Security Camera Night Vision','YourMart','electronics',1400,1650,5.0,42,25,['https://picsum.photos/seed/el1/800/800','https://picsum.photos/seed/el2/800/800','https://picsum.photos/seed/el3/800/800'],{trending:true,description:'Compact 1080P HD WiFi security camera with IR night vision up to 10m. Motion detection alerts, two-way audio, mobile app remote viewing.',features:['1080P Full HD','WiFi Connected','IR Night Vision 10m','Motion Detection','Two-way Audio','Mobile App'],specs:{'Brand':'YourMart','Resolution':'1080P','Night Vision':'10m IR','Connectivity':'WiFi 2.4GHz','Audio':'Two-way','Power':'USB 5V'}}),
P(4,'Premium Wireless Earbuds Bluetooth 5.3','YourMart','electronics',1300,1550,5.0,85,50,['https://sfile.chatglm.cn/images-ppt/75f28e44f0a6.webp','https://sfile.chatglm.cn/images-ppt/75f28e44f0a6.webp','https://sfile.chatglm.cn/images-ppt/bec9909b6ffb.jpeg'],{trending:true,description:'Premium TWS wireless earbuds with Bluetooth 5.3, touch controls, and deep bass. 35-hour total battery with charging case. IPX5 water resistant.',features:['Bluetooth 5.3','Touch Controls','Deep Bass','35H Battery','IPX5 Waterproof','Charging Case'],specs:{'Brand':'YourMart','Bluetooth':'5.3','Battery':'35H with case','Driver':'13mm','Charging':'USB-C','Waterproof':'IPX5'}}),
P(5,'Wireless Bluetooth 5.3 Earbuds Noise Cancellation','YourMart','electronics',980,1200,5.0,120,60,['https://sfile.chatglm.cn/images-ppt/75f28e44f0a6.webp','https://sfile.chatglm.cn/images-ppt/75f28e44f0a6.webp','https://sfile.chatglm.cn/images-ppt/75f28e44f0a6.webp'],{trending:true,description:'Active noise cancelling Bluetooth 5.3 earbuds with LED battery display. Deep bass, clear HD calls, comfortable in-ear fit.',features:['Active Noise Cancellation','Bluetooth 5.3','LED Battery Display','Deep Bass','HD Clear Calls','Comfortable Fit'],specs:{'Brand':'YourMart','ANC':'Yes - 35dB','Bluetooth':'5.3','Display':'LED','Battery':'30H total','Driver':'12mm'}}),
P(6,'Mini Massager Gun Portable Deep Tissue','YourMart','sports-fitness',3000,3500,5.0,55,20,['https://picsum.photos/seed/s1/800/800','https://picsum.photos/seed/s2/800/800','https://picsum.photos/seed/s3/800/800'],{trending:true,description:'Compact mini massage gun for deep tissue muscle relief. 4 massage heads, 6 speed levels, ultra-quiet motor. USB-C rechargeable.',features:['4 Massage Heads','6 Speed Levels','Ultra-Quiet <45dB','USB-C Rechargeable','Portable 350g','Deep Tissue'],specs:{'Brand':'YourMart','Speeds':'6 levels','Heads':'4 interchangeable','Battery':'2000mAh','Noise':'<45dB','Weight':'350g'}}),
P(7,'Mini Handheld Fan USB Rechargeable 3-Speed','YourMart','electronics',1000,1200,4.3,38,40,['https://sfile.chatglm.cn/images-ppt/380c25955d43.jpg','https://sfile.chatglm.cn/images-ppt/380c25955d43.jpg','https://sfile.chatglm.cn/images-ppt/9107e4f7ff16.jpg'],{trending:true,description:'Portable mini handheld fan with 2000mAh USB rechargeable battery. 3 speed settings, 180-degree rotation. Perfect for outdoors and travel.',features:['USB Rechargeable','3 Speed Settings','180 Degree Rotation','2000mAh Battery','Quiet Motor','LED Indicator'],specs:{'Brand':'YourMart','Speeds':'3 levels','Battery':'2000mAh','Charging':'USB','Rotation':'180 degrees','Weight':'150g'}}),
P(8,'Rechargeable LED Flashlight USB-C Zoomable','YourMart','electronics',650,800,5.0,30,45,['https://sfile.chatglm.cn/images-ppt/9107e4f7ff16.jpg','https://sfile.chatglm.cn/images-ppt/9107e4f7ff16.jpg','https://sfile.chatglm.cn/images-ppt/9107e4f7ff16.jpg'],{trending:true,description:'High-power LED rechargeable flashlight with USB-C. Zoomable focus, 4 modes (High/Low/SOS/Strobe). Aircraft-grade aluminum, IPX4 waterproof.',features:['USB-C Charging','Zoomable Focus','4 Modes','IPX4 Waterproof','Aluminum Body','High Power LED'],specs:{'Brand':'YourMart','Power':'XML-T6 LED','Charging':'USB-C','Modes':'High/Low/SOS/Strobe','Material':'Aircraft Aluminum','Waterproof':'IPX4'}}),
P(9,'Phone Screen Magnifier HD Video Amplifier','YourMart','electronics',600,750,5.0,65,35,['https://sfile.chatglm.cn/images-ppt/9107e4f7ff16.jpg','https://sfile.chatglm.cn/images-ppt/9107e4f7ff16.jpg','https://sfile.chatglm.cn/images-ppt/9107e4f7ff16.jpg'],{trending:true,description:'HD phone screen magnifier with 3D acrylic lens. Enlarges screen 2-4x for movies and videos. Foldable, no battery needed.',features:['3D HD Lens','2-4x Magnification','Foldable Design','No Battery Needed','Universal Fit','Eye Protection'],specs:{'Brand':'YourMart','Magnification':'2-4x','Lens':'Acrylic 3D','Screen':'12 inch','Compatibility':'All phones','Design':'Foldable'}}),
P(10,'Mini Air Cooler 3-Speed with Perfume Diffuser','YourMart','home-lifestyle',2750,3200,3.9,28,15,['https://picsum.photos/seed/h1/800/800','https://picsum.photos/seed/h2/800/800','https://picsum.photos/seed/h3/800/800'],{trending:true,description:'Portable mini air cooler with 3-speed fan and built-in perfume diffuser. USB powered, add ice cubes for extra cooling. LED mood lights.',features:['3 Speed Settings','Perfume Diffuser','USB Powered','Ice Compatible','LED Mood Lights','500ml Tank'],specs:{'Brand':'YourMart','Speeds':'3 levels','Power':'USB/Adapter','Tank':'500ml','Feature':'Perfume diffuser','Cooling':'Evaporative'}}),
P(11,'LED Table Lamp Touch Control Desk Lamp','YourMart','home-lifestyle',700,850,5.0,45,30,['https://picsum.photos/seed/h4/800/800','https://picsum.photos/seed/h5/800/800','https://picsum.photos/seed/h6/800/800'],{trending:true,description:'Modern LED desk lamp with sensitive touch control. 3 color temperatures, stepless dimming. Eye-caring LED, USB charging port, foldable.',features:['Touch Control','3 Color Temperatures','Stepless Dimming','Eye-Caring LED','USB Charging Port','Foldable'],specs:{'Brand':'YourMart','LED':'Eye-Caring 12W','Colors':'3000K/4500K/6500K','Control':'Touch','USB Port':'5V/1A','Material':'ABS + Metal'}}),
P(12,'Zafarani Freckle Cream Glutathione Serum','YourMart','beauty',900,1100,4.9,180,50,['https://sfile.chatglm.cn/images-ppt/8ad8fe14b7b9.jpg','https://picsum.photos/seed/b5/800/800','https://picsum.photos/seed/b6/800/800'],{featured:true,bestSeller:true,description:'Zafarani freckle cream with glutathione serum for skin whitening. Removes dark spots, freckles, and pigmentation naturally.',features:['Glutathione Serum','Freckle Removal','Dark Spot Treatment','Natural Ingredients','All Skin Types','Visible in 2 Weeks'],specs:{'Brand':'YourMart','Type':'Freckle Cream','Key Ingredient':'Glutathione','Size':'30g','Skin Type':'All types'}}),
P(13,'Whitening Zafarani Cream Set of 2','YourMart','beauty',1250,1500,5.0,95,40,['https://picsum.photos/seed/b7/800/800','https://picsum.photos/seed/b8/800/800','https://picsum.photos/seed/b9/800/800'],{featured:true,bestSeller:true,description:'Pack of 2 Zafarani whitening creams. Vitamin C and glutathione formula for brightening skin and removing dark spots.',features:['Set of 2 Creams','Skin Whitening','Spot Removal','Vitamin C + Glutathione','Natural Formula','All Skin Types'],specs:{'Brand':'YourMart','Quantity':'2 pieces','Size':'30g each','Key Ingredients':'Vitamin C, Glutathione','Results':'2 weeks'}}),
P(14,'Whitening Brightening Facial Kit Rice Extract','YourMart','beauty',900,1100,5.0,72,35,['https://picsum.photos/seed/b10/800/800','https://picsum.photos/seed/b11/800/800','https://picsum.photos/seed/b12/800/800'],{featured:true,bestSeller:true,description:'Complete 4-step facial kit with rice extract. Korean beauty formula includes cleanser, scrub, mask, and serum.',features:['Rice Extract','4-Step System','Korean Formula','Cleanser + Scrub + Mask + Serum','Brightening Effect','All Skin Types'],specs:{'Brand':'YourMart','Type':'Facial Kit','Key Ingredient':'Rice Extract','Steps':'4','Origin':'Korean Formula'}}),
P(15,'5-in-1 Hair Curler and Straightener','YourMart','beauty',3450,4000,5.0,88,20,['https://picsum.photos/seed/b13/800/800','https://picsum.photos/seed/b14/800/800','https://picsum.photos/seed/b15/800/800'],{featured:true,bestSeller:true,description:'Professional 5-in-1 hair styler. Curl, straighten, crimp, and wave with ceramic plates. Fast 30-second heat-up to 230C.',features:['5-in-1 Styling','Ceramic Plates','30s Fast Heat-up','230C Max Temp','Auto Shut-off','360 Swivel Cord'],specs:{'Brand':'YourMart','Functions':'5 in 1','Plates':'Ceramic Coated','Temp':'130-230C','Heat-up':'30 seconds','Cord':'2m 360 swivel'}}),
P(16,'3-in-1 Makeup and Skincare Bundle','YourMart','beauty',1350,1600,5.0,110,45,['https://picsum.photos/seed/b16/800/800','https://picsum.photos/seed/b17/800/800','https://picsum.photos/seed/b18/800/800'],{featured:true,bestSeller:true,description:'Complete 3-in-1 makeup and skincare bundle. Foundation, lipstick set, and skincare essentials in a premium gift case.',features:['3-in-1 Bundle','Makeup + Skincare','Gift Ready Case','Premium Quality','All Essentials','Compact'],specs:{'Brand':'YourMart','Type':'Bundle Set','Pieces':'3-in-1','Gift':'Premium Case','Quality':'Premium'}}),
P(17,'5-in-1 Premium Skincare Set','YourMart','beauty',2200,2600,5.0,65,25,['https://picsum.photos/seed/b19/800/800','https://picsum.photos/seed/b20/800/800','https://picsum.photos/seed/b21/800/800'],{featured:true,bestSeller:true,description:'Premium 5-step Korean skincare routine. Cleanser, toner, serum, moisturizer, and SPF sunscreen in travel sizes.',features:['5-Step Routine','Korean Formula','Cleanser + Toner + Serum + Moisturizer + SPF','Travel Size','Premium Ingredients','All Skin Types'],specs:{'Brand':'YourMart','Steps':'5','Formula':'Korean','SPF':'Included','Size':'Travel','Skin Type':'All'}}),
P(18,'Wellice Onion Anti-Hair Loss Shampoo','Wellice','beauty',640,800,4.6,200,60,['https://picsum.photos/seed/b22/800/800','https://picsum.photos/seed/b23/800/800','https://picsum.photos/seed/b24/800/800'],{featured:true,bestSeller:true,description:'Wellice onion shampoo with biotin for anti-hair loss. Strengthens roots, promotes growth, reduces hair fall. Sulfate free.',features:['Onion Extract','Biotin Enriched','Anti-Hair Loss','Strengthens Roots','Sulfate Free','400ml Large Size'],specs:{'Brand':'Wellice','Size':'400ml','Key Ingredient':'Onion Extract + Biotin','Sulfate Free':'Yes','Hair Type':'All types'}}),
P(19,'Nano Hydroxyapatite Teeth Whitening Toothpaste','YourMart','beauty',720,900,5.0,90,55,['https://picsum.photos/seed/b25/800/800','https://picsum.photos/seed/b26/800/800','https://picsum.photos/seed/b27/800/800'],{featured:true,bestSeller:true,description:'Professional nano hydroxyapatite toothpaste for teeth whitening. Removes stains, strengthens enamel, freshens breath.',features:['Nano Hydroxyapatite','Professional Whitening','Enamel Strengthener','Stain Removal','Fresh Mint Breath','Daily Use Safe'],specs:{'Brand':'YourMart','Key Ingredient':'Nano Hydroxyapatite','Size':'100g','Whitening':'Professional','Safe':'Daily Use','Flavor':'Fresh Mint'}}),
P(20,'Iconic London Highlighter 3 Shades','Iconic London','beauty',550,700,4.2,35,20,['https://picsum.photos/seed/b28/800/800','https://picsum.photos/seed/b29/800/800','https://picsum.photos/seed/b30/800/800'],{featured:true,description:'Iconic London highlighter palette with 3 shimmer shades. Illuminating formula for face and body. Buildable and long-lasting.',features:['3 Shimmer Shades','Illuminating Formula','Face and Body','Buildable','Long-Lasting','Compact Palette'],specs:{'Brand':'Iconic London','Shades':'3','Finish':'Shimmer','Longevity':'8+ hours','Use':'Face & Body'}}),
P(21,'8 Pcs Apple Shape Manicure Kit','YourMart','beauty',900,1100,5.0,75,40,['https://picsum.photos/seed/b31/800/800','https://picsum.photos/seed/b32/800/800','https://picsum.photos/seed/b33/800/800'],{featured:true,bestSeller:true,description:'Cute apple-shaped 8-piece manicure kit. Nail clipper, file, cuticle pusher, tweezers, scissors and more in compact case.',features:['8 Essential Tools','Apple Shape Case','Stainless Steel','Cuticle Pusher','Nail Clipper + File','Compact Design'],specs:{'Brand':'YourMart','Pieces':'8','Design':'Apple Shape','Material':'Stainless Steel','Case':'Compact'}}),
P(22,'19-in-1 Bridal Makeup Kit Complete','YourMart','beauty',2600,3100,5.0,95,18,['https://picsum.photos/seed/b34/800/800','https://picsum.photos/seed/b35/800/800','https://picsum.photos/seed/b36/800/800'],{featured:true,bestSeller:true,description:'Complete 19-piece bridal makeup kit. Foundations, lipsticks, eyeshadows, brushes all in premium gift box packaging.',features:['19 Pieces Complete','Bridal Special','Foundation + Lipstick + Eyeshadow','Brushes Included','Premium Quality','Gift Box'],specs:{'Brand':'YourMart','Pieces':'19','Occasion':'Bridal','Quality':'Premium','Packaging':'Gift Box','Includes':'Brushes Set'}}),
P(23,'16-in-1 Makeup Set Professional','YourMart','beauty',1850,2200,4.0,60,25,['https://picsum.photos/seed/b37/800/800','https://picsum.photos/seed/b38/800/800','https://picsum.photos/seed/b39/800/800'],{featured:true,description:'Professional 16-in-1 makeup set with color palettes, brushes, and tools. Complete daily and occasion makeup solution.',features:['16 Pieces','Professional Quality','Color Palettes','Brushes Included','Multi-Use','Compact Case'],specs:{'Brand':'YourMart','Pieces':'16','Type':'Professional Set','Includes':'Palettes + Brushes','Quality':'Premium'}}),
P(24,'Unisex Floral Perfume Pack Janan Zarar','Janan Zarar','beauty',900,1100,5.0,150,35,['https://sfile.chatglm.cn/images-ppt/c20a562c63c6.jpeg','https://sfile.chatglm.cn/images-ppt/380c25955d43.jpg','https://sfile.chatglm.cn/images-ppt/c20a562c63c6.jpeg'],{featured:true,bestSeller:true,description:'Janan Zarar unisex floral perfume. Long-lasting fragrance with premium floral notes. Perfect for daily wear and gifting.',features:['Unisex Floral Scent','Long-Lasting 8+ Hours','Premium Notes','Daily Wear','Gift Ready','50ml Bottle'],specs:{'Brand':'Janan Zarar','Type':'Eau de Parfum','Scent':'Floral','Size':'50ml','Longevity':'8+ hours','Gender':'Unisex'}}),
P(25,'Colorful Charm Bracelet Women','YourMart','watches-bags',1400,1700,5.0,42,30,['https://sfile.chatglm.cn/images-ppt/a9964f59aff7.png','https://sfile.chatglm.cn/images-ppt/a9964f59aff7.png','https://sfile.chatglm.cn/images-ppt/a9964f59aff7.png'],{trending:true,description:'Stunning colorful charm bracelet for women. Premium alloy with crystal charms, adjustable size, tarnish resistant.',features:['Colorful Crystal Charms','Adjustable Size','Tarnish Resistant','Premium Alloy','Gift Ready','Lightweight'],specs:{'Brand':'YourMart','Type':'Charm Bracelet','Material':'Alloy + Crystal','Adjustable':'Yes','Color':'Multi-color','Gender':'Women'}}),
P(26,'Turkish-Inspired Mens Ring Set of 3','YourMart','watches-bags',580,700,5.0,55,40,['https://sfile.chatglm.cn/images-ppt/a9964f59aff7.png','https://picsum.photos/seed/w5/800/800','https://picsum.photos/seed/w6/800/800'],{trending:true,description:'Set of 3 Turkish Ottoman-inspired men rings. Stainless steel with premium finish. Various intricate designs.',features:['Set of 3 Rings','Turkish Ottoman Design','Stainless Steel','Premium Finish','Comfortable Fit','Intricate Details'],specs:{'Brand':'YourMart','Quantity':'3 pieces','Material':'Stainless Steel','Style':'Turkish Ottoman','Finish':'Premium Polish','Fit':'Adjustable'}}),
P(27,'Stainless Steel Heart Love Watch Women','YourMart','watches-bags',680,850,5.0,38,25,['https://picsum.photos/seed/w7/800/800','https://picsum.photos/seed/w8/800/800','https://picsum.photos/seed/w9/800/800'],{trending:true,description:'Elegant heart-shaped dial watch for women. Stainless steel mesh band, quartz movement. Beautiful love-themed design.',features:['Heart Shape Dial','Stainless Steel Mesh Band','Quartz Movement','Adjustable Band','Elegant Design','Perfect Gift'],specs:{'Brand':'YourMart','Dial':'Heart Shape','Movement':'Japanese Quartz','Band':'Stainless Steel Mesh','Water Resistant':'3ATM','Gender':'Women'}}),
P(28,'Black Skeleton Chronograph Watch Men','YourMart','watches-bags',2800,3300,5.0,48,15,['https://picsum.photos/seed/w10/800/800','https://picsum.photos/seed/w11/800/800','https://picsum.photos/seed/w12/800/800'],{trending:true,description:'Premium black skeleton watch with chronograph. See-through mechanical dial, stainless steel bracelet, luminous hands.',features:['Skeleton See-Through Dial','Chronograph Function','Stainless Steel Bracelet','Japanese Movement','Luminous Hands','Sapphire Crystal'],specs:{'Brand':'YourMart','Dial':'Skeleton','Movement':'Japanese Mechanical','Band':'Stainless Steel','Chronograph':'Yes','Water Resistant':'3ATM'}}),
P(29,'RALEX Gold Plated Watch Men Luxury','RALEX','watches-bags',1500,1800,5.0,62,20,['https://picsum.photos/seed/w13/800/800','https://picsum.photos/seed/w14/800/800','https://picsum.photos/seed/w15/800/800'],{trending:true,description:'RALEX luxury gold-plated watch for men. Genuine leather strap, elegant design for formal and casual occasions.',features:['Gold Plated Case','Genuine Leather Strap','RALEX Brand','Japanese Quartz','Formal and Casual','Gift Box Included'],specs:{'Brand':'RALEX','Plating':'Gold','Strap':'Genuine Leather','Movement':'Japanese Quartz','Case':'40mm','Style':'Luxury'}}),
P(30,'Premium Croc Embossed Leather Wallet Men','YourMart','watches-bags',620,800,5.0,80,35,['https://picsum.photos/seed/w16/800/800','https://picsum.photos/seed/w17/800/800','https://picsum.photos/seed/w18/800/800'],{trending:true,description:'Premium crocodile embossed genuine leather wallet. RFID blocking, 8+ card slots, slim bifold design with gift box.',features:['Croc Embossed Pattern','Genuine Leather','RFID Blocking','8+ Card Slots','Slim Bifold','Gift Box'],specs:{'Brand':'YourMart','Material':'Genuine Leather','Pattern':'Crocodile Embossed','RFID':'Yes','Card Slots':'8+','Type':'Slim Bifold'}}),
P(31,'Mustard PU Leather Crossbody Bag','YourMart','watches-bags',1200,1450,5.0,45,20,['https://picsum.photos/seed/w19/800/800','https://picsum.photos/seed/w20/800/800','https://picsum.photos/seed/w21/800/800'],{trending:true,description:'Stylish mustard yellow PU leather crossbody bag. Adjustable strap, multiple compartments, compact everyday design.',features:['Mustard Yellow Color','Premium PU Leather','Crossbody Style','Adjustable Strap','Multiple Compartments','Compact Design'],specs:{'Brand':'YourMart','Color':'Mustard Yellow','Material':'PU Leather','Style':'Crossbody','Strap':'Adjustable','Compartments':'3+'}}),
P(32,'Green Crossbody Bag Rose Gold Chain','YourMart','watches-bags',1450,1700,4.6,32,18,['https://picsum.photos/seed/w22/800/800','https://picsum.photos/seed/w23/800/800','https://picsum.photos/seed/w24/800/800'],{trending:true,description:'Elegant green crossbody bag with rose gold chain strap. Premium PU leather, spacious interior, perfect for parties.',features:['Elegant Green Color','Rose Gold Chain Strap','Premium PU Leather','Spacious Interior','Party Ready','Lining':'Polyester']],specs:{'Brand':'YourMart','Color':'Green','Chain':'Rose Gold','Material':'Premium PU Leather','Style':'Crossbody','Occasion':'Party/Formal'}}),
P(33,'Manual Food Chopper Vegetable Cutter','YourMart','kitchen',900,1100,5.0,130,40,['https://sfile.chatglm.cn/images-ppt/380c25955d43.jpg','https://sfile.chatglm.cn/images-ppt/03407873302e.jpg','https://sfile.chatglm.cn/images-ppt/03407873302e.jpg'],{trending:true,description:'Manual pull-string food chopper. Sharp stainless steel blades, 900ml BPA-free container. Quick vegetable and fruit cutting.',features:['Pull String Operation','Stainless Steel Blades','900ml BPA-Free Container','Sharp and Fast','Easy to Clean','Compact Design'],specs:{'Brand':'YourMart','Type':'Manual Chopper','Blades':'Stainless Steel 3 pcs','Capacity':'900ml','Material':'BPA-Free PP','Dishwasher Safe':'Container Only'}}),
P(34,'Nano Tape Reusable Home Organization','YourMart','home-lifestyle',490,600,5.0,200,60,['https://picsum.photos/seed/h7/800/800','https://picsum.photos/seed/h8/800/800','https://picsum.photos/seed/h9/800/800'],{trending:true,description:'Reusable nano magic tape for home organization. Strong adhesion, no residue, washable. Works on walls, glass, tiles.',features:['Reusable and Washable','Strong Adhesion','No Residue','Multi-Surface','Transparent','3m Roll'],specs:{'Brand':'YourMart','Type':'Nano Magic Tape','Adhesion':'Strong','Reusable':'Yes','Washable':'Yes','Size':'3m x 3cm x 1mm'}}),
P(35,'Quilted Microwave Cover Dust Protection','YourMart','kitchen',550,700,4.3,55,35,['https://sfile.chatglm.cn/images-ppt/03407873302e.jpg','https://picsum.photos/seed/k5/800/800','https://picsum.photos/seed/k6/800/800'],{trending:true,description:'Quilted cotton microwave cover with beautiful print. Protects from dust and splatters, machine washable, easy fit.',features:['Quilted Cotton','Dust and Splash Protection','Machine Washable','Beautiful Print','Easy Fit','Standard Size'],specs:{'Brand':'YourMart','Material':'Quilted Cotton','Fit':'Standard Microwave','Washable':'Machine Wash','Design':'Printed','Protection':'Dust + Splash'}}),
P(36,'Vibrant Wall Stickers Room Decor','YourMart','home-lifestyle',460,580,5.0,85,50,['https://picsum.photos/seed/h10/800/800','https://picsum.photos/seed/h11/800/800','https://picsum.photos/seed/h12/800/800'],{trending:true,description:'Vibrant colorful wall stickers for room decoration. Self-adhesive, waterproof, removable vinyl. Multiple designs for any room.',features:['Self-Adhesive','Waterproof','Removable No Residue','Multiple Designs','Easy to Apply','Vibrant Colors'],specs:{'Brand':'YourMart','Type':'Wall Sticker','Material':'Vinyl','Waterproof':'Yes','Removable':'Yes','Application':'Smooth Surfaces'}}),
P(37,'Silicone Back Bath Scrubber Belt','YourMart','home-lifestyle',530,650,4.0,40,25,['https://picsum.photos/seed/h13/800/800','https://picsum.photos/seed/h14/800/800','https://picsum.photos/seed/h15/800/800'],{trending:true,description:'Silicone back scrubber with extended handle. Soft silicone bristles for comfortable cleaning, hangable design for drying.',features:['Silicone Bristles','Extended Handle','Comfortable Grip','Hangable Design','Easy to Clean','Gentle on Skin'],specs:{'Brand':'YourMart','Material':'Food-Grade Silicone','Handle':'Extended 40cm','Bristles':'Soft Silicone','Design':'Ergonomic','Storage':'Hangable'}}),
P(38,'Mens Dri-Fit Track Suit 2pc Set','YourMart','mens-fashion',1200,1450,5.0,95,30,['https://sfile.chatglm.cn/images-ppt/a9964f59aff7.png','https://sfile.chatglm.cn/images-ppt/a9964f59aff7.png','https://sfile.chatglm.cn/images-ppt/a9964f59aff7.png'],{trending:true,description:"Men's premium dri-fit track suit. Quick-dry moisture-wicking fabric, 2 pieces (jacket + pants). Available in multiple colors.",features:['Dri-Fit Quick Dry','Moisture Wicking','2 Piece Set','Comfortable Fit','Multiple Colors','Gym and Casual'],specs:{'Brand':'YourMart','Type':'Track Suit','Pieces':'2 (Jacket + Pants)','Fabric':'Dri-Fit Polyester','Fit':'Regular','Sizes':'M, L, XL, XXL'}}),
P(39,'Unisex Printed Polyester T-Shirt','YourMart','mens-fashion',590,750,5.0,110,50,['https://sfile.chatglm.cn/images-ppt/a9964f59aff7.png','https://picsum.photos/seed/m5/800/800','https://picsum.photos/seed/m6/800/800'],{trending:true,description:'Premium printed polyester t-shirt with soft fabric and durable DTF print. Unisex design, multiple colors and prints available.',features:['Unisex Design','Premium DTF Print','Soft Polyester Fabric','Durable Print','Multiple Options','Casual Everyday'],specs:{'Brand':'YourMart','Material':'Polyester','Print':'Premium DTF','Fit':'Regular','Sizes':'S, M, L, XL, XXL','Care':'Machine Wash'}}),
P(40,'Mens Knitted Zip-Up Cardigan Sweater','YourMart','mens-fashion',3700,4200,4.8,35,15,['https://picsum.photos/seed/m7/800/800','https://picsum.photos/seed/m8/800/800','https://picsum.photos/seed/m9/800/800'],{trending:true,description:"Premium men's knitted zip-up cardigan. Soft warm acrylic blend, full zip front. Perfect for winter casual and semi-formal wear.",features:['Knitted Warm Fabric','Full Zip Front','Soft Acrylic Blend','Premium Quality','Winter Essential','Versatile Style'],specs:{'Brand':'YourMart','Type':'Cardigan','Material':'Acrylic Blend Knit','Closure':'Full Zip','Fit':'Regular','Season':'Winter'}}),

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
