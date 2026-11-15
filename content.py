# Site text and settings for both languages.
# Projects, news and service page texts are in the data/ folder.

COMPANY = {
    "email": "info@omrantech.com",
    "phones": ["+966564623847", "+966563314948", "+966920017424"],
    "linktree": "https://linktr.ee/omran_tech_group",
    # Social accounts: (English name, Arabic name, X link, Instagram link)
    "social": [
        ("Hakeem Al-Emaar", "حكيم الإعمار", "https://twitter.com/hkym_11", "https://www.instagram.com/hkym_112/"),
        ("Dr. Ali Al-Jouf Office", "مكتب د. علي الجوف", "https://twitter.com/dralialjouf", "https://www.instagram.com/dr_alialjouf/"),
    ],
}

# The AI assistant has its own website. Change this link when it's ready.
AI_URL = "https://ai.omrantech.com"

AI = {
    "en": {
        "nav": "AI Assistant",
        "badge": "New",
        "kicker": "New: Omran Tech AI",
        "title": "Meet our <em>AI assistant.</em>",
        "text": "Get instant answers about our services, projects and modern building methods like Light Gauge Steel, and take the first step toward your project any time of day.",
        "points": [
            "Questions about our services and departments",
            "Modern construction: LGS, Hollow Core, Precast",
            "A quick first step toward your project",
        ],
        "button": "Try the AI assistant",
        "chat_name": "Omran Tech AI",
        "chat_status": "Online",
        "chat_questions": [
            "What is Light Gauge Steel construction?",
            "Which of your services fit a residential villa?",
            "How do I start a project with you?",
        ],
        "chat_input": "Ask anything about building...",
        "contact_title": "Need a quick answer?",
        "contact_text": "Ask our AI assistant on its own website.",
    },
    "ar": {
        "nav": "المساعد الذكي",
        "badge": "جديد",
        "kicker": "جديد: عمران تك AI",
        "title": "تعرّف على <em>مساعدنا الذكي.</em>",
        "text": "احصل على إجابات فورية عن خدماتنا ومشاريعنا وتقنيات البناء الحديث مثل الحديد البارد، وابدأ أول خطوة نحو مشروعك في أي وقت.",
        "points": [
            "استفسارات عن خدماتنا وأقسامنا",
            "البناء الحديث: الحديد البارد، الهولوكور، الخرسانة مسبقة الصب",
            "خطوة أولى سريعة نحو مشروعك",
        ],
        "button": "جرّب المساعد الذكي",
        "chat_name": "عمران تك AI",
        "chat_status": "متصل",
        "chat_questions": [
            "ما هو البناء بالحديد البارد؟",
            "أي خدماتكم تناسب فيلا سكنية؟",
            "كيف أبدأ مشروعي معكم؟",
        ],
        "chat_input": "اسأل أي شيء عن البناء...",
        "contact_title": "تحتاج إجابة سريعة؟",
        "contact_text": "اسأل مساعدنا الذكي على موقعه الخاص.",
    },
}

# Images
LOGO = "media/logo.png"
HERO_IMAGE = "media/hero.jpg"
ABOUT_IMAGES = ["media/about-1.jpg", "media/about-2.jpg", "media/lgs-frame.jpg"]
LGS_VIDEO = "media/lgs-construction.mp4"
LGS_POSTER = "media/lgs-frame.jpg"
PARTNERS = [f"media/partners/partner-{i:02d}.jpg" for i in range(1, 27)]

CERTIFICATES = [
    ("media/certificates/cert-01.jpg", "Great Place To Work", "بيئة عمل رائعة"),
    ("media/certificates/cert-02.png", "Best Contractor Award", "جائزة أفضل مقاول"),
    ("media/certificates/cert-03.png", "Ministry of Health", "وزارة الصحة"),
    ("media/certificates/cert-04.png", "LGS Overview Workshop", "ورشة عمل نظرة عامة عن الحديد البارد"),
    ("media/certificates/cert-05.jpg", "Certificate of Appreciation", "شهادة تقدير"),
    ("media/certificates/cert-06.jpg", "Certificate of Appreciation", "شهادة تقدير"),
    ("media/certificates/cert-07.jpg", "Mehnati: Thanks & Appreciation", "شكر وتقدير مهنتي"),
    ("media/certificates/cert-08.jpg", "Mosques, Da'wah & Guidance Administration", "شكر إدارة المساجد والدعوة والإرشاد"),
]

