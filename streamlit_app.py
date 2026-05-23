import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np

# 1. إعدادات الإمبراطورية الرقمية (Sovereign OS v6.5)
st.set_page_config(
    page_title="Adid Al-Eid Global Sovereign OS v6.5",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. إدارة حالة النظام
if "cart" not in st.session_state: st.session_state["cart"] = []
if "page" not in st.session_state: st.session_state["page"] = "🏠 الرئيسية"

# 3. محرك التصميم البصري الخارق (CSS شامل للرئيسية والجهة اليسرى)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;700;900&display=swap');
    
    /* خلفية الموقع العامة */
    html, body, [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at center, #0f172a 0%, #020617 100%) !important;
        color: #e2e8f0 !important;
        font-family: 'Cairo', sans-serif !important;
    }

    /* --- تطوير الجهة اليسرى (Sidebar) --- */
    [data-testid="stSidebar"] {
        background: rgba(15, 23, 42, 0.95) !important;
        backdrop-filter: blur(15px);
        border-right: 1px solid rgba(251, 191, 36, 0.3) !important;
        box-shadow: 10px 0 30px rgba(0,0,0,0.5);
    }
    
    /* تصميم شعار الجهة اليسرى */
    .sidebar-logo {
        background: linear-gradient(135deg, #fbbf24, #d97706);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 32px; font-weight: 900; text-align: center;
        margin-bottom: 20px; filter: drop-shadow(0 0 10px rgba(251,191,36,0.5));
    }

    /* أيقونات 3D جانبية */
    .nav-icon {
        font-size: 24px; margin-left: 10px;
        display: inline-block;
        transition: transform 0.3s ease;
    }
    
    /* تخصيص أزرار التنقل في القائمة */
    .stRadio [data-testid="stWidgetLabel"] { display: none; } /* إخفاء العنوان الافتراضي */
    
    .stRadio div[role="radiogroup"] label {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 12px 20px !important;
        border-radius: 12px !important;
        margin-bottom: 10px !important;
        transition: 0.3s !important;
        color: #94a3b8 !important;
    }
    
    .stRadio div[role="radiogroup"] label:hover {
        background: rgba(59, 130, 246, 0.2) !important;
        border-color: #3b82f6 !important;
        transform: translateX(5px);
    }
    
    .stRadio div[role="radiogroup"] label[data-checked="true"] {
        background: linear-gradient(90deg, rgba(59, 130, 246, 0.3), transparent) !important;
        border-right: 4px solid #fbbf24 !important;
        color: #fff !important;
    }

    /* سلة المشتريات الجانبية */
    .sidebar-cart-box {
        background: rgba(16, 185, 129, 0.1);
        border: 1px dashed #10b981;
        border-radius: 10px;
        padding: 15px;
        margin-top: 20px;
    }

    /* --- تصميم الصفحة الرئيسية (Amazon Style) --- */
    .amazon-card {
        background: rgba(30, 41, 59, 0.7);
        border-radius: 15px; border: 1px solid #334155;
        padding: 20px; transition: 0.4s; text-align: center; height: 100%;
    }
    .amazon-card:hover {
        border-color: #fbbf24; box-shadow: 0 0 30px rgba(251, 191, 36, 0.2);
        transform: translateY(-10px);
    }
    .price-tag { color: #10b981; font-size: 26px; font-weight: 900; margin: 10px 0; }
    
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 4. بناء الجهة اليسرى المتطورة (Advanced Sidebar)
# ==========================================
with st.sidebar:
    st.markdown('<div class="sidebar-logo">LFD EMPIRE</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align:center; font-size:10px; color:#64748b; margin-top:-15px;">GLOBAL SOVEREIGN OS v6.5</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # اختيار اللغة بتصميم ذهبي
    lang = st.selectbox("🌐 Select Language", ["العربية", "English"], label_visibility="collapsed")
    
    st.markdown("<p style='color:#fbbf24; font-size:12px; font-weight:bold; margin-top:20px;'>🖥️ لوحة التحكم الرئيسية</p>", unsafe_allow_html=True)
    
    # القائمة مع الأيقونات ثلاثية الأبعاد
    menu_options = {
        "🏠 الرئيسية": "🏠",
        "🛍️ المتجر العالمي": "🎁",
        "📍 خريطة GPS": "🌍",
        "🛡️ حصن الأمان": "🔒",
        "📖 فلسفة النظام": "🔮",
        "⚙️ مركز التحكم": "🛰️"
    }
    
    # الراديو الفاخر
    choice = st.radio(
        "Navigation",
        list(menu_options.keys()),
        index=0,
        key="navigation_radio"
    )
    st.session_state["page"] = choice

    # سلة المشتريات الفاخرة في الجانب
    st.markdown('<div class="sidebar-cart-box">', unsafe_allow_html=True)
    st.markdown(f"<p style='margin:0; color:#10b981; font-weight:bold;'>🛒 السلة الذكية ({len(st.session_state['cart'])})</p>", unsafe_allow_html=True)
    if st.session_state["cart"]:
        for item in st.session_state["cart"][-3:]: # إظهار آخر 3 منتجات
            st.markdown(f"<p style='font-size:10px; color:#94a3b8; margin:0;'>• {item}</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("🚀 إتمام الطلب الآن"):
        st.balloons()
    
    st.divider()
    st.markdown("<p style='text-align:center; font-size:10px; color:#475569;'>Sovereign Nodes: Active ✅</p>", unsafe_allow_html=True)

# ==========================================
# 5. محتوى الصفحة الرئيسية (Amazon/Alibaba Style)
# ==========================================
if st.session_state["page"] == "🏠 الرئيسية":
    st.markdown("""
    <div style="text-align:center; padding:40px;">
        <h1 style="font-size:60px; font-weight:900; background: linear-gradient(to right, #fbbf24, #3b82f6); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            Empire of Adid Al-Eid
        </h1>
        <p style="font-size:22px; color:#94a3b8;">المنصة الأقوى في العالم للسيادة الرقمية والأتمتة القانونية</p>
    </div>
    """, unsafe_allow_html=True)

    # الكاروسيل (الصور القديمة المفضلة لديك)
    carousel_html = """
    <div style="display: flex; gap: 15px; overflow-x: auto; padding: 20px; scrollbar-width: none;">
        <div style="min-width:350px;"><img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=500" style="border-radius:20px; border: 2px solid #3b82f6; width:100%;"></div>
        <div style="min-width:350px;"><img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=500" style="border-radius:20px; border: 2px solid #fbbf24; width:100%;"></div>
        <div style="min-width:350px;"><img src="https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=500" style="border-radius:20px; border: 2px solid #3b82f6; width:100%;"></div>
        <div style="min-width:350px;"><img src="https://images.unsplash.com/photo-1600132806370-bf17e65e942f?w=500" style="border-radius:20px; border: 2px solid #fbbf24; width:100%;"></div>
    </div>
    """
    components.html(carousel_html, height=350)
    
    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🎥 استعراض البنية التحتية")
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    with col2:
        st.markdown("### 📞 الاتصال الإستراتيجي")
        st.markdown("""
        <div class="amazon-card" style="height:auto; border-left: 5px solid #25D366;">
            <p>اتصل مباشرة بغرفة عمليات الأتمتة والسيادة.</p>
            <a href="https://wa.me/213671816346" style="background:#25D366; color:white; padding:15px; border-radius:12px; text-decoration:none; font-weight:bold; display:block; text-align:center; font-size:18px;">
                WhatsApp Direct Link 💬
            </a>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# 6. باقي الصفحات (المتجر، الخريطة، إلخ) - كما هي
# ==========================================
elif st.session_state["page"] == "🛍️ المتجر العالمي":
    st.markdown("## 🛒 متجر الأنظمة الإمبراطوري")
    products = [
        {"n": "Sovereign AI Node 1000", "p": "$12,000", "i": "🧠", "img": "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=400"},
        {"n": "Smart Legal Auditor", "p": "$2,500", "i": "📜", "img": "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=400"},
        {"n": "Military VPN Node", "p": "$1,100", "i": "🛡️", "img": "https://images.unsplash.com/photo-1558494949-ef010cbdcc51?w=400"},
    ]
    cols = st.columns(3)
    for idx, p in enumerate(products):
        with cols[idx]:
            st.markdown(f'<div class="amazon-card"><img src="{p["img"]}" style="width:100%; border-radius:10px; height:180px; object-fit:cover;"><h3>{p["i"]} {p["n"]}</h3><div class="price-tag">{p["p"]}</div></div>', unsafe_allow_html=True)
            if st.button(f"أضف {p['n']}", key=f"shop_{idx}"):
                st.session_state["cart"].append(p['n'])
                st.toast(f"تمت إضافة {p['n']}")

elif st.session_state["page"] == "📍 خريطة GPS":
    st.markdown("## 📍 التوزيع العالمي للعقد السيادية")
    df = pd.DataFrame({'city': ['Algeria', 'Dubai', 'Paris', 'New York'], 'lat': [36.7, 25.2, 48.8, 40.7], 'lon': [3.0, 55.2, 2.3, -74.0]})
    st.map(df)

elif st.session_state["page"] == "🛡️ حصن الأمان":
    st.markdown("## 🛡️ بروتوكولات الحماية")
    st.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=800")
    st.success("جميع الأنظمة تعمل بتشفير AES-512")

elif st.session_state["page"] == "⚙️ مركز التحكم":
    st.markdown("## ⚙️ وحدة الإدارة المركزية")
    if st.text_input("Password", type="password") == "0000":
        st.metric("النظام", "Online", "Secure")
        st.area_chart(np.random.randn(20, 3))

# 7. التذييل الفاخر
st.divider()
st.markdown("<div style='text-align:center; color:#475569;'>Adid Al-Eid Global Sovereign OS | 📧 laidadid21@gmail.com | 📱 +213 671 81 63 46</div>", unsafe_allow_html=True)
