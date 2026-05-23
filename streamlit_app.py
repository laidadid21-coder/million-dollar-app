import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np

# 1. إعدادات الإمبراطورية الرقمية (Sovereign OS v6.2)
st.set_page_config(
    page_title="Adid Al-Eid Global Sovereign OS v6.2",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. إدارة حالة النظام (State Management)
if "cart" not in st.session_state: st.session_state["cart"] = []
if "lang" not in st.session_state: st.session_state["lang"] = "العربية"
if "page" not in st.session_state: st.session_state["page"] = "🏠 الرئيسية"

# 3. محرك التصميم البصري (Amazon Ultra-Luxury Style)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;700;900&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at center, #0f172a 0%, #020617 100%) !important;
        color: #e2e8f0 !important;
        font-family: 'Cairo', sans-serif !important;
    }

    /* تصميم بطاقات أمازون */
    .amazon-card {
        background: rgba(30, 41, 59, 0.7);
        border-radius: 15px;
        border: 1px solid #334155;
        padding: 20px;
        transition: 0.4s;
        text-align: center;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .amazon-card:hover {
        border-color: #fbbf24;
        box-shadow: 0 0 30px rgba(251, 191, 36, 0.2);
        transform: translateY(-10px);
    }

    .price-tag { color: #10b981; font-size: 26px; font-weight: 900; margin: 10px 0; }
    
    /* أيقونات 3D */
    .icon-3d { font-size: 50px; margin-bottom: 15px; filter: drop-shadow(0 0 10px #3b82f6); }

    /* الشعار */
    .digital-logo {
        width: 80px; height: 80px; margin: 0 auto;
        border-radius: 50%; background: linear-gradient(135deg, #1e3a8a, #3b82f6);
        border: 2px solid #fbbf24; display: flex; align-items: center; justify-content: center;
        font-weight: 900; font-size: 22px; color: white;
    }
    </style>
""", unsafe_allow_html=True)

# 4. القائمة الجانبية (Navigation Sidebar)
with st.sidebar:
    st.markdown('<div class="digital-logo">LFD</div>', unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center; color:#fbbf24;'>إمبراطورية العيد</h2>", unsafe_allow_html=True)
    
    st.session_state["lang"] = st.selectbox("🌐 لغة النظام", ["العربية", "English"])
    st.divider()
    
    # الـ 6 صفحات الاحترافية
    menu_options = ["🏠 الرئيسية", "🛍️ المتجر العالمي", "📍 خريطة GPS السيادية", "🛡️ حصن الأمان", "📖 فلسفة النظام", "⚙️ مركز التحكم"]
    st.session_state["page"] = st.radio("انتقل إلى:", menu_options)
    
    st.divider()
    st.markdown(f"### 🛒 السلة ({len(st.session_state['cart'])})")
    for item in st.session_state["cart"]:
        st.caption(f"✅ {item}")
    if st.button("إتمام الدفع الآمن 💳"):
        st.balloons()
        st.success("تم إرسال طلبك للتدقيق السيادي")

# ==========================================
# الصفحة 1: الرئيسية (الصور والكاروسيل)
# ==========================================
if st.session_state["page"] == "🏠 الرئيسية":
    st.markdown("""
    <div style="text-align:center; padding:40px;">
        <h1 style="font-size:55px; font-weight:900; background: linear-gradient(to right, #fbbf24, #3b82f6); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            Sovereign Tech OS v6.2
        </h1>
        <p style="font-size:20px; color:#94a3b8;">الموقع الأفضل عالمياً لأتمتة الشركات والسيادة الرقمية</p>
    </div>
    """, unsafe_allow_html=True)

    # الكاروسيل الأصلي (بدون حذف)
    carousel_html = """
    <div style="display: flex; gap: 15px; overflow-x: auto; padding: 20px; scrollbar-width: none;">
        <div style="min-width:300px;"><img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=500" style="border-radius:15px; width:100%;"></div>
        <div style="min-width:300px;"><img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=500" style="border-radius:15px; width:100%;"></div>
        <div style="min-width:300px;"><img src="https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=500" style="border-radius:15px; width:100%;"></div>
        <div style="min-width:300px;"><img src="https://images.unsplash.com/photo-1600132806370-bf17e65e942f?w=500" style="border-radius:15px; width:100%;"></div>
    </div>
    """
    components.html(carousel_html, height=320)
    
    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🎥 استعراض كفاءة الأتمتة")
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    with col2:
        st.markdown("### ⚙️ الاتصال المباشر")
        st.markdown("""
        <div class="amazon-card" style="height:auto;">
            <p>تواصل مع فريق الأتمتة لتنفيذ مشروعك السيادي فوراً.</p>
            <a href="https://wa.me/213671816346" style="background:#25D366; color:white; padding:15px; border-radius:10px; text-decoration:none; font-weight:bold; display:block; text-align:center;">
                WhatsApp Instant Connection
            </a>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# الصفحة 2: المتجر (Amazon/Alibaba Style)
# ==========================================
elif st.session_state["page"] == "🛍️ المتجر العالمي":
    st.markdown("## 🛒 متجر السيادة الرقمي (Mega Store)")
    
    # تصنيفات
    st.multiselect("تصفية حسب النوع:", ["AI Servers", "Legal Bots", "Cyber Security", "Industrial Nodes"], default=["AI Servers"])
    
    products = [
        {"n": "Sovereign AI Node 1000", "p": "$12,000", "i": "🧠", "img": "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=400"},
        {"n": "Smart Legal Auditor", "p": "$2,500", "i": "📜", "img": "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=400"},
        {"n": "n8n Enterprise server", "p": "$950", "i": "🔗", "img": "https://images.unsplash.com/photo-1551434678-e076c223a692?w=400"},
        {"n": "Military VPN Node", "p": "$1,100", "i": "🛡️", "img": "https://images.unsplash.com/photo-1558494949-ef010cbdcc51?w=400"},
        {"n": "Reverse Engineering Kit", "p": "$5,400", "i": "⚙️", "img": "https://images.unsplash.com/photo-1563986768609-322da13575f3?w=400"},
        {"n": "Global SME Pack", "p": "$3,200", "i": "🏢", "img": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=400"},
    ]
    
    cols = st.columns(3)
    for idx, p in enumerate(products):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="amazon-card">
                <img src="{p['img']}" style="width:100%; border-radius:10px; height:180px; object-fit:cover;">
                <h3>{p['i']} {p['n']}</h3>
                <p style="color:#94a3b8; font-size:12px;">أفضل تقنية سيادية لعام 2024</p>
                <div class="price-tag">{p['p']}</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"أضف إلى السلة 🛒", key=f"buy_{idx}"):
                st.session_state["cart"].append(p['n'])
                st.toast(f"تمت إضافة {p['n']} إلى سلتك")

# ==========================================
# الصفحة 3: GPS (خريطة العقد العالمية)
# ==========================================
elif st.session_state["page"] == "📍 خريطة GPS السيادية":
    st.markdown("## 📍 خريطة المواقع والعقد السيادية")
    st.write("توزيع الخوادم والـ Nodes الخاصة بالمؤسسة حول العالم (تتبع مباشر).")
    
    # بيانات الـ GPS
    df = pd.DataFrame({
        'city': ['Algeria HQ', 'Dubai Node', 'Paris Node', 'New York Vault'],
        'lat': [36.7538, 25.2048, 48.8566, 40.7128],
        'lon': [3.0588, 55.2708, 2.3522, -74.0060]
    })
    
    st.map(df) # خريطة Streamlit المدمجة (لا تسبب أخطاء)
    
    st.info("💡 جميع العقد (Nodes) الموضحة أعلاه تعمل بتشفير سيادي كامل ومحمية ببروتوكولات Air-Gapped.")

# ==========================================
# الصفحة 4: حصن الأمان (Security)
# ==========================================
elif st.session_state["page"] == "🛡️ حصن الأمان":
    st.markdown("## 🛡️ ميثاق الأمن السيادي العالمي")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### بروتوكول Zero-Knowledge
        نحن نضمن أن بيانات شركتك:
        - لا تخرج من السيرفر المحلي.
        - مشفرة بمفتاح خاص تملكه أنت فقط.
        - محمية من التجسس السحابي (Public Cloud Security).
        """)
    with col2:
        st.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=500")

# ==========================================
# الصفحة 5: الفلسفة (Philosophy)
# ==========================================
elif st.session_state["page"] == "📖 فلسفة النظام":
    st.markdown("## 📖 فلسفة (إنسان + آلة + سيادة)")
    st.write("""
    رؤيتنا في مكتب عديد العيد ليست مجرد بيع برامج، بل بناء **إمبراطوريات رقمية مستقلة**.
    نحن نعيد القوة للمؤسسة لتمتلك "عقلها الرقمي" الخاص بعيداً عن هيمنة الشركات الكبرى.
    """)
    st.image("https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800")

# ==========================================
# الصفحة 6: مركز التحكم (Control Center)
# ==========================================
elif st.session_state["page"] == "⚙️ مركز التحكم":
    st.markdown("## ⚙️ وحدة التحكم المركزية (Admin)")
    password = st.text_input("أدخل كلمة مرور النظام السيادي:", type="password")
    if password == "0000":
        st.success("تم الدخول إلى العصب المركزي.")
        col_a, col_b, col_c = st.columns(3)
        col_a.metric("المبيعات العالمية", "$1.2M", "+12%")
        col_b.metric("العقد النشطة", "450", "Stable")
        col_c.metric("مستوى التشفير", "AES-512", "Secure")
        st.line_chart(np.random.randn(20, 3))

# 6. التذييل (Footer)
st.divider()
st.markdown("""
<div style="text-align:center; color:#475569; font-size:12px;">
    Adid Al-Eid Global Sovereign OS v6.2 | Powering the Future of SME & Corporations<br>
    📧 laidadid21@gmail.com | 📱 +213 671 81 63 46
</div>
""", unsafe_allow_html=True)