# Services. The full text of each one is in data/pages.json
SERVICES = [
    {
        "slug": "architecture", "icon": "compass", "image": "media/services/architecture.jpg",
        "en": ("Architecture", "Architectural design at every stage, from the first idea to the full executive plans."),
        "ar": ("الهندسة المعمارية", "مختصون في تقديم خدمات التصميم المعماري بكافة مراحله بدءًا من إعداد التصاميم وانتهاءً بالمخططات التنفيذية."),
    },
    {
        "slug": "safety-electromechanics", "icon": "shield", "image": "media/services/safety-electromechanics.jpg",
        "en": ("Safety & Electromechanics", "Our engineers set up the rules and procedures for safety and occupational health on site."),
        "ar": ("السلامة والإلكتروميكانيك", "يعمل المهندسون على إعداد وتطوير أسس وقواعد وإجراءات السلامة والصحة المهنية بموقع العمل."),
    },
    {
        "slug": "structural-engineering", "icon": "beam", "image": "media/services/structural-engineering.jpg",
        "en": ("Structural Engineering & Project Management", "An experienced structural team, plus a supervision department that follows every project."),
        "ar": ("الهندسة الإنشائية وإدارة المشاريع", "يمتلك المكتب كادرًا متميزًا في القسم الإنشائي من المهندسين ذوي الخبرة العالية، مع قسم للإشراف والمتابعة."),
    },
    {
        "slug": "survey-engineering", "icon": "survey", "image": "media/services/survey-engineering.jpg",
        "en": ("Survey Engineering", "Surveying engineers and technicians, certified by the Eastern Province Municipality."),
        "ar": ("هندسة المساحة", "مهندسون وفنيون من ذوي الخبرة بالرفع المساحي والأجهزة والتقنيات المساحية، معتمدون من أمانة المنطقة الشرقية."),
    },
    {
        "slug": "real-estate-sorting", "icon": "grid", "image": "media/services/real-estate-sorting.jpg",
        "en": ("Real Estate & Land Sorting", "Splitting properties and buildings into separate units, each with its own deed."),
        "ar": ("الفرز العقاري والأراضي", "تقسيم العقارات أو المباني أو المجمعات العقارية إلى عدة وحدات، يتم تخصيص كل وحدة بكافة مواصفاتها."),
    },
    {
        "slug": "output-development", "icon": "layers", "image": "media/services/output-development.jpg",
        "en": ("Output & Development", "Smart solutions for interior spaces that add real value to existing and new buildings."),
        "ar": ("الإخراج والتطوير", "ندرك فن التعامل مع الفراغات الداخلية لإيجاد الحلول المناسبة لها بما يحقق الراحة النفسية ويضيف قيمة للمباني."),
    },
    {
        "slug": "pools", "icon": "wave", "image": "media/services/pools.jpg",
        "en": ("Pool Installation & Construction", "Pools, fountains, steam rooms and jacuzzis: built, equipped and maintained."),
        "ar": ("إنشاء وتركيب المسابح", "إنشاء المسابح والشلالات وغرف البخار والجاكوزي وتركيب معداتها وصيانتها بأحدث التقنيات والأدوات."),
    },
    {
        "slug": "lgs-machine", "icon": "machine", "image": "media/services/lgs-machine.jpg",
        "en": ("LGS Machine", "We supply Light Gauge Steel machines to factories, with training and one year of free remote support."),
        "ar": ("آلة الحديد البارد", "نوفر آلات الحديد البارد للمصانع مع تدريب المهندس المختص ودعم فني مجاني عن بُعد لمدة سنة كاملة."),
    },
]

