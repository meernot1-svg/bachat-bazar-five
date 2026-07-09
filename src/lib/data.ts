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
