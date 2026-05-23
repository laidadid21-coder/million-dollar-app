import streamlit as st
import streamlit.components.v1 as components
import random

# 1. إعدادات الإمبراطورية الرقمية v10.0
st.set_page_config(
    page_title="Adid Al-Eid | Global Digital Nexus",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. إدارة الحالة (الدولة، السلة، التصنيف)
if "cart" not in st.session_state: st.session_state["cart"] = []
if "category" not in st.session_state: st.session_state["category"] = "الكل"

# 3. محرك التصميم البصري (فخامة الألوان السيادية: الكحلي الملكي، الذهبي، والأسود)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;700;900&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        background: #020617 !important;
        color: #f1f5f9 !important;
        font-family: 'Cairo', sans-serif !important;
    }

    /* --- الجهة اليسرى (Sidebar) الفخمة جداً --- */
    [data-testid="stSidebar"] {
        background: rgba(15, 23, 42, 1) !important;
        border-right: 2px solid #d4af37 !important; /* لون ذهبي ملكي */
    }
    
    .sidebar-title {
        color: #d4af37; font-size: 28px; font-weight: 900; text-align: center;
        margin-bottom: 20px; text-transform: uppercase; letter-spacing: 2px;
    }

    /* تحسين وضوح أزرار القائمة الجانبية */
    .stRadio div[role="radiogroup"] label {
        background: #1e293b !important;
        border: 1px solid #334155 !important;
        padding: 12px 20px !important;
        border-radius: 12px !important;
        color: #ffffff !important;
        font-weight: 700 !important;
        font-size: 16px !important;
        margin-bottom: 8px !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
    }
    .stRadio div[role="radiogroup"] label:hover {
        border-color: #d4af37 !important;
        transform: translateX(10px);
    }

    /* --- السلايدر المتحرك التلقائي --- */
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
        border-radius: 20px; border: 3px solid #d4af37;
        object-fit: cover; filter: brightness(0.8);
    }

    /* --- بطاقات المتجر (Amazon Style Luxury) --- */
    .product-card {
        background: #0f172a;
        border: 1px solid #334155;
        border-radius: 20px;
        padding: 20px;
        text-align: center;
        transition: 0.4s;
        height: 480px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .product-card:hover {
        border-color: #d4af37;
        box-shadow: 0 0 30px rgba(212, 175, 55, 0.2);
        transform: translateY(-10px);
    }
    .product-img { width: 100%; height: 180px; border-radius: 10px; object-fit: cover; }
    .product-price { color: #d4af37; font-size: 24px; font-weight: 900; }
    
    /* أيقونات 3D للمنتجات */
    .icon-3d-box {
        font-size: 40px; margin-bottom: 10px;
        filter: drop-shadow(0 0 10px #d4af37);
    }

    /* زر الشراء الذهبي */
    .buy-btn {
        background: linear-gradient(135deg, #d4af37 0%, #b8860b 100%);
        color: #000 !important;
        padding: 10px; border-radius: 10px;
        font-weight: 900; text-decoration: none; display: block;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 4. القائمة الجانبية (The Control Center)
# ==========================================
with st.sidebar:
    st.markdown('<div class="sidebar-title">ADID AL-EID</div>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#94a3b8; font-size:12px; margin-top:-20px;">The Digitalization Source</p>', unsafe_allow_html=True)
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
    
    st.session_state["category"] = st.radio("تصفح الإمبراطورية:", categories)
    
    st.divider()
    st.markdown(f"### 🛒 سلة المشتريات ({len(st.session_state['cart'])})")
    if st.button("تأكيد الحجز العالمي 🚀"):
        st.balloons()
        st.success("تم إرسال الطلب لغرفة العمليات")

# ==========================================
# 5. محتوى الصفحة الرئيسية
# ==========================================
if st.session_state["category"] == "🌐 الرئيسية":
    st.markdown("""
    <div style="text-align:center; padding:20px;">
        <h1 style="font-size:55px; font-weight:900; color:#d4af37;">مكتب المحامي عديد العيد</h1>
        <h2 style="color:#ffffff;">المنبع العالمي لرقمنة القانون والمؤسسات</h2>
        <p style="font-size:20px; color:#94a3b8; max-width:900px; margin:auto;">نحن لا نتبع التكنولوجيا، نحن من نضع قواعدها. شراكات مع كبرى الشركات العالمية وعقود عابرة للقارات في مجال الأتمتة والسيادة الرقمية.</p>
    </div>
    """, unsafe_allow_html=True)

    # السلايدر التلقائي الفخم
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
    
    # قسم الشركاء
    st.markdown("<h3 style='text-align:center; color:#d4af37;'>🤝 شركاء النجاح العالمي</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#64748b;'>نظامنا معتمد في أكثر من 50 شركة كبرى ومكاتب محاماة دولية</p>", unsafe_allow_html=True)

# ==========================================
# 6. نظام المتجر العالمي (Dynamic Marketplace)
# ==========================================
else:
    st.markdown(f"<h1 style='color:#d4af37;'>{st.session_state['category']}</h1>", unsafe_allow_html=True)
    
    # توليد بيانات وهمية للمنتجات بناءً على الفئة المختارة (لمحاكاة 10 صفحات)
    data = {
        "🤖 عملاء الذكاء الاصطناعي": [("AI Legal Agent Pro", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=400", "5,000$")],
        "⚡ أنظمة الأتمتة": [("n8n Enterprise Node", "https://images.unsplash.com/photo-1551434678-e076c223a692?w=400", "1,200$")],
        "📚 مكتبة PDF الرقمية": [("دليل الرقمنة الشامل", "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=400", "150$")],
        "📖 كتب ورقية تكنولوجية": [("مستقبل القانون 2030", "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=400", "85$")],
        "🏛️ تكنولوجيا المكاتب": [("Sovereign Office Server", "https://images.unsplash.com/photo-1558494949-ef010cbdcc51?w=400", "3,500$")]
    }
    
    # عرض المنتجات
    category_items = data.get(st.session_state["category"], [("منتج عالمي جديد", "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=400", "اتصل للسعر")])
    
    # تكرار المنتجات لمحاكاة ضخامة المتجر
    cols = st.columns(3)
    for i in range(6): # عرض 6 منتجات في كل فئة
        item = category_items[0]
        with cols[i % 3]:
            st.markdown(f"""
            <div class="product-card">
                <div>
                    <div class="icon-3d-box">💎</div>
                    <img src="{item[1]}" class="product-img">
                    <h3 style="margin-top:10px;">{item[0]}</h3>
                    <p style="color:#94a3b8; font-size:12px;">حل رقمي معتمد من مكتب عديد العيد</p>
                </div>
                <div>
                    <div class="product-price">{item[2]}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"أضف للسلة - {i}", key=f"btn_{st.session_state['category']}_{i}"):
                st.session_state["cart"].append(f"{item[0]} {i}")
                st.toast(f"تمت إضافة {item[0]}")

# ==========================================
# 7. التذييل العالمي (Footer)
# ==========================================
st.divider()
st.markdown("""
<div style="text-align:center; padding:40px; color:#64748b;">
    <h3 style="color:#d4af37;">مؤسسة عديد العيد العالمية للرقمنة</h3>
    <p>المقر الرئيسي للأتمتة والسيادة الرقمية | 📧 laidadid21@gmail.com | 📱 +213 671 81 63 46</p>
    <div style="font-size:10px;">Build v10.0 Global Nexus | 2024 All Rights Reserved</div>
</div>
""", unsafe_allow_html=True)
