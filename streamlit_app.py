import streamlit as st
import streamlit.components.v1 as components
import random

# 1. إعدادات الإمبراطورية الرقمية v11.6 (تحديث وإصلاح شامل للأخطاء النحوية)
st.set_page_config(
    page_title="Adid Al-Eid | Digital Powerhouse",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. إدارة الحالة 
if "cart" not in st.session_state: st.session_state["cart"] = []
if "category" not in st.session_state: st.session_state["category"] = "الكل"

# 3. محرك التصميم البصري (مستقر وفاتح بالكامل)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;700;900&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        background: #f0f2f6 !important;
        color: #1e293b !important;
        font-family: 'Cairo', sans-serif !important;
    }

    /* --- الجهة اليسرى (Sidebar) --- */
    [data-testid="stSidebar"] {
        background: #ffffff !important;
        border-right: 2px solid #e2e8f0 !important;
    }
    
    .sidebar-title {
        color: #0f172a;
        font-size: 28px; font-weight: 900; text-align: center;
        margin-bottom: 20px; text-transform: uppercase; letter-spacing: 2px;
    }

    /* تحسين وضوح أزرار القائمة الجانبية */
    .stRadio div[role="radiogroup"] label {
        background: #f8fafc !important;
        border: 1px solid #e2e8f0 !important;
        padding: 12px 20px !important;
        border-radius: 10px !important;
        color: #334155 !important;
        font-weight: 600 !important;
        font-size: 16px !important;
        margin-bottom: 6px !important;
    }
    .stRadio div[role="radiogroup"] label:hover {
        background-color: #f1f5f9 !important;
        border-color: #cbd5e1 !important;
        transform: translateX(5px);
        transition: all 0.3s;
    }
    .stRadio div[role="radiogroup"] label[data-selected="true"] {
        background-color: #0f172a !important;
        color: #ffffff !important;
        font-weight: 700 !important;
    }

    /* --- شعار "L" الأنيق والجديد --- */
    .logo-l {
        width: 80px;
        height: 80px;
        border: 4px solid #0f172a;
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        font-family: 'Arial', sans-serif;
        font-size: 50px;
        font-weight: 900;
        color: #0f172a;
        margin: 0 auto 15px auto;
    }

    /* --- السلايدر المتحرك التلقائي --- */
    @keyframes scroll {
        0% { transform: translateX(0); }
        100% { transform: translateX(calc(-400px * 4)); }
    }
    .slider-wrapper {
        display: flex; width: calc(400px * 8);
        animation: scroll 25s linear infinite;
    }
    .slider-wrapper:hover { animation-play-state: paused; }
    .slide-item {
        width: 380px; height: 500px; margin: 10px;
        border-radius: 20px; border: 3px solid #0f172a;
        object-fit: cover; filter: brightness(1.0);
    }

    /* --- بطاقات المتجر المحدثة --- */
    .product-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 25px;
        text-align: center;
        transition: 0.3s;
        height: 520px; 
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .product-card:hover {
        border-color: #cbd5e1;
        box-shadow: 0 10px 15px rgba(0,0,0,0.1);
    }
    .product-img { width: 100%; height: 180px; border-radius: 8px; object-fit: cover; }
    .product-price { color: #0f172a; font-size: 26px; font-weight: 800; margin: 10px 0; }
    
    .icon-3d-box {
        font-size: 40px; margin-bottom: 10px;
        filter: drop-shadow(0 0 10px rgba(15, 23, 42, 0.3));
    }

    /* زر الشراء الداكن والأنيق */
    .buy-btn {
        background: #0f172a;
        color: #ffffff !important;
        padding: 12px; border-radius: 8px;
        font-weight: 700; text-decoration: none; display: block;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 4. القائمة الجانبية (The Control Center)
# ==========================================
with st.sidebar:
    st.markdown('<div class="sidebar-title">ADID AL-EID</div>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#64748b; font-size:12px; margin-top:-20px;">The Digitalization Source</p>', unsafe_allow_html=True)
    st.divider()
    
    categories = [
        "🌐 الرئيسية",
        "🤖 عملاء الذكاء الاصطناعي",
        "⚡ أنظمة الأتمتة",
        "📚 مكتبة PDF الرقمية",
        "📖 كتب ورقية تكنولوجية",
        "🏛️ تكنولوجيا المكاتب",
        "🛡️ الأمن والسيادة",
        "🔗 عقود الشركات الكبرى",
        "⚙️ الهندسة العكسية",
        "🎓 التدريب والماستركلاس",
        "💻 تراخيص البرمجيات"
    ]
    
    st.session_state["category"] = st.radio("تصفح الإمبراطورية:", categories, key="global_category")
    
    st.divider()
    st.markdown(f"### 🛒 سلة المشتريات ({len(st.session_state['cart'])})")
    if st.button("تأكيد الحجز العالمي 🚀"):
        st.balloons()
        st.success("تم إرسال الطلب لغرفة العمليات")

# ==========================================
# 5. محتوى الصفحة الرئيسية
# ==========================================
if st.session_state["category"] == "🌐 الرئيسية":
    st.markdown("""
    <div style="text-align:center; padding:20px;">
        <div class="logo-l">L</div>
        <h1 style="font-size:55px; font-weight:900; color:#0f172a;">مكتب المحامي عديد العيد</h1>
        <h2 style="color:#334155;">المنبع العالمي لرقمنة القانون والمؤسسات</h2>
        <p style="font-size:20px; color:#64748b; max-width:900px; margin:auto;">نحن لا نتبع التكنولوجيا، نحن من نضع قواعدها. شراكات مع كبرى الشركات العالمية وعقود عابرة للقارات في مجال الأتمتة والسيادة الرقمية.</p>
    </div>
    """, unsafe_allow_html=True)

    images = [
        "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600",
        "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600",
        "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=600",
        "https://images.unsplash.com/photo-1600132806370-bf17e65e942f?w=600"
    ]
    
    slider_code = f"""
    <div style="overflow: hidden; width: 100%; padding: 30px 0;">
        <div class="slider-wrapper">
            <img src="{images[0]}" class="slide-item">
            <img src="{images[1]}" class="slide-item">
            <img src="{images[2]}" class="slide-item">
            <img src="{images[3]}" class="slide-item">
            <img src="{images[0]}" class="slide-item">
            <img src="{images[1]}" class="slide-item">
            <img src="{images[2]}" class="slide-item">
            <img src="{images[3]}" class="slide-item">
        </div>
    </div>
    """
    components.html(slider_code, height=550)
    
    st.markdown("<h3 style='text-align:center; color:#0f172a;'>🤝 شركاء النجاح العالمي</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#64748b;'>نظامنا معتمد في أكثر من 50 شركة كبرى ومكاتب محاماة دولية</p>", unsafe_allow_html=True)

# ==========================================
# 6. نظام المتجر العالمي المصحح والمحمي تماماً
# ==========================================
else:
    st.markdown(f"<h1 style='color:#0f172a;'>{st.session_state['category']}</h1>", unsafe_allow_html=True)
    
    # تم إغلاق جميع النصوص وعلامات التنصيص بدقة متناهية هنا لتجنب خطأ صورة image_6758a2.png
    data = {
        "🤖 عملاء الذكاء الاصطناعي": [
            ("AI Legal Agent Pro", "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=400", "5,000$", "المساعد القانوني الرقمي لصياغة ومراجعة العقود وتوقع الأحكام."),
            ("AI Financial Auditor", "https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?w=400", "4,500$", "المحاسب الذكي والتدقيق المالي الفوري وتحليل الثغرات الضريبية."),
            ("AI Executive Secretary", "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=400", "3,200$", "سكرتير تنفيذي ذكي لإدارة المراسلات الرسمية، الجدولة وتلخيص الاجتماعات."),
            ("AI HR Specialist", "https://images.unsplash.com/photo-1560250097-0b93528c311a?w=400", "3,800$", "عميل ذكاء اصطناعي متكامل لفرز السير الذاتية وإجراء المقابلات الأولية."),
            ("AI Risk Analyst", "https://images.unsplash.com/photo-1504868584819-f8e8b4b6d7e3?w=400", "6,000$", "محلل المخاطر السيادية والتحذير من البنود التعاقدية الخطرة غيابيًا."),
            ("AI Operations Manager", "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=400", "5,500$", "المدير الرقمي لمراقبة سير العمل وكفاءة الأقسام التشغيلية لحظيًا.")
        ],
        "⚡ أنظمة الأتمتة": [
            ("أتمتة الموارد البشرية (HR-Auto)", "https://images.unsplash.com/photo-1521791136368-1a46827d53b2?w=400", "2,500$", "نظام أتمتة كامل لإدارة الحضور، الرواتب، وتتبع الأداء بدون تدخل بشري."),
            ("نظام أتمتة المخازن الذكي", "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?w=400", "3,800$", "الربط الآلي للمخزون مع سلاسل التوريد وإصدار أوامر الشراء تلقائيًا."),
            ("منظومة الأتمتة الكلية الشاملة", "https://images.unsplash.com/photo-1518770660439-4636190af475?w=400", "12,000$", "ربط مكاتب المؤسسة وفروعها بالكامل في شبكة عصبية مؤتمتة موحدة."),
            ("نظام الأتمتة الجزئية للمهام", "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=400", "1,500$", "أتمتة المهام الروتينية المتكررة مثل الفواتير البريدية وإدخال البيانات."),
            ("أتمتة العمليات القانونية (LPA)", "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=400", "4,200$", "أتمتة رفع الدعاوى ومتابعة المواعيد القضائية مع المحاكم إلكترونيًا."),
            ("أتمتة علاقات العملاء (CRM-Flow)", "https://images.unsplash.com/photo-1552581234-2612b75de6d6?w=400", "2,900$", "نظام ذكي للاستجابة التلقائية لاستفسارات الشركاء والعملاء الكبار.")
        ],
        "🔗 عقود الشركات الكبرى": [
            ("حزمة التحول الرقمي السيادي", "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=400", "اتصل للسعر", "عقد استراتيجي لنقل البنية التحتية للمؤسسات إلى سحابة محلية آمنة ومحمية."),
            ("عقد الفحص النافي للجهالة الذكي", "https://images.unsplash.com/photo-1450133064473-71024230f91b?w=400", "15,000$", "اتفاقية فحص الشركات وتدقيق سجلاتها بالذكاء الاصطناعي قبل الاستحواذ."),
            ("اتفاقية صيانة الحصانة الرقمية", "https://images.unsplash.com/photo-1563986768609-322da13575f3?w=400", "8,000$", "عقد سنوي لحماية وتأمين الخوادم والأنظمة ضد عمليات الهندسة العكسية."),
            ("اتفاقية صياغة حوكمة الشركات", "https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=400", "9,500$", "إعداد اللوائح الداخلية وهيكلة الصلاحيات الرقمية للمدريرن والموظفين."),
            ("عقد الدمج والربط العابر للقارات", "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=400", "اتصل للسعر", "تكامل الأنظمة والبيانات بين الفروع الدولية للشركات متعددة الجنسيات."),
            ("عقد تراخيص الأنظمة السيادية", "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=400", "20,000$", "منح حقوق الملكية البرمجية المستقلة للمؤسسات دون الاعتماد على خوادم خارجية.")
        ]
    }
    
    category_items = data.get(
        st.session_state["category"], 
        [
            ("حل رقمي استشاري مخصص", "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=400", "حسب الطلب", "حلول برمجية مخصصة ومصممة بدقة لتلبية تطلعات واحتياجات مؤسستك.")
        ]
    )
    
    cols = st.columns(3)
    num_items = len(category_items)
    
    for i in range(6): 
        item = category_items[i % num_items]
        
        with cols[i % 3]:
            st.markdown(f"""
            <div class="product-card">
                <div>
                    <div class="icon-3d-box">💎</div>
                    <img src="{item[1]}" class="product-img">
                    <h3 style="margin-top:12px; color:#0f172a; font-size:20px; font-weight:700;">{item[0]}</h3>
                    <p style="color:#64748b; font-size:13px; text-align:justify; margin-top:8px; line-height:1.5;">{item[3] if len(item) > 3 else item[0]}</p>
                    <p style="color:#94a3b8; font-size:11px; margin-top:5px;">💡 معتمد من مكتب عديد العيد</p>
                </div>
                <div>
                    <div class="product-price">{item[2]}</div>
                    <a href="#" class="buy-btn">أضف للسلة الآن</a>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"تأكيد الإضافة - {item[0]}", key=f"btn_{st.session_state['category']}_{i}"):
                st.session_state["cart"].append(f"{item[0]}")
                st.toast(f"تمت إضافة {item[0]} إلى سلة المشتريات")

# ==========================================
# 7. التذييل العالمي (Footer)
# ==========================================
st.divider()
st.markdown("""
<div style="text-align:center; padding:40px; color:#64748b;">
    <h3 style="color:#0f172a;">مؤسسة عديد العيد العالمية للرقمنة</h3>
    <p>المقر الرئيسي للأتمتة والسيادة الرقمية | 📧 laidadid21@gmail.com | 📱 +213 671 81 63 46</p>
    <div style="font-size:10px;">Build v11.6 Global Nexus | 2026 All Rights Reserved</div>
</div>
""", unsafe_allow_html=True)
