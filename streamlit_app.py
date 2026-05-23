import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from streamlit_folium import folium_static
import folium

# 1. إعدادات الإمبراطورية الرقمية
st.set_page_config(
    page_title="Adid Al-Eid Global Sovereign OS v6.0",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. نظام إدارة الحالة (السلة، البحث، اللغة، الصفحات)
if "cart" not in st.session_state: st.session_state["cart"] = []
if "lang" not in st.session_state: st.session_state["lang"] = "العربية"
if "page" not in st.session_state: st.session_state["page"] = "الرئيسية"

# 3. محرك التصميم البصري (Amazon Luxury Style)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;700;900&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at center, #0f172a 0%, #020617 100%) !important;
        color: #e2e8f0 !important;
        font-family: 'Cairo', sans-serif !important;
    }

    /* شريط التنقل العلوي - Amazon Style */
    .nav-bar {
        background: rgba(15, 23, 42, 0.9);
        padding: 10px 20px;
        border-bottom: 2px solid #3b82f6;
        display: flex;
        justify-content: space-between;
        align-items: center;
        position: sticky;
        top: 0; z-index: 999;
    }

    /* بطاقات المنتجات الضخمة */
    .amazon-card {
        background: #1e293b;
        border-radius: 15px;
        border: 1px solid #334155;
        padding: 15px;
        transition: 0.3s;
        height: 100%;
    }
    .amazon-card:hover {
        border-color: #fbbf24;
        box-shadow: 0 0 20px rgba(251, 191, 36, 0.2);
        transform: translateY(-5px);
    }

    .price-tag { color: #f59e0b; font-size: 24px; font-weight: 900; }
    
    .badge-sovereign {
        background: linear-gradient(90deg, #3b82f6, #10b981);
        color: white; padding: 2px 10px; border-radius: 5px; font-size: 10px;
    }

    /* زر الشراء الضخم */
    .buy-btn-main {
        background: #febd69;
        color: #131921 !important;
        font-weight: 700;
        text-align: center;
        padding: 10px;
        border-radius: 8px;
        text-decoration: none;
        display: block;
        margin-top: 10px;
    }
    
    /* 3D Icons */
    .icon-3d-large { font-size: 50px; filter: drop-shadow(0 0 10px #3b82f6); }
    </style>
""", unsafe_allow_html=True)

# 4. القائمة الجانبية المتقدمة
with st.sidebar:
    st.markdown('<div style="text-align:center;"><h1 style="color:#fbbf24;">LFD GLOBAL</h1></div>', unsafe_allow_html=True)
    st.session_state["lang"] = st.selectbox("🌐 لغة النظام", ["العربية", "English"])
    st.divider()
    
    # التنقل بين الـ 6 صفحات
    pages = {
        "الرئيسية": "🏠 الرئيسية",
        "المتجر": "🛍️ متجر السيادة العالمي",
        "GPS": "📍 خريطة العقد (GPS)",
        "الأمان": "🛡️ حصن البيانات",
        "الشركات": "🏢 حلول المؤسسات",
        "التحكم": "⚙️ مركز الإدارة"
    }
    
    for key, val in pages.items():
        if st.button(val, use_container_width=True):
            st.session_state["page"] = key

    st.divider()
    st.markdown(f"### 🛒 السلة ({len(st.session_state['cart'])})")
    for item in st.session_state["cart"]:
        st.caption(f"✅ {item}")
    if st.button("إتمام الدفع الآمن"): st.balloons()

# ==========================================
# الصفحة 1: الرئيسية (Mega Hub)
# ==========================================
if st.session_state["page"] == "الرئيسية":
    st.markdown("""
    <div style="text-align:center; padding:50px;">
        <h1 style="font-size:60px; font-weight:900; color:white;">إمبراطورية عديد العيد الرقمية</h1>
        <p style="font-size:24px; color:#94a3b8;">المنصة الأولى عالمياً في دمج القانون والسيادة والذكاء الاصطناعي</p>
    </div>
    """, unsafe_allow_html=True)
    
    # الكاروسيل القديم (لا يحذف!)
    carousel_html = """
    <div style="display: flex; gap: 10px; overflow-x: auto; padding: 20px;">
        <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=400" style="border-radius:15px; width:300px;">
        <img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=400" style="border-radius:15px; width:300px;">
        <img src="https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=400" style="border-radius:15px; width:300px;">
        <img src="https://images.unsplash.com/photo-1600132806370-bf17e65e942f?w=400" style="border-radius:15px; width:300px;">
    </div>
    """
    components.html(carousel_html, height=300)

# ==========================================
# الصفحة 2: المتجر العالمي (Amazon Style)
# ==========================================
elif st.session_state["page"] == "المتجر":
    st.markdown("# 🛍️ متجر السيادة العالمي")
    search = st.text_input("🔍 ابحث عن نظام، عقد، أو حل رقمي...", placeholder="مثلاً: أتمتة عقود")
    
    # تصنيفات علي بابا
    st.tabs(["كل المنتجات", "الذكاء الاصطناعي", "الأتمتة", "الأمن السيبراني", "الاستشارات"])
    
    products = [
        {"n": "Sovereign AI Node v1", "p": "9,999", "img": "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=200"},
        {"n": "Legal Automation Suite", "p": "2,450", "img": "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=200"},
        {"n": "Military Grade Encryption", "p": "1,200", "img": "https://images.unsplash.com/photo-1558494949-ef010cbdcc51?w=200"},
        {"n": "n8n Local Server", "p": "850", "img": "https://images.unsplash.com/photo-1551434678-e076c223a692?w=200"},
        {"n": "Reverse Engineering Audit", "p": "5,000", "img": "https://images.unsplash.com/photo-1563986768609-322da13575f3?w=200"},
        {"n": "SME Digital Fortress", "p": "3,100", "img": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=200"},
    ]
    
    cols = st.columns(3)
    for i, p in enumerate(products):
        with cols[i%3]:
            st.markdown(f"""
            <div class="amazon-card">
                <img src="{p['img']}" style="width:100%; border-radius:10px; height:150px; object-fit:cover;">
                <h4 style="margin-top:10px;">{p['n']}</h4>
                <span class="badge-sovereign">SOVEREIGN CERTIFIED</span>
                <div class="price-tag">${p['p']}</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"إضافة للسلة {p['n']}", key=f"btn_{i}"):
                st.session_state["cart"].append(p['n'])
                st.toast(f"تمت إضافة {p['n']}!")

# ==========================================
# الصفحة 3: GPS (خريطة العقد العالمية)
# ==========================================
elif st.session_state["page"] == "GPS":
    st.markdown("# 📍 خريطة السيادة الرقمية (GPS)")
    st.write("تتبع مواقع الخوادم السيادية والعقد المشفرة التي تديرها المؤسسة حول العالم.")
    
    # إنشاء الخريطة
    m = folium.Map(location=[28.0339, 1.6596], zoom_start=3, tiles="CartoDB dark_matter")
    
    # إضافة نقاط افتراضية (عقد النظام)
    locations = [
        {"loc": [36.7538, 3.0588], "name": "مركز الجزائر الرئيسي"},
        {"loc": [25.2048, 55.2708], "name": "عقدة دبي للتجارة"},
        {"loc": [48.8566, 2.3522], "name": "سيرفر باريس المشفر"},
        {"loc": [40.7128, -74.0060], "name": "بوابة نيويورك"}
    ]
    
    for l in locations:
        folium.Marker(l["loc"], popup=l["name"], icon=folium.Icon(color='blue', icon='info-sign')).add_to(m)
    
    folium_static(m, width=1200, height=500)
    st.success("جميع العقد (Nodes) تعمل بكفاءة 100% وتحت التشفير السيادي.")

# ==========================================
# الصفحة 4: حصن الأمان (Security)
# ==========================================
elif st.session_state["page"] == "الأمان":
    st.markdown("# 🛡️ حصن الأمان والسيادة")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### البروتوكولات الأمنية المتبعة:
        - **تشفير الكم (Post-Quantum):** استعداد للمستقبل.
        - **الذكاء الاصطناعي المعزول (Air-Gapped AI):** لا بيانات تخرج للإنترنت.
        - **Blockchain Verification:** توثيق العقود عبر سلاسل الكتل.
        """)
        st.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=500")
    with col2:
        st.markdown("""
        ### حالة النظام الحالية:
        - **Active Nodes:** 1,240
        - **Threat Level:** Zero
        - **Encrypted Traffic:** 4.2 PB
        """)
        st.progress(100)

# ==========================================
# الصفحة 5: حلول الشركات (B2B)
# ==========================================
elif st.session_state["page"] == "الشركات":
    st.markdown("# 🏢 حلول المؤسسات الكبرى")
    st.write("نقدم خدمات التحول الرقمي الكامل للمصانع والشركات القابضة.")
    
    st.markdown("""
    <div class="amazon-card" style="padding:40px; text-align:center;">
        <h2 style="color:#fbbf24;">هل أنت مستعد للأتمتة الكاملة؟</h2>
        <p>نحن لا نبيع برامج، نحن نغير هيكل العمل الخاص بك ليصبح آلة منتجة.</p>
        <a href="https://wa.me/213671816346" class="buy-btn-main" style="max-width:300px; margin:auto;">اطلب استشارة للمؤسسات</a>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# الصفحة 6: مركز التحكم (Admin)
# ==========================================
elif st.session_state["page"] == "التحكم":
    st.markdown("# ⚙️ مركز التحكم في النظام")
    pwd = st.text_input("Master Password", type="password")
    if pwd == "0000":
        st.metric("إجمالي المبيعات", "$540,200")
        st.metric("العملاء النشطون", "1,043")
        st.bar_chart(pd.DataFrame({"Sales": [10, 20, 15, 40, 30, 60]}))

# 6. التذييل العالمي
st.divider()
st.markdown("""
<div style="text-align:center; color:#475569;">
    Adid Al-Eid Sovereign Tech OS v6.0 | Global Logistics & Digital Jurisprudence<br>
    📧 laidadid21@gmail.com | 📱 +213 671 81 63 46
</div>
""", unsafe_allow_html=True)
