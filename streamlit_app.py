import streamlit as st
import streamlit.components.v1 as components
import json

# ==========================================
# 1. إعدادات البنية السيادية فائقة التوسع (CORE CONFIG)
# ==========================================
st.set_page_config(
    page_title="Sovereign Tech OS v5.0 | Adid Al-Eid",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# إدارة حالة النظام (Session State)
if "lang" not in st.session_state:
    st.session_state["lang"] = "العربية"
if "cart" not in st.session_state:
    st.session_state["cart"] = []
if "auth" not in st.session_state:
    st.session_state["auth"] = False

# ==========================================
# 2. القاموس المهني الشامل (MULTILINGUAL ENGINE)
# ==========================================
translations = {
    "العربية": {
        "title": "مؤسسة عديد العيد للسيادة الرقمية",
        "tagline": "هندسة النظم القانونية والأتمتة السيادية للمؤسسات",
        "subtitle": "عصر الورق انتهى. نحن نبني حصوناً رقمية تدير نفسها ذاتياً بعيداً عن الرقابة السحابية العامة.",
        "nav_home": "🏠 الرئيسية",
        "nav_market": "🛍️ المتجر السيادي",
        "nav_security": "🛡️ ميثاق الأمان",
        "nav_about": "📖 فلسفة النظام",
        "nav_admin": "🔒 تحكم النظام",
        "buy_now": "إضافة للتعاقد 🛒",
        "cart_title": "📦 سلة الأنظمة المختارة",
        "checkout": "تأكيد طلب التفعيل",
        "sidebar_head": "🖥️ تحكم السيادة v5.0",
        "prod_1": "أتمتة العقود الذكية", "desc_1": "نظام تدقيق وتوقيع آلي يكتشف الثغرات القانونية فورياً.",
        "prod_2": "بنية n8n السيادية", "desc_2": "ربط كامل لأقسام الشركة عبر سيرفرات محلية مشفرة.",
        "prod_3": "الهندسة العكسية للمصانع", "desc_3": "فحص الأنظمة التشغيلية وسد الثغرات الأمنية في خطوط الإنتاج.",
        "prod_4": "Ollama AI Hub", "desc_4": "ذكاء اصطناعي محلي (LLM) يعمل بدون إنترنت لخصوصية تامة.",
        "prod_5": "محرك العمولات الآلي", "desc_5": "نظام جني أرباح من الترافيك والتحويلات الرقمية بشكل مستقل.",
        "prod_6": "حزمة التحول SME", "desc_6": "خطة الانتقال الكامل للمؤسسات الصغيرة من الورق إلى الأتمتة."
    },
    "English": {
        "title": "Adid Al-Eid Sovereign Tech OS",
        "tagline": "Architecting Digital Sovereignty & Legal Automation",
        "subtitle": "The paper era is over. We build self-governing digital fortresses independent of public clouds.",
        "nav_home": "🏠 Home",
        "nav_market": "🛍️ Sovereign Market",
        "nav_security": "🛡️ Security Vault",
        "nav_about": "📖 Philosophy",
        "nav_admin": "🔒 Admin Control",
        "buy_now": "Add to Contract 🛒",
        "cart_title": "📦 Selected Systems Cart",
        "checkout": "Confirm Activation",
        "sidebar_head": "🖥️ Sovereign Control v5.0",
        "prod_1": "Smart Contracts Automation", "desc_1": "Automated legal auditing and signing system.",
        "prod_2": "Sovereign n8n Node", "desc_2": "Full enterprise connectivity via local encrypted servers.",
        "prod_3": "Industrial Rev-Engineering", "desc_3": "Operational auditing and security patching for factories.",
        "prod_4": "Ollama AI Hub", "desc_4": "Local AI (LLM) operating offline for total data privacy.",
        "prod_5": "Comm. Arbitrage Engine", "desc_5": "Automated monetization system for digital traffic.",
        "prod_6": "SME Digital Pack", "desc_6": "Complete paperless transformation for small businesses."
    }
}

t = translations[st.session_state["lang"]]

# ==========================================
# 3. هندسة التصميم الخارقة (CSS 3D & NEON)
# ==========================================
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;700;900&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {{
        background: radial-gradient(circle at top right, #0f172a, #020617) !important;
        color: #e2e8f0 !important;
        font-family: 'Cairo', sans-serif !important;
        direction: {"rtl" if st.session_state["lang"] == "العربية" else "ltr"};
    }}

    /* تأثير الزجاج المتوهج */
    .glass-card {{
        background: rgba(30, 41, 59, 0.4);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 24px;
        padding: 30px;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.4);
        text-align: center;
        margin-bottom: 20px;
    }}
    .glass-card:hover {{
        transform: translateY(-12px) scale(1.02);
        border-color: #3b82f6;
        box-shadow: 0 0 25px rgba(59, 130, 246, 0.3);
    }}

    .icon-3d {{
        font-size: 60px;
        margin-bottom: 20px;
        filter: drop-shadow(0 10px 15px rgba(0,0,0,0.5));
        display: inline-block;
        animation: float 3s ease-in-out infinite;
    }}
    @keyframes float {{
        0% {{ transform: translateY(0px); }}
        50% {{ transform: translateY(-10px); }}
        100% {{ transform: translateY(0px); }}
    }}

    .hero-title {{
        font-size: 55px;
        font-weight: 900;
        background: linear-gradient(to right, #60a5fa, #f472b6, #34d399);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }}

    .stButton>button {{
        background: linear-gradient(135deg, #2563eb 0%, #1e40af 100%);
        color: white !important;
        border: none;
        border-radius: 15px;
        padding: 12px 30px;
        font-weight: 700;
        width: 100%;
        transition: 0.4s;
    }}
    .stButton>button:hover {{
        box-shadow: 0 0 20px rgba(37, 99, 235, 0.6);
        transform: scale(1.03);
    }}

    [data-testid="stSidebar"] {{
        background-color: #020617 !important;
        border-right: 1px solid #1e293b !important;
    }}
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 4. القائمة الجانبية (CONTROL SIDEBAR)
# ==========================================
with st.sidebar:
    st.markdown('<div style="text-align:center;"><span class="icon-3d">💎</span></div>', unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align:center;'>{t['sidebar_head']}</h2>", unsafe_allow_html=True)
    
    st.session_state["lang"] = st.selectbox("🌐 لغة النظام / Language", ["العربية", "English"])
    
    st.divider()
    menu = st.radio("القائمة الرئيسية", [t["nav_home"], t["nav_market"], t["nav_security"], t["nav_about"], t["nav_admin"]])
    
    st.divider()
    st.markdown(f"### {t['cart_title']}")
    if not st.session_state["cart"]:
        st.caption("السلة فارغة حالياً")
    else:
        for item in st.session_state["cart"]:
            st.success(f"✅ {item}")
        if st.button(t["checkout"]):
            st.balloons()
            st.toast("تم إرسال طلب تفعيل الأنظمة للمكتب!")

# ==========================================
# 5. الصفحة الرئيسية (HERO SECTION)
# ==========================================
if menu == t["nav_home"]:
    st.markdown(f"""
    <div style="text-align:center; padding: 50px 0;">
        <h1 class="hero-title">{t['title']}</h1>
        <h3 style="color: #94a3b8; font-weight: 400;">{t['tagline']}</h3>
        <p style="max-width: 900px; margin: 30px auto; font-size: 18px; color: #64748b; line-height: 1.8;">{t['subtitle']}</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    features = [
        {"icon": "🛡️", "title": "سيادة كاملة", "desc": "بياناتك تحت سيطرتك الفيزيائية، لا سحابة عامة بعد اليوم."},
        {"icon": "⚡", "title": "أتمتة فورية", "desc": "تحويل العمليات الإدارية من أيام إلى ثوانٍ معدودة."},
        {"icon": "🧠", "title": "ذكاء محلي", "desc": "نماذج AI ضخمة تعمل على سيرفراتك الخاصة وبدون إنترنت."}
    ]
    for i, col in enumerate([col1, col2, col3]):
        with col:
            st.markdown(f"""
            <div class="glass-card">
                <div class="icon-3d">{features[i]['icon']}</div>
                <h3>{features[i]['title']}</h3>
                <p style="color:#94a3b8; font-size:14px;">{features[i]['desc']}</p>
            </div>
            """, unsafe_allow_html=True)

# ==========================================
# 6. المتجر الرقمي (MARKETPLACE)
# ==========================================
elif menu == t["nav_market"]:
    st.markdown(f"<h1 style='text-align:center;'>{t['nav_market']}</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#60a5fa;'>اختر الأنظمة المطلوبة لبناء بنيتك السيادية</p>", unsafe_allow_html=True)
    
    products = [
        {"id": 1, "name": t["prod_1"], "price": "$499", "desc": t["desc_1"], "icon": "📜"},
        {"id": 2, "name": t["prod_2"], "price": "$850", "desc": t["desc_2"], "icon": "🔗"},
        {"id": 3, "name": t["prod_3"], "price": "$1,200", "desc": t["desc_3"], "icon": "⚙️"},
        {"id": 4, "name": t["prod_4"], "price": "$1,900", "desc": t["desc_4"], "icon": "🧠"},
        {"id": 5, "name": t["prod_5"], "price": "$350", "desc": t["desc_5"], "icon": "💰"},
        {"id": 6, "name": t["prod_6"], "price": "$2,500", "desc": t["desc_6"], "icon": "🏢"}
    ]

    col_m1, col_m2, col_m3 = st.columns(3)
    for idx, p in enumerate(products):
        current_col = [col_m1, col_m2, col_m3][idx % 3]
        with current_col:
            st.markdown(f"""
            <div class="glass-card" style="height: 380px; display: flex; flex-direction: column; justify-content: space-between;">
                <div>
                    <div class="icon-3d">{p['icon']}</div>
                    <h4 style="color:white;">{p['name']}</h4>
                    <p style="font-size:12px; color:#94a3b8;">{p['desc']}</p>
                </div>
                <h3 style="color:#10b981;">{p['price']}</h3>
            </div>
            """, unsafe_allow_html=True)
            if st.button(t["buy_now"], key=f"btn_{p['id']}"):
                st.session_state["cart"].append(p['name'])
                st.rerun()

# ==========================================
# 7. ميثاق الأمان (SECURITY VAULT)
# ==========================================
elif menu == t["nav_security"]:
    st.markdown(f"<h1>{t['nav_security']}</h1>", unsafe_allow_html=True)
    col_sec1, col_sec2 = st.columns(2)
    
    with col_sec1:
        st.markdown("""
        <div class="glass-card" style="text-align:right;">
            <h3>🛡️ ميثاق الخصوصية المطلقة</h3>
            <p>نحن نؤمن أن المعلومة هي رأس المال الحقيقي، لذلك:</p>
            <ul style="color:#94a3b8;">
                <li>لا يتم تخزين أي بيانات للعملاء على سيرفرات خارجية.</li>
                <li>يتم تسليم العميل 'نود' (Node) محلي خاص به.</li>
                <li>تشفير PGP لكافة المراسلات الحساسة.</li>
                <li>إمكانية التشغيل في بيئة معزولة تماماً عن الإنترنت (Air-Gapped).</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col_sec2:
        st.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=500", caption="تشفير سيادي متقدم")

# ==========================================
# 8. فلسفة المشروع (PHILOSOPHY)
# ==========================================
elif menu == t["nav_about"]:
    st.markdown(f"<h1>{t['nav_about']}</h1>", unsafe_allow_html=True)
    st.info("نحن ندمج بين القانون، التقنية، والسيادة الرقمية.")
    
    st.markdown("""
    ### رؤية عديد العيد الرقمية
    في ظل التحولات العالمية، أصبحت السحابة العامة (Public Cloud) خطراً على سرية الشركات والمؤسسات. 
    رؤيتنا تتلخص في **"إعادة توطين التقنية"**. 
    
    - **لماذا الأتمتة؟** لتقليل الخطأ البشري بنسبة 99%.
    - **لماذا السيادة؟** لأن من يملك بياناته يملك قراره.
    - **لماذا عديد العيد؟** لأننا ندمج الخبرة القانونية الصارمة مع هندسة النظم الحديثة.
    """)
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # رابط تجريبي

# ==========================================
# 9. تحكم النظام (ADMIN LOCK)
# ==========================================
elif menu == t["nav_admin"]:
    st.markdown("## 🔒 Sovereign Control Room")
    pwd = st.text_input("Enter Master Password:", type="password")
    if st.button("Authorize"):
        if pwd == "0000":
            st.session_state["auth"] = True
            st.success("Access Granted.")
        else:
            st.error("Access Denied.")
            
    if st.session_state["auth"]:
        st.write("---")
        st.markdown("### 🛠️ مراقبة الأداء المحلي")
        st.metric(label="Local AI Status", value="Online", delta="Stable")
        st.metric(label="Automation Flows", value="14 Active", delta="2 Updates")

# ==========================================
# التذييل الفاخر (FOOTER)
# ==========================================
st.markdown("---")
f_col1, f_col2, f_col3 = st.columns(3)
with f_col1:
    st.markdown("🌐 **مكتب عديد العيد** - السيادة الرقمية")
with f_col2:
    st.markdown("📧 laidadid21@gmail.com")
with f_col3:
    st.markdown("📱 WhatsApp: [+213671816346](https://wa.me/213671816346)")

st.markdown("<div style='text-align:center; font-size:10px; color:#475569;'>Sovereign Tech OS v5.0 | All Rights Reserved 2024</div>", unsafe_allow_html=True)