# Departments: (name, company, short description)
DEPARTMENTS = [
    {
        "slug": "engineering-consultancy", "image": "media/departments/engineering-consultancy.jpg",
        "en": ("Engineering Consultancy", "Ali Fahad Al-Jouf Engineering & Safety Consultancy",
               "Engineering consultancy, architectural and interior design, site coordination, supervision, surveying and project management."),
        "ar": ("الاستشارات الهندسية", "شركة علي فهد الجوف للاستشارات الهندسية والسلامة",
               "نخبة من ذوي الخبرة والكفاءة يقدمون الاستشارات الهندسية والتصميم المعماري والداخلي وتنسيق المواقع والإشراف والمساحة وإدارة المشاريع."),
    },
    {
        "slug": "architectural-contracting", "image": "media/departments/architectural-contracting.jpg",
        "en": ("Architectural Contracting", "Hakeem Al-Emaar Architectural Contracting",
               "Modern construction with Light Steel Structure, Hollow Core and Precast, in line with Saudi Vision 2030."),
        "ar": ("المقاولات المعمارية", "مؤسسة حكيم الإعمار للمقاولات المعمارية",
               "تقنيات البناء الحديثة مثل الحديد البارد والهولوكور والخرسانة مسبقة الصب، بما يتوافق مع رؤية المملكة 2030."),
    },
    {
        "slug": "factory", "image": "media/departments/factory.jpg",
        "en": ("Factory", "Qemt Al Omran Industrial Factory",
               "One of the leading factories for Light Gauge Steel, aluminium and glass, with modern production lines."),
        "ar": ("المصنع", "مصنع قمة العمران للصناعة",
               "من أبرز المصانع في مجال صناعة الحديد البارد والألمنيوم والزجاج، بخطوط إنتاج حديثة لمنتجات فائقة التحمل."),
    },
    {
        "slug": "interior-finishes", "image": "media/departments/interior-finishes.jpg",
        "en": ("Interior Finishes & Decoration", "Hakeem Al-Emaar Workshop",
               "Interior finishes, woodwork and décor by skilled craftsmen, including WPC and UPVC doors and windows."),
        "ar": ("التشطيبات الداخلية والديكور", "معرض حكيم الإعمار",
               "تشطيبات داخلية وأعمال خشب وديكور بأيدي حرفيين مهرة، بما في ذلك أبواب ونوافذ WPC و UPVC."),
    },
    {
        "slug": "environmental-services", "image": "media/departments/environmental-services.jpg",
        "en": ("Environmental Services", "ESSCO, Environmental Services Supporting Testing Co.",
               "Geotechnical investigations, materials testing and surveys for sand, aggregates, concrete, asphalt and more."),
        "ar": ("الخدمات البيئية", "ESSCO، شركة الخدمات البيئية المساندة للاختبارات",
               "تحريات جيوتقنية واختبارات مواد ومسوحات للرمل والركام والخرسانة والأسفلت وغيرها وفق معايير جودة صارمة."),
    },
]

PROCESS = {
    "en": [
        ("Tell us about your need", "Send us the details that help us understand the type and area of your building."),
        ("Share your ideas and taste", "Our architect turns your ideas into a design that suits you."),
        ("Receive your designs", "2D and 3D designs, together with the building permit."),
        ("We build it", "Built to high quality, following the latest standards and technologies."),
        ("Receive your space ready", "Your space is handed over the way you imagined it, ready to use."),
    ],
    "ar": [
        ("أخبرنا عن احتياجك", "أرسل لنا تفاصيل تساعدنا لمعرفة نوع مساحة البناء."),
        ("شارك المهندس أفكارك وذوقك", "نترجمها لتصميم يناسب ذوقك."),
        ("استلم المخططات والتصاميم", "تصاميم 2D و 3D ورخصة البناء."),
        ("نحوّل تصاميمك إلى واقع", "يتم التنفيذ بجودة عالية وفقًا لأحدث المعايير والتقنيات."),
        ("استلم مساحتك جاهزة", "ستستلم مساحتك كما ترغب، جاهزة للاستخدام وفقًا لرؤيتك."),
    ],
}

