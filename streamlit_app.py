import streamlit as st

# 1. إعدادات المنصة بملء الشاشة المتقدم
st.set_page_config(
    page_title="Sovereign Automation Hub | مكتب عديد العيد",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. هندسة التصميم البصري (CSS المتقدم لإلغاء النمط البدائي)
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    h1, h2, h3 { font-family: 'Cairo', sans-serif; text-align: right; color: #0f172a; }
    
    /* بنر القضاء على الفوضى الورقية */
    .hero-banner {
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        color: white;
        padding: 45px;
        border-radius: 16px;
        text-align: right;
        margin-bottom: 35px;
        box-shadow: 0 10px 25px rgba(59, 130, 246, 0.15);
    }
    .hero-banner h1 { color: white; font-size: 36px; font-weight: 800; margin: 0; }
    .hero-banner p { font-size: 18px; margin-top: 12px; opacity: 0.9; }
    
    /* بطاقات الأنظمة والمخططات */
    .workflow-card {
        background-color: white;
        border-radius: 14px;
        padding: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.02);
        border: 1px solid #e2e8f0;
        text-align: right;
        margin-bottom: 25px;
        transition: all 0.3s ease;
    }
    .workflow-card:hover { transform: translateY(-5px); box-shadow: 0 12px 25px rgba(0,0,0,0.06); }
    .price-tag { color: #ef4444; font-size: 24px; font-weight: 700; margin: 12px 0; font-family: sans-serif; }
    .system-status { background-color: #e2fbe8; color: #15803d; padding: 4px 10px; border-radius: 6px; font-size: 12px; font-weight: bold; display: inline-block; }
    
    /* أزرار التشغيل والطلب */
    .stButton>button {
        background-color: #1e3a8a !important;
        color: white !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        padding: 10px !important;
        width: 100%;
    }
    .stButton>button:hover { background-color: #2563eb !important; }
    </style>
""", unsafe_allow_html=True)

# 3. لوحة التحكم الجانبية لإدارة البيانات النشطة
with st.sidebar:
    st.header("🛠️ مركز إدارة البنية التحتية")
    st.write("تحرير بيانات الواجهة وتغذية محرك n8n سحابياً.")
    dynamic_title = st.text_input("عنوان النظام المخصص:", value="نظام التحليل الآلي للفرص والعقود الاستثمارية")
    dynamic_price = st.number_input("سعر الترخيص والتنفيذ (USD):", min_value=0.0, value=499.00)
    st.divider()
    uploaded_flow_img = st.file_uploader("📸 رفع لقطة شاشة لمخطط n8n لتحديث المعرض محلياً:", type=["png", "jpg", "jpeg"])

# 4. محتوى واجهة العرض الرئيسية
st.markdown("""
    <div class="hero-banner">
        <h1>من الفوضى المكتبية إلى الرقمنة الشاملة ⚡</h1>
        <p>الجيل الجديد من أنظمة تشغيل المكاتب القانونية والتجارية • بروتوكول 2026 (صفر ورقة)</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("## 🤖 مستودع محركات الأتمتة السيادية (n8n Workflows)")
st.markdown("تحويل العمل النظري والمعلومات المتدفقة إلى عوائد وعمولات مؤتمتة بالكامل بدون أي تدخل ورقي.")
st.markdown("---")

# بناء شبكة العرض (Grid) باستخدام 3 أعمدة لعرض الأنظمة والمخططات
col1, col2, col3 = st.columns(3)

# --- النظام الأول: نظام تحليل وتصنيف الفرص (AI Opportunity Analyzer) ---
with col1:
    st.markdown('<div class="workflow-card">', unsafe_allow_html=True)
    st.markdown('<span class="system-status">نشط ومستقر • Active</span>', unsafe_allow_html=True)
    
    # إذا قام المستخدم برفع صورة مخصصة من السايدبار يتم عرضها، وإلا يعرض صورة توضيحية لنظام المحرك الأول
    if uploaded_flow_img is not None:
        st.image(uploaded_flow_img, use_container_width=True)
    else:
        # صورة تمثيلية دقيقة لغرفة محرك الويب هوك والذكاء الاصطناعي (مستوحاة من image_e81c6b.png)
        st.image("https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=500", caption="مخطط التدفق الرقمي: Webhook -> AI Classifier", use_container_width=True)
        
    st.markdown(f'### {dynamic_title}')
    st.markdown("محرك متطور يستقبل البيانات عبر الـ Webhook ويقوم بتشغيل نماذج الذكاء الاصطناعي لفرز الفرص الثمينة وإرسال تنبيهات فورية عبر Gmail والتقويم تلقائياً.")
    st.markdown(f'<div class="price-tag">${dynamic_price:,.2f}</div>', unsafe_allow_html=True)
    
    if st.button("⚡ تفعيل البنية التحتية", key="flow_1"):
        st.success("✅ أرسل النظام إشارة النبض السحابية لبيئة n8n الجاهزة! تم الربط.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- النظام الثاني: نظام الأرشفة التلقائية وتطهير السحابة (Google Drive Cloud Cleaner) ---
with col2:
    st.markdown('<div class="workflow-card">', unsafe_allow_html=True)
    st.markdown('<span class="system-status">جاهز للنشر • Ready</span>', unsafe_allow_html=True)
    
    # صورة تمثيلية لنظام أتمتة السجلات والتحكم السحابي في الملفات (مستوحاة من image_e81fea.png)
    st.image("https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=500", caption="مخطط الأتمتة: Cloud Drive Automation Nexus", use_container_width=True)
    
    st.markdown("### نظام التطهير والأرشفة الرقمية المستدامة")
    st.markdown("تطبيق عملي لمبدأ (صفر ورقة). يقوم النظام بمراقبة المجلدات المحلية، تحويل الصيغ إلى JSON، فرز وتصنيف الملفات وتحديث قواعد البيانات مع حذف المجلدات القديمة آلياً.")
    st.markdown('<div class="price-tag">$750.00</div>', unsafe_allow_html=True)
    
    if st.button("⚡ تفعيل البنية التحتية", key="flow_2"):
        st.info("🔄 جاري مزامنة المجلدات المحلية مع نظام الأتمتة المركزي...")
    st.markdown('</div>', unsafe_allow_html=True)

# --- النظام الثالث: نظام المراقبة واقتناص عمولات التسويق (Arbitrage Marketing Engine) ---
with col3:
    st.markdown('<div class="workflow-card">', unsafe_allow_html=True)
    st.markdown('<span class="system-status">قيد المراقبة • Monitoring</span>', unsafe_allow_html=True)
    
    # صورة تمثيلية للوحات المراقبة وتحليل تدفقات المال والعمولات الرقمية
    st.image("https://images.unsplash.com/photo-1551836022-d5d88e9218df?w=500", caption="مخطط الرقابة: Market Arbitrage Loop", use_container_width=True)
    
    st.markdown("### محرك أتمتة التسويق الرقمي وجني العمولات الوسيطة")
    st.markdown("نظام سحابي متكامل يربط بين المنصات الوسيطة (تيك توك، فايسبوك، لينكدين) لتحويل المنشورات والعناوين الترويجية إلى تدفق مالي مباشر وتأكيد طلبيات العملاء آلياً.")
    st.markdown('<div class="price-tag">$890.00</div>', unsafe_allow_html=True)
    
    if st.button("⚡ تفعيل البنية التحتية", key="flow_3"):
        st.success("🔥 تم تشغيل محرك اقتناص العمولات! البيانات تتدفق إلى Airtable.")
    st.markdown('</div>', unsafe_allow_html=True)

# تذييل المنصة الاحترافي
st.markdown("---")
st.markdown("<p style='text-align: center; color: #64748b;'>🔒 السيادة الكاملة للبيانات • تم التطوير بواسطة الأنظمة التشغيلية الذكية لمكتب المحامي عديد العيد</p>", unsafe_allow_html=True)
