import streamlit as st
import streamlit.components.v1 as components
import random

# 1. إعدادات المنصة الرقمية العالمية v11.9
st.set_page_config(
    page_title="Adid Al-Eid | Global Digital Platform",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. إدارة الحالة البرمجية لسلة المشتريات والدردشة التفاعلية
if "cart" not in st.session_state: st.session_state["cart"] = []
if "chat_history" not in st.session_state: st.session_state["chat_history"] = []

# 3. محرك التصميم البصري (تنسيق الواجهات والأزرار وعلم الجزائر في الرئيسية)
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

    /* هيدر ألوان علم الجزائر للرئيسية لضمان الامتثال والتصميم الإبداعي */
    .dz-banner {
        display: flex;
        height: 15px;
        width: 100%;
        border-radius: 8px;
        overflow: hidden;
        margin-bottom: 25px;
    }
    .dz-green { background-color: #006633; flex: 1; }
    .dz-white { background-color: #ffffff; flex: 1; display: flex; justify-content: center; align-items: center; position: relative; }
    .dz-red { background-color: #d21034; flex: 1; }
    
    /* بطاقات التعريف بالشركة والخانات المحدثة */
    .info-card {
        background: #ffffff;
        border-left: 5px solid #006633;
        border-right: 5px solid #d21034;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 20px;
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
# 4. قاموس الترجمة العالمي الشامل المحدث بالكامل
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
        "main_desc": "المنصة الرقمية العالمية لأتمتة وتطوير المؤسسات واستغلال ثغرات السوق وتحويل المعلومات إلى عوائد.",
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
        "about_firm": "🏢 التعريف بالمؤسسة الرقمية ومكوناتها",
        "about_desc": "مؤسسة تكنولوجية رائدة تدمج الذكاء الاصطناعي والأتمتة لتطوير البنى التحتية القانونية والتجارية للمؤسسات حول العالم.",
        "exp_title": "🎯 خبراتنا ونشاطنا العابر للمنصات",
        "exp_desc": "خبرة متكاملة في إدارة المشاريع الرقمية، التسويق الإلكتروني، وإدارة الحملات الإعلانية على المنصات الرسمية مثل LinkedIn و TikTok و Facebook Ads وتحقيق الأرباح عبر بيع المنتجات على Gumroad وأتمتة العمليات.",
        "ai_bot_title": "🤖 مستشار السوبرماركت الرقمي (الرد الفوري والذكي)",
        "ai_bot_prompt": "اسأل العميل الذكي عن أي شيء يخص التجارة والتسويق وأتمتة شؤون الحياة ومشاريعك:",
        "ai_bot_btn": "إرسال الاستفسار",
        "products": {
            "p1_name": "AI Legal Agent Pro",
            "p1_desc": "المساعد القانوني الرقمي لصياغة ومراجعة العقود وتوقع الأحكام بدقة.",
            "p2_name": "Automatisation des Processus (LPA)",
            "p2_desc": "أتمتة كاملة لربط المهام الروتينية وإدخال البيانات وإصدار الفواتير إلكترونياً.",
            "p3_name": "Contrat de Fusion & d'Intégration Globale",
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
        "about_firm": "🏢 About our Digital Institution & Components",
        "about_desc": "A leading technological enterprise integrating AI and automation to build the next generation of legal and business ecosystems worldwide.",
        "exp_title": "🎯 Our Cross-Platform Expertise & Operations",
        "exp_desc": "Complete mastery over digital product execution, global marketing strategy, official advertising campaigns across LinkedIn, TikTok, Facebook Ads, and generating automated revenue streams via platforms like Gumroad.",
        "ai_bot_title": "🤖 Digital Supermarket AI Agent (Instant Response)",
        "ai_bot_prompt": "Ask our smart AI client about commerce, marketing, automation, or your lifegoals:",
        "ai_bot_btn": "Send Inquiry",
        "products": {
            "p1_name": "AI Legal Agent Pro",
            "p1_desc": "The digital legal assistant for precise drafting, reviewing of contracts, and predicting judgments.",
            "p2_name": "Automatisation des Processus (LPA)",
            "p2_desc": "Complete automation to link routine tasks, data entry, and electronic invoicing.",
            "p3_name": "Contrat de Fusion & d'Intégration Globale",
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
        "about_firm": "🏢 À propos de notre Institution Digitale & Composants",
        "about_desc": "Une entreprise technologique de pointe intégrant l'IA et l'automatisation pour concevoir l'infrastructure juridique et commerciale globale.",
        "exp_title": "🎯 Notre Expertise Multi-Plateformes & Activités",
        "exp_desc": "Maîtrise totale du déploiement de produits digitaux, marketing global, campagnes publicitaires ciblées sur LinkedIn, TikTok, Facebook Ads, et monétisation automatisée sur des plateformes telles que Gumroad.",
        "ai_bot_title": "🤖 Agent IA du Supermarché Digital (Réponse Instantanée)",
        "ai_bot_prompt": "Posez vos questions sur le commerce, le marketing, l'automatisation ou vos objectifs de vie :",
        "ai_bot_btn": "Envoyer la Demande",
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
# 5. القائمة الجانبية (إدارة اللغات والتصنيفات)
# ==========================================
with st.sidebar:
    st.markdown('<div class="sidebar-title">ADID AL-EID</div>', unsafe_allow_html=True)
    
    selected_lang = st.selectbox("🌐 Choose Language / اختر اللغة / Choisir la Langue", list(lexicon.keys()))
    ctx = lexicon[selected_lang]
    
    st.markdown(f'<p style="text-align:center; color:#64748b; font-size:12px; margin-top:-5px;">{ctx["subtitle"]}</p>', unsafe_allow_html=True)
    st.divider()
    
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
# 6. محتوى الصفحة الرئيسية (المحدثة بألوان العلم والخانات الاستشارية)
# ==========================================
if current_page == "HOME":
    # 🇩🇿 هيدر ألوان علم الجزائر في واجهة الرئسية لإرضاء السلطات المحلية وتنظيم المظهر البصري الوطني
    st.markdown("""
        <div class="dz-banner">
            <div class="dz-green"></div>
            <div class="dz-white"></div>
            <div class="dz-red"></div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="text-align:center; padding:10px;">
        <div class="logo-l">L</div>
        <h1 style="font-size:45px; font-weight:900; color:#0f172a;">{ctx['main_title']}</h1>
        <h2 style="color:#334155; font-size:22px;">{ctx['main_desc']}</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # شبكة العرض التفاعلية لخانات التعريف والخبرات
    st.divider()
    col_info1, col_info2 = st.columns(2)
    
    with col_info1:
        st.markdown(f"""
        <div class="info-card">
            <h3>{ctx['about_firm']}</h3>
            <p style="text-align: justify; line-height: 1.6; color:#334155;">{ctx['about_desc']}</p>
            <span style="font-size:12px; color:#64748b;">💎 Zero Paper mandate initialized.</span>
        </div>
        """, unsafe_allow_html=True)
        
    with col_info2:
        st.markdown(f"""
        <div class="info-card">
            <h3>{ctx['exp_title']}</h3>
            <p style="text-align: justify; line-height: 1.6; color:#334155;">{ctx['exp_desc']}</p>
            <span style="font-size:12px; color:#64748b;">🚀 Maximizing digital product margins.</span>
        </div>
        """, unsafe_allow_html=True)

    # 🤖 خانة الاتصال والاستفسار: رد عميل الذكاء الاصطناعي (صاحب السوبرماركت الرقمي الشامل)
    st.markdown(f"### {ctx['ai_bot_title']}")
    user_query = st.text_input(ctx["ai_bot_prompt"])
    
    if st.button(ctx["ai_bot_btn"]):
        if user_query:
            # محاكاة الردود الذكية والشاملة القائمة على عولمة التجارة والأتمتة والوظائف الحقيقية وتحويل المعلومة لمال
            responses = [
                "Welcome to the Digital Supermarket! Transforming theoretical ideas into pure automated profits on Gumroad, LinkedIn, and TikTok is our core asset. Your plan is bulletproof, expand it globally!",
                "أهلاً بك في السوبرماركت الرقمي الشامل! كل جانب في الحياة يمكن أتمتته وتحويل معلوماته إلى عمولات أرباح عبر إعلانات تيك توك وفايسبوك ادس ولينكد إن. مشروعك جاهز لربطه بوظيفة حقيقية فوراً.",
                "Bienvenue au Supermarché Digital! Notre infrastructure d'automatisation intègre vos flux de commerce électronique de manière transparente pour maximiser vos marges nettes. Exécutez maintenant!"
            ]
            selected_resp = random.choice(responses) if "English" in selected_lang or "Français" in selected_lang else responses[1]
            st.session_state["chat_history"].append((user_query, selected_resp))
            
    # عرض سجل حوارات المستشار الرقمي
    for q, r in reversed(st.session_state["chat_history"]):
        st.info(f"**💬 Q:** {q}")
        st.success(f"**🤖 AI:** {r}")

# ==========================================
# 7. نظام عرض المنتجات (مع حماية وثبات الكود السابق والصور الثلاث)
# ==========================================
else:
    st.markdown(f"<h1 style='color:#0f172a;'>{selected_radio}</h1>", unsafe_allow_html=True)
    
    # البيانات البرمجية للصور الثلاث مع الحفاظ التام على كامل الخيارات السابقة
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
            
            # الخيارات التفاعلية للصور الثلاث كاملة وبدون تغيير الكود الأصلي
            with st.expander(ctx["expander_title"]):
                st.write(f"**{ctx['prod_summary']}** {item['desc']}")
                
                quantity = st.number_input(ctx["prod_qty"], min_value=1, max_value=100, value=1, key=f"qty_{idx}_{ctx['lang_code']}")
                
                user_search = st.text_input(ctx["prod_ask"], key=f"ask_{idx}_{ctx['lang_code']}")
                if user_search:
                    st.info(ctx["prod_tip"])
                
                st.divider()
                
                # تحميل مستند العقد والشرك بصيغة PDF
                pdf_content = f"Product: {item['name']}\nPrice: {item['price']}\nDescription: {item['desc']}\nGenerated officially by Adid Al-Eid Infrastructure."
                st.download_button(
                    label=ctx["pdf_btn"],
                    data=pdf_content,
                    file_name=f"{item['name']}_{ctx['lang_code']}.pdf",
                    mime="application/pdf",
                    key=f"pdf_{idx}_{ctx['lang_code']}"
                )
            
            # زر الشراء وإضافة المنتجات إلى السلة
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
    <p style="margin:2px;">{ctx['footer_desc']} | Build v11.9 Global Nexus</p>
</div>
""", unsafe_allow_html=True)
