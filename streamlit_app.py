import streamlit as st
import streamlit.components.v1 as components
import random

# 1. إعدادات الإمبراطورية الرقمية v11.0 (تحديث)
st.set_page_config(
    page_title="Adid Al-Eid | Digital Powerhouse",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. إدارة الحالة (لا تغيير)
if "cart" not in st.session_state: st.session_state["cart"] = []
if "category" not in st.session_state: st.session_state["category"] = "الكل"

# 3. محرك التصميم البصري المحدث (ألوان فواتح، وضوح، شعار جديد)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;700;900&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        background: #f0f2f6 !important; /* لون خلفية رئيسي فاتح */
        color: #1e293b !important; /* نص رئيسي داكن */
        font-family: 'Cairo', sans-serif !important;
    }

    /* --- الجهة اليسرى (Sidebar) - تحويل للألوان الفاتحة --- */
    [data-testid="stSidebar"] {
        background: #ffffff !important; /* خلفية جانبية بيضاء نقية */
        border-right: 2px solid #e2e8f0 !important; /* حدود رمادية خفيفة */
    }
    
    .sidebar-title {
        color: #0f172a; /* عنوان داكن جداً وواضح */
        font-size: 28px; font-weight: 900; text-align: center;
        margin-bottom: 20px; text-transform: uppercase; letter-spacing: 2px;
    }

    /* تحسين وضوح أزرار القائمة الجانبية (تصميم مسطح وأكثر سطوعاً) */
    .stRadio div[role="radiogroup"] label {
        background: #f8fafc !important; /* خلفية زر فاتحة جداً */
        border: 1px solid #e2e8f0 !important; /* حدود خفيفة */
        padding: 12px 20px !important;
        border-radius: 10px !important;
        color: #334155 !important; /* نص داكن وواضح */
        font-weight: 600 !important;
        font-size: 16px !important;
        margin-bottom: 6px !important;
    }
    .stRadio div[role="radiogroup"] label:hover {
        background-color: #f1f5f9 !important;
        border-color: #cbd5e1 !important;
        transform: translateX(5px);
        transition: all 0.3s;
    }
    .stRadio div[role="radiogroup"] label[data-selected="true"] {
        background-color: #0f172a !important; /* خلفية الزر المحدد */
        color: #ffffff !important; /* نص أبيض للزر المحدد */
        font-weight: 700 !important;
    }

    /* --- شعار "L" الأنيق والجديد --- */
    .logo-l {
        width: 80px;
        height: 80px;
        border: 4px solid #0f172a;
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        font-family: 'Arial', sans-serif;
        font-size: 50px;
        font-weight: 900;
        color: #0f172a;
        margin: 0 auto 15px auto;
    }

    /* --- السلايدر المتحرك (لا تغيير كبير، لكن ألوانه متناسبة) --- */
    @keyframes scroll {
        0% { transform: translateX(0); }
        100% { transform: translateX(calc(-400px * 4)); }
    }
    .slider-wrapper {
        display: flex; width: calc(400px * 8);
        animation: scroll 25s linear infinite;
    }
    .slider-wrapper:hover { animation-play-state: paused; }
    .slide-item {
        width: 380px; height: 500px; margin: 10px;
        border-radius: 20px; border: 3px solid #0f172a; /* حدود داكنة للوضوح */
        object-fit: cover; filter: brightness(1.0); /* إرجاع السطوع الكامل */
    }

    /* --- بطاقات المتجر المحدثة (تصميم مسطح، ألوان فواتح) --- */
    .product-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 25px;
        text-align: center;
        transition: 0.3s;
        height: 480px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .product-card:hover {
        border-color: #cbd5e1;
        box-shadow: 0 10px 15px rgba(0,0,0,0.1);
    }
    .product-img { width: 100%; height: 180px; border-radius: 8px; object-fit: cover; }
    .product-price { color: #0f172a; font-size: 26px; font-weight: 800; }
    
    /* أيقونات 3D للمنتجات (تحديث للتدرج) */
    .icon-3d-box {
        font-size: 40px; margin-bottom: 10px;
        filter: drop-shadow(0 0 10px rgba(15, 23, 42, 0.3));
    }

    /* زر الشراء الداكن والأنيق */
    .buy-btn {
        background: #0f172a;
        color: #ffffff !important;
        padding: 12px; border-radius: 8px;
        font-weight: 700; text-decoration: none; display: block;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 4. القائمة الجانبية المحدثة (The Control Center)
# ==========================================
with st.sidebar:
    st.markdown('<div class="sidebar-title">ADID AL-EID</div>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#64748b; font-size:12px; margin-top:-20px;">The Digitalization Source</p>', unsafe_allow_html=True)
    st.divider()
    
    # تصنيفات المتجر (10 صفحات)
    categories = [
        "🌐 الرئيسية",
        "🤖 عملاء الذكاء الاصطناعي",
        "⚡ أنظمة الأتمتة",
        "📚 مكتبة PDF الرقمية",
        "📖 كتب ورقية تكنولوجية",
        "🏛️ تكنولوجيا المكاتب",
        "🛡️ الأمن والسيادة",
        "🔗 عقود الشركات الكبرى",
        "⚙️ الهندسة العكسية",
        "🎓 التدريب والماستركلاس",
        "💻 تراخيص البرمجيات"
    ]
    
    # تحديث `key` لضمان إعادة رسم الراديو بالألوان الجديدة
    st.session_state["category"] = st.radio("تصفح الإمبراطورية:", categories, key="global_category")
    
    st.divider()
    st.markdown(f"### 🛒 سلة المشتريات ({len(st.session_state['cart'])})")
    if st.button("تأكيد الحجز العالمي 🚀"):
        st.balloons()
        st.success("تم إرسال الطلب لغرفة العمليات")

# ==========================================
# 5. محتوى الصفحة الرئيسية (تحديث: شعار "L")
# ==========================================
if st.session_state["category"] == "🌐 الرئيسية":
    st.markdown("""
    <div style="text-align:center; padding:20px;">
        <!-- إضافة شعار 'L' الجديد -->
        <div class="logo-l">L</div>
        <h1 style="font-size:55px; font-weight:900; color:#0f172a;">مكتب المحامي عديد العيد</h1>
        <h2 style="color:#334155;">المنبع العالمي لرقمنة القانون والمؤسسات</h2>
        <p style="font-size:20px; color:#64748b; max-width:900px; margin:auto;">نحن لا نتبع التكنولوجيا، نحن من نضع قواعدها. شراكات مع كبرى الشركات العالمية وعقود عابرة للقارات في مجال الأتمتة والسيادة الرقمية.</p>
    </div>
    """, unsafe_allow_html=True)

    # السلايدر التلقائي (لا تغيير في الصور)
    images = [
        "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600",
        "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600",
        "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600",
        "https://images.unsplash.com/photo-1600132806370-bf17e65e942f?w=600"
    ]
    
    slider_code = f"""
    <div style="overflow: hidden; width: 100%; padding: 30px 0;">
        <div class="slider-wrapper">
            <img src="{images[0]}" class="slide-item">
            <img src="{images[1]}" class="slide-item">
            <img src="{images[2]}" class="slide-item">
            <img src="{images[3]}" class="slide-item">
            <img src="{images[0]}" class="slide-item">
            <img src="{images[1]}" class="slide-item">
            <img src="{images[2]}" class="slide-item">
            <img src="{images[3]}" class="slide-item">
        </div>
    </div>
    """
    components.html(slider_code, height=550)
    
    # قسم الشركاء (تحديث لون العنوان)
    st.markdown("<h3 style='text-align:center; color:#0f172a;'>🤝 شركاء النجاح العالمي</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#64748b;'>نظامنا معتمد في أكثر من 50 شركة كبرى ومكاتب محاماة دولية</p>", unsafe_allow_html=True)

# ==========================================
# 6. نظام المتجر العالمي المحدث (Dynamic Marketplace)
# ==========================================
else:
    st.markdown(f"<h1 style='color:#0f172a;'>{st.session_state['category']}</h1>", unsafe_allow_html=True)
    
    # توليد بيانات وهمية للمنتجات (تحديث الأسعار لأرقام واقعية)
    data = {
        "🤖 عملاء الذكاء الاصطناعي": [("AI Legal Agent Pro", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=400", "5,000$")],
        "⚡ أنظمة الأتمتة": [("n8n Enterprise Node", "https://images.unsplash.com/photo-1551434678-e076c223a692?w=400", "1,200$")],
        "📚 مكتبة PDF الرقمية": [("دليل الرقمنة الشامل", "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=400", "150$")],
        "📖 كتب ورقية تكنولوجية": [("مستقبل القانون 2030", "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=400", "85$")],
        "🏛️ تكنولوجيا المكاتب": [("Sovereign Office Server", "https://images.unsplash.com/photo-1558494949-ef010cbdcc51?w=400", "3,500$")]
    }
    
    # عرض المنتجات (لا تغيير في المنطق، فقط الأسلوب البصري)
    category_items = data.get(st.session_state["category"], [("منتج عالمي جديد", "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=400", "اتصل للسعر")])
    
    cols = st.columns(3)
    for i in range(6): # عرض 6 منتجات في كل فئة
        item = category_items[0]
        with cols[i % 3]:
            st.markdown(f"""
            <div class="product-card">
                <div>
                    <div class="icon-3d-box">💎</div>
                    <img src="{item[1]}" class="product-img">
                    <h3 style="margin-top:10px; color:#0f172a;">{item[0]}</h3>
                    <p style="color:#64748b; font-size:12px;">حل رقمي معتمد من مكتب عديد العيد</p>
                </div>
                <div>
                    <div class="product-price">{item[2]}</div>
                    <!-- زر الشراء الجديد -->
                    <a href="#" class="buy-btn">أضف للسلة الآن</a>
                </div>
            </div>
            """, unsafe_allow_html=True)
            # زر streamlit الأصلي تحت البطاقة لإضافة الوظيفة
            if st.button(f"تأكيد الإضافة - {i}", key=f"btn_{st.session_state['category']}_{i}"):
                st.session_state["cart"].append(f"{item[0]} {i}")
                st.toast(f"تمت إضافة {item[0]}")

# ==========================================
# 7. التذييل العالمي المحدث (Footer)
# ==========================================
st.divider()
st.markdown("""
<div style="text-align:center; padding:40px; color:#64748b;">
    <h3 style="color:#0f172a;">مؤسسة عديد العيد العالمية للرقمنة</h3>
    <p>المقر الرئيسي للأتمتة والسيادة الرقمية | 📧 laidadid21@gmail.com | 📱 +213 671 81 63 46</p>
    <div style="font-size:10px;">Build v11.0 Global Nexus | 2024 All Rights Reserved</div>
</div>
""", unsafe_allow_html=True)
