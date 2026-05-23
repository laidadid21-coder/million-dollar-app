import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np

# 1. إعدادات الإمبراطورية العائمة (The Floating Palace)
st.set_page_config(
    page_title="Adid Al-Eid | The Sovereign Ocean v8.0",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. إدارة حالة النظام
if "cart" not in st.session_state: st.session_state["cart"] = []
if "page" not in st.session_state: st.session_state["page"] = "🏠 القصر الرئيسي"

# 3. محرك التصميم الخارق (CSS: Ocean & Gold Luxury)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;700;900&display=swap');
    
    /* خلفية المحيط المتحركة */
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(180deg, #001219 0%, #003049 50%, #005f73 100%) !important;
        color: #e9d8a6 !important;
        font-family: 'Cairo', sans-serif !important;
    }

    /* تأثير الطفو لجميع العناصر */
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-15px); }
        100% { transform: translateY(0px); }
    }

    /* --- الجهة اليسرى: لوحة تحكم القصر (Sidebar) --- */
    [data-testid="stSidebar"] {
        background: rgba(0, 18, 25, 0.9) !important;
        backdrop-filter: blur(20px);
        border-right: 2px solid #ee9b00 !important;
    }

    .stRadio div[role="radiogroup"] label {
        background: rgba(10, 147, 150, 0.2) !important;
        border: 1px solid #ee9b00 !important;
        padding: 15px 25px !important;
        border-radius: 50px !important; /* شكل بيضاوي فخم */
        margin-bottom: 15px !important;
        color: #ffffff !important;
        font-size: 18px !important;
        font-weight: 700 !important;
        transition: 0.4s;
        text-align: center;
        display: block;
    }
    
    .stRadio div[role="radiogroup"] label:hover {
        background: #ee9b00 !important;
        color: #001219 !important;
        transform: scale(1.05) translateX(10px);
    }

    /* --- السلايدر المتحرك (الصور القديمة مع تأثيرات حديثة) --- */
    .slider-container {
        display: flex;
        gap: 20px;
        animation: slide 25s linear infinite;
        width: calc(400px * 8);
    }
    @keyframes slide {
        0% { transform: translateX(0); }
        100% { transform: translateX(calc(-400px * 4)); }
    }
    .ocean-slide {
        width: 380px; height: 500px;
        border-radius: 30px;
        border: 4px solid #ee9b00;
        object-fit: cover;
        box-shadow: 0 20px 40px rgba(0,0,0,0.6);
        filter: brightness(0.9);
    }

    /* --- بطاقات المتجر (Amazon Luxury Card) --- */
    .luxury-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(238, 155, 0, 0.3);
        border-radius: 25px;
        padding: 25px;
        text-align: center;
        transition: 0.5s;
        animation: float 4s ease-in-out infinite;
    }
    .luxury-card:hover {
        background: rgba(238, 155, 0, 0.1);
        border-color: #ee9b00;
        transform: scale(1.05);
    }

    .gold-text {
        background: linear-gradient(90deg, #ee9b00, #e9d8a6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
    }

    .buy-button {
        background: #ee9b00;
        color: #001219 !important;
        padding: 12px 25px;
        border-radius: 15px;
        font-weight: bold;
        text-decoration: none;
        display: inline-block;
        margin-top: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 4. لوحة التحكم الجانبية (The Bridge)
# ==========================================
with st.sidebar:
    st.markdown('<h1 style="color:#ee9b00; text-align:center; font-size:35px;">LFD OCEAN</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#94d2bd;">SOVEREIGN CONTROL v8.0</p>', unsafe_allow_html=True)
    st.divider()
    
    pages = {
        "🏠 القصر الرئيسي": "🏠",
        "🛍️ متجر السيادة": "💎",
        "📍 رادار الـ GPS": "📡",
        "🛡️ حصن البيانات": "🔒",
        "📖 الفلسفة الملكية": "🔱",
        "⚙️ غرفة المحركات": "⚙️"
    }
    
    st.session_state["page"] = st.radio("بوصلة النظام:", list(pages.keys()), label_visibility="collapsed")
    
    st.divider()
    st.markdown(f"### 🛒 السلة الملكية ({len(st.session_state['cart'])})")
    if st.button("🚀 تفعيل البروتوكول"):
        st.balloons()
        st.success("تم تأكيد الطلب بنجاح")

# ==========================================
# 1. الصفحة الرئيسية (The Grand Hall)
# ==========================================
if st.session_state["page"] == "🏠 القصر الرئيسي":
    st.markdown("""
    <div style="text-align:center; padding:30px;">
        <h1 class="gold-text" style="font-size:70px;">مكتب عديد العيد للسيادة الرقمية</h1>
        <p style="font-size:25px; color:#94d2bd;">نظام تشغيل المؤسسات العائم فوق سحابة الأمان المطلق</p>
    </div>
    """, unsafe_allow_html=True)

    # السلايدر المتحرك التلقائي (الصور التي طلبتها)
    images = [
        "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600",
        "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600",
        "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600",
        "https://images.unsplash.com/photo-1600132806370-bf17e65e942f?w=600"
    ]
    
    carousel_code = f"""
    <div style="overflow: hidden; width: 100%; padding: 40px 0;">
        <div class="slider-container">
            <img src="{images[0]}" class="ocean-slide">
            <img src="{images[1]}" class="ocean-slide">
            <img src="{images[2]}" class="ocean-slide">
            <img src="{images[3]}" class="ocean-slide">
            <img src="{images[0]}" class="ocean-slide">
            <img src="{images[1]}" class="ocean-slide">
            <img src="{images[2]}" class="ocean-slide">
            <img src="{images[3]}" class="ocean-slide">
        </div>
    </div>
    """
    components.html(carousel_code, height=600)
    
    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h3 class='gold-text'>🔱 استراتيجية الطفو الرقمي</h3>", unsafe_allow_html=True)
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    with col2:
        st.markdown(f"""
        <div class="luxury-card" style="height:auto; border-top: 5px solid #ee9b00;">
            <h2 class="gold-text">تواصل مباشر مع الإدارة 📞</h2>
            <p style="color:#94d2bd;">نحن نبني مستقبلك الرقمي بعيداً عن أعين المتطفلين.</p>
            <a href="https://wa.me/213671816346" class="buy-button" style="width:100%; font-size:20px;">
                WhatsApp Instant Bridge 💬
            </a>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# 2. متجر السيادة (The Sovereign Market)
# ==========================================
elif st.session_state["page"] == "🛍️ متجر السيادة":
    st.markdown("<h1 class='gold-text' style='text-align:center;'>🛍️ متجر الإمبراطورية العائمة</h1>", unsafe_allow_html=True)
    
    products = [
        {"n": "Oceanic AI Node", "p": "$18,000", "i": "🔱", "img": "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=400"},
        {"n": "Sovereign Legal Bot", "p": "$4,500", "i": "📜", "img": "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=400"},
        {"n": "Military Deep Security", "p": "$7,200", "i": "🔒", "img": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=400"},
    ]
    
    cols = st.columns(3)
    for idx, p in enumerate(products):
        with cols[idx]:
            st.markdown(f"""
            <div class="luxury-card">
                <div style="font-size:50px; margin-bottom:10px;">{p['i']}</div>
                <h3 class="gold-text">{p['n']}</h3>
                <h2 style="color:#10b981;">{p['p']}</h2>
                <img src="{p['img']}" style="width:100%; border-radius:15px; margin:15px 0;">
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"أضف إلى الأسطول {idx}", key=f"buy_{idx}"):
                st.session_state["cart"].append(p['n'])
                st.toast(f"تمت إضافة {p['n']}")

# ==========================================
# 3. رادار الـ GPS (The Radar)
# ==========================================
elif st.session_state["page"] == "📍 رادار الـ GPS":
    st.markdown("<h1 class='gold-text'>📡 رادار العقد السيادية</h1>", unsafe_allow_html=True)
    df = pd.DataFrame({
        'lat': [36.7, 25.2, 48.8, 40.7, 1.3],
        'lon': [3.0, 55.2, 2.3, -74.0, 103.8]
    })
    st.map(df)
    st.info("مواقع محطاتنا السيادية الموزعة في المحيطات الرقمية العالمية.")

# ==========================================
# 4. باقي الصفحات (Security & Admin)
# ==========================================
elif st.session_state["page"] == "🛡️ حصن البيانات":
    st.markdown("<h1 class='gold-text'>🔒 الحماية تحت الصفر</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class="luxury-card">
        <h3>تشفيرنا أعمق من المحيط</h3>
        <p>نستخدم بروتوكولات Air-Gapped AI التي تعزل بياناتك تماماً عن شبكة الإنترنت العامة.</p>
    </div>
    """, unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1563986768609-322da13575f3?w=800")

elif st.session_state["page"] == "⚙️ غرفة المحركات":
    st.markdown("<h1 class='gold-text'>⚙️ مركز التحكم الفني</h1>", unsafe_allow_html=True)
    if st.text_input("أدخل شفرة القبطان:", type="password") == "0000":
        st.success("مرحباً أيها القبطان عديد العيد.")
        st.metric("قوة المحرك الرقمي", "100%", "Full Power")
        st.line_chart(np.random.randn(30, 3))

# 7. التذييل (Footer)
st.divider()
st.markdown("<div style='text-align:center; color:#ee9b00; padding:20px;'>Adid Al-Eid Sovereign Ocean OS v8.0 | Built for the Elite | 2024</div>", unsafe_allow_html=True)
