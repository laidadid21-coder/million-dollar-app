import streamlit as st
import streamlit.components.v1 as components

# 1. إعدادات المنصة الرقمية العالمية
st.set_page_config(
    page_title="Adid Al-Eid | Global Digital Platform",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. إدارة الحالة البرمجية لسلة المشتريات
if "cart" not in st.session_state: st.session_state["cart"] = []
if "category" not in st.session_state: st.session_state["category"] = "🌐 الرئيسية"

# 3. محرك التصميم البصري (تنسيق الواجهات والأزرار والأيقونات)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;700;900&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        background: #f0f2f6 !important;
        color: #1e293b !important;
        font-family: 'Cairo', sans-serif !important;
    }

    [data-testid="stSidebar"] {
        background: #ffffff !important;
        border-right: 2px solid #e2e8f0 !important;
    }
    
    .sidebar-title {
        color: #0f172a;
        font-size: 26px; font-weight: 900; text-align: center;
        margin-bottom: 5px; text-transform: uppercase;
    }

    .stRadio div[role="radiogroup"] label {
        background: #f8fafc !important;
        border: 1px solid #e2e8f0 !important;
        padding: 10px 15px !important;
        border-radius: 10px !important;
        color: #334155 !important;
        font-weight: 600 !important;
        font-size: 15px !important;
        margin-bottom: 5px !important;
    }

    .logo-l {
        width: 80px; height: 80px; border: 4px solid #0f172a; border-radius: 50%;
        display: flex; justify-content: center; align-items: center;
        font-family: 'Arial', sans-serif; font-size: 50px; font-weight: 900;
        color: #0f172a; margin: 0 auto 15px auto;
    }

    .product-card {
        background: #ffffff; border: 1px solid #e2e8f0; border-radius: 16px;
        padding: 20px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 15px;
    }
    .product-img { width: 100%; height: 160px; border-radius: 8px; object-fit: cover; }
    .product-price { color: #0f172a; font-size: 24px; font-weight: 800; margin: 10px 0; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 4. القائمة الجانبية (إضافة اللغات الثلاث والتحكم)
# ==========================================
with st.sidebar:
    st.markdown('<div class="sidebar-title">ADID AL-EID</div>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#64748b; font-size:12px; margin-top:-5px;">Global Digital Platform</p>', unsafe_allow_html=True)
    
    # 🌍 إضافة خيار اللغات الثلاث لضمان عالمية المنتج
    selected_lang = st.selectbox("🌐 اختر اللغة / Choose Language / Choisir la Langue", ["العربية (Arabic)", "English", "Français"])
    st.divider()
    
    # نصوص القوائم بناءً على اللغة المختارة
    if "English" in selected_lang:
        categories = ["🌐 Home", "🤖 AI Agents", "⚡ Automation Systems", "🔗 Enterprise Contracts"]
        cart_text = "🛒 Shopping Cart"
        confirm_btn = "Confirm Global Booking 🚀"
    elif "Français" in selected_lang:
        categories = ["🌐 Accueil", "🤖 Agents d'IA", "⚡ Systèmes d'Automatisation", "🔗 Contrats d'Entreprise"]
        cart_text = "🛒 Panier"
        confirm_btn = "Confirmer la Réservation 🚀"
    else:
        categories = ["🌐 الرئيسية", "🤖 عملاء الذكاء الاصطناعي", "⚡ أنظمة الأتمتة", "🔗 عقود الشركات الكبرى"]
        cart_text = "🛒 سلة المشتريات"
        confirm_btn = "تأكيد الحجز العالمي 🚀"
        
    st.session_state["category"] = st.radio("التصنيفات / Categories:", categories)
    
    st.divider()
    st.markdown(f"### {cart_text} ({len(st.session_state['cart'])})")
    if st.button(confirm_btn):
        st.balloons()
        st.success("Success / تم استلام طلبك بنجاح")

# ==========================================
# 5. محتوى الصفحة الرئيسية
# ==========================================
if st.session_state["category"] in ["🌐 الرئيسية", "🌐 Home", "🌐 Accueil"]:
    st.markdown("""
    <div style="text-align:center; padding:20px;">
        <div class="logo-l">L</div>
        <h1 style="font-size:45px; font-weight:900; color:#0f172a;">مكتب المحامي عديد العيد</h1>
        <h2 style="color:#334155;">المنصة الرقمية العالمية لأتمتة وتطوير المؤسسات</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # السلايدر التلقائي للمنتجات العالمية
    images = [
        "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600",
        "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600"
    ]
    slider_code = f"""
    <div style="overflow: hidden; width: 100%; padding: 10px 0; display: flex; justify-content: center;">
        <img src="{images[0]}" style="width:380px; height:250px; margin:10px; border-radius:15px; border: 3px solid #0f172a;">
        <img src="{images[1]}" style="width:380px; height:250px; margin:10px; border-radius:15px; border: 3px solid #0f172a;">
    </div>
    """
    components.html(slider_code, height=280)

# ==========================================
# 6. نظام عرض المنتجات المطور مع الأيقونات والخيارات التفاعلية و PDF
# ==========================================
else:
    st.markdown(f"<h1 style='color:#0f172a;'>{st.session_state['category']}</h1>", unsafe_allow_html=True)
    
    # قاعدة البيانات البرمجية للمنتجات
    products_data = [
        {"name": "AI Legal Agent Pro", "price": "5,000$", "img": "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=400", "desc": "المساعد القانوني الرقمي لصياغة ومراجعة العقود وتوقع الأحكام بدقة."},
        {"name": "أتمتة العمليات (LPA)", "price": "4,200$", "img": "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=400", "desc": "أتمتة كاملة لربط المهام الروتينية وإدخال البيانات وإصدار الفواتير إلكترونياً."},
        {"name": "عقد الدمج والربط العالمي", "price": "15,000$", "img": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=400", "desc": "اتفاقية صياغة حوكمة وتكامل الأنظمة والبيانات بين الفروع الدولية للشركات."}
    ]
    
    cols = st.columns(3)
    
    for idx, item in enumerate(products_data):
        with cols[idx % 3]:
            # عرض بطاقة المنتج الأساسية لضمان عدم تغير التصميم الأصلي
            st.markdown(f"""
            <div class="product-card">
                <div style="font-size: 30px;">💎</div>
                <img src="{item['img']}" class="product-img">
                <h3 style="color:#0f172a; margin-top:10px;">{item['name']}</h3>
                <div class="product-price">{item['price']}</div>
            </div>
            """, unsafe_allow_html=True)
            
            # ℹ️ أيقونة الخيارات التفاعلية (الملخص، كم نسخة، توجيه الزبون، تحميل عقد PDF)
            with st.expander(f"ℹ️ تفاصيل وملاءمة المنتج | Details & PDF"):
                st.write(f"**ملخص المنتج:** {item['desc']}")
                
                # تحديد كم نسخة يحتاجها الزبون
                quantity = st.number_input(f"كم نسخة تحتاج؟ / Quantity ({item['name']})", min_value=1, max_value=100, value=1, key=f"qty_{idx}")
                
                # سؤال توجيهي لمساعدة الزبون وفهم ما يبحث عنه
                user_search = st.text_input("ما هي المشكلة أو الهدف الذي تبحث عن حله بهذا المنتج؟", key=f"ask_{idx}")
                if user_search:
                    st.info("💡 نصيحة النظام: هذا المنتج يتوافق تماماً مع متطلباتك وسيقوم بتغطية هذا الجانب تلقائياً.")
                
                st.divider()
                
                # 📄 زر تحميل وثيقة الشرك أو تفاصيل العقد بصيغة PDF
                pdf_content = f"Product: {item['name']}\nPrice: {item['price']}\nDescription: {item['desc']}\nAuthorized by Adid Al-Eid Office."
                st.download_button(
                    label="📥 تحميل مستند العقد والشرك (PDF)",
                    data=pdf_content,
                    file_name=f"{item['name']}_details.pdf",
                    mime="application/pdf",
                    key=f"pdf_{idx}"
                )
            
            # زر الشراء الأصلي لإضافة المنتج للسلة
            if st.button(f"🛒 أضف للسلة - {item['name']}", key=f"buy_{idx}"):
                st.session_state["cart"].append(f"{item['name']} (x{quantity})")
                st.toast(f"تمت إضافة {quantity} نسخة من {item['name']} إلى السلة")

# ==========================================
# 7. التذييل العالمي (Footer)
# ==========================================
st.divider()
st.markdown("""
<div style="text-align:center; padding:10px; color:#64748b; font-size:12px;">
    <h4 style="color:#0f172a; margin:0;">مؤسسة عديد العيد العالمية للرقمنة</h4>
    <p style="margin:2px;">Build v11.7 Global Nexus | 2026 All Rights Reserved</p>
</div>
""", unsafe_allow_html=True)