TESTIMONIALS = {
    "en": [
        ("Choosing Omran Tech for our construction needs was one of the best decisions we've made. From the first planning steps to the final touches, the team was reliable and committed to excellence. They kept us updated, dealt with every concern quickly, and showed a level of integrity that's hard to find in this industry.", "Youssef Hussin"),
        ("Working with Omran Tech was an exceptional experience. They paid close attention to detail, and the quality of work and respect for deadlines went beyond our expectations. Communication was smooth throughout the project. We highly recommend Omran Tech for any construction project.", "Ahmed Mohamed"),
        ("We hired Omran Tech for our latest project and their professionalism was clear from day one. They understand the construction industry deeply, came up with smart solutions to problems, and finished the project on time and within budget.", "Mohamed El Shareef"),
    ],
    "ar": [
        ("كان اختيارنا لعمران تك لاحتياجات البناء من أفضل القرارات التي اتخذناها. من الخطوات التخطيطية الأولى إلى اللمسات الأخيرة، كان الفريق موثوقًا وملتزمًا بالتميز، وتواصل معنا بانتظام لإطلاعنا على التقدم، وعالج أي ملاحظة بسرعة، وأظهر مستوى من النزاهة يصعب العثور عليه في هذه الصناعة.", "يوسف حسين"),
        ("كانت تجربة العمل مع عمران تك استثنائية. كانوا يولون اهتمامًا خاصًا للتفاصيل، وكانت جودة العمل والالتزام بالمواعيد تتجاوز توقعاتنا. كان التواصل على مدار المشروع سلسًا، وكان الفريق دائمًا متجاوبًا مع احتياجاتنا. نوصي بشدة بعمران تك لأي مشروع بناء.", "أحمد محمد"),
        ("تعاقدنا مع عمران تك لمشروعنا الأخير، وكانت احترافيتهم وخبرتهم واضحة من اليوم الأول. أظهروا فهمًا عميقًا لصناعة البناء، وقدموا حلولًا مبتكرة للتحديات، وضمنوا الانتهاء من المشروع في الوقت المحدد وضمن الميزانية.", "محمد الشريف"),
    ],
}

LGS_BENEFITS = {
    "en": ["Fast to build", "Eco-friendly", "Light, easy to transport and install", "Easy to recycle",
           "High heat and sound insulation", "Far fewer errors than concrete", "Rust-proof, lasts 150+ years",
           "High earthquake and fire resistance"],
    "ar": ["سرعة التنفيذ", "صديق ممتاز للبيئة", "خفيف وسهل النقل والتركيب", "سهل إعادة التدوير",
           "كفاءة عالية للعزل الحراري والصوتي", "نسبة خطأ أقل بكثير من البناء الخرساني", "مقاوم للصدأ بعمر افتراضي يتجاوز 150 عامًا",
           "مقاومة عالية للزلازل والحرائق"],
}

BRANCHES = {
    "en": [
        ("Riyadh", "Anas Ibn Malik Rd, Al Yasmin"),
        ("Al Khobar", "Al Jarbou Tower, Custodian of the Two Holy Mosques Rd"),
        ("AlUla", "AlUla"),
        ("Al-Ahsa, Al-Taraf", "Al-Taraf, Al-Ahsa"),
        ("Al-Ahsa, Al-Hofuf", "Al-Faisaliah District, Al-Hofuf"),
        ("Bahrain", "Kingdom of Bahrain"),
    ],
    "ar": [
        ("الرياض", "حي الياسمين، طريق أنس بن مالك"),
        ("الخبر", "برج الجربوع، طريق خادم الحرمين الشريفين"),
        ("العلا", "العلا"),
        ("الأحساء، الطرف", "الطرف، الأحساء"),
        ("الأحساء، الهفوف", "حي الفيصلية الأول، الهفوف"),
        ("البحرين", "مملكة البحرين"),
    ],
}

# Project filters: (tag, English, Arabic)
FILTERS = [
    ("contracting", "Architectural Contracting", "المقاولات المعمارية"),
    ("residential", "Residential", "سكني"),
    ("commercial", "Commercial", "تجاري"),
    ("fuel", "Fuel Stations", "محطات الوقود"),
    ("public", "Mosques, Schools & Clinics", "مساجد ومدارس وعيادات"),
    ("development", "Output & Development", "الإخراج والتطوير"),
    ("realestate", "Real Estate Sorting", "الفرز العقاري"),
]

# Projects shown on the home page
FEATURED_PROJECTS = [
    "portable-buildings", "amwaj-chalets", "drees-gas-station",
    "alula-chalets", "anime-town-boulevard-riyadh", "visitor-reception-center-at-imam-turki",
]

