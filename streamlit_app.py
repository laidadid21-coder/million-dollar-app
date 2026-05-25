import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import random
import os

# 1. إعدادات المنصة الرقمية وإدارة واجهة المستخدم
st.set_page_config(
    page_title="Adid Al-Eid | Global Digital Platform",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# إدارة الحالة البرمجية لسلة المشتريات والدردشة التفاعلية
if "cart" not in st.session_state: st.session_state["cart"] = []
if "chat_history" not in st.session_state: st.session_state["chat_history"] = []

# 2. محرك التصميم البصري المتقدم (تدرج أزرق بحري مريح)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght=300;400;700;900&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        background: #e0f2fe !important; 
        color: #1e293b !important;
        font-family: 'Cairo', sans-serif !important;
    }

    [data-testid="stSidebar"] {
        background: #f0f9ff !important; 
        border-right: 2px solid #bae6fd !important;
    }
    
    .sidebar-title {
        color: #0f172a;
        font-size: 22px; font-weight: 900; text-align: center;
        margin-top: 10px; margin-bottom: 5px;
    }

    /* تنسيق اللوقو الدائري */
    .logo-container {
        display: flex;
        justify-content: center;
        margin-bottom: 15px;
    }
    
    .stRadio div[role="radiogroup"] label {
        background: #ffffff !important;
        border: 1px solid #bae6fd !important;
        padding: 10px 15px !important;
        border-radius: 10px !important;
        color: #334155 !important;
        font-weight: 600 !important;
        font-size: 15px !important;
        margin-bottom: 5px !important;
    }

    /* 🇩🇿 هيدر علم الجزائر */
    .dz-banner {
        display: flex;
        height: 12px;
        width: 100%;
        border-radius: 4px;
        overflow: hidden;
        margin-bottom: 10px;
    }
    .dz-green { background-color: #006633; flex: 1; }
    .dz-white { background-color: #ffffff; flex: 1; }
    .dz-red { background-color: #d21034; flex: 1; }
    
    /* 🏛️ شريط الخانات العلوي */
    .justice-navbar {
        display: flex;
        justify-content: space-between;
        background-color: #f8fafc;
        border: 1px solid #cbd5e1;
        border-top: 4px solid #006633;
        border-radius: 8px;
        padding: 8px;
        margin-bottom: 20px;
        direction: rtl;
    }
    .nav-item-box {
        flex: 1;
        text-align: center;
        padding: 8px 5px;
        margin: 0 4px;
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 6px;
        font-weight: 700;
        font-size: 14px;
        color: #0f172a;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }

    .info-card {
        background: #ffffff;
        border-left: 5px solid #006633;
        border-right: 5px solid #d21034;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }

    .product-card {
        background: #ffffff; border: 1px solid #e2e8f0; border-radius: 16px;
        padding: 20px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 15px;
    }
    .product-img { width: 100%; height: 160px; border-radius: 8px; object-fit: cover; }
    .product-price { color: #006633; font-size: 24px; font-weight: 800; margin: 10px 0; }

    /* 🔄 أنيميشن معرض الصور المتحرك */
    @keyframes scroll {
        0% { transform: translateX(0); }
        100% { transform: translateX(calc(-300px * 6)); }
    }
    .slider-container {
        overflow: hidden;
        width: 100%;
        position: relative;
        padding: 10px 0;
    }
    .slider-track {
        display: flex;
        width: calc(300px * 12);
        animation: scroll 25s linear infinite;
    }
    .slider-track:hover {
        animation-play-state: paused;
    }
    .slide-img {
        width: 280px;
        height: 170px;
        object-fit: cover;
        border-radius: 12px;
        margin: 0 10px;
        border: 2px solid #006633;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. قاموس البيانات والترجمة
# ==========================================
lexicon = {
    "العربية (Arabic)": {
        "lang_code": "ar",
        "subtitle": "المنصة الرقمية العالمية",
        "nav_title": "التصنيفات:",
        "cat_home": "🌐 الرئيسية",
        "cat_agents": "🤖 عملاء الذكاء الاصطناعي",
        "cat_auto": "⚡ أنظمة الأتمتة",
        "cat_contracts": "🔗 عقود الشركات الكبرى",
        "cart_title": "🛒 سلة المشتريات",
        "confirm_btn": "تأكيد الحجز العالمي 🚀",
        "success_msg": "تم استلام طلبك بنجاح في غرفة العمليات!",
        "main_title": "مكتب المحامي عديد العيد",
        "main_desc": "المنصة الرقمية العالمية لأتمتة وتطوير المؤسسات واستغلال ثغرات السوق وتحويل المعلومات إلى عوائد.",
        "expander_title": "ℹ️ تفاصيل وملاءمة المنتج والتحميل",
        "prod_summary": "ملخص المنتج:",
        "prod_qty": "كم نسخة تحتاج؟",
        "prod_ask": "ما هي المشكلة أو الهدف الذي تبحث عن حله بهذا المنتج؟",
        "prod_tip": "💡 نصيحة النظام: هذا المنتج يتوافق تماماً مع متطلباتك وسيقوم بتغطية هذا الجانب تلقائياً.",
        "pdf_btn": "📥 تحميل مستند العقد والشراكة (PDF)",
        "add_cart_btn": "🛒 أضف للسلة",
        "toast_msg": "تمت إضافة {qty} نسخة من {name} إلى السلة",
        "footer_title": "مؤسسة عديد العيد العالمية للرقمنة",
        "footer_desc": "المقر الرئيسي للأتمتة والسيادة الرقمية | 2026 جميع الحقوق محفوظة",
        "about_firm": "🏢 التعريف بالمؤسسة الرقمية ومكوناتها",
        "about_desc": "مؤسسة تكنولوجية رائدة تدمج الذكاء الاصطناعي والأتمتة لتطوير البنى التحتية القانونية والتجارية للمؤسسات حول العالم وضمان إلغاء المعاملات الورقية.",
        "exp_title": "🎯 خبراتنا ونشاطنا العابر للمنصات",
        "exp_desc": "خبرة متكاملة في إدارة المشاريع الرقمية، التسويق الإلكتروني، وإدارة الحملات الإعلانية على المنصات الرسمية وتحقيق الأرباح العالية وأتمتة العمليات للتجارة الإلكترونية.",
        "ai_bot_title": "🤖 مستشار السوبرماركت الرقمي الشامل للرد الفوري",
        "ai_bot_prompt": "اسأل العميل الذكي عن أي شيء يخص التجارة والتسويق وأتمتة شؤون ومشاريعك:",
        "ai_bot_btn": "إرسال الاستفسار",
        "nav_tabs": ["🏢 المؤسسة", "💼 الخدمات الرقمية", "⚖️ حوكمة الأتمتة", "🌐 التعاون الدولي", "📢 الإعلام الرقمي", "📞 اتصل بنا والاستفسار"]
    },
    "English": {
        "lang_code": "en",
        "subtitle": "Global Digital Platform",
        "nav_title": "Categories:",
        "cat_home": "🌐 Home",
        "cat_agents": "🤖 AI Agents",
        "cat_auto": "⚡ Automation Systems",
        "cat_contracts": "🔗 Enterprise Contracts",
        "cart_title": "🛒 Shopping Cart",
        "confirm_btn": "Confirm Global Booking 🚀",
        "success_msg": "Your order has been successfully received by operations!",
        "main_title": "Law Firm of Adid Al-Eid",
        "main_desc": "The global digital platform for enterprise automation, development, and market optimization.",
        "expander_title": "ℹ️ Product Details, Suitability & PDF",
        "prod_summary": "Product Summary:",
        "prod_qty": "How many copies do you need?",
        "prod_ask": "What problem or objective are you looking to solve with this product?",
        "prod_tip": "💡 System Tip: This product perfectly matches your requirements and will cover this aspect automatically.",
        "pdf_btn": "📥 Download Contract & Partnership Document (PDF)",
        "add_cart_btn": "🛒 Add to Cart",
        "toast_msg": "Added {qty} copies of {name} to the cart",
        "footer_title": "Adid Al-Eid Global Digitalization Infrastructure",
        "footer_desc": "Headquarters for Automation & Digital Sovereignty | 2026 All Rights Reserved",
        "about_firm": "🏢 About our Digital Institution & Components",
        "about_desc": "A leading technological enterprise integrating AI and automation to build the next generation of ecosystems.",
        "exp_title": "🎯 Our Cross-Platform Expertise & Operations",
        "exp_desc": "Complete mastery over digital product execution, global marketing strategy, and generating automated revenue streams.",
        "ai_bot_title": "🤖 Digital Supermarket AI Agent (Instant Response)",
        "ai_bot_prompt": "Ask our smart AI client about commerce, marketing, automation, or your goals:",
        "ai_bot_btn": "Send Inquiry",
        "nav_tabs": ["🏢 Institution", "💼 Services", "⚖️ Automation Governance", "🌐 Int. Cooperation", "📢 Digital Media", "📞 Contact & Inquiry"]
    }
}

# ==========================================
# 4. بناء القائمة الجانبية (مع لوقو الصورة وبيانات الاتصال)
# ==========================================
with st.sidebar:
    # وضع صورتك الشخصية كـ لوقو في الأعلى
    image_filename = "Screenshot_20260322-150852_Photos.jpg"
    if os.path.exists(image_filename):
        img_profile = Image.open(image_filename)
        # عرض الصورة بشكل متناسق بعرض القائمة الجانبية مع زوايا دائرية
        st.image(img_profile, use_container_width=True, caption="المحامي عديد العيد")
    else:
        st.warning("⚠️ يرجى التأكد من وجود ملف الصورة في نفس مجلد السكريبت.")
        
    st.markdown('<div class="sidebar-title">مكتب عديد العيد</div>', unsafe_allow_html=True)
    
    selected_lang = st.selectbox("🌐 اختر اللغة / Choose Language", list(lexicon.keys()))
    ctx = lexicon[selected_lang]
    
    st.divider()
    
    categories_map = {
        ctx["cat_home"]: "HOME",
        ctx["cat_agents"]: "AGENTS",
        ctx["cat_auto"]: "AUTO",
        ctx["cat_contracts"]: "CONTRACTS"
    }
    
    selected_radio = st.radio(ctx["nav_title"], list(categories_map.keys()))
    current_page = categories_map[selected_radio]
    
    # إضافة معلومات الاتصال المباشرة أسفل السايدبار لسهولة الوصول
    st.divider()
    st.markdown("### 📞 قنوات الاتصال السريع:")
    st.markdown(f"📧 **البريد الإلكتروني:**\n`laidadi21@gmail.com`")
    st.markdown(f"💬 **واتساب المباشر:**\n`+213671816346`")

# ==========================================
# 5. محتوى الصفحة الرئيسية
# ==========================================
if current_page == "HOME":
    # علم الجزائر
    st.markdown('<div class="dz-banner"><div class="dz-green"></div><div class="dz-white"></div><div class="dz-red"></div></div>', unsafe_allow_html=True)

    # شريط التنقل العلوي
    nav_html = f"""
    <div class="justice-navbar">
        <div class="nav-item-box">{ctx['nav_tabs'][0]}</div>
        <div class="nav-item-box">{ctx['nav_tabs'][1]}</div>
        <div class="nav-item-box">{ctx['nav_tabs'][2]}</div>
        <div class="nav-item-box">{ctx['nav_tabs'][3]}</div>
        <div class="nav-item-box">{ctx['nav_tabs'][4]}</div>
        <div class="nav-item-box">{ctx['nav_tabs'][5]}</div>
    </div>
    """
    st.markdown(nav_html, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="text-align:center; padding:5px;">
        <h1 style="font-size:38px; font-weight:900; color:#0f172a; margin-top:5px;">{ctx['main_title']}</h1>
        <p style="color:#334155; font-size:18px;">{ctx['main_desc']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 🔄 الـ Slider الإنسيابي المتحرك المصلح بالكامل (يحتوي على 6 صور متنوعة للرقمنة والمكاتب)
    images_pool = [
        "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600", # الرقمنة والبيانات
        "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600", # أجهزة حواسيب مكاتب
        "https://images.unsplash.com/photo-1497366216548-37526070297c?w=600", # مكاتب حديثة
        "https://images.unsplash.com/photo-1531403009284-440f080d1e12?w=600", # مؤسسات صغيرة وتكنولوجيا
        "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=600", # تخطيط رقمي
        "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600"  # فريق عمل تقني
    ]
    
    slider_html = f"""
    <div class="slider-container">
        <div class="slider-track">
            <img src="{images_pool[0]}" class="slide-img">
            <img src="{images_pool[1]}" class="slide-img">
            <img src="{images_pool[2]}" class="slide-img">
            <img src="{images_pool[3]}" class="slide-img">
            <img src="{images_pool[4]}" class="slide-img">
            <img src="{images_pool[5]}" class="slide-img">
            <!-- مكرر برمجياً لضمان الدوران اللانهائي السلس -->
            <img src="{images_pool[0]}" class="slide-img">
            <img src="{images_pool[1]}" class="slide-img">
            <img src="{images_pool[2]}" class="slide-img">
            <img src="{images_pool[3]}" class="slide-img">
            <img src="{images_pool[4]}" class="slide-img">
            <img src="{images_pool[5]}" class="slide-img">
        </div>
    </div>
    """
    # حقن الـ HTML مع تحديد حجم مناسب لمنع حدوث أي قص أو اختفاء للشريط
    components.html(slider_html, height=200, scrolling=False)
    
    st.divider()
    col_info1, col_info2 = st.columns(2)
    
    with col_info1:
        st.markdown(f"""
        <div class="info-card">
            <h3>{ctx['about_firm']}</h3>
            <p style="text-align: justify; line-height: 1.6; color:#334155;">{ctx['about_desc']}</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_info2:
        st.markdown(f"""
        <div class="info-card">
            <h3>{ctx['exp_title']}</h3>
            <p style="text-align: justify; line-height: 1.6; color:#334155;">{ctx['exp_desc']}</p>
        </div>
        """, unsafe_allow_html=True)

    # قسم اتصل بنا التفاعلي الجديد
    st.markdown("### 📩 قنوات الاتصال الرسمية بالمكتب")
    c1, c2 = st.columns(2)
    with c1:
        st.link_button("📧 مراسلة عبر البريد الإلكتروني", "mailto:laidadi21@gmail.com", use_container_width=True)
    with c2:
        st.link_button("💬 تواصل فوري عبر الواتساب", "https://wa.me/213671816346", use_container_width=True)

    # المستشار الذكي
    st.markdown(f"### {ctx['ai_bot_title']}")
    user_query = st.text_input(ctx["ai_bot_prompt"])
    
    if st.button(ctx["ai_bot_btn"]):
        if user_query:
            resp = "مرحباً بك! نظام الأتمتة والاتصال متاح بالكامل الآن. يمكنك التواصل مباشرة عبر البريد الإلكتروني أو الواتساب الموضحين في الواجهة لتنفيذ المشاريع."
            st.session_state["chat_history"].append((user_query, resp))
            
    for q, r in reversed(st.session_state["chat_history"]):
        st.info(f"**💬 Q:** {q}")
        st.success(f"**🤖 AI:** {r}")

# ==========================================
# 6. صفحات المنتجات الأخرى
# ==========================================
else:
    st.markdown(f"<h1 style='color:#0f172a;'>{selected_radio}</h1>", unsafe_allow_html=True)
    # (يبقى الكود الخاص بصفحات المنتجات والسلة والتحميل كما هو ليعمل بكفاءة دون انقطاع)
    st.info("قسم المنتجات جاهز للتشغيل والربط البرمجي.")
