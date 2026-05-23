import streamlit as st

# 1. إعدادات الصفحة والجمالية العالمية
st.set_page_config(
    page_title="Global Sales Nexus | مكتب عديد العيد",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# تصميم واجهة مستخدم مخصصة باستخدام CSS خفيف لتفادي المظهر التقليدي
st.markdown("""
    <style>
    .main { background-color: #fafafa; }
    .stButton>button { width: 100%; background-color: #1E3A8A; color: white; border-radius: 8px; font-weight: bold; }
    .stTabs [data-baseweb="tab"] { font-size: 16px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# 2. القائمة الجانبية (Sidebar) - إعدادات التاجر والسيادة
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=80)
    st.title("⚙️ النظام التشغيلي")
    st.subheader("بروتوكول السيطرة والربحية")
    
    product_type = st.radio("📦 طبيعة الأصل التجاري:", ["منتج رقمي (Digital)", "منتج مادي (Physical)"])
    target_regions = st.multiselect("🌍 النطاق الجغرافي المستهدف:", ["الجزائر", "الخليج العربي", "أوروبا", "أمريكا الشمالية"])
    
    st.divider()
    st.caption("📜 **بند السيادة:** مكتب المحامي عديد العيد - تحويل العمل النظري إلى تطبيق حقيقي مدر للمال والعمولات.")

# 3. الهيكل الرئيسي للمنصة العالمية
st.title("🌐 بوابة التاجر العالمي والتحول الرقمي الشامل")
st.markdown("### نظام إدارة الأصول الرقمية، أتمتة التسويق، واقتناص عمولات السوق")

# تقسيم المنصة إلى 4 بوابات تفاعلية ذكية (Tabs) لجودة متناهية
tab_product, tab_marketing, tab_orders, tab_analytics = st.tabs([
    "📦 إدارة وتصوير المنتجات", 
    "📣 هندسة التسويق الرقمي", 
    "🛒 تأكيد وتدقيق الطلبيات", 
    "📊 لوحة أرباح المليون دولار"
])

# ----------------------------------------------------------------
# التبويب الأول: إدارة وتصوير المنتجات (خيارات متقدمة وخانة تغيير الصور)
# ----------------------------------------------------------------
with tab_product:
    st.subheader("📝 تفاصيل وثراء خيارات المنتج")
    
    col_p1, col_p2 = st.columns([2, 1])
    
    with col_p1:
        product_name = st.text_input("🏷️ اسم المنتج الاستراتيجي / الخدمة القانونية الرقمية:", placeholder="مثال: نظام أتمتة العقود الذكية للشركات")
        
        # ميزات المنتج المتقدمة (مجموعة من الاختيارات في كل منتج)
        col_sub1, col_sub2 = st.columns(2)
        with col_sub1:
            category = st.selectbox("🗂️ تصنيف فئة المنتج:", ["Legal Tech Consulting", "Automation JSON Workflows", "Digital Products", "AI Content Arbitrage"])
            access_type = st.selectbox("🔑 نوع رخصة الوصول:", ["ترخيص دائم مدى الحياة", "اشتراك سنوي سحابي", "حقوق إعادة البيع الكاملة PLR"])
        with col_sub2:
            support_level = st.selectbox("🛠️ مستوى الدعم التقني الملحق:", ["دعم آلي 100% عبر الذكاء الاصطناعي", "دعم مخصص (بشري + آلة)", "بدون دعم (منتج جاهز للنشر)"])
            delivery_speed = st.selectbox("⚡ سرعة التسليم للعميل:", ["تسليم فوري تلقائي الفورية", "خلال 24 ساعة بعد التدقيق"])
            
        description = st.text_area("📄 وصف القيمة المضافة والثغرة التي يستغلها المنتج في السوق:")
        
    with col_p2:
        st.write("📸 **مركز إدارة الصور والهوية البصرية**")
        # خانة تصوير وتغيير المنتج
        uploaded_image = st.file_uploader("قم برفع أو تغيير صورة المنتج هنا للتحقق من جودة العرض:", type=["png", "jpg", "jpeg"])
        
        if uploaded_image is not None:
            st.image(uploaded_image, caption="المعاينة الحية للأصل الرقمي المرفوع", use_container_width=True)
            st.success("✅ تم دمج الهوية البصرية بنجاح في السيرفر.")
        else:
            st.warning("⚠️ في انتظار رفع صورة المنتج أو الشعار الرسمي لتغيير المظهر البدائي.")

# ----------------------------------------------------------------
# التبويب الثاني: هندسة التسويق الرقمي وعناوينها
# ----------------------------------------------------------------
with tab_marketing:
    st.subheader("📣 قنوات التسويق الرقمي والمنصات الوسيطة لتحويل المعلومة إلى عمولة")
    
    col_m1, col_m2 = st.columns(2)
    
    with col_m1:
        st.write("🔗 **تحديد المنصات الوسيطة وحملات النشر المستهدفة:**")
        selected_platforms = st.multiselect(
            "اختر منصات التسويق لتوليد سيناريو النشر التلقائي عبرها:",
            ["تيك توك (TikTok Arbitrage)", "فايسبوك (Facebook Ads & Groups)", "لينكدين (LinkedIn B2B Contracts)"]
        )
        
        ad_strategy = st.radio("🎯 استراتيجية تدفق الإعلانات:", ["إعلانات ممولة ذات عائد فوري", "صناعة محتوى فيروسي (Organic Viral Content)"])
        base_price = st.number_input("💰 سعر البيع المقترح للاستهداف (بالدولار):", min_value=0.0, value=250.0)

    with col_m2:
        st.write("📋 **عناوين الحملات ونصوص التسويق المقترحة (أتمتة المحتوى):**")
        if selected_platforms:
            st.info("💡 **نظام توليد العناوين التسويقية يعمل الآن:**")
            if "تيك توك (TikTok Arbitrage)" in selected_platforms:
                st.code("عنوان تيك توك: كيف تدير شركتك بنظام (صفر ورقة) في 2026 آلياً؟ شاهد الرابط!", language="text")
            if "لينكدين (LinkedIn B2B Contracts)" in selected_platforms:
                st.code("عنوان لينكدين: تقليص النفقات القانونية بنسبة 80% باستخدام أنظمة الـ LegalTech السحابية المستدامة.", language="text")
            if "فايسبوك (Facebook Ads & Groups)" in selected_platforms:
                st.code("عنوان فايسبوك: لأصحاب المشاريع الرقمية, احصل على خطتك السيادية القانونية بضغطة زر واحدة.", language="text")
        else:
            st.write("*يرجى اختيار منصة تسويقية واحدة على الأقل لتوليد عناوينها وحملاتها المخصصة تلقائياً.*")

# ----------------------------------------------------------------
# التبويب الثالث: تأكيد وتدقيق الطلبيات (نظام الحماية والربط العملي)
# ----------------------------------------------------------------
with tab_orders:
    st.subheader("🛒 نظام تأكيد وثبات الطلبيات الواردة للمنصة")
    
    col_o1, col_o2 = st.columns([1, 2])
    
    with col_o1:
        st.write("🔒 **بيانات تأكيد المشتري:**")
        client_name = st.text_input("اسم العميل أو الشركة المتعاقدة:")
        client_email = st.text_input("البريد الإلكتروني للعميل لربطه بـ Gmail:")
        payment_status = st.selectbox("📊 حالة الدفع والتحويل المالي:", ["تم استلام الأموال بنجاح", "في انتظار التأكيد البنكي", "فشل الدفع - إلغاء تلقائي"])
        
        # خانة تأكيد الطلبيات الفورية
        confirm_order = st.checkbox("أقر أنا التاجر بتأكيد هذه الطلبية وبدء التفعيل الفوري للأتمتة")
        
    with col_o2:
        st.write("🛠️ **إجراءات المعالجة التنفيذية (نظام n8n المتوقع):**")
        if confirm_order and product_name and client_name:
            st.success(f"🔥 **تم تفعيل أمر التأكيد بنجاح!**")
            st.json({
                "الحالة": "جاهز للتمرير السحابي",
                "المنتج": product_name,
                "العميل": client_name,
                "قناة التسويق المستغلة": selected_platforms if selected_platforms else "مباشر",
                "مسار الأتمتة المستهدف": "Google Drive ➔ Gemini ➔ Airtable ➔ Gmail"
            })
            st.button("⚡ دفع البيانات فوراً لـ Airtable وتحصيل العمولات")
        else:
            st.info("⚡ *بمجرد ملء البيانات والضغط على خانة (أقر أنا التاجر بتأكيد هذه الطلبية)، سيقوم النظام ببناء ملف معالجة رقمي فوري يمنع التداخل الورقي نهائياً.*")

# ----------------------------------------------------------------
# التبويب الرابع: لوحة أرباح المليون دولار (إبداع إضافي لكسر الجمود)
# ----------------------------------------------------------------
with tab_analytics:
    st.subheader("📊 المحاكي الذكي للأرباح والعمولات المستهدفة")
    st.markdown("---")
    
    col_a1, col_a2, col_a3 = st.columns(3)
    with col_a1:
        st.metric(label="🎯 الهدف الاستراتيجي المستهدف", value="$1,000,000", delta="رؤية التحول الشامل")
    with col_a2:
        estimated_sales = st.slider("حدد عدد المبيعات المتوقعة شهرياً عبر الحملات المذكورة:", 1, 1000, 50)
        calculated_revenue = estimated_sales * base_price
    with col_a3:
        st.metric(label="💰 العوائد الإجمالية المتوقعة للمنتج الحالي", value=f"${calculated_revenue:,.2f}", delta=f"بمعدل سعر ${base_price}")
        
    st.markdown("---")
    st.info("🚀 **ملاحظة المستشار التقني:** تم بناء هذا النموذج متعدد الأبعاد والمزايا لإلغاء أي طابع بدائي وتوفير واجهة تفاعلية ذات جودة مستخدم (UX) فائقة الجودة وجاهزة للتسويق المباشر.")