TEXT = {
    "en": {
        "dir": "ltr",
        "other": "ar",
        "other_name": "العربية",
        "brand": "Omran Tech Group",
        "short_name": "Omran Tech",
        "tagline": "Innovate · Design · Build",
        "nav": [("index", "Home"), ("about", "About"), ("services", "Services"), ("projects", "Projects"),
                ("news", "News"), ("articles", "Articles"), ("contact", "Contact")],
        "start_project": "Start a project",
        "menu": "Menu",
        "close": "Close",
        "skip": "Skip to content",

        "hero_kicker": "Innovate · Design · Build",
        "hero_title": "We build what's next, <em>faster, stronger, smarter.</em>",
        "hero_text": "A leading group certified by reputable institutions, specializing in modern construction such as Light Gauge Steel, Hollow Core ceilings and Precast. We make the whole process simple, from idea to handover.",
        "hero_button": "Explore our projects",
        "stats": [("1433", "AH, founded in Saudi Arabia"), ("projects", "Completed projects"),
                  ("5", "Specialized departments"), ("5", "Cities in KSA & Bahrain")],
        "techs": ["Light Gauge Steel", "Hollow Core", "Precast Concrete", "3D BIM", "Sandwich Panel",
                  "Aluminium & Glass", "Waterproofing", "Turnkey Delivery"],

        "dept_kicker": "Our departments",
        "dept_title": "Five specialists. One point of contact.",
        "dept_text": "Every discipline you need is under one roof, from the first sketch to the final handover.",
        "services_kicker": "What we offer",
        "services_title": "Engineering services, start to finish.",
        "process_kicker": "How we work",
        "process_title": "From your idea to a ready space in five steps.",
        "projects_kicker": "Selected work",
        "projects_title": "Projects that speak for themselves.",
        "lgs_kicker": "Why Light Gauge Steel",
        "lgs_title": "The modern way to build in the Gulf.",
        "lgs_text": "LGS makes construction faster and cheaper, and it insulates sound and resists wind, fire and mould. It's the ideal choice for building today.",
        "lgs_badge": "years lifespan, rust-proof",
        "reviews_kicker": "Client reviews",
        "reviews_title": "What our clients say.",
        "partners_title": "Success partners",
        "certs_kicker": "Recognition",
        "certs_title": "Certificates & achievements",
        "news_kicker": "Newsroom",
        "news_title": "Latest news",
        "cta_title": "Have a project in mind?",
        "cta_text": "Tell us what you need and our engineers will get back to you with the right solution.",

        "view_all": "View all",
        "learn_more": "Learn more",
        "all": "All",
        "previous": "Previous",
        "next": "Next",
        "gallery": "Gallery",
        "more_projects": "More projects",
        "project_details": "Project details",
        "why_us": "What sets us apart",
        "why_us_text": "We are always looking for new materials and methods. That lets us keep the quality high, work faster, lower costs and hand over projects sooner.",

        "about_title": "Design and build: the complete solution for architectural projects.",
        "vision": "Our vision",
        "mission": "Our mission",
        "values": "Our core values",
        "news_page": "News",
        "news_intro": "Exhibitions, awards and milestones from across the group.",
        "articles_page": "Articles",
        "articles_intro": "Articles about modern construction, Light Gauge Steel and architecture.",
        "projects_page": "Our projects",
        "projects_intro": "Villas, chalets, fuel stations, mosques, commercial and public buildings delivered by the group.",
        "services_page": "Our services",
        "services_intro": "Consultancy, design, engineering, surveying and construction by specialist teams across the group.",
        "contact_page": "Contact us",
        "contact_intro": "How can we help? Choose a topic and send us your request.",
        "service": "Service",

        "branches": "Our branches",
        "phone": "Phone",
        "email": "Email",
        "hours": "Working hours",
        "hours_list": [("Sunday - Thursday", "9:00 - 18:00"), ("Saturday", "9:00 - 13:00"), ("Friday", "Closed")],
        "follow": "Follow us",
        "links": "Quick links",
        "footer_text": "A team of experienced engineers working to give you the best choice and the right solution.",
        "rights": "All rights reserved.",

        "form_tabs": [("office", "Engineering Office"), ("contracting", "Architectural Contracting"),
                      ("lgs", "LGS Machines"), ("feedback", "Service Evaluation")],
        "name": "Full name",
        "phone_number": "Phone number",
        "branch": "Nearest branch",
        "choose": "Choose...",
        "has_plans": "Do you have the plans?",
        "is_designed": "Is the design already done?",
        "is_planned": "Has your building been planned in advance?",
        "has_factory": "Is there an existing factory?",
        "entity": "Who do you represent?",
        "company": "Company",
        "individual": "Individual",
        "company_name": "Company name",
        "wants_training": "Does your organization want training?",
        "your_service": "Which service did you receive?",
        "responsible": "Who was responsible for your service?",
        "heard_from": "Where did you hear about us?",
        "opinion": "What do you think of Omran Tech Group?",
        "difficulties": "Did you face any problems with customer service?",
        "suggestions": "Any suggestions to improve our services?",
        "message": "Message",
        "yes": "Yes",
        "no": "No",
        "send": "Send request",
        "form_note": "This opens your email app with your details filled in.",
        "form_branches": ["Riyadh", "Al Khobar", "AlUla", "Al-Ahsa, Al-Mubarraz", "Al-Ahsa, Al-Taraf"],
    },
    "ar": {
        "dir": "rtl",
        "other": "en",
        "other_name": "English",
        "brand": "مجموعة عمران تك",
        "short_name": "عمران تك",
        "tagline": "ابتكار · تصميم · بناء",
        "nav": [("index", "الرئيسية"), ("about", "من نحن"), ("services", "خدماتنا"), ("projects", "مشاريعنا"),
                ("news", "الأخبار"), ("articles", "المقالات"), ("contact", "تواصل معنا")],
        "start_project": "ابدأ مشروعك",
        "menu": "القائمة",
        "close": "إغلاق",
        "skip": "تخطَّ إلى المحتوى",

        "hero_kicker": "ابتكار · تصميم · بناء",
        "hero_title": "نبني المستقبل، <em>أسرع، أقوى، وأذكى.</em>",
        "hero_text": "مجموعة رائدة في مجال الهندسة في المملكة العربية السعودية، معتمدة من العديد من المؤسسات المرموقة، ومتخصصة في تقنيات البناء الحديث مثل الحديد البارد والأسقف المجوفة والخرسانة سابقة الصب. نبسّط عملية البناء برمتها من الفكرة إلى الاكتمال.",
        "hero_button": "استعرض مشاريعنا",
        "stats": [("1433", "هـ، سنة التأسيس"), ("projects", "مشروعًا منجزًا"),
                  ("5", "أقسام متخصصة"), ("5", "مدن في المملكة والبحرين")],
        "techs": ["الحديد البارد", "الهولوكور", "الخرسانة مسبقة الصب", "نمذجة BIM ثلاثية الأبعاد", "الساندويتش بانل",
                  "الألمنيوم والزجاج", "العزل المائي", "التسليم على المفتاح"],

        "dept_kicker": "أقسامنا",
        "dept_title": "خمسة أقسام متخصصة. جهة تواصل واحدة.",
        "dept_text": "من الفكرة الأولى حتى التسليم النهائي، كل التخصصات التي تحتاجها تحت سقف واحد.",
        "services_kicker": "ما نقدمه لك",
        "services_title": "خدمات هندسية متكاملة من البداية للنهاية.",
        "process_kicker": "طريقة العمل",
        "process_title": "من فكرتك إلى مساحة جاهزة في خمس خطوات.",
        "projects_kicker": "من أعمالنا",
        "projects_title": "مشاريع تتحدث عن نفسها.",
        "lgs_kicker": "لماذا الحديد البارد",
        "lgs_title": "الطريقة الحديثة للبناء في الخليج.",
        "lgs_text": "يساهم الحديد البارد في زيادة سرعة التنفيذ وتقليل التكاليف، مع عزل الصوت ومقاومة الرياح والحرائق والعفن، وهو الخيار الأمثل في قطاع المباني الإنشائية.",
        "lgs_badge": "عامًا عمر افتراضي ضد الصدأ",
        "reviews_kicker": "آراء عملائنا",
        "reviews_title": "ماذا يقول عملاؤنا.",
        "partners_title": "شركاء النجاح",
        "certs_kicker": "التقدير",
        "certs_title": "شهادات وإنجازات",
        "news_kicker": "المركز الإعلامي",
        "news_title": "آخر الأخبار",
        "cta_title": "لديك مشروع في ذهنك؟",
        "cta_text": "أخبرنا بما تحتاجه، وسيتواصل معك مهندسونا بالحل المناسب.",

        "view_all": "عرض الكل",
        "learn_more": "اعرف المزيد",
        "all": "الكل",
        "previous": "السابق",
        "next": "التالي",
        "gallery": "معرض الصور",
        "more_projects": "مشاريع أخرى",
        "project_details": "تفاصيل المشروع",
        "why_us": "ما يميزنا",
        "why_us_text": "التزامنا الدائم بالابتكار ومواكبة كل ما هو جديد. نسعى دائمًا للاستفادة من أحدث المواد والتقنيات في عمليات البناء لضمان جودة الأعمال وزيادة الإنتاجية، بالإضافة إلى تقليل التكاليف وتسريع تسليم المشاريع.",

        "about_title": "تصميم وبناء: الحل الشامل للمشاريع المعمارية.",
        "vision": "رؤيتنا",
        "mission": "رسالتنا",
        "values": "قيمنا الأساسية",
        "news_page": "الأخبار",
        "news_intro": "معارض وجوائز وإنجازات من مختلف شركات المجموعة.",
        "articles_page": "المقالات",
        "articles_intro": "مقالات حول البناء الحديث والحديد البارد والعمارة.",
        "projects_page": "مشاريعنا",
        "projects_intro": "مجموعة مختارة من الفلل والشاليهات ومحطات الوقود والمساجد والمباني التجارية والعامة التي نفذتها المجموعة.",
        "services_page": "خدماتنا",
        "services_intro": "استشارات وتصميم وهندسة ومساحة وبناء بفرق متخصصة في مختلف شركات المجموعة.",
        "contact_page": "تواصل معنا",
        "contact_intro": "كيف يمكننا مساعدتك؟ اختر الموضوع وأرسل لنا طلبك.",
        "service": "خدمة",

        "branches": "فروعنا",
        "phone": "رقم الهاتف",
        "email": "البريد الإلكتروني",
        "hours": "ساعات العمل",
        "hours_list": [("الأحد - الخميس", "9:00 - 18:00"), ("السبت", "9:00 - 13:00"), ("الجمعة", "مغلق")],
        "follow": "تابعنا",
        "links": "روابط سريعة",
        "footer_text": "نخبة من ذوي الخبرة والكفاءة في القطاع الهندسي يعملون معنا لتقديم الاختيار الأفضل والحل الأنسب لكم.",
        "rights": "جميع الحقوق محفوظة.",

        "form_tabs": [("office", "المكتب الهندسي"), ("contracting", "المقاولات المعمارية"),
                      ("lgs", "آلات الحديد البارد"), ("feedback", "تقييم الخدمة")],
        "name": "الاسم الكامل",
        "phone_number": "رقم الهاتف",
        "branch": "أقرب فرع لك",
        "choose": "اختر...",
        "has_plans": "هل قمت بالتخطيط مسبقًا؟",
        "is_designed": "هل تم التصميم بالفعل؟",
        "is_planned": "هل تم التخطيط مسبقًا للبناء الذي ترغب فيه؟",
        "has_factory": "هل يوجد مصنع قائم؟",
        "entity": "ما الجهة التي تمثلها؟",
        "company": "شركة",
        "individual": "فرد",
        "company_name": "اسم الشركة",
        "wants_training": "هل لديك مؤسسة ترغب في التدريب؟",
        "your_service": "ما هي الخدمة التي حصلت عليها؟",
        "responsible": "من المسؤول المباشر عن خدمتك؟",
        "heard_from": "أين سمعت عن مجموعة عمران تك؟",
        "opinion": "ما رأيك في مجموعة عمران تك؟",
        "difficulties": "هل واجهت أي صعوبات في خدمة العملاء؟",
        "suggestions": "هل لديك اقتراحات لتحسين خدماتنا؟",
        "message": "رسالتك",
        "yes": "نعم",
        "no": "لا",
        "send": "إرسال الطلب",
        "form_note": "عند الإرسال سيُفتح تطبيق البريد لديك مع تعبئة التفاصيل تلقائيًا.",
        "form_branches": ["الرياض", "الخبر", "العلا", "الأحساء، المبرز", "الأحساء، الطرف"],
    },
}

