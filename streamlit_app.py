import streamlit as st
import streamlit.components.v1 as components

# 1. إعدادات البنية السيادية فائقة التوسع (V5.2)
st.set_page_config(
    page_title="Sovereign Tech OS v5.2 | مكتب عديد العيد",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. إدارة النظام واللغة وسلة التسوق
if "lang" not in st.session_state:
    st.session_state["lang"] = "العربية"
if "cart" not in st.session_state:
    st.session_state["cart"] = []

translations = {
    "العربية": {
        "title": "مكتب المحامي عديد العيد",
        "tagline": "الرقمنة القانونية والتجارية الشاملة للمؤسسات والشركات",
        "subtitle": "عصر الورق انتهى. نظام الأتمتة المتقدم والسيادة الرقمية المستدامة عبر تقنيات Air-Gapped AI.",
        "download_btn": "📥 تحميل العرض التنفيذي للمؤسسات (PDF)",
        "contact_title": "⚙️ مركز الاتصال وتحويل العمولات المباشر",
        "whatsapp_text": "💬 تواصل فوري عبر WhatsApp لتأكيد التعاقد",
        "sidebar_head": "🖥️ لوحة التحكم السيادية",
        "lang_label": "🌐 لغة النظام:",
        "buy_btn": "إضافة للسلة 🛒",
        "security_tab": "🛡️ حصن الأمان",
        "philosophy_tab": "📖 الفلسفة الرقمية",
        "prod_tag_1": "أتمتة كاملة", "prod_title_1": "نظام تدقيق وأتمتة العقود الذكية",
        "prod_tag_2": "أتمتة سحابية", "prod_title_2": "مستودعات n8n السيادية المتكاملة",
        "prod_tag_3": "هندسة عكسية", "prod_title_3": "جلسة التدقيق الهيكلي للمصانع",
        "prod_tag_4": "أتمتة محلية", "prod_title_4": "البنية المستقلة (Ollama Hub)",
        "prod_tag_5": "تسويق رقمي", "prod_title_5": "محرك جني العمولات الآلي",
        "prod_tag_6": "رقمنة جزئية", "prod_title_6": "حزمة التحول الرقمي للمؤسسات",
        "sec_desc": "نظامنا يعمل ببروتوكول 'Zero-Knowledge'، مما يعني أن بياناتك مشفرة محلياً ولا يمكن حتى لنا الوصول إليها."
    },
    "English": {
        "title": "Adid Al-Eid Law Firm",
        "tagline": "Comprehensive Legal & Corporate Digitalization",
        "subtitle": "The paper era is over. Advanced automation and sustainable digital sovereignty via Air-Gapped AI.",
        "download_btn": "📥 Download SME Corporate Proposal (PDF)",
        "contact_title": "⚙️ Conversion & Commission Center",
        "whatsapp_text": "💬 Instant WhatsApp for Contract Activation",
        "sidebar_head": "🖥️ Sovereign Tech OS",
        "lang_label": "🌐 System Language:",
        "buy_btn": "Add to Cart 🛒",
        "security_tab": "🛡️ Security Vault",
        "philosophy_tab": "📖 Philosophy",
        "prod_tag_1": "Total Automation", "prod_title_1": "Smart Contracts Auditing Pipeline",
        "prod_tag_2": "Cloud Automation", "prod_title_2": "Sovereign n8n Infrastructure",
        "prod_tag_3": "Reverse Engineering", "prod_title_3": "Industrial Operational Auditing",
        "prod_tag_4": "Local Sovereignty", "prod_title_4": "Offline AI (Ollama Hub)",
        "prod_tag_5": "Digital Arbitrage", "prod_title_5": "Automated Affiliate Engine",
        "prod_tag_6": "Partial Digitalization", "prod_title_6": "SME Transformation Package",
        "sec_desc": "Our system runs on 'Zero-Knowledge' protocols. Your data is encrypted locally and remains inaccessible even to us."
    }
}

t = translations[st.session_state["lang"]]

# 3. هندسة التصميم البصري (دمج القديم مع 3D الجديد)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    html, body, [data-testid="stAppViewContainer"], .main {
        background-color: #0b0f19 !important;
        color: #f8fafc !important;
        font-family: 'Cairo', sans-serif !important;
    }
    
    /* الشعار الرقمي القديم */
    .digital-logo {
        width: 100px; height: 100px; margin: 0 auto 15px auto;
        border-radius: 50%; background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        border: 3px solid #60a5fa; box-shadow: 0 0 25px rgba(59, 130, 246, 0.6);
        display: flex; align-items: center; justify-content: center;
        font-weight: 900; font-size: 28px; color: white;
    }
    
    /* بطاقات المنتجات مع تأثيرات إضافية */
    .premium-card {
        background: linear-gradient(145deg, #111827, #1f2937);
        border: 1px solid #374151; border-radius: 16px; padding: 20px;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.4);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        text-align: center; height: 350px;
        display: flex; flex-direction: column; justify-content: space-between;
    }
    .premium-card:hover { transform: translateY(-10px); border-color: #3b82f6; box-shadow: 0 0 20px rgba(59,130,246,0.4); }

    .card-tag { background: #1e293b; color: #60a5fa; padding: 4px 10px; border-radius: 6px; font-size: 11px; font-weight: 700; }
    .card-price { color: #10b981; font-size: 24px; font-weight: bold; }
    
    /* أيقونات 3D متحركة */
    .floating-icon { font-size: 40px; animation: float 3s ease-in-out infinite; display: block; margin: 10px 0; }
    @keyframes float { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-10px); } }

    .whatsapp-btn {
        background: linear-gradient(135deg, #25D366 0%, #128C7E 100%);
        color: white !important; text-align: center; padding: 14px;
        border-radius: 30px; display: block; font-weight: bold; text-decoration: none;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 4. القائمة الجانبية (نفس الشعار القديم + ميزات جديدة)
# ==========================================
with st.sidebar:
    st.markdown('<div class="digital-logo">LFD</div>', unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align:center; color:white;'>{t['sidebar_head']}</h3>", unsafe_allow_html=True)
    
    st.session_state["lang"] = st.selectbox(t['lang_label'], ["العربية", "English"])
    
    st.divider()
    app_mode = st.radio("القائمة:", ["🏠 الواجهة الرئيسية", t["security_tab"], t["philosophy_tab"], "🔒 إدارة النظام"])
    
    st.divider()
    st.markdown("### 🛒 سلة المشتريات")
    if not st.session_state["cart"]: st.caption("السلة فارغة")
    else:
        for item in st.session_state["cart"]: st.success(f"✅ {item}")
        if st.button("تأكيد الطلب 🚀"): st.balloons()

# ==========================================
# 5. الواجهة الرئيسية (الصور والكاروسيل القديم مع التحديث)
# ==========================================
if app_mode == "🏠 الواجهة الرئيسية":
    # الهيدر القديم الرائع
    st.markdown(f"""
    <div style="text-align:center; margin-bottom:30px;">
        <h1 style="font-size: 45px; font-weight: 900; background: linear-gradient(to left, #3b82f6, #60a5fa, #10b981); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            {t['title']}
        </h1>
        <h3 style="color: #cbd5e1; font-weight: 400;">{t['tagline']}</h3>
        <p style="color: #64748b; max-width: 800px; margin: 0 auto;">{t['subtitle']}</p>
    </div>
    """, unsafe_allow_html=True)

    # زر التحميل القديم
    st.columns([1, 2, 1])[1].download_button(t["download_btn"], "EXECUTIVE PROPOSAL CONTENT", file_name="Proposal.txt")

    st.divider()

    # --- رجوع الكاروسيل بالصور القديمة (لا حذف!) ---
    carousel_html = """
    <div style="direction: ltr; display: flex; justify-content: center; align-items: center; background: #0b0f19; padding: 10px 0; overflow: hidden;">
        <style>
            .container { width: 100%; max-width: 1100px; height: 300px; display: flex; gap: 15px; perspective: 1000px; }
            .card {
                flex: 1; height: 100%; border-radius: 12px; overflow: hidden; position: relative;
                border: 2px solid #334155; transition: all 0.5s cubic-bezier(0.25, 1, 0.5, 1); cursor: pointer;
            }
            .card:hover { flex: 3.5; border-color: #3b82f6; box-shadow: 0 15px 30px rgba(59,130,246,0.3); }
            .card img { width: 100%; height: 100%; object-fit: cover; }
            .card-info {
                position: absolute; bottom: 0; left: 0; right: 0; padding: 15px; text-align: right;
                background: linear-gradient(to top, rgba(0,0,0,0.95), transparent); color: white; opacity: 0; transition: 0.3s;
            }
            .card:hover .card-info { opacity: 1; }
            .card-info h3 { margin: 0; font-size: 16px; color: #60a5fa; font-family: 'Cairo', sans-serif; }
        </style>
        <div class="container">
            <div class="card"><img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=500"><div class="card-info"><h3>Contracts Automation</h3></div></div>
            <div class="card"><img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=500"><div class="card-info"><h3>n8n Local Ecosystem</h3></div></div>
            <div class="card"><img src="https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=500"><div class="card-info"><h3>Reverse Engineering</h3></div></div>
            <div class="card"><img src="https://images.unsplash.com/photo-1600132806370-bf17e65e942f?w=500"><div class="card-info"><h3>Offline AI Sovereign</h3></div></div>
            <div class="card"><img src="https://images.unsplash.com/photo-1432888622747-4eb9a8efeb07?w=500"><div class="card-info"><h3>Commission Arbitrage</h3></div></div>
            <div class="card"><img src="https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=500"><div class="card-info"><h3>SME Transformation</h3></div></div>
        </div>
    </div>
    """
    components.html(carousel_html, height=330)
    
    st.divider()

    # --- شبكة المنتجات (تمت إضافة زر الشراء والشرح) ---
    st.markdown("<h3 style='color:#60a5fa; font-weight:700;'>🔥 الحلول الرقمية (إصدار المؤسسات)</h3>", unsafe_allow_html=True)
    
    row1 = st.columns(3)
    row2 = st.columns(3)
    
    products = [
        {"tag": t["prod_tag_1"], "title": t["prod_title_1"], "price": "$249.99", "icon": "📜"},
        {"tag": t["prod_tag_2"], "title": t["prod_title_2"], "price": "$642.23", "icon": "🔗"},
        {"tag": t["prod_tag_3"], "title": t["prod_title_3"], "price": "$525.20", "icon": "⚙️"},
        {"tag": t["prod_tag_4"], "title": t["prod_title_4"], "price": "$999.00", "icon": "🧠"},
        {"tag": t["prod_tag_5"], "title": t["prod_title_5"], "price": "$450.00", "icon": "💰"},
        {"tag": t["prod_tag_6"], "title": t["prod_title_6"], "price": "$1,200.00", "icon": "🏢"},
    ]

    for i, p in enumerate(products):
        with (row1[i] if i < 3 else row2[i-3]):
            st.markdown(f"""
            <div class="premium-card">
                <span class="card-tag">{p['tag']}</span>
                <span class="floating-icon">{p['icon']}</span>
                <h4 style="color:white;">{p['title']}</h4>
                <div class="card-price">{p['price']}</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(t["buy_btn"], key=f"p_{i}"):
                st.session_state["cart"].append(p['title'])
                st.toast(f"تمت إضافة {p['title']}")

    st.divider()
    
    # منطقة الاتصال والفيديو القديمة
    col_v, col_w = st.columns([1.8, 1.2])
    with col_v:
        st.markdown("<h4 style='color:white;'>🎥 استعراض كفاءة البنية والتشغيل</h4>", unsafe_allow_html=True)
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # ضع رابط الفيديو هنا
    with col_w:
        st.markdown(f"<h4>{t['contact_title']}</h4>", unsafe_allow_html=True)
        st.markdown(f"""
        <div class="premium-card" style="height:auto; padding:25px;">
            <p style='font-size:13px; color:#94a3b8;'>بوابة توجيه حركة المرور متصلة بنظام الأتمتة المحلي وإشعارات العمولات الفورية.</p>
            <a href="https://wa.me/213671816346" target="_blank" class="whatsapp-btn">{t['whatsapp_text']}</a>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# 6. قسم الأمان الجديد (Security Vault)
# ==========================================
elif app_mode == t["security_tab"]:
    st.markdown(f"<h1>{t['security_tab']} 🛡️</h1>", unsafe_allow_html=True)
    st.info(t["sec_desc"])
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### ميزات الحماية السيادية:
        1. **تشفير AES-256:** جميع الملفات والعقود مشفرة بأعلى المعايير العسكرية.
        2. **Air-Gapped Ready:** الأنظمة يمكنها العمل بدون إنترنت (Offline) تماماً.
        3. **سيادة محلية:** بياناتك تخزن في 'نود' محلي داخل مكتبك وليس في خوادم أمريكية أو أوروبية.
        """)
    with col2:
        st.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=500")

# ==========================================
# 7. قسم الفلسفة (Philosophy)
# ==========================================
elif app_mode == t["philosophy_tab"]:
    st.markdown(f"<h1>{t['philosophy_tab']} 📖</h1>", unsafe_allow_html=True)
    st.write("""
    نحن نؤمن في **مكتب عديد العيد** بدمج ثلاثة أركان:
    - **القانون (العدالة):** لضمان حقوقك في العالم الرقمي.
    - **الإنسان (الإبداع):** لتبقى أنت المتحكم في استراتيجية عملك.
    - **الآلة (السرعة):** لأتمتة المهام المملة والورقية بنسبة 100%.
    """)
    st.image("https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800")

# ==========================================
# 8. تحكم النظام (Admin)
# ==========================================
elif app_mode == "🔒 إدارة النظام":
    st.markdown("## 🔒 Sovereign Control Room")
    pwd = st.text_input("كلمة المرور:", type="password")
    if pwd == "0000":
        st.success("تم الاتصال بالبنية التحتية بنجاح.")
        st.metric("الحالة", "Online", "Stable")
