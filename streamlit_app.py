import streamlit as st
import streamlit.components.v1 as components
import random

# 1. إعدادات المنصة الرقمية العالمية v12.6 (إصلاح الصور والبيانات الشامل)
st.set_page_config(
    page_title="Adid Al-Eid | Global Digital Platform",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. إدارة الحالة البرمجية لسلة المشتريات والدردشة التفاعلية
if "cart" not in st.session_state: st.session_state["cart"] = []
if "chat_history" not in st.session_state: st.session_state["chat_history"] = []

# 3. محرك التصميم البصري المتقدم لضمان الأناقة الاحترافية للمنصة (تم تعديل اللون الأبيض إلى أزرق فاتح/بحري)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght=300;400;700;900&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        background: #e0f2fe !important; /* لون أزرق بحري فاتح ومريح */
        color: #1e293b !important;
        font-family: 'Cairo', sans-serif !important;
    }

    [data-testid="stSidebar"] {
        background: #f0f9ff !important; /* لون متناسق مع السيرفر والخلفية البحرية */
        border-right: 2px solid #bae6fd !important;
    }
    
    .sidebar-title {
        color: #0f172a;
        font-size: 26px; font-weight: 900; text-align: center;
        margin-bottom: 5px; text-transform: uppercase;
    }

    .stRadio div[role="radiogroup"] label {
        background: #ffffff !important;
        border: 1px solid #bae6fd !important;
        padding: 10px 15px !important;
        border-radius: 10px !important;
        color: #334155 !important;
        font-weight: 600 !important;
        font-size: 15px !important;
        margin-bottom: 5px !important;
    }

    /* 🇩🇿 تصميم هيدر علم الجزائر */
    .dz-banner {
        display: flex;
        height: 12px;
        width: 100%;
        border-radius: 4px;
        overflow: hidden;
        margin-bottom: 10px;
    }
    .dz-green { background-color: #006633; flex: 1; }
    .dz-white { background-color: #ffffff; flex: 1; }
    .dz-red { background-color: #d21034; flex: 1; }
    
    /* 🏛️ شريط الخانات العلوي المقتبس من الهياكل الرسمية */
    .justice-navbar {
        display: flex;
        justify-content: space-between;
        background-color: #f8fafc;
        border: 1px solid #cbd5e1;
        border-top: 4px solid #006633;
        border-radius: 8px;
        padding: 8px;
        margin-bottom: 20px;
        direction: rtl;
    }
    .nav-item-box {
        flex: 1;
        text-align: center;
        padding: 8px 5px;
        margin: 0 4px;
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 6px;
        font-weight: 700;
        font-size: 14px;
        color: #0f172a;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        transition: all 0.2s ease;
    }
    .nav-item-box:hover {
        background: #006633;
        color: #ffffff;
        border-color: #006633;
    }

    /* تصميم بطاقات عرض معلومات البنية التحتية والمكونات */
    .info-card {
        background: #ffffff;
        border-left: 5px solid #006633;
        border-right: 5px solid #d21034;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }

    /* تصميم بطاقات المنتجات والخدمات */
    .product-card {
        background: #ffffff; border: 1px solid #e2e8f0; border-radius: 16px;
        padding: 20px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 15px;
    }
    .product-img { width: 100%; height: 160px; border-radius: 8px; object-fit: cover; }
    .product-price { color: #006633; font-size: 24px; font-weight: 800; margin: 10px 0; }

    /* 🔄 تأثير الأنميشن لشريط الصور المتحرك */
    @keyframes scroll {
        0% { transform: translateX(0); }
        100% { transform: translateX(calc(-310px * 6)); }
    }
    .slider-container {
        overflow: hidden;
        width: 100%;
        position: relative;
        padding: 10px 0;
    }
    .slider-track {
        display: flex;
        width: calc(310px * 12);
        animation: scroll 30s linear infinite;
    }
    .slider-track:hover {
        animation-play-state: paused;
    }
    .slide-img {
        width: 290px;
        height: 180px;
        object-fit: cover;
        border-radius: 12px;
        margin: 0 10px;
        border: 2px solid #006633;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 4. قاموس البيانات والترجمة
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
        "pdf_btn": "📥 تحميل مستند العقد والشراكة (PDF)",
        "add_cart_btn": "🛒 أضف للسلة",
        "toast_msg": "تمت إضافة {qty} نسخة من {name} إلى السلة",
        "footer_title": "مؤسسة عديد العيد العالمية للرقمنة",
        "footer_desc": "المقر الرئيسي للأتمتة والسيادة الرقمية | 2026 جميع الحقوق محفوظة",
        "about_firm": "🏢 التعريف بالمؤسسة الرقمية ومكوناتها",
        "about_desc": "مؤسسة تكنولوجية رائدة تدمج الذكاء الاصطناعي والأتمتة لتطوير البنى التحتية القانونية والتجارية للمؤسسات حول العالم وضمان إلغاء المعاملات الورقية.",
        "exp_title": "🎯 خبراتنا ونشاطنا العابر للمنصات",
        "exp_desc": "خبرة متكاملة في إدارة المشاريع الرقمية، التسويق الإلكتروني، وإدارة الحملات الإعلانية على المنصات الرسمية مثل LinkedIn و TikTok و Facebook Ads وتحقيق الأرباح عبر بيع المنتجات على Gumroad وأتمتة العمليات للتجارة الإلكترونية.",
        "ai_bot_title": "🤖 مستشار السوبرماركت الرقمي الشامل للرد الفوري",
        "ai_bot_prompt": "اسأل العميل الذكي عن أي شيء يخص التجارة والتسويق وأتمتة شؤون الحياة ومشاريعك:",
        "ai_bot_btn": "إرسال الاستفسار",
        "nav_tabs": ["🏢 المؤسسة", "💼 الخدمات الرقمية", "⚖️ حوكمة الأتمتة", "🌐 التعاون الدولي", "📢 الإعلام الرقمي", "📞 اتصل بنا والاستفسار"]
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
        "nav_tabs": ["🏢 Institution", "💼 Services", "⚖️ Automation Governance", "🌐 Int. Cooperation", "📢 Digital Media", "📞 Contact & Inquiry"]
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
        "nav_tabs": ["🏢 Institution", "💼 Services", "⚖️ Gouvernance", "🌐 Coopération Int.", "📢 Médias", "📞 Contact & Demande"]
    }
}

# ==========================================
# 5. القائمة الجانبية
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
# 6. محتوى الصفحة الرئيسية الأساسية والثابتة للمنصة
# ==========================================
if current_page == "HOME":
    # 🇩🇿 هيدر ألوان علم الجزائر للامتثال والاتساق الوطني
    st.markdown("""
        <div class="dz-banner">
            <div class="dz-green"></div>
            <div class="dz-white"></div>
            <div class="dz-red"></div>
        </div>
    """, unsafe_allow_html=True)

    # 🏛️ بناء شريط الخانات الصغيرة المتراصة في الأعلى
    nav_html = f"""
    <div class="justice-navbar">
        <div class="nav-item-box">{ctx['nav_tabs'][0]}</div>
        <div class="nav-item-box">{ctx['nav_tabs'][1]}</div>
        <div class="nav-item-box">{ctx['nav_tabs'][2]}</div>
        <div class="nav-item-box">{ctx['nav_tabs'][3]}</div>
        <div class="nav-item-box">{ctx['nav_tabs'][4]}</div>
        <div class="nav-item-box">{ctx['nav_tabs'][5]}</div>
    </div>
    """
    st.markdown(nav_html, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="text-align:center; padding:5px;">
        <h1 style="font-size:42px; font-weight:900; color:#0f172a; margin-top:10px;">{ctx['main_title']}</h1>
        <h2 style="color:#334155; font-size:20px; font-weight:400;">{ctx['main_desc']}</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # 💻 محرك عرض الصور المتحركة - يحتوي على 6 صور متخصصة في الرقمنة والمكاتب والمؤسسات
    images_pool = [
        "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600",  # الرقمنة والبيانات
        "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600",  # أجهزة حواسيب مكاتب
        "https://images.unsplash.com/photo-1497366216548-37526070297c?w=600",  # مكاتب ومؤسسات حديثة
        "https://images.unsplash.com/photo-1531403009284-440f080d1e12?w=600",  # واجهات عمل رقمية ومؤسسات صغيرة
        "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=600",  # تخطيط مالي ورقمي
        "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=600"   # عمل جماعي في شركة تقنية
    ]
    
    # بناء الـ Slider البرمجي عبر HTML والـ CSS لضمان حركة انسيابية لا تتوقف ومستمرة
    slider_html = f"""
    <div class="slider-container">
        <div class="slider-track">
            <!-- الـ 6 صور الأساسية -->
            <img src="{images_pool[0]}" class="slide-img">
            <img src="{images_pool[1]}" class="slide-img">
            <img src="{images_pool[2]}" class="slide-img">
            <img src="{images_pool[3]}" class="slide-img">
            <img src="{images_pool[4]}" class="slide-img">
            <img src="{images_pool[5]}" class="slide-img">
            <!-- تكرار الصور برمجياً لضمان حركة سلسة وبدون فراغات أثناء الحركة الدائرية -->
            <img src="{images_pool[0]}" class="slide-img">
            <img src="{images_pool[1]}" class="slide-img">
            <img src="{images_pool[2]}" class="slide-img">
            <img src="{images_pool[3]}" class="slide-img">
            <img src="{images_pool[4]}" class="slide-img">
            <img src="{images_pool[5]}" class="slide-img">
        </div>
    </div>
    """
    components.html(slider_html, height=210)
    
    # شبكة الخانات التعريفية بالخبرات والمكونات والنشاط التجاري الإلكتروني
    st.divider()
    col_info1, col_info2 = st.columns(2)
    
    with col_info1:
        st.markdown(f"""
        <div class="info-card">
            <h3>{ctx['about_firm']}</h3>
            <p style="text-align: justify; line-height: 1.6; color:#334155;">{ctx['about_desc']}</p>
            <span style="font-size:12px; color:#64748b;">⚙️ Infrastructure Active.</span>
        </div>
        """, unsafe_allow_html=True)
        
    with col_info2:
        st.markdown(f"""
        <div class="info-card">
            <h3>{ctx['exp_title']}</h3>
            <p style="text-align: justify; line-height: 1.6; color:#334155;">{ctx['exp_desc']}</p>
            <span style="font-size:12px; color:#64748b;">💰 Commission Arbitrage Enabled.</span>
        </div>
        """, unsafe_allow_html=True)

    # 🤖 خانة الاستفسار والاتصال الفوري
    st.markdown(f"### {ctx['ai_bot_title']}")
    user_query = st.text_input(ctx["ai_bot_prompt"])
    
    if st.button(ctx["ai_bot_btn"]):
        if user_query:
            responses = [
                "Welcome to the Digital Supermarket Hub! Your lifegoals, e-commerce products, and social media campaigns on Gumroad, TikTok, and LinkedIn are fully optimized here to generate high-efficiency margins.",
                "مرحباً بك في نظام السوبرماركت الرقمي الشامل الذي يمس كل جوانب الحياة! هدفنا الأساسي هو تحويل كل فكرة ومعلومة نظرية إلى تطبيق حقيقي مدر للربح والعمولات عبر أتمتة الحملات والبيع على قامرود، لينكد إن، وتيك توك وفايسبوك آدس.",
                "Bienvenue sur l'infrastructure du Supermarché Digital! Chaque aspect opérationnel est automatisé para convertir les informations stratégiques en commissions nettes sur LinkedIn et Gumroad."
            ]
            selected_resp = random.choice(responses) if "English" in selected_lang or "Français" in selected_lang else responses[1]
            st.session_state["chat_history"].append((user_query, selected_resp))
            
    for q, r in reversed(st.session_state["chat_history"]):
        st.info(f"**💬 Q:** {q}")
        st.success(f"**🤖 AI:** {r}")

# ==========================================
# 7. نظام عرض المنتجات المطور والمصلح بالكامل
# ==========================================
else:
    st.markdown(f"<h1 style='color:#0f172a;'>{selected_radio}</h1>", unsafe_allow_html=True)
    
    if current_page == "AGENTS":
        badge_icon = "🤖"
        products_pool = [
            {
                "name": "Legal AI Assistant Pro" if ctx["lang_code"] == "en" else "مساعد القانون الذكي المحترف" if ctx["lang_code"] == "ar" else "Assistant Juridique IA Pro",
                "price": "5,000$",
                "img": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=500",
                "desc": "تحليل مستندات القضايا واستخراج الثغرات بدقة متناهية."
            },
            {
                "name": "Contract Analytical Agent" if ctx["lang_code"] == "en" else "عميل تحليل ومراجعة العقود" if ctx["lang_code"] == "ar" else "Agent d'Analyse de Contrats",
                "price": "4,200$",
                "img": "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=500",
                "desc": "مراجعة بنود الاتفاقيات الدولية ومطابقتها للقوانين تلقائياً."
            },
            {
                "name": "Judicial Predictive Engine" if ctx["lang_code"] == "en" else "محرك التنبؤ بالأحكام القضائية" if ctx["lang_code"] == "ar" else "Moteur de Prédiction Judiciaire",
                "price": "15,000$",
                "img": "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=500",
                "desc": "التنبؤ بنسبة نجاح القضايا بناءً على الأرشيف القضائي الرقمي."
            }
        ]
    elif current_page == "AUTO":
        badge_icon = "⚡"
        products_pool = [
            {
                "name": "Workflow Automation Nexus (n8n)" if ctx["lang_code"] == "en" else "نظام ربط وأتمتة سير العمل" if ctx["lang_code"] == "ar" else "Liaison d'Automatisation n8n",
                "price": "3,800$",
                "img": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=500",
                "desc": "ربط الأنظمة لضمان تدفق البيانات الرقمية تلقائياً وبسرعة فائقة لإنهاء المعاملات الورقية."
            },
            {
                "name": "E-Invoicing Automated Core" if ctx["lang_code"] == "en" else "محرك الفوترة والتحصيل الإلكتروني" if ctx["lang_code"] == "ar" else "Noyau de Facturation Électronique",
                "price": "4,500$",
                "img": "https://images.unsplash.com/photo-1504639725590-34d0984388bd?w=500",
                "desc": "إصدار وإرسال الفواتير ومتابعة المدفوعات أوتوماتيكياً دون تدخل بشري لتوفير الوقت."
            },
            {
                "name": "Digital Archiving Syncer" if ctx["lang_code"] == "en" else "نظام المزامنة والأرشفة السحابية" if ctx["lang_code"] == "ar" else "Synchroniseur d'Archivage Numérique",
                "price": "6,000$",
                "img": "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=500",
                "desc": "أرشفة وحماية المستندات بشكل فوري ومستمر لضمان أعلى مستويات الأمان والسيادة الرقمية."
            }
        ]
    else:
        badge_icon = "🔗"
        products_pool = [
            {
                "name": "Global Merger Constitution" if ctx["lang_code"] == "en" else "عقد الاندماج والتحالف المؤسسي العالمي" if ctx["lang_code"] == "ar" else "Contrat de Fusion Globale",
                "price": "12,500$",
                "img": "https://images.unsplash.com/photo-1450133064473-71024230f91b?w=500",
                "desc": "حوكمة وصياغة تكامل الشركات الكبرى وتأمين الاستثمارات العابرة للحدود."
            },
            {
                "name": "Data Integration Governance Agreement" if ctx["lang_code"] == "en" else "اتفاقية حوكمة وتكامل البيانات الرقمية" if ctx["lang_code"] == "ar" else "Accord de Gouvernance des Données",
                "price": "9,800$",
                "img": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=500",
                "desc": "صياغة الشروط القانونية لنقل وتبادل البيانات الرقمية بين الفروع الدولية والشركاء."
            },
            {
                "name": "International Tech Venture Framework" if ctx["lang_code"] == "en" else "عقد الشراكة والاستثمار التكنولوجي الدولي" if ctx["lang_code"] == "ar" else "Cadre d'Investissement Technologique Inter",
                "price": "18,000$",
                "img": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=500",
                "desc": "تنظيم أطر الاستثمار المشترك في البنى التحتية الرقمية وحماية الملكية الفكرية."
            }
        ]

    cols = st.columns(3)
    
    for idx, item in enumerate(products_pool):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="product-card">
                <div style="font-size: 32px; margin-bottom: 5px;">{badge_icon}</div>
                <img src="{item['img']}" class="product-img">
                <h3 style="color:#0f172a; margin-top:10px;">{item['name']}</h3>
                <div class="product-price">{item['price']}</div>
            </div>
            """, unsafe_allow_html=True)
            
            with st.expander(ctx["expander_title"]):
                st.write(f"**{ctx['prod_summary']}** {item['desc']}")
                
                quantity = st.number_input(ctx["prod_qty"], min_value=1, max_value=100, value=1, key=f"qty_{idx}_{ctx['lang_code']}")
                
                user_search = st.text_input(ctx["prod_ask"], key=f"ask_{idx}_{ctx['lang_code']}")
                if user_search:
                    st.info(ctx["prod_tip"])
                
                st.divider()
                
                pdf_content = f"Product: {item['name']}\nPrice: {item['price']}\nDescription: {item['desc']}\nGenerated officially by Adid Al-Eid Infrastructure."
                st.download_button(
                    label=ctx["pdf_btn"],
                    data=pdf_content,
                    file_name=f"{item['name']}_{ctx['lang_code']}.pdf",
                    mime="application/pdf",
                    key=f"pdf_{idx}_{ctx['lang_code']}"
                )
            
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
    <p style="margin:2px;">{ctx['footer_desc']} | Build v12.6 Refactored Imagery Architecture</p>
</div>
""", unsafe_allow_html=True)
