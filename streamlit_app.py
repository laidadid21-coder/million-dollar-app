import streamlit as st
import streamlit.components.v1 as components

# 1. إعدادات المنصة الموسعة فائقة الأداء لقسم السيادة
st.set_page_config(
    page_title="Sovereign Tech OS v4.0 | مكتب عديد العيد",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. نظام إدارة اللغات الثلاثية (عربي - English - Français)
if "lang" not in st.session_state:
    st.session_state["lang"] = "العربية"

# محتوى النصوص المترجمة لضمان التوافق العالمي واقتناص الصفقات
translations = {
    "العربية": {
        "title": "مكتب المحامي عديد العيد - الرقمنة القانونية والتجارية الشاملة",
        "subtitle": "عصر الورق انتهى. تصفح حلول الأتمتة والسيادة الرقمية عبر السحب 3D.",
        "download_btn": "📥 تحميل العرض التنفيذي للمؤسسات (PDF)",
        "contact_title": "📞 مركز التواصل والعمولات",
        "whatsapp_text": "💬 تواصل معنا فوراً عبر WhatsApp",
        "admin_title": "🔒 حصن الإدارة والسيطرة الشاملة",
        "admin_desc": "إدارة الأجهزة والمراقبة الأمنية والمالية وتحديث الخطط.",
        "prod_tag_1": "العروض الفائقة", "prod_title_1": "نظام أتمتة العقود الذكية للشركات",
        "prod_tag_2": "عروض الحزمة", "prod_title_2": "مستودعات أتمتة n8n وجداول Airtable",
        "prod_tag_3": "تخفيض 50%", "prod_title_3": "جلسة هندسة عكسية وتدقيق البنية التحتية",
        "prod_tag_4": "السيادة المحلية", "prod_title_4": "نظام أتمتة السيرفرات المحلية (Ollama Hub)",
        "prod_tag_5": "التسويق الآلي", "prod_title_5": "محرك جني عمولات السوشيال ميديا (Arbitrage)",
        "prod_tag_6": "الإشهار الموسع", "prod_title_6": "حزمة ترقية المؤسسات الصغيرة والمتوسطة"
    },
    "English": {
        "title": "Adid Al-Eid Law Firm - Comprehensive Legal & Tech Digitalization",
        "subtitle": "The paper era is over. Swipe and browse our modern automation solutions in 3D.",
        "download_btn": "📥 Download Corporate Executive Proposal (PDF)",
        "contact_title": "📞 Conversion & Commission Center",
        "whatsapp_text": "💬 Contact Us Instantly via WhatsApp",
        "admin_title": "🔒 Sovereign Admin Fortress",
        "admin_desc": "Manage hardware, monitor security/finances, and inject new plans.",
        "prod_tag_1": "Mega Deals", "prod_title_1": "Smart Contracts Automation System for Enterprises",
        "prod_tag_2": "Bundle Offer", "prod_title_2": "Sovereign n8n Ecosystem & Airtable Architectures",
        "prod_tag_3": "50% OFF", "prod_title_3": "Reverse Engineering & Infrastructure Auditing Session",
        "prod_tag_4": "Local Sovereignty", "prod_title_4": "On-Premise Offline AI System (Ollama Hub)",
        "prod_tag_5": "Automated Marketing", "prod_title_5": "Social Media Affiliate Commission Arbitrage Engine",
        "prod_tag_6": "SME Scaling", "prod_title_6": "Digital Transformation Package for SMEs"
    },
    "Français": {
        "title": "Cabinet Adid Al-Eid - Digitalisation Juridique & Tech Globale",
        "subtitle": "L'ère du papier est révolue. Naviguez dans nos solutions d'automatisation en 3D.",
        "download_btn": "📥 Télécharger la Proposition Exécutive (PDF)",
        "contact_title": "📞 Centre de Conversion & Commissions",
        "whatsapp_text": "💬 Contactez-nous Instantanément via WhatsApp",
        "admin_title": "🔒 Forteresse Admin Souveraine",
        "admin_desc": "Gérer le matériel, surveiller la sécurité/finances et injecter des plans.",
        "prod_tag_1": "Offres Flash", "prod_title_1": "Système d'Automatisation des Contrats Intelligents",
        "prod_tag_2": "Pack Solution", "prod_title_2": "Écosystème Souverain n8n & Tables Airtable",
        "prod_tag_3": "50% DE RABAIS", "prod_title_3": "Session d'Ingénierie Inverse & Audit d'Infrastructure",
        "prod_tag_4": "Souveraineté Locale", "prod_title_4": "Système IA Local Hors-Ligne (Ollama Hub)",
        "prod_tag_5": "Marketing Automatisé", "prod_title_5": "Moteur d'Arbitrage et de Commission Médias Sociaux",
        "prod_tag_6": "Optimisation PME", "prod_title_6": "Pack de Transformation Digitale pour PME/PMI"
    }
}

t = translations[st.session_state["lang"]]

# 3. هندسة التصميم البصري الخارق (CSS المتقدم للواجهة الداكنة والنيون)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    * { font-family: 'Cairo', sans-serif; }
    .main { background-color: #0b0f19; color: #f8fafc; }
    
    /* تنسيق اللوجو الدائري المطور من صورة المعاملة */
    .logo-container { text-align: center; margin-bottom: 15px; }
    .logo-img { width: 130px; border-radius: 50%; border: 3px solid #3b82f6; box-shadow: 0 0 20px rgba(59, 130, 246, 0.5); }
    
    /* بطاقات المنتجات الممتدة بملء الشاشة */
    .premium-card {
        background: linear-gradient(145deg, #111827, #1f2937);
        border: 1px solid #374151;
        border-radius: 20px;
        padding: 22px;
        box-shadow: 0 12px 30px rgba(0, 0, 0, 0.4);
        transition: all 0.4s ease;
        text-align: center;
        margin-bottom: 20px;
    }
    .premium-card:hover {
        transform: translateY(-5px);
        border-color: #3b82f6;
        box-shadow: 0 15px 35px rgba(59, 130, 246, 0.2);
    }
    .card-price { color: #10b981; font-size: 24px; font-weight: bold; margin: 10px 0; font-family: monospace; }
    .card-tag { background-color: #1e293b; color: #3b82f6; padding: 4px 12px; border-radius: 8px; font-size: 12px; font-weight: bold; display: inline-block; margin-bottom: 10px; }
    
    .whatsapp-btn {
        background: linear-gradient(135deg, #25D366 0%, #128C7E 100%);
        color: white !important; text-align: center !important; padding: 12px; border-radius: 30px;
        display: block; font-weight: bold; text-decoration: none; box-shadow: 0 5px 15px rgba(37, 211, 102, 0.3);
    }
    </style>
""", unsafe_allow_html=True)

# 4. لوحة التحكّم والاتصال الجانبية الذكية ومحدد اللغات
with st.sidebar:
    st.markdown("<div class='logo-container'>", unsafe_allow_html=True)
    # استخدام الرابط المباشر لشعار LAW-FIRM-DIGITAL المتطابق تماماً مع صورة المجلد المرفوع image_e97984.jpg
    st.image("https://i.ibb.co/6R2NfWh/image-e97984.jpg", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.session_state["lang"] = st.selectbox("🌐 تدويل النظام / Select Language / Langue:", ["العربية", "English", "Français"])
    st.write(f"📧 `laidadid21@gmail.com`")
    st.divider()
    
    app_mode = st.radio("البيئة التشغيلية / Interface Mode:", ["🌐 Client Display", "🔒 Sovereign Control"])

# ==========================================
# محرك بناء مستندات PDF الاستراتيجية الثلاثية للمؤسسات الكبرى (SMEs Summary)
# ==========================================
pdf_content = """
==================================================
EXECUTIVE PROPOSAL: DIGITAL TRANSFORMATION & AUTOMATION
==================================================
Provider: Law Firm Digital - Maître Adid Al-Eid
Target: Small & Medium Enterprises (SMEs)
Core Protocol: Zero Paper - Human + Machine Integration

1. STRATEGIC ROADMAP: (Plan, Monitor, Repair)
- Deconstruct manual workflows.
- Implement real-time monitoring structures via Airtable & Google Sheets.
- Real-time continuous diagnostics and algorithmic error patches.

2. TRANSFORMATION MODES:
- Partial Digitalization: Gradual transition of core transaction nodes.
- Total Digitalization: 100% Comprehensive paperless transformation.
- On-Premise Infrastructure: Secure offline servers (Ollama/Llama) for absolute data sovereignty.
- Cloud Infrastructure: Secure cloud-based automated pipelines using n8n and encrypted APIs.
==================================================
"""

# ==========================================
# البيئة الأولى: واجهة العرض العامة والتسويقية (6+ منتجات مع عرض ثلاثي الأبعاد)
# ==========================================
if app_mode == "🌐 Client Display":
    st.markdown(f"<h1 style='text-align: center; font-weight: 900; color: #3b82f6;'>{t['title']}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; font-size: 18px; color: #94a3b8;'>{t['subtitle']}</p>", unsafe_allow_html=True)
    st.divider()

    # زر تنزيل مستند PDF الموحد للمؤسسات باللغات الثلاث باختصار شديد
    st.download_button(
        label=t["download_btn"],
        data=pdf_content,
        file_name="Law_Firm_Digital_SME_Proposal.txt",
        mime="text/plain"
    )
    
    st.divider()
    
    # محرك التصفح ثلاثي الأبعاد المتكامل (3D Expanded Carousel) - يحتوي على كافة المنتجات لإبراز قوة الإشهار
    carousel_html = """
    <div style="direction: ltr; display: flex; justify-content: center; align-items: center; background: #0b0f19; padding: 20px 0; overflow: hidden;">
        <style>
            .container { width: 100%; max-width: 1100px; height: 320px; display: flex; gap: 15px; perspective: 1000px; }
            .card {
                flex: 1; height: 100%; border-radius: 15px; overflow: hidden; position: relative;
                transition: all 0.6s cubic-bezier(0.25, 1, 0.5, 1); cursor: pointer; border: 2px solid #374151;
            }
            .card:hover { flex: 3; transform: scale(1.01); border-color: #3b82f6; box-shadow: 0 15px 30px rgba(59,130,246,0.3); }
            .card img { width: 100%; height: 100%; object-fit: cover; }
            .card-info {
                position: absolute; bottom: 0; left: 0; right: 0; padding: 15px; text-align: right;
                background: linear-gradient(to top, rgba(0,0,0,0.9), transparent); color: white; opacity: 0; transition: 0.3s;
            }
            .card:hover .card-info { opacity: 1; }
        </style>
        <div class="container">
            <div class="card"><img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=500"><div class="card-info"><h3>Contrats Intelligents</h3><p>$249.99</p></div></div>
            <div class="card"><img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=500"><div class="card-info"><h3>n8n & Airtable Hub</h3><p>$642.23</p></div></div>
            <div class="card"><img src="https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=500"><div class="card-info"><h3>Auditing Sessions</h3><p>$525.20</p></div></div>
            <div class="card"><img src="https://images.unsplash.com/photo-1600132806370-bf17e65e942f?w=500"><div class="card-info"><h3>Local AI Ollama</h3><p>$999.00</p></div></div>
            <div class="card"><img src="https://images.unsplash.com/photo-1432888622747-4eb9a8efeb07?w=500"><div class="card-info"><h3>Arbitrage Engine</h3><p>$450.00</p></div></div>
            <div class="card"><img src="https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=500"><div class="card-info"><h3>SME Package</h3><p>$1,200.00</p></div></div>
        </div>
    </div>
    """
    components.html(carousel_html, height=360)
    
    st.divider()
    
    # شبكة العرض الفائقة الموسعة والمحدثة لـ 6 منتجات دون حذف أي منتج سابق لإثراء مساحة الإشهار
    st.markdown("### 🔥 مستودع الحلول والمنتجات الاستراتيجية")
    
    row1_c1, row1_c2, row1_c3 = st.columns(3)
    row2_c1, row2_c2, row2_c3 = st.columns(3)
    
    with row1_c1:
        st.markdown(f'<div class="premium-card"><span class="card-tag">{t["prod_tag_1"]}</span><h4>{t["prod_title_1"]}</h4><div class="card-price">$249.99</div></div>', unsafe_allow_html=True)
    with row1_c2:
        st.markdown(f'<div class="premium-card"><span class="card-tag">{t["prod_tag_2"]}</span><h4>{t["prod_title_2"]}</h4><div class="card-price">$642.23</div></div>', unsafe_allow_html=True)
    with row1_c3:
        st.markdown(f'<div class="premium-card"><span class="card-tag">{t["prod_tag_3"]}</span><h4>{t["prod_title_3"]}</h4><div class="card-price">$525.20</div></div>', unsafe_allow_html=True)
        
    with row2_c1:
        st.markdown(f'<div class="premium-card"><span class="card-tag">{t["prod_tag_4"]}</span><h4>{t["prod_title_4"]}</h4><div class="card-price">$999.00</div></div>', unsafe_allow_html=True)
    with row2_c2:
        st.markdown(f'<div class="premium-card"><span class="card-tag">{t["prod_tag_5"]}</span><h4>{t["prod_title_5"]}</h4><div class="card-price">$450.00</div></div>', unsafe_allow_html=True)
    with row2_c3:
        st.markdown(f'<div class="premium-card"><span class="card-tag">{t["prod_tag_6"]}</span><h4>{t["prod_title_6"]}</div></div>', unsafe_allow_html=True)

    st.divider()
    
    col_v, col_w = st.columns([2, 1])
    with col_v:
        st.video("https://www.youtube.com/watch?v=Adg8_6vC63g")
    with col_w:
        st.markdown(f"### {t['contact_title']}")
        st.markdown(f"""
        <div class="premium-card">
            <p style='font-size:14px; color:#94a3b8;'>الربط المباشر ببوابة الأتمتة واستقبال طلبات تراخيص الأنظمة مفعّل بالكامل.</p>
            <a href="https://wa.me/213671816346" target="_blank" class="whatsapp-btn">{t['whatsapp_text']}</a>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# البيئة الثانية: حصن القيادة والتحكم المشفر للإدارة
# ==========================================
elif app_mode == "🔒 Sovereign Control":
    st.markdown(f"## {t['admin_title']}")
    st.write(t["admin_desc"])
    
    if "auth" not in st.session_state:
        st.session_state["auth"] = False
        
    pwd = st.text_input("Master Password:", type="password")
    if st.button("Unlock Dashboard"):
        if pwd == "0000":
            st.session_state["auth"] = True
            st.rerun()
            
    if st.session_state["auth"]:
        st.success("Access Granted to Drive + Sheets + n8n Pipelines.")
        st.info(f"All tracking data and automation triggers are linked directly to: laidadid21@gmail.com")
