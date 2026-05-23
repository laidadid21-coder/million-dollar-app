import streamlit as st
import streamlit.components.v1 as components

# 1. إعدادات البنية السيادية فائقة التوسع
st.set_page_config(
    page_title="Sovereign Tech OS v4.2 | مكتب عديد العيد",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. إدارة النظام اللغوي التلقائي
if "lang" not in st.session_state:
    st.session_state["lang"] = "العربية"

# قاموس المصطلحات الاحترافية الشامل للمؤسسات الصغيرة والمتوسطة
translations = {
    "العربية": {
        "title": "مكتب المحامي عديد العيد",
        "tagline": "الرقمنة القانونية والتجارية الشاملة للمؤسسات والشركات",
        "subtitle": "عصر الورق انتهى. نظام الأتمتة المتقدم والسيادة الرقمية المستدامة.",
        "download_btn": "📥 تحميل العرض التنفيذي للمؤسسات (PDF)",
        "contact_title": "⚙️ مركز الاتصال وتحويل العمولات المباشر",
        "whatsapp_text": "💬 تواصل فوري عبر WhatsApp لتأكيد التعاقد",
        "sidebar_head": "🖥️ لوحة التحكم السيادية",
        "lang_label": "🌐 لغة النظام الحالية:",
        "mode_label": "🎛️ البيئة التشغيلية الحالية:",
        "prod_tag_1": "أتمتة كاملة", "prod_title_1": "نظام تدقيق وأتمتة العقود الذكية للمؤسسات",
        "prod_tag_2": "أتمتة سحابية", "prod_title_2": "مستودعات وبنية n8n السيادية المتكاملة مع Airtable",
        "prod_tag_3": "هندسة عكسية", "prod_title_3": "جلسة التدقيق الهيكلي وسد الثغرات التشغيلية للمصانع",
        "prod_tag_4": "أتمتة محلية", "prod_title_4": "البنية التحتية المحلية المستقلة عن الإنترنت (Ollama Hub)",
        "prod_tag_5": "تسويق رقمي", "prod_title_5": "محرك جني العمولات الآلي لوسائل التواصل الاجتماعي",
        "prod_tag_6": "رقمنة جزئية", "prod_title_6": "حزمة التحول الرقمي التدريجي للمؤسسات الصغيرة والمتوسطة"
    },
    "English": {
        "title": "Adid Al-Eid Law Firm",
        "tagline": "Comprehensive Legal & Corporate Digitalization",
        "subtitle": "The paper era is over. Advanced automated pipelines and sovereign architectures.",
        "download_btn": "📥 Download SME Corporate Executive Proposal (PDF)",
        "contact_title": "⚙️ Conversion & Direct Commission Control Center",
        "whatsapp_text": "💬 Instant WhatsApp Connection for Contract Activation",
        "sidebar_head": "🖥️ Sovereign Tech OS Control",
        "lang_label": "🌐 System Core Language:",
        "mode_label": "🎛️ Operational Environment Mode:",
        "prod_tag_1": "Total Automation", "prod_title_1": "Enterprise Smart Contracts & Auditing Digital Pipeline",
        "prod_tag_2": "Cloud Automation", "prod_title_2": "Sovereign n8n Infrastructure integrated with Airtable",
        "prod_tag_3": "Reverse Engineering", "prod_title_3": "Industrial Infrastructure Security & Operational Auditing",
        "prod_tag_4": "Local Sovereignty", "prod_title_4": "On-Premise Offline Artificial Intelligence (Ollama Hub)",
        "prod_tag_5": "Digital Arbitrage", "prod_title_5": "Automated Affiliate Commission & Traffic Monetization Engine",
        "prod_tag_6": "Partial Digitalization", "prod_title_6": "Gradual Tech Transformation Package for SMEs & Private Sectors"
    },
    "Français": {
        "title": "Cabinet Adid Al-Eid",
        "tagline": "Digitalisation Juridique & Entreprise Globale",
        "subtitle": "L'ère du papier est révolue. Automatisation avancée et architectures souveraines.",
        "download_btn": "📥 Télécharger la Proposition Exécutive PME (PDF)",
        "contact_title": "⚙️ Centre de Contrôle des Commissions & Conversions",
        "whatsapp_text": "💬 Connexion WhatsApp Instantanée pour Activation de Contrat",
        "sidebar_head": "🖥️ Contrôle Souverain du Système",
        "lang_label": "🌐 Langue Principale du Système:",
        "mode_label": "🎛️ Mode d'Environnement Opérationnel:",
        "prod_tag_1": "Digitalisation Totale", "prod_title_1": "Système d'Automatisation des Contrats d'Entreprise",
        "prod_tag_2": "Automatisation Cloud", "prod_title_2": "Infrastructure Souveraine n8n Connectée à Airtable",
        "prod_tag_3": "Ingénierie Inverse", "prod_title_3": "Audit de Sécurité Industrielle et Correction de Flux",
        "prod_tag_4": "Souveraineté Locale", "prod_title_4": "Intelligence Artificielle Locale Hors-Ligne (Ollama Hub)",
        "prod_tag_5": "Arbitrage Digital", "prod_title_5": "Moteur de Commission d'Affiliation Automatisé Médias Sociaux",
        "prod_tag_6": "Digitalisation Partielle", "prod_title_6": "Pack de Transformation Technologique Évolutif pour PME"
    }
}

t = translations[st.session_state["lang"]]

# 3. هندسة التصميم البصري الخارق ومعالجة عيوب الواجهة بالكامل عبر الـ CSS المتقدم
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    /* فرض خط Cairo الاحترافي وضمان المحاذاة المتناسقة */
    html, body, [data-testid="stAppViewContainer"], .main {
        background-color: #0b0f19 !important;
        color: #f8fafc !important;
        font-family: 'Cairo', sans-serif !important;
    }
    
    /* تصحيح محاذاة النصوص حسب اللغة المختارة تلقائياً للتحكم بالجمالية */
    .directional-box {
        text-align: center;
        margin-bottom: 35px;
        padding: 20px;
    }
    
    /* شعار رقمي فاخر مبني بالـ CSS الصافي لإنهاء مشكلة روابط الصور المكسورة */
    .digital-logo {
        width: 110px;
        height: 110px;
        margin: 0 auto 15px auto;
        border-radius: 50%;
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        border: 3px solid #60a5fa;
        box-shadow: 0 0 25px rgba(59, 130, 246, 0.6);
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 900;
        font-size: 28px;
        color: #ffffff;
        letter-spacing: 1px;
    }
    
    /* تصحيح خط وهيكل القائمة الجانبية (المنطقة المحاطة بالحيز الأحمر يساراً) */
    [data-testid="stSidebar"] {
        background-color: #0f172a !important;
        border-right: 1px solid #1e293b !important;
        border-left: 1px solid #1e293b !important;
    }
    .sidebar-card {
        background: #1e293b;
        padding: 15px;
        border-radius: 12px;
        margin-bottom: 15px;
        border: 1px solid #334155;
    }
    
    /* تصميم بطاقات عرض المنتجات الستة لملء وتنسيق المساحة السفلية */
    .premium-card {
        background: linear-gradient(145deg, #111827, #1f2937);
        border: 1px solid #374151;
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.4);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        text-align: center;
        height: 250px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .premium-card:hover {
        transform: translateY(-5px);
        border-color: #3b82f6;
        box-shadow: 0 15px 30px rgba(59, 130, 246, 0.25);
    }
    .card-tag {
        background-color: #1e293b;
        color: #60a5fa;
        padding: 4px 10px;
        border-radius: 6px;
        font-size: 11px;
        font-weight: 700;
        align-self: center;
    }
    .card-price {
        color: #10b981;
        font-size: 22px;
        font-weight: bold;
        font-family: monospace;
    }
    
    /* تنسيق زر الواتساب العصري */
    .whatsapp-btn {
        background: linear-gradient(135deg, #25D366 0%, #128C7E 100%);
        color: white !important;
        text-align: center !important;
        padding: 14px;
        border-radius: 30px;
        display: block;
        font-weight: bold;
        text-decoration: none;
        box-shadow: 0 5px 15px rgba(37, 211, 102, 0.3);
        transition: opacity 0.2s;
    }
    .whatsapp-btn:hover { opacity: 0.95; text-decoration: none; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# معالجة وهندسة القائمة الجانبية (تصحيح تشوهات الحيز الأيسر بالكامل)
# ==========================================
with st.sidebar:
    # الشعار الرقمي الجديد المعتمد كلياً على البناء البرمجي الداخلي المستقر
    st.markdown('<div class="digital-logo">LFD</div>', unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align:center; color:#ffffff; font-weight:900; margin-bottom:2px;'>{t['sidebar_head']}</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#64748b; font-size:12px; margin-top:0;'>Adid Al-Eid Sovereign OS v4.2</p>", unsafe_allow_html=True)
    st.divider()
    
    # تنظيم أدوات التحكم بداخل حاويات مخصصة لمنع التشتت والتبعثر البصري
    st.markdown(f"<label style='font-size:13px; color:#94a3b8;'>{t['lang_label']}</label>", unsafe_allow_html=True)
    st.session_state["lang"] = st.selectbox("Select Language:", ["العربية", "English", "Français"], label_visibility="collapsed")
    
    st.markdown("<div style='margin-top:15px;'></div>", unsafe_allow_html=True)
    
    st.markdown(f"<label style='font-size:13px; color:#94a3b8;'>{t['mode_label']}</label>", unsafe_allow_html=True)
    app_mode = st.radio("Mode:", ["🌐 Client Interface", "🔒 System Control"], label_visibility="collapsed")
    
    st.divider()
    # إبراز البريد الرسمي بشكل محمي ومقروء داخل القائمة
    st.markdown("""
    <div class="sidebar-card" style="text-align:center;">
        <span style="color:#94a3b8; font-size:11px; display:block;">البريد المربوط بالأتمتة</span>
        <code style="color:#60a5fa; font-size:13px;">laidadid21@gmail.com</code>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# محرك بناء مستندات الـ PDF الثلاثية الموجهة للمؤسسات (SMEs Executive Proposal)
# ==========================================
pdf_content = """
======================================================================
EXECUTIVE CORPORATE PROPOSAL: MULTI-TIER DIGITAL TRANSFORMATION
======================================================================
Provider: Law Firm Digital (LFD) | Maître Adid Al-Eid
Target Sector: Small & Medium Enterprises (SMEs) & Private Corporations
Strategic Philosophy: [God + Human + Machine] | Objective: Zero Paper 

1. OPERATIONAL ROADMAP: (Plan, Monitor, Repair / خطة، متابعة، تصليح)
- Comprehensive workflow deconstruction to discover systemic gaps.
- Real-time monitoring infrastructure utilizing n8n, Airtable & Google Drive.
- Continuous algorithmic diagnostic patches for complete operational security.

2. DIGITAL TRANSFORMATION MODES:
- Partial Digitalization (رقمنة جزئية): Gradual migration of core transactional nodes.
- Total Digitalization (رقمنة كلية): 100% comprehensive and paperless automation.
- Local Infrastructure (رقمنة محلية): Deployment of secure offline LLMs (Ollama Hub) for total data privacy.
- Cloud Infrastructure (رقمنة سحابية): Highly efficient and scalable cloud pipelines with encrypted APIs.
======================================================================
"""

# ==========================================
# البيئة الأولى: واجهة العرض والتسويق الرقمي الفاخرة (العملاء والمؤسسات)
# ==========================================
if app_mode == "🌐 Client Interface":
    # تصحيح تشوه العنوان العلوي (المنطقة الكبرى المحاطة بالحيز الأحمر) وجعله متناسقاً وثابتاً
    st.markdown(f"""
    <div class="directional-box">
        <h1 style="font-size: 40px; font-weight: 900; background: linear-gradient(to left, #3b82f6, #60a5fa, #10b981); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 5px;">
            {t['title']}
        </h1>
        <h3 style="font-size: 20px; color: #cbd5e1; font-weight: 400; margin-top:0; margin-bottom:10px;">
            {t['tagline']}
        </h3>
        <p style="font-size: 15px; color: #64748b; margin: 0 auto; max-width: 800px;">
            {t['subtitle']}
        </p>
    </div>
    """, unsafe_allow_html=True)

    # زر التحميل الفوري للمقترح التنفيذي (PDF المستند القصير) المترجم للمؤسسات
    st.columns([1, 2, 1])[1].download_button(
        label=t["download_btn"],
        data=pdf_content,
        file_name="Law_Firm_Digital_SME_Architecture.txt",
        mime="text/plain",
        use_container_width=True
    )
    
    st.divider()

    # محرك التصفح ثلاثي الأبعاد المتكامل والنشط لـ 6 منتجات كبرى للإشهار المتقدم
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
    
    # شبكة العرض والبيع الواسعة والمكونة من 6 بطاقات احترافية لملء أسفل الشاشة ومنع الفراغات
    st.markdown("<h3 style='color:#60a5fa; font-weight:700;'>🔥 الحلول الرقمية التنافسية المتوفرة حالياً</h3>", unsafe_allow_html=True)
    
    row1_c1, row1_c2, row1_c3 = st.columns(3)
    row2_c1, row2_c2, row2_c3 = st.columns(3)
    
    with row1_c1:
        st.markdown(f'<div class="premium-card"><span class="card-tag">{t["prod_tag_1"]}</span><h4 style="color:#ffffff;">{t["prod_title_1"]}</h4><div class="card-price">$249.99</div></div>', unsafe_allow_html=True)
    with row1_c2:
        st.markdown(f'<div class="premium-card"><span class="card-tag">{t["prod_tag_2"]}</span><h4 style="color:#ffffff;">{t["prod_title_2"]}</h4><div class="card-price">$642.23</div></div>', unsafe_allow_html=True)
    with row1_c3:
        st.markdown(f'<div class="premium-card"><span class="card-tag">{t["prod_tag_3"]}</span><h4 style="color:#ffffff;">{t["prod_title_3"]}</h4><div class="card-price">$525.20</div></div>', unsafe_allow_html=True)
        
    with row2_c1:
        st.markdown(f'<div class="premium-card"><span class="card-tag">{t["prod_tag_4"]}</span><h4 style="color:#ffffff;">{t["prod_title_4"]}</h4><div class="card-price">$999.00</div></div>', unsafe_allow_html=True)
    with row2_c2:
        st.markdown(f'<div class="premium-card"><span class="card-tag">{t["prod_tag_5"]}</span><h4 style="color:#ffffff;">{t["prod_title_5"]}</h4><div class="card-price">$450.00</div></div>', unsafe_allow_html=True)
    with row2_c3:
        st.markdown(f'<div class="premium-card"><span class="card-tag">{t["prod_tag_6"]}</span><h4 style="color:#ffffff;">{t["prod_title_6"]}</h4><div class="card-price">$1,200.00</div></div>', unsafe_allow_html=True)

    st.divider()
    
    # منطقة المراقبة والإغلاق الفوري للصفقات أسفل الصفحة
    col_v, col_w = st.columns([1.8, 1.2])
    with col_v:
        st.markdown("<h4 style='color:#ffffff;'>🎥 استعراض كفاءة البنية والتشغيل الذكي</h4>", unsafe_allow_html=True)
        st.video("https://www.youtube.com/watch?v=Adg8_6vC63g")
    with col_w:
        st.markdown(f"<h4 style='color:#ffffff;'>{t['contact_title']}</h4>", unsafe_allow_html=True)
        st.markdown(f"""
        <div class="premium-card" style="height:auto; padding:25px;">
            <p style='font-size:13px; color:#94a3b8; margin-top:0;'>بوابة توجيه حركة المرور والمشترين متصلة تلقائياً بنظام الأتمتة المحلي وجداول البيانات لإشعارات العمولات الفورية.</p>
            <a href="https://wa.me/213671816346" target="_blank" class="whatsapp-btn">{t['whatsapp_text']}</a>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# البيئة الثانية: حصن التحكم والإدارة (مخفية للخصوصية السيادية)
# ==========================================
elif app_mode == "🔒 System Control":
    st.markdown("## 🔒 Sovereign Control Room")
    if "auth" not in st.session_state:
        st.session_state["auth"] = False
        
    pwd = st.text_input("Enter Master Security Password:", type="password")
    if st.button("Authorize Connection"):
        if pwd == "0000":
            st.session_state["auth"] = True
            st.rerun()
            
    if st.session_state["auth"]:
        st.success("Secure Pipeline Link Established via Local Webhooks.")
        st.info("System linked to operational nodes and database tracking.")