ABOUT = {
    "en": {
        "paragraphs": [
            "As a leading group certified by reputable institutions, we specialize in modern construction methods such as Cold-Formed Steel, Hollow Core ceilings and Precast.",
            "We make the whole process simple, from the first idea to the finished building. With us you get creative design ideas, smooth coordination and expert execution.",
            "We want to be your trusted partner in turning your vision into reality. From the first idea to the final handover, Omran Tech Group is the only contact you need for a successful project.",
            "Relax while we take care of every detail and give you everything you need under one roof.",
        ],
        "vision": "We work every day to earn a respected position in our field. We want to be a benchmark for success and excellence, and we believe that growth, innovation and well-delivered projects go hand in hand with building a successful engineering company.",
        "mission": "We build lasting relationships with our clients by offering something different and going beyond what they expect, as leaders in design and project management.",
        "values": [
            ("Excellence", "Excellence is at our core. We believe in sustainable growth and in giving our clients exceptional service and fresh solutions."),
            ("Integrity", "We work in a transparent and ethical way with our clients, our partners and the communities we serve."),
            ("Passion", "Everything we do comes from a real passion for engineering, and that drives us far beyond making a profit."),
            ("Commitment", "We keep every promise and agreement we make, and we follow all laws and regulations."),
        ],
    },
    "ar": {
        "paragraphs": [
            "مجموعة رائدة في مجال الهندسة في المملكة العربية السعودية تأسست عام 1433هـ، معتمدة من قبل العديد من المؤسسات المرموقة، ومتخصصة في تقنيات البناء الحديث مثل الحديد البارد والأسقف المجوفة والخرسانة سابقة الصب.",
            "نحن نبسّط عملية البناء برمتها من المفهوم إلى الاكتمال. معنا، يمكنك الوصول إلى أفكار التصميم المبتكرة والتنسيق السلس والتنفيذ الاحترافي.",
            "نحن ملتزمون بأن نكون شريكك الموثوق في تحويل رؤيتك المعمارية إلى واقع. من الفكرة الأولية إلى التنفيذ النهائي، تُعد مجموعة عمران تك نقطة الاتصال الوحيدة التي تحتاجها لمشروع معماري ناجح.",
            "استمتع براحة البال لأننا نتعامل مع كل جانب، ونوفر لك كل ما تحتاجه تحت سقف واحد.",
        ],
        "vision": "رؤيتنا تنعكس بعملنا الدائم لتحقيق مكانة مرموقة، وفي هذا المجال نتطلع لنكون معيارًا لقياس مستوى النجاح والتميز. ونؤمن أن إمكانيات التطور والابتكار وإنجاز المشاريع بشكل ممتاز تتلازم مع بنائنا لنموذج ناجح في القطاع الهندسي.",
        "mission": "نسعى إلى خلق علاقات ناجحة مع عملائنا من خلال تقديم كل ما هو مميز وفريد ويتخطى مستوى التوقعات، وذلك لتجسيد رسالتنا في الريادة وتقديم خدمات التصميم وإدارة المشاريع.",
        "values": [
            ("التميز", "نضع التميز كأحد قيمنا الأساسية، ونؤمن بأهمية التطور المستدام وتقديم خدمات استثنائية وحلول مبتكرة لعملائنا."),
            ("النزاهة", "نؤمن بأهمية القيام بالأعمال بطريقة شفافة وأخلاقية، سواء في التعامل مع عملائنا أو شركائنا أو المجتمعات التي نخدمها."),
            ("الشغف", "كل ما نقوم به ينبع من شغفنا الحقيقي بالهندسة، وهو ما يمدنا بحافز قوي للنجاح يمتد إلى ما هو أبعد من تحقيق الأرباح."),
            ("الالتزام", "نسعى لتحقيق الالتزام الكامل بكافة التعهدات والاتفاقيات التي نبرمها، وكذلك الالتزام بكافة القوانين والأنظمة."),
        ],
    },
}
