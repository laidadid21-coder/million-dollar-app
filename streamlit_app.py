import streamlit as st

# 1. إعدادات المنصة العالمية بملء الشاشة
st.set_page_config(
    page_title="AliExpress Style Global Market | مكتب عديد العيد",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. تصميم CSS مخصص متقدم لكسر المظهر البدائي وتحويله إلى متجر حقيقي
st.markdown("""
    <style>
    /* خلفية المنصة وتنسيق النصوص */
    .main { background-color: #f4f4f7; }
    h1, h2, h3 { color: #222222; font-family: 'Cairo', sans-serif; text-align: right; }
    
    /* تصميم البنر الإعلاني العلوي الاحترافي */
    .promo-banner {
        background: linear-gradient(135deg, #FF4742 0%, #FDC830 100%);
        color: white;
        padding: 40px;
        border-radius: 15px;
        text-align: right;
        margin-bottom: 30px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.05);
    }
    .promo-banner h1 { color: white; margin: 0; font-size: 32px; font-weight: bold; }
    .promo-banner p { font-size: 18px; margin-top: 10px; opacity: 0.9; }
    
    /* تصميم بطاقات المنتجات الاحترافية (Product Cards) */
    .product-card {
        background-color: white;
        border-radius: 12px;
        padding: 16px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.04);
        transition: transform 0.3s ease;
        margin-bottom: 20px;
        border: 1px solid #eaeaea;
        text-align: right;
    }
    .product-card:hover { transform: translateY(-5px); box-shadow: 0 6px 15px rgba(0,0,0,0.08); }
    .product-price { color: #FF4742; font-size: 22px; font-weight: bold; margin: 10px 0; font-family: sans-serif; }
    .product-title { font-size: 16px; font-weight: bold; color: #333; height: 45px; overflow: hidden; }
    .product-tag { background-color: #FFF0F0; color: #FF4742; padding: 3px 8px; border-radius: 4px; font-size: 12px; font-weight: bold; display: inline-block; }
    
    /* أزرار الشراء الفورية */
    .stButton>button {
        background-color: #FF4742 !important;
        color: white !important;
        border-radius: 20px !important;
        border: none !important;
        font-weight: bold !important;
        width: 100%;
    }
    .stButton>button:hover { background-color: #E03E39 !important; }
    </style>
""", unsafe_allow_html=True)

# 3. القائمة الجانبية لإدارة المتجر وتغيير المنتجات (مخفية لراحة المستخدم)
with st.sidebar:
    st.header("⚙️ مركز إدارة وعرض المنتجات")
    st.write("استخدم هذه اللوحة لتعديل المنتج المعروض في الواجهة الرئيسية.")
    
    input_title = st.text_input("اسم المنتج النشط:", value="نظام أتمتة العقود الذكية والتحول الرقمي للشركات")
    input_price = st.number_input("سعر العرض المباشر (USD):", min_value=0.0, value=249.99)
    input_tag = st.text_input("ملصق العرض (Tag):", value="العروض الفائقة")
    
    st.divider()
    uploaded_file = st.file_uploader("📸 تغيير صورة المنتج الرئيسي بالواجهة:", type=["png", "jpg", "jpeg"])
    
    st.divider()
    st.caption("📜 بروتوكول مكتب عديد العيد - السيطرة الرقمية وتحصيل العمولات آلياً.")

# 4. واجهة المتجر الرئيسية (AliExpress UI)

# أ. البنر الإعلاني العلوي الضخم لقسم الترويج
st.markdown("""
    <div class="promo-banner">
        <h1>ترقية الأعمال والرقمنة السيادية 🌐</h1>
        <p>تعزيز كفاءة الأداء التجاري والقانوني • رؤية 2026 (صفر ورقة)</p>
        <span style="background-color: black; color: white; padding: 6px 15px; border-radius: 20px; font-weight: bold; display: inline-block; margin-top: 15px;">تسوق الآن</span>
    </div>
""", unsafe_allow_html=True)

st.markdown("## 🔥 صفقات اليوم والحلول الرقمية الفائقة")
st.markdown("---")

# ب. شبكة عرض المنتجات الديناميكية (Product Grid) مقسمة إلى 3 أعمدة مثل المتاجر العالمية
col1, col2, col3 = st.columns(3)

# --- المنتج الأول: المنتج الديناميكي المرتبط بلوحة التحكم والرفع الجانبية ---
with col1:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    
    # التحقق من رفع صورة مخصصة من اللوحة الجانبية، وإلا عرض صورة افتراضية احترافية لقسم الرقمنة
    if uploaded_file is not None:
        st.image(uploaded_file, use_container_width=True)
    else:
        st.image("https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=500", use_container_width=True)
        
    st.markdown(f'<span class="product-tag">{input_tag}</span>', unsafe_allow_html=True)
    st.markdown(f'<div class="product-title">{input_title}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="product-price">${input_price:,.2f}</div>', unsafe_allow_html=True)
    
    # زر تأكيد الطلب الفوري المرتبط بالأتمتة
    if st.button("🛒 شراء الآن الفوري", key="btn_prod_1"):
        st.success("🎯 تم تأكيد طلبيتك بنظام الأتمتة! جاري تحويل البيانات إلى غرف المعالجة السحابية.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- المنتج الثاني: حزمة الأتمتة الجاهزة (مثال ثابت لتأكيد الثراء البصري) ---
with col2:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=500", use_container_width=True)
    st.markdown('<span class="product-tag">عروض الحزمة</span>', unsafe_allow_html=True)
    st.markdown('<div class="product-title">مستودعات أتمتة n8n الكاملة وجداول Airtable القانونية السيادية</div>', unsafe_allow_html=True)
    st.markdown('<div class="product-price">$642.23</div>', unsafe_allow_html=True)
    
    if st.button("🛒 شراء الآن الفوري", key="btn_prod_2"):
        st.success("🔥 تم تسجيل طلبك للحزمة الاستراتيجية. تفقد البريد الإلكتروني آلياً.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- المنتج الثالث: استشارات التحول الرقمي والتسويق (مثال ثابت) ---
with col3:
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=500", use_container_width=True)
    st.markdown('<span class="product-tag">تخفيض 50%</span>', unsafe_allow_html=True)
    st.markdown('<div class="product-title">جلسة هندسة عكسية وتدقيق البنية التحتية الرقمية للمؤسسات الكبرى</div>', unsafe_allow_html=True)
    st.markdown('<div class="product-price">$525.20</div>', unsafe_allow_html=True)
    
    if st.button("🛒 شراء الآن الفوري", key="btn_prod_3"):
        st.info("🔒 تم تفعيل مسار الحماية وتأكيد طلب الاستشارة الشخصية.")
    st.markdown('</div>', unsafe_allow_html=True)

# تذييل الصفحة الاحترافي لنظام السيادة
st.markdown("---")
st.markdown("<p style='text-align: center; color: #888888;'>© 2026 جميع الحقوق محفوظة لشبكة التاجر العالمي السحابية | مكتب المحامي عديد العيد</p>", unsafe_allow_html=True)
