import streamlit as st
import streamlit.components.v1 as components

# 1. إعدادات المنصة الرقمية العالمية v11.8
st.set_page_config(
    page_title="Adid Al-Eid | Global Digital Platform",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. إدارة الحالة البرمجية لسلة المشتريات
if "cart" not in st.session_state: st.session_state["cart"] = []

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
# 4. قاموس الترجمة العالمي الشامل (عربي - إنجليزي - فرنسي)
# ==========================================
lexicon = {
    "العربية (Arabic)": {
        "lang_code": "ar",
        "subtitle": "المنصة الرقمية العالمية",
        "nav_title": "التصنيفات:",
        "cat_home": "🌐 الرئيسية",
        "cat_agents": "🤖 عملاء الذكاء الاصطناعي",
        "cat_auto": "⚡ أنظمة الأتمتة",
        "cat_contracts": "🔗 عقود الشركات الكبرى",
        "cart_title": "🛒 سلة المشتريات",
        "confirm_btn": "تأكيد الحجز العالمي 🚀",
        "success_msg": "تم استلام طلبك بنجاح في غرفة العمليات!",
        "main_title": "مكتب المحامي عديد العيد",
        "main_desc": "المنصة الرقمية العالمية لأتمتة وتطوير المؤسسات واستغلال ثغرات السوق.",
        "expander_title": "ℹ️ تفاصيل وملاءمة المنتج والتحميل",
        "prod_summary": "ملخص المنتج:",
        "prod_qty": "كم نسخة تحتاج؟",
        "prod_ask": "ما هي المشكلة أو الهدف الذي تبحث عن حله بهذا المنتج؟",
        "prod_tip": "💡 نصيحة النظام: هذا المنتج يتوافق تماماً مع متطلباتك وسيقوم بتغطية هذا الجانب تلقائياً.",
        "pdf_btn": "📥 تحميل مستند العقد والشرك (PDF)",
        "add_cart_btn": "🛒 أضف للسلة",
        "toast_msg": "تمت إضافة {qty} نسخة من {name} إلى السلة",
        "footer_title": "مؤسسة عديد العيد العالمية للرقمنة",
        "footer_desc": "المقر الرئيسي للأتمتة والسيادة الرقمية | 2026 جميع الحقوق محفوظة",
        "products": {
            "p1_name": "AI Legal Agent Pro",
            "p1_desc": "المساعد القانوني الرقمي لصياغة ومراجعة العقود وتوقع الأحكام بدقة.",
            "p2_name": "أتمتة العمليات (LPA)",
            "p2_desc": "أتمتة كاملة لربط المهام الروتينية وإدخال البيانات وإصدار الفواتير إلكترونياً.",
            "p3_name": "عقد الدمج والربط العالمي",
            "p3_desc": "اتفاقية صياغة حوكمة وتكامل الأنظمة والبيانات بين الفروع الدولية للشركات."
        }
    },
    "English": {
        "lang_code": "en",
        "subtitle": "Global Digital Platform",
        "nav_title": "Categories:",
        "cat_home": "🌐 Home",
        "cat_agents": "🤖 AI Agents",
        "cat_auto": "⚡ Automation Systems",
        "cat_contracts": "🔗 Enterprise Contracts",
        "cart_title": "🛒 Shopping Cart",
        "confirm_btn": "Confirm Global Booking 🚀",
        "success_msg": "Your order has been successfully received by operations!",
        "main_title": "Law Firm of Adid Al-Eid",
        "main_desc": "The global digital platform for enterprise automation, development, and market optimization.",
        "expander_title": "ℹ️ Product Details, Suitability & PDF",
        "prod_summary": "Product Summary:",
        "prod_qty": "How many copies do you need?",
        "prod_ask": "What problem or objective are you looking to solve with this product?",
        "prod_tip": "💡 System Tip: This product perfectly matches your requirements and will cover this aspect automatically.",
        "pdf_btn": "📥 Download Contract & Partnership Document (PDF)",
        "add_cart_btn": "🛒 Add to Cart",
        "toast_msg": "Added {qty} copies of {name} to the cart",
        "footer_title": "Adid Al-Eid Global Digitalization Infrastructure",
        "footer_desc": "Headquarters for Automation & Digital Sovereignty | 2026 All Rights Reserved",
        "products": {
            "p1_name": "AI Legal Agent Pro",
            "p1_desc": "The digital legal assistant for precise drafting, reviewing of contracts, and predicting judgments.",
            "p2_name": "Process Automation (LPA)",
            "p2_desc": "Complete automation to link routine tasks, data entry, and electronic invoicing.",
            "p3_name": "Global Merger & Integration Contract",
            "p3_desc": "Agreement for drafting governance and integrating systems and data between international corporate branches."
        }
    },
    "Français": {
        "lang_code": "fr",
        "subtitle": "Plateforme Digitale Globale",
        "nav_title": "Catégories:",
        "cat_home": "🌐 Accueil",
        "cat_agents": "🤖 Agents d'IA",
        "cat_auto": "⚡ Systèmes d'Automatisation",
        "cat_contracts": "🔗 Contrats d'Entreprise",
        "cart_title": "🛒 Panier",
        "confirm_btn": "Confirmer la Réservation Globale 🚀",
        "success_msg": "Votre commande a été reçue avec succès par les opérations !",
        "main_title": "Cabinet d'Avocat Adid Al-Eid",
        "main_desc": "La plateforme digitale mondiale pour l'automatisation, le développement des entreprises et l'optimisation des marchés.",
        "expander_title": "ℹ️ Détails du Produit, Adéquation & PDF",
        "prod_summary": "Résumé du Produit:",
        "prod_qty": "Combien d'exemplaires avez-vous besoin ?",
        "prod_ask": "Quel problème ou objectif cherchez-vous à résoudre avec ce produit ?",
        "prod_tip": "💡 Conseil du Système: Ce produit correspond parfaitement à vos exigences et couvrira cet aspect automatiquement.",
        "pdf_btn": "📥 Télécharger le Document de Contrat & Partenariat (PDF)",
        "add_cart_btn": "🛒 Ajouter au Panier",
        "toast_msg": "Ajouté {qty} exemplaires de {name} au panier",
        "footer_title": "Infrastructure Globale de Digitalisation Adid Al-Eid",
        "footer_desc": "Siège de l'Automatisation & Souveraineté Numérique | 2026 Tous Droits Réservés",
        "products": {
            "p1_name": "AI Legal Agent Pro",
            "p1_desc": "L'assistant juridique digital pour la rédaction précise, la révision des contrats et la prédiction des jugements.",
            "p2_name": "Automatisation des Processus (LPA)",
            "p2_desc": "Automatisation complète pour lier les tâches de routine, la saisie de données et la facturation électronique.",
            "p3_name": "Contrat de Fusion & d'Intégration Globale",
            "p3_desc": "Accord pour la rédaction de la gouvernance et l'intégration des systèmes et des données entre les succursales internationales."
        }
    }
}

# ==========================================
# 5. القائمة الجانبية المترجمة ديناميكياً
# ==========================================
with st.sidebar:
    st.markdown('<div class="sidebar-title">ADID AL-EID</div>', unsafe_allow_html=True)
    
    # 🌍 اختيار اللغة - المحرك الأساسي للترجمة
    selected_lang = st.selectbox("🌐 Choose Language / اختر اللغة / Choisir la Langue", list(lexicon.keys()))
    
    # جلب قاموس نصوص اللغة النشطة فوراً
    ctx = lexicon[selected_lang]
    
    st.markdown(f'<p style="text-align:center; color:#64748b; font-size:12px; margin-top:-5px;">{ctx["subtitle"]}</p>', unsafe_allow_html=True)
    st.divider()
    
    # بناء القائمة بالفروع المترجمة بالكامل
    categories_map = {
        ctx["cat_home"]: "HOME",
        ctx["cat_agents"]: "AGENTS",
        ctx["cat_auto"]: "AUTO",
        ctx["cat_contracts"]: "CONTRACTS"
    }
    
    selected_radio = st.radio(ctx["nav_title"], list(categories_map.keys()))
    current_page = categories_map[selected_radio]
    
    st.divider()
    st.markdown(f"### {ctx['cart_title']} ({len(st.session_state['cart'])})")
    if st.button(ctx["confirm_btn"]):
        st.balloons()
        st.success(ctx["success_msg"])

# ==========================================
# 6. محتوى الصفحة الرئيسية المترجم
# ==========================================
if current_page == "HOME":
    st.markdown(f"""
    <div style="text-align:center; padding:20px;">
        <div class="logo-l">L</div>
        <h1 style="font-size:45px; font-weight:900; color:#0f172a;">{ctx['main_title']}</h1>
        <h2 style="color:#334155;">{ctx['main_desc']}</h2>
    </div>
    """, unsafe_allow_html=True)
    
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
# 7. نظام عرض المنتجات المترجم كلياً للغات الثلاث
# ==========================================
else:
    st.markdown(f"<h1 style='color:#0f172a;'>{selected_radio}</h1>", unsafe_allow_html=True)
    
    # تعبئة المنتجات بالنصوص المترجمة ديناميكياً من القاموس
    products_data = [
        {"name": ctx["products"]["p1_name"], "price": "5,000$", "img": "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=400", "desc": ctx["products"]["p1_desc"]},
        {"name": ctx["products"]["p2_name"], "price": "4,200$", "img": "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=400", "desc": ctx["products"]["p2_desc"]},
        {"name": ctx["products"]["p3_name"], "price": "15,000$", "img": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=400", "desc": ctx["products"]["p3_desc"]}
    ]
    
    cols = st.columns(3)
    
    for idx, item in enumerate(products_data):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="product-card">
                <div style="font-size: 30px;">💎</div>
                <img src="{item['img']}" class="product-img">
                <h3 style="color:#0f172a; margin-top:10px;">{item['name']}</h3>
                <div class="product-price">{item['price']}</div>
            </div>
            """, unsafe_allow_html=True)
            
            # ℹ️ صندوق الخيارات التفاعلية المترجم بالكامل
            with st.expander(ctx["expander_title"]):
                st.write(f"**{ctx['prod_summary']}** {item['desc']}")
                
                quantity = st.number_input(ctx["prod_qty"], min_value=1, max_value=100, value=1, key=f"qty_{idx}_{ctx['lang_code']}")
                
                user_search = st.text_input(ctx["prod_ask"], key=f"ask_{idx}_{ctx['lang_code']}")
                if user_search:
                    st.info(ctx["prod_tip"])
                
                st.divider()
                
                # 📄 محتوى ملف الـ PDF يتم إنشاؤه بلغة المستخدم المختارة لضمان الاحترافية
                pdf_content = f"Product: {item['name']}\nPrice: {item['price']}\nDescription: {item['desc']}\nGenerated officially by Adid Al-Eid Infrastructure."
                st.download_button(
                    label=ctx["pdf_btn"],
                    data=pdf_content,
                    file_name=f"{item['name']}_{ctx['lang_code']}.pdf",
                    mime="application/pdf",
                    key=f"pdf_{idx}_{ctx['lang_code']}"
                )
            
            # زر إضافة للسلة المترجم
            if st.button(f"{ctx['add_cart_btn']} - {item['name']}", key=f"buy_{idx}_{ctx['lang_code']}"):
                st.session_state["cart"].append(f"{item['name']} (x{quantity})")
                st.toast(ctx["toast_msg"].format(qty=quantity, name=item['name']))

# ==========================================
# 8. التذييل العالمي المترجم (Footer)
# ==========================================
st.divider()
st.markdown(f"""
<div style="text-align:center; padding:10px; color:#64748b; font-size:12px;">
    <h4 style="color:#0f172a; margin:0;">{ctx['footer_title']}</h4>
    <p style="margin:2px;">{ctx['footer_desc']} | Build v11.8 Global Nexus</p>
</div>
""", unsafe_allow_html=True)
