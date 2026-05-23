import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np

# 1. إعدادات النظام السيادي v7.0
st.set_page_config(
    page_title="Adid Al-Eid Sovereign OS v7.0",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. إدارة الحالة
if "cart" not in st.session_state: st.session_state["cart"] = []
if "page" not in st.session_state: st.session_state["page"] = "🏠 الرئيسية"

# 3. محرك التصميم البصري (إصدار الفخامة المطلقة)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at center, #0f172a 0%, #020617 100%) !important;
        color: #f8fafc !important;
        font-family: 'Cairo', sans-serif !important;
    }

    /* --- تحسين القائمة الجانبية لجعل الكتابة واضحة جداً --- */
    [data-testid="stSidebar"] {
        background: #020617 !important;
        border-right: 2px solid #fbbf24 !important;
    }
    
    .stRadio div[role="radiogroup"] label {
        background: rgba(30, 41, 59, 1) !important; /* خلفية داكنة تماماً للوضوح */
        border: 1px solid #334155 !important;
        padding: 15px 25px !important;
        border-radius: 15px !important;
        margin-bottom: 12px !important;
        color: #ffffff !important; /* نص أبيض ناصع */
        font-size: 18px !important;
        font-weight: 700 !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    }
    
    .stRadio div[role="radiogroup"] label:hover {
        border-color: #fbbf24 !important;
        transform: scale(1.02);
    }

    /* --- كود تحريك الصور تلقائياً (Carousel Animation) --- */
    @keyframes scroll {
        0% { transform: translateX(0); }
        100% { transform: translateX(calc(-350px * 4)); }
    }
    .slider {
        display: flex;
        width: calc(350px * 8);
        animation: scroll 20s linear infinite;
    }
    .slider:hover { animation-play-state: paused; }
    .slide-img {
        width: 330px; height: 400px;
        margin: 10px; border-radius: 20px;
        object-fit: cover; border: 3px solid #fbbf24;
        box-shadow: 0 10px 20px rgba(0,0,0,0.5);
    }

    /* --- أيقونات 3D متطورة للمنتجات --- */
    .icon-box-3d {
        width: 80px; height: 80px;
        margin: 0 auto 20px;
        background: linear-gradient(135deg, #3b82f6, #1e3a8a);
        border-radius: 20px;
        display: flex; align-items: center; justify-content: center;
        font-size: 40px;
        box-shadow: 10px 10px 20px rgba(0,0,0,0.4), -5px -5px 15px rgba(255,255,255,0.05);
        transform: perspective(500px) rotateX(10deg) rotateY(-10px);
    }

    .amazon-card {
        background: rgba(30, 41, 59, 0.8);
        border: 1px solid #475569;
        border-radius: 25px; padding: 30px;
        text-align: center; transition: 0.5s;
    }
    .amazon-card:hover {
        border-color: #fbbf24; box-shadow: 0 0 40px rgba(251, 191, 36, 0.3);
        transform: translateY(-15px);
    }

    .price-tag { color: #fbbf24; font-size: 30px; font-weight: 900; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 4. القائمة الجانبية المتطورة (Sidebar UI)
# ==========================================
with st.sidebar:
    st.markdown('<h1 style="color:#fbbf24; text-align:center;">LFD EMPIRE</h1>', unsafe_allow_html=True)
    st.divider()
    
    # قائمة بوضوح كتابة عالي
    menu = {
        "🏠 الرئيسية": "🏠",
        "🛍️ المتجر العالمي": "🎁",
        "📍 خريطة GPS": "🌍",
        "🛡️ حصن الأمان": "🔒",
        "📖 فلسفة النظام": "🔮",
        "⚙️ مركز التحكم": "🛰️"
    }
    
    choice = st.radio("قائمة التحكم السيادي:", list(menu.keys()), label_visibility="collapsed")
    st.session_state["page"] = choice

    st.divider()
    st.markdown(f"### 🛒 السلة الملكية ({len(st.session_state['cart'])})")
    if st.button("🚀 تفعيل التعاقد الفوري"):
        st.balloons()

# ==========================================
# 1. الصفحة الرئيسية (الصور المتحركة تلقائياً)
# ==========================================
if st.session_state["page"] == "🏠 الرئيسية":
    st.markdown("""
    <div style="text-align:center; padding:20px;">
        <h1 style="font-size:65px; font-weight:900; background: linear-gradient(to right, #fbbf24, #ffffff); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            Empire of Adid Al-Eid
        </h1>
        <p style="font-size:25px; color:#94a3b8;">القمة العالمية في السيادة والذكاء الاصطناعي</p>
    </div>
    """, unsafe_allow_html=True)

    # كاروسيل الصور المتحرك تلقائياً
    images = [
        "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=500",
        "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=500",
        "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=500",
        "https://images.unsplash.com/photo-1600132806370-bf17e65e942f?w=500"
    ]
    
    carousel_html = f"""
    <div style="overflow: hidden; width: 100%; background: transparent; padding: 20px 0;">
        <div class="slider">
            <img src="{images[0]}" class="slide-img">
            <img src="{images[1]}" class="slide-img">
            <img src="{images[2]}" class="slide-img">
            <img src="{images[3]}" class="slide-img">
            <img src="{images[0]}" class="slide-img">
            <img src="{images[1]}" class="slide-img">
            <img src="{images[2]}" class="slide-img">
            <img src="{images[3]}" class="slide-img">
        </div>
    </div>
    """
    components.html(carousel_html, height=450)
    
    st.divider()
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### 🎥 الأتمتة الإستراتيجية")
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    with c2:
        st.markdown(f"""
        <div class="amazon-card" style="height:auto; border-bottom: 5px solid #25D366;">
            <h2>تواصل فوري مع المؤسس 💬</h2>
            <p>للمشاريع الضخمة والتحول السيادي الكامل</p>
            <a href="https://wa.me/213671816346" style="background:#25D366; color:white; padding:20px; border-radius:15px; text-decoration:none; font-weight:bold; display:block; font-size:20px;">
                فتح قناة WhatsApp
            </a>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# 2. المتجر العالمي (الأيقونات 3D الجديدة)
# ==========================================
elif st.session_state["page"] == "🛍️ المتجر العالمي":
    st.markdown("<h1 style='text-align:center;'>🛍️ متجر الإمبراطورية العالمي</h1>", unsafe_allow_html=True)
    
    products = [
        {"n": "Sovereign AI Node", "p": "$15,000", "i": "🧠", "img": "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=400"},
        {"n": "Smart Legal Bot", "p": "$3,200", "i": "📜", "img": "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=400"},
        {"n": "Industrial Security Node", "p": "$5,800", "i": "⚙️", "img": "https://images.unsplash.com/photo-1563986768609-322da13575f3?w=400"},
    ]
    
    cols = st.columns(3)
    for idx, p in enumerate(products):
        with cols[idx]:
            st.markdown(f"""
            <div class="amazon-card">
                <div class="icon-box-3d">{p['i']}</div>
                <h3>{p['n']}</h3>
                <div class="price-tag">{p['p']}</div>
                <img src="{p['img']}" style="width:100%; border-radius:15px; margin-top:15px;">
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"إضافة للسلطة الرقمية {idx}", key=f"shop_{idx}"):
                st.session_state["cart"].append(p['n'])
                st.toast("تمت الإضافة بنجاح")

# ==========================================
# 3. باقي الصفحات (GPS، أمان، تحكم)
# ==========================================
elif st.session_state["page"] == "📍 خريطة GPS":
    st.markdown("## 📍 المواقع الإستراتيجية للعقد")
    df = pd.DataFrame({'lat': [36.7, 25.2, 48.8, 40.7], 'lon': [3.0, 55.2, 2.3, -74.0]})
    st.map(df)

elif st.session_state["page"] == "🛡️ حصن الأمان":
    st.markdown("## 🛡️ ميثاق الأمن المطلق")
    st.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=800")
    st.success("تشفير مفاتيح السيادة: AES-512 ACTIVE")

elif st.session_state["page"] == "⚙️ مركز التحكم":
    if st.text_input("أدخل شفرة الدخول:", type="password") == "0000":
        st.metric("قوة النظام", "100%", "Optimal")
        st.area_chart(np.random.randn(20, 2))

# 7. التذييل (Footer)
st.divider()
st.markdown("<div style='text-align:center; color:#64748b;'>Adid Al-Eid Global Sovereign OS v7.0 | 2024</div>", unsafe_allow_html=True)
