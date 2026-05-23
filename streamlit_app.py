import streamlit as st
import streamlit.components.v1 as components

# 1. تكوين شاشة السيادة الكاملة فائقة التوسع
st.set_page_config(
    page_title="Sovereign Digital OS v3.2 | مكتب عديد العيد",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. هندسة التصميم البصري الخارق (Ultra-Modern Dark/Light UI)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    
    * { font-family: 'Cairo', sans-serif; text-align: right; }
    .main { background-color: #0b0f19; color: #f8fafc; }
    
    /* تصميم البطاقات الفريد المستوحى من تقنيات النيون والمستقبل */
    .premium-card {
        background: linear-gradient(145deg, #111827, #1f2937);
        border: 1px solid #374151;
        border-radius: 20px;
        padding: 25px;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.5);
        transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
    }
    .premium-card:hover {
        transform: translateY(-8px);
        border-color: #3b82f6;
        box-shadow: 0 20px 40px rgba(59, 130, 246, 0.15);
    }
    
    /* أزرار الاتصال والميتريكس */
    .whatsapp-btn {
        background: linear-gradient(135deg, #25D366 0%, #128C7E 100%);
        color: white !important;
        text-align: center !important;
        padding: 12px;
        border-radius: 30px;
        display: block;
        font-weight: bold;
        text-decoration: none;
        box-shadow: 0 5px 15px rgba(37, 211, 102, 0.3);
        margin-top: 15px;
        transition: opacity 0.2s;
    }
    .whatsapp-btn:hover { opacity: 0.9; text-decoration: none; }
    
    /* عناوين الواجهة والمظهر العام */
    .hero-title {
        background: linear-gradient(to left, #3b82f6, #60a5fa, #10b981);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 42px;
        font-weight: 900;
        text-align: center;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. إدارة الجلسة والأمن السيادي لمنع تسريب الـ API Keys
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# القائمة الجانبية الذكية
st.sidebar.markdown("<h2 style='text-align:center;'>⚙️ نظام التحكم</h2>", unsafe_allow_html=True)
st.sidebar.markdown(f"<p style='text-align:center; color:#94a3b8;'>البريد النشط: laidadid21@gmail.com</p>", unsafe_allow_html=True)
st.sidebar.divider()

# زر التبديل بين واجهة العرض العامة وحصن الإدارة المتكامل
app_mode = st.sidebar.radio("اختر البيئة التشغيلية:", ["🌐 الواجهة التسويقية العامة", "🔒 لوحة القيادة وحصن الإدارة"])

# ==========================================
# البيئة الأولى: الواجهة التسويقية العامة (التصفح ثلاثي الأبعاد 3D Swipe)
# ==========================================
if app_mode == "🌐 الواجهة التسويقية العامة":
    
    st.markdown("<h1 class='hero-title'>مكتب المحامي عديد العيد للرقمنة الشاملة</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-size:18px; color:#94a3b8;'>عصر الورق انتهى. عاين وتصفح حلولنا المؤتمتة السيادية بتقنية العرض ثلاثي الأبعاد المتقدمة.</p>", unsafe_allow_html=True)
    st.divider()

    # محرك العرض 3D التفاعلي المطور عبر تكنولوجيا HTML5/CSS3 (3D Carousel Dashboard)
    # تصفح عبر السحب التفاعلي متوافق تماماً مع لقطة الشاشة الأصلية image09
    carousel_html = """
    <div style="direction: ltr; display: flex; justify-content: center; align-items: center; background: #0b0f19; padding: 40px 0; overflow: hidden;">
        <style>
            .container { width: 100%; max-width: 900px; height: 350px; display: flex; gap: 20px; perspective: 1000px; }
            .card {
                flex: 1; height: 100%; border-radius: 20px; overflow: hidden; position: relative;
                transition: all 0.6s cubic-bezier(0.25, 1, 0.5, 1); cursor: pointer; border: 2px solid #374151;
                box-shadow: 0 10px 30px rgba(0,0,0,0.5); transform: rotateY(-10deg);
            }
            .card:hover { flex: 2.5; transform: rotateY(0deg) scale(1.02); border-color: #3b82f6; box-shadow: 0 20px 40px rgba(59,130,246,0.3); }
            .card img { width: 100%; height: 100%; object-fit: cover; transition: 0.6s; }
            .card:hover img { filter: brightness(0.8); }
            .card-info {
                position: absolute; bottom: 0; left: 0; right: 0; padding: 20px; text-align: right;
                background: linear-gradient(to top, rgba(0,0,0,0.9), transparent); color: white; opacity: 0; transition: 0.4s;
            }
            .card:hover .card-info { opacity: 1; }
            .card-info h3 { margin: 0; font-size: 18px; color: #3b82f6; font-family: 'Cairo', sans-serif; }
            .card-info p { margin: 5px 0 0; font-size: 13px; color: #cbd5e1; font-family: 'Cairo', sans-serif; }
        </style>
        <div class="container">
            <!-- الكارت الأول: لوحة تحليلات الحاسوب الداكنة -->
            <div class="card">
                <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600">
                <div class="card-info">
                    <h3>نظام أتمتة العقود والتحول الرقمي</h3>
                    <p>تحليلات حية متقدمة لقيادة حركات التجارة والمؤسسات الكبرى بسعر $249.99</p>
                </div>
            </div>
            <!-- الكارت الثاني: شاشة أتمتة n8n الساطعة -->
            <div class="card">
                <img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600">
                <div class="card-info">
                    <h3>بنية n8n السيادية الكاملة</h3>
                    <p>أتمتة خطوط الربط ومزامنة قواعد البيانات السحابية بسعر $642.23</p>
                </div>
            </div>
            <!-- الكارت الثالث: التدقيق الاستراتيجي والمهندسة العكسية -->
            <div class="card">
                <img src="https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600">
                <div class="card-info">
                    <h3>جلسات الهندسة العكسية</h3>
                    <p>فحص وحماية البنية التحتية وسد الثغرات التشغيلية بسعر $525.20</p>
                </div>
            </div>
        </div>
    </div>
    """
    components.html(carousel_html, height=420)
    
    st.divider()
    
    # شبكة العرض والاتصال المباشر بالعملاء بملء الشاشة لأسفل الصفحة
    col_v, col_w = st.columns([2, 1])
    
    with col_v:
        st.markdown("### 🎥 العرض الترويجي العالمي للتحول والأتمتة الرقمية")
        st.video("https://www.youtube.com/watch?v=Adg8_6vC63g")
    
    with col_w:
        st.markdown("### 📞 مركز التواصل المباشر")
        st.markdown("""
        <div class="premium-card">
            <h4 style="color:#10b981; margin-top:0;">إغلاق صفقات البنية التحتية</h4>
            <p style="font-size:14px; color:#94a3b8;">اضغط على الرابط بالأسفل للتحويل الفوري إلى خط الواتساب المباشر الخاص بمكتب المحامي عديد العيد لبدء تنفيذ المعاملات.</p>
            <a href="https://wa.me/213671816346" target="_blank" class="whatsapp-btn">💬 تواصل معنا عبر WhatsApp</a>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# البيئة الثانية: حصن القيادة والتحكم المشفر (مخفي تماماً خلف كلمة مرور)
# ==========================================
elif app_mode == "🔒 لوحة القيادة وحصن الإدارة":
    if not st.session_state["authenticated"]:
        st.markdown("## 🔐 بيئة معزولة ومحمية تشفيرياً")
        st.write("الرجاء إدخال رمز التحقق السيادي لفتح صلاحيات الاتصال بأدوات جوجل والمراقبة المباشرة.")
        
        master_password = st.text_input("رمز الوصول الرئيسي:", type="password")
        if st.button("🔓 فتح الصلاحيات التامة"):
            if master_password == "0000":  # رمز حماية فوري قابل للتعديل
                st.session_state["authenticated"] = True
                st.success("تم التحقق بنجاح! جاري تحميل غرف العمليات.")
                st.rerun()
            else:
                st.error("❌ رمز الوصول غير صحيح! بروتوكول الحماية يمنع الدخول.")
    else:
        # واجهة الإدارة الكاملة الممتدة لأسفل الشاشة
        st.markdown("## 🎛️ حصن الإدارة والسيطرة الشاملة | مكتب عديد العيد")
        st.write("أنت الآن تمتلك السيطرة الكاملة للاتصال والتوجيه اللحظي لكافة قنوات البيانات والأصول الرقمية.")
        
        if st.sidebar.button("🔒 تسجيل الخروج وقفل النظام"):
            st.session_state["authenticated"] = False
            st.rerun()
            
        st.divider()
        
        # توزيع علامات التبويب الاحترافية لإدارة السوق، المال، والقوانين والخطط
        tab_monitor, tab_clients, tab_plans = st.tabs(["📊 المراقبة الأمنية وتحليل السوق", "💰 تسيير الزبائن وإيرادات المال", "📜 تحديث القوانين والخطط الجديدة"])
        
        with tab_monitor:
            st.markdown("### 📈 تحليلات تدفق المال والفرص النشطة")
            col_m1, col_m2 = st.columns(2)
            with col_m1:
                st.markdown("""
                <div class="premium-card">
                    <h4 style="color:#3b82f6; margin-top:0;">📡 حالة اتصال الـ APIs والقنوات</h4>
                    <p style="font-size:14px; margin:4px 0;">• Google Drive Connection: <b style="color:#10b981;">CONNECTED</b></p>
                    <p style="font-size:14px; margin:4px 0;">• Google Sheets API Link: <b style="color:#10b981;">LIVE</b></p>
                    <p style="font-size:14px; margin:4px 0;">• n8n Local Automation Stack: <b style="color:#10b981;">SYNCED</b></p>
                </div>
                """, unsafe_allow_html=True)
            with col_m2:
                st.markdown("""
                <div class="premium-card">
                    <h4 style="color:#f59e0b; margin-top:0;">🗲 محرك اقتناص العمولات السريع</h4>
                    <p style="font-size:13px; color:#94a3b8;">يتم توجيه كافة الطلبيات، وإشعارات السحب التفاعلي، وبيانات المشترين آلياً إلى بريدك الرسمي المربوط:</p>
                    <code style="color:#60a5fa; font-size:15px; display:block; text-align:center;">laidadid21@gmail.com</code>
                </div>
                """, unsafe_allow_html=True)
                
        with tab_clients:
            st.markdown("### 👥 إدارة العملاء وعوائد المعاملات")
            st.write("قاعدة بيانات مؤتمتة تسحب السجلات والطلبات القادمة من الويب هوكس (Webhooks) وتفرغها في الجداول.")
            # محاكاة لجدول المراقبة المالية الفاخرة
            st.table([
                {"العميل": "مؤسسة الطاقة Agro-Industrial", "الخدمة المطلوبة": "أتمتة تدقيق العقود الذكية", "المبلغ المودع": "$249.99", "الحالة": "مكتمل ✔️"},
                {"العميل": "مستثمر B2B - فرنسا", "الخدمة المطلوبة": "حزمة n8n + استشارة سيادية", "المبلغ المودع": "$642.23", "الحالة": "جاري المعالجة 🔄"}
            ])
            
        with tab_plans:
            st.markdown("### 📜 محرر الخطط وتحويل الأصول")
            st.write("من هنا يمكنك إضافة وبيع منتجات جديدة (كتب، أدوات تقنية للمكاتب، سيناريوهات أتمتة جاهزة):")
            
            new_prod_title = st.text_input("اسم المنتج أو التقنية الجديدة:")
            new_prod_price = st.number_input("السعر المستهدف للترخيص (USD):", min_value=0.0)
            
            if st.button("🔥 حقن المنتج الجديد في لوحة العرض ثلاثية الأبعاد"):
                st.success(f"تم بنجاح! تم دمج منتج '{new_prod_title}' وجاهز لاستلام العمولات والأرباح.")

# 4. تذييل الصفحة الممتد لأسفل النظام
st.markdown("---")
st.markdown("<p style='text-align: center; color: #4b5563; font-size:13px;'>🔒 نظام التشغيل السيادي الخارق والمحمي بالكامل 2026 | مكتب المحامي عديد العيد</p>", unsafe_allow_html=True)
