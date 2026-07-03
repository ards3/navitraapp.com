from __future__ import annotations

from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LASTMOD = "2026-07-03"

LANGS = {
    "en": {"name": "English", "url": "/", "hreflang": "en"},
    "tr": {"name": "Türkçe", "url": "/tr/", "hreflang": "tr"},
    "de": {"name": "Deutsch", "url": "/de/", "hreflang": "de"},
    "es": {"name": "Español", "url": "/es/", "hreflang": "es"},
    "fr": {"name": "Français", "url": "/fr/", "hreflang": "fr"},
    "it": {"name": "Italiano", "url": "/it/", "hreflang": "it"},
    "nl": {"name": "Nederlands", "url": "/nl/", "hreflang": "nl"},
    "pt-br": {"name": "Português (Brasil)", "url": "/pt-br/", "hreflang": "pt-BR"},
    "ar": {"name": "العربية", "url": "/ar/", "hreflang": "ar"},
    "ja": {"name": "日本語", "url": "/ja/", "hreflang": "ja"},
    "ko": {"name": "한국어", "url": "/ko/", "hreflang": "ko"},
    "ru": {"name": "Русский", "url": "/ru/", "hreflang": "ru"},
    "zh-hans": {"name": "简体中文", "url": "/zh-hans/", "hreflang": "zh-Hans"},
}

UI_LABELS = {
    "tr": {
        "route_engine": "Rota motoru",
        "faq": "SSS",
        "year_unit": "yıl",
        "month_unit": "ay",
        "support": "Destek",
        "legal": "Yasal",
        "privacy": "Gizlilik Politikası",
        "terms": "Kullanım Şartları",
        "languages": "Diller",
        "preview": "Navitra rota planlama önizlemesi",
    },
    "de": {
        "route_engine": "Routenmotor",
        "faq": "FAQ",
        "year_unit": "Jahr",
        "month_unit": "Monat",
        "support": "Support",
        "legal": "Rechtliches",
        "privacy": "Datenschutzrichtlinie",
        "terms": "Nutzungsbedingungen",
        "languages": "Sprachen",
        "preview": "Vorschau der Navitra-Routenplanung",
    },
    "es": {
        "route_engine": "Motor de rutas",
        "faq": "FAQ",
        "year_unit": "año",
        "month_unit": "mes",
        "support": "Soporte",
        "legal": "Legal",
        "privacy": "Política de privacidad",
        "terms": "Condiciones del servicio",
        "languages": "Idiomas",
        "preview": "Vista previa de planificación de rutas de Navitra",
    },
    "fr": {
        "route_engine": "Moteur d'itinéraire",
        "faq": "FAQ",
        "year_unit": "an",
        "month_unit": "mois",
        "support": "Support",
        "legal": "Mentions légales",
        "privacy": "Politique de confidentialité",
        "terms": "Conditions d'utilisation",
        "languages": "Langues",
        "preview": "Aperçu de la planification d'itinéraire Navitra",
    },
    "it": {
        "route_engine": "Motore di itinerari",
        "faq": "FAQ",
        "year_unit": "anno",
        "month_unit": "mese",
        "support": "Supporto",
        "legal": "Legale",
        "privacy": "Informativa sulla privacy",
        "terms": "Termini di servizio",
        "languages": "Lingue",
        "preview": "Anteprima della pianificazione itinerari Navitra",
    },
    "nl": {
        "route_engine": "Route-engine",
        "faq": "FAQ",
        "year_unit": "jaar",
        "month_unit": "maand",
        "support": "Support",
        "legal": "Juridisch",
        "privacy": "Privacybeleid",
        "terms": "Servicevoorwaarden",
        "languages": "Talen",
        "preview": "Voorvertoning van Navitra-routeplanning",
    },
    "pt-br": {
        "route_engine": "Motor de rotas",
        "faq": "FAQ",
        "year_unit": "ano",
        "month_unit": "mês",
        "support": "Suporte",
        "legal": "Legal",
        "privacy": "Política de Privacidade",
        "terms": "Termos de Serviço",
        "languages": "Idiomas",
        "preview": "Prévia do planejamento de rotas do Navitra",
    },
    "ar": {
        "route_engine": "محرك المسارات",
        "faq": "الأسئلة الشائعة",
        "year_unit": "سنة",
        "month_unit": "شهر",
        "support": "الدعم",
        "legal": "قانوني",
        "privacy": "سياسة الخصوصية",
        "terms": "شروط الخدمة",
        "languages": "اللغات",
        "preview": "معاينة تخطيط المسارات في Navitra",
    },
    "ja": {
        "route_engine": "ルートエンジン",
        "faq": "FAQ",
        "year_unit": "年",
        "month_unit": "月",
        "support": "サポート",
        "legal": "法務",
        "privacy": "プライバシーポリシー",
        "terms": "利用規約",
        "languages": "言語",
        "preview": "Navitraのルート計画プレビュー",
    },
    "ko": {
        "route_engine": "루트 엔진",
        "faq": "FAQ",
        "year_unit": "년",
        "month_unit": "월",
        "support": "지원",
        "legal": "법적 고지",
        "privacy": "개인정보 처리방침",
        "terms": "서비스 약관",
        "languages": "언어",
        "preview": "Navitra 경로 계획 미리보기",
    },
    "ru": {
        "route_engine": "Маршрутный движок",
        "faq": "FAQ",
        "year_unit": "год",
        "month_unit": "месяц",
        "support": "Поддержка",
        "legal": "Правовая информация",
        "privacy": "Политика конфиденциальности",
        "terms": "Условия использования",
        "languages": "Языки",
        "preview": "Предпросмотр планирования маршрута Navitra",
    },
    "zh-hans": {
        "route_engine": "路线引擎",
        "faq": "FAQ",
        "year_unit": "年",
        "month_unit": "月",
        "support": "支持",
        "legal": "法律",
        "privacy": "隐私政策",
        "terms": "服务条款",
        "languages": "语言",
        "preview": "Navitra 路线规划预览",
    },
}

LOCALES = {
    "tr": {
        "lang": "tr",
        "dir": "ltr",
        "title": "Navitra - AI Gezi Planlayıcı | Akıllı Rotalar",
        "description": "Navitra, sevdiğin yerleri sesli rehberler, offline haritalar ve akıllı keşifle optimize edilmiş günlük rotalara dönüştüren AI gezi planlayıcıdır.",
        "nav_features": "Özellikler",
        "nav_how": "Nasıl çalışır",
        "nav_pricing": "Fiyatlar",
        "nav_support": "Destek",
        "launch": "Lansman durumu",
        "app_store": "App Store yakında",
        "google_play": "Google Play sonra",
        "hero_fact": "İstanbul'da doğdu",
        "hero_fact_strong": "Her şehir için",
        "hero_title": "Daha akıllı planla,<br>daha iyi <em>gez</em>.",
        "hero_body": "Navitra sevdiğin yerleri açılış saatlerini, mesafeleri ve temponu dikkate alan günlük rotalara çevirir. Online ya da offline, AI seyahat arkadaşın cebinde.",
        "features_title": "Gezi planlamak karmaşık olmak zorunda değil.",
        "features_accent": "Navitra ile sadece seçersin.",
        "features_lead": "Lojistiği Navitra taşır; sana anıları taşımak kalır.",
        "features": [
            ("AI Rota Planlama", "Sevdiğin yerleri seç; AI her günü açılış saatlerine, mesafelere ve tempona göre kurar."),
            ("AI Sesli Rehber", "Yürürken her durağın hikayesini desteklenen anlatım dillerinden birinde dinle."),
            ("Offline Haritalar", "Rotanı, haritanı ve sesli rehberlerini yolculuktan önce indir; internet olmasa da devam et."),
            ("Akıllı Keşif", "Rota üzerindeki gizli yerler, yemek molaları ve alternatifler tam zamanında önerilir."),
        ],
        "route_title": "İstek listesinden yürünebilir rotaya.",
        "route_body": "Şehri seç, ilgini çeken yerleri işaretle ve Navitra'nın gerçek hayatta çalışan günlük planı oluşturmasını izle.",
        "route_bullets": [
            ("Açılış saatleri dikkate alınır", "Pazartesi kapalıysa pazartesi planına girmez."),
            ("Günler bölgelere ayrılır", "Tek bir müze için şehrin öbür ucuna gidip gelmezsin."),
            ("Konaklama hesaba katılır", "Her gün gerçekten kaldığın yerden başlar ve oraya döner."),
            ("Her an yeniden düzenlenir", "Yoruldun, acıktın ya da plan değişti; tek dokunuşla gün yenilenir."),
        ],
        "steps_title": "Nasıl çalışır",
        "steps_lead": "Nereden başlayacağını bilemediğin andan hazır plana dört adımda geçersin.",
        "steps": [
            ("Şehri seç", "Bir destinasyon ara veya nasıl bir gezi istediğini asistana anlat."),
            ("Sevdiklerini işaretle", "Müze, pazar, manzara ya da sokak lezzeti; ilgini çekenleri seç."),
            ("AI günlerini kurar", "Rota motoru durakları saatlere, mesafelere ve enerjine göre sıralar."),
            ("Hikayelerle keşfet", "Rota takibi, sesli rehber ve offline modla seyahat boyunca yanında kalır."),
        ],
        "pricing_title": "Gezine uygun plan.",
        "pricing_lead": "Navitra lansmanda indirmesi ve planlaması ücretsiz olacak. Premium, yıllık planda 7 gün ücretsiz deneme ile tam deneyimi açar.",
        "best_value": "En avantajlı",
        "yearly": "Yıllık",
        "monthly": "Aylık",
        "yearly_for": "Sık seyahat edenler için.",
        "monthly_for": "Büyük seyahat için.",
        "trial": "7 gün ücretsiz deneme dahil",
        "all_year": "Tüm yıl Premium deneyim",
        "month_equiv": "Aylık yaklaşık $3.33",
        "full_access": "Tüm Premium özellikler",
        "voice_guides": "Her durakta AI sesli rehber",
        "offline_nav": "Offline harita ve navigasyon",
        "higher_limits": "Daha yüksek AI rota limitleri",
        "price_note": "Fiyatlar USD'dir; mağaza yerel fiyatlandırmayı gösterir. Abonelikler otomatik yenilenir ve mağaza ayarlarından iptal edilebilir.",
        "faq_title": "Sık sorulan sorular",
        "faqs": [
            ("Navitra ücretsiz mi?", "Evet. Navitra lansmanda indirmesi ve gezi planlaması ücretsiz olacak. Premium; sesli rehber, offline haritalar ve daha yüksek AI rota limitleri ekler."),
            ("Offline gerçekten çalışır mı?", "Premium ile destinasyonu önceden indirirsin. Harita, rota ve sesli rehberler cihazda saklanır."),
            ("Aboneliği nasıl iptal ederim?", "Abonelikler App Store veya Google Play hesabından yönetilir. İstediğin zaman iptal edebilirsin."),
        ],
        "final_title": "Dünya bekliyor.<br><em>Rotan hazır.</em>",
        "final_lead": "Navitra iOS lansmanına hazırlanıyor; Android daha sonra gelecek.",
        "tiny": "Lansmanda ücretsiz · Yıllık planda 7 gün deneme · İstediğin zaman iptal",
        "footer": "Keşfetmene, planlamana ve yolunu bulmana yardım eden AI seyahat arkadaşı.",
    },
    "de": {
        "lang": "de",
        "dir": "ltr",
        "title": "Navitra - KI-Reiseplaner | Smarte Routen",
        "description": "Navitra verwandelt deine Lieblingsorte in optimierte Tagesrouten mit Sprachguides, Offline-Karten und smarter Entdeckung.",
        "nav_features": "Funktionen",
        "nav_how": "So funktioniert es",
        "nav_pricing": "Preise",
        "nav_support": "Support",
        "launch": "Launch-Status",
        "app_store": "Bald im App Store",
        "google_play": "Google Play spater",
        "hero_fact": "Geboren in Istanbul",
        "hero_fact_strong": "Fur jede Stadt gemacht",
        "hero_title": "Plane smarter,<br>reise <em>besser</em>.",
        "hero_body": "Navitra macht aus deinen Lieblingsorten eine optimierte Tagesroute: Offnungszeiten, Wege und dein Tempo werden mitgedacht. Dein KI-Reisebegleiter funktioniert online und offline.",
        "features_title": "Reiseplanung muss nicht kompliziert sein.",
        "features_accent": "Mit Navitra wischt du einfach.",
        "features_lead": "Vier Superkrafte in einer App. Navitra ubernimmt die Logistik, du sammelst die Erinnerungen.",
        "features": [
            ("KI-Routenplanung", "Wahle Orte aus, die du sehen willst. Die KI plant jeden Tag nach Offnungszeiten, Distanzen und Tempo."),
            ("KI-Sprachguide", "Ein Erzahler in deiner Tasche: Hore die Geschichte jedes Stopps in einer unterstutzten Erzahlsprache."),
            ("Offline-Karten", "Lade Reise, Karten und Sprachguides vorab herunter. Kein Empfang, kein Problem."),
            ("Smarte Entdeckung", "Versteckte Orte, Essensstopps und Alternativen erscheinen genau dann, wenn sie passen."),
        ],
        "route_title": "Von der Wunschliste zur laufbaren Route.",
        "route_body": "Wahle eine Stadt, markiere deine Favoriten und lass Navitra daraus einen Tagesplan bauen, der vor Ort wirklich funktioniert.",
        "route_bullets": [
            ("Offnungszeiten respektiert", "Montags geschlossen? Dann landet es nicht im Montag."),
            ("Tage geografisch gebundelt", "Kein Hin und Her quer durch die Stadt fur ein einziges Museum."),
            ("Dein Hotel im Plan", "Jeder Tag startet und endet dort, wo du wirklich schlafst."),
            ("Jederzeit neu mischen", "Mude, hungrig oder spontan? Ein Tipp formt den Rest des Tages neu."),
        ],
        "steps_title": "So funktioniert es",
        "steps_lead": "Vom ersten Wo-anfangen-wir? bis zum fertigen Plan sind es vier Schritte.",
        "steps": [
            ("Stadt wahlen", "Suche ein Ziel oder beschreibe dem Assistenten deine Wunschreise."),
            ("Lieblingsorte markieren", "Museen, Markte, Aussichtspunkte oder Streetfood: Entscheide, was dich reizt."),
            ("Die KI baut deine Tage", "Der Routenmotor sortiert Stopps nach Zeiten, Wegen und Energie."),
            ("Mit Geschichten losziehen", "Folge der Route, hore Sprachguides und nutze alles offline."),
        ],
        "pricing_title": "Ein Plan, der zu deiner Reise passt.",
        "pricing_lead": "Navitra ist zum Launch kostenlos zum Herunterladen und Planen. Premium schaltet die volle Erfahrung frei, mit 7 Tagen Testphase im Jahresplan.",
        "best_value": "Bester Wert",
        "yearly": "Jahrlich",
        "monthly": "Monatlich",
        "yearly_for": "Fur haufige Reisende.",
        "monthly_for": "Fur die grosse Reise.",
        "trial": "7 Tage kostenlos testen",
        "all_year": "Premium das ganze Jahr",
        "month_equiv": "Etwa $3.33 pro Monat",
        "full_access": "Voller Premium-Zugriff",
        "voice_guides": "KI-Sprachguides an jedem Stopp",
        "offline_nav": "Offline-Karten und Navigation",
        "higher_limits": "Hoheres Limit fur KI-Routen",
        "price_note": "Preise in USD; dein Store zeigt lokale Preise. Abos erneuern sich automatisch und konnen jederzeit im Store gekundigt werden.",
        "faq_title": "Haufige Fragen",
        "faqs": [
            ("Ist Navitra kostenlos?", "Ja. Zum Launch sind Download und Reiseplanung kostenlos. Premium erganzt Sprachguides, Offline-Karten und hohere KI-Routenlimits."),
            ("Funktioniert es wirklich offline?", "Mit Premium ladst du dein Ziel vor der Reise herunter. Karten, Routen und Sprachguides bleiben auf dem Gerat."),
            ("Wie kundige ich?", "Abos werden uber den App Store oder Google Play verwaltet und konnen dort jederzeit gekundigt werden."),
        ],
        "final_title": "Die Welt wartet.<br><em>Deine Route ist bereit.</em>",
        "final_lead": "Navitra bereitet den iOS-Launch vor; Android folgt spater.",
        "tiny": "Kostenlos zum Launch · 7 Tage Testphase im Jahresplan · Jederzeit kundbar",
        "footer": "KI-Reisebegleiter zum Entdecken, Planen und Navigieren.",
    },
    "es": {
        "lang": "es",
        "dir": "ltr",
        "title": "Navitra - Planificador de viajes con IA | Rutas inteligentes",
        "description": "Navitra convierte tus lugares favoritos en rutas diarias optimizadas con guias de voz, mapas offline y descubrimiento inteligente.",
        "nav_features": "Funciones",
        "nav_how": "Como funciona",
        "nav_pricing": "Precios",
        "nav_support": "Soporte",
        "launch": "Estado de lanzamiento",
        "app_store": "App Store pronto",
        "google_play": "Google Play despues",
        "hero_fact": "Nacida en Estambul",
        "hero_fact_strong": "Hecha para cada ciudad",
        "hero_title": "Planifica mejor,<br>viaja <em>mejor</em>.",
        "hero_body": "Navitra convierte los lugares que te gustan en una ruta dia por dia: horarios, distancias y ritmo real incluidos. Tu companero de viaje con IA, online u offline.",
        "features_title": "Planear un viaje no deberia ser pesado.",
        "features_accent": "Con Navitra, solo eliges.",
        "features_lead": "La app se encarga de la logistica para que tu te quedes con el viaje.",
        "features": [
            ("Rutas con IA", "Elige los lugares que te interesan y la IA organiza cada dia segun horarios, distancias y tu ritmo."),
            ("Guia de voz con IA", "Escucha la historia de cada parada en uno de los idiomas de narracion compatibles."),
            ("Mapas offline", "Descarga ruta, mapas y guias antes de salir. Sin cobertura, sigues adelante."),
            ("Descubrimiento inteligente", "Lugares ocultos, pausas para comer y alternativas aparecen en el momento adecuado."),
        ],
        "route_title": "De lista de deseos a ruta caminable.",
        "route_body": "Elige una ciudad, guarda lo que te gusta y deja que Navitra construya un plan diario que funcione de verdad.",
        "route_bullets": [
            ("Respeta horarios", "Si cierra el lunes, no aparecera en tu lunes."),
            ("Dias agrupados por zona", "Sin cruzar la ciudad por una sola parada."),
            ("Tu alojamiento cuenta", "Cada dia empieza y termina donde duermes."),
            ("Reorganiza cuando quieras", "Si estas cansado, con hambre o cambias de idea, el dia se adapta."),
        ],
        "steps_title": "Como funciona",
        "steps_lead": "Pasas de no saber por donde empezar a tener un plan en cuatro pasos.",
        "steps": [
            ("Elige una ciudad", "Busca un destino o describe al asistente el viaje que tienes en mente."),
            ("Marca lo que te gusta", "Museos, mercados, miradores o comida callejera: elige sin complicarte."),
            ("La IA arma tus dias", "El motor ordena las paradas por horarios, distancias y energia diaria."),
            ("Explora con historias", "Sigue la ruta, escucha guias de voz y usalo offline cuando lo necesites."),
        ],
        "pricing_title": "Un plan para tu forma de viajar.",
        "pricing_lead": "Navitra sera gratis para descargar y planificar en el lanzamiento. Premium desbloquea la experiencia completa con 7 dias de prueba en el plan anual.",
        "best_value": "Mejor valor",
        "yearly": "Anual",
        "monthly": "Mensual",
        "yearly_for": "Para quien viaja seguido.",
        "monthly_for": "Para el gran viaje.",
        "trial": "7 dias de prueba gratis",
        "all_year": "Premium todo el ano",
        "month_equiv": "Aprox. $3.33 al mes",
        "full_access": "Acceso Premium completo",
        "voice_guides": "Guias de voz con IA en cada parada",
        "offline_nav": "Mapas y navegacion offline",
        "higher_limits": "Mas limites para rutas con IA",
        "price_note": "Precios en USD; tu tienda muestra precios locales. Las suscripciones se renuevan automaticamente y se pueden cancelar en la tienda.",
        "faq_title": "Preguntas frecuentes",
        "faqs": [
            ("Navitra es gratis?", "Si. En el lanzamiento, descargar y planificar viajes sera gratis. Premium agrega guias de voz, mapas offline y limites mas altos."),
            ("Funciona offline?", "Con Premium descargas tu destino antes de viajar. Mapas, rutas y guias quedan guardados en el dispositivo."),
            ("Como cancelo?", "La suscripcion se gestiona desde App Store o Google Play y puedes cancelarla cuando quieras."),
        ],
        "final_title": "El mundo espera.<br><em>Tu ruta esta lista.</em>",
        "final_lead": "Navitra prepara su lanzamiento en iOS; Android llegara despues.",
        "tiny": "Gratis en el lanzamiento · 7 dias de prueba anual · Cancela cuando quieras",
        "footer": "Companero de viaje con IA para descubrir, planificar y navegar.",
    },
    "fr": {
        "lang": "fr",
        "dir": "ltr",
        "title": "Navitra - Planificateur de voyage IA | Itineraires intelligents",
        "description": "Navitra transforme vos lieux favoris en itineraires optimises, avec guides vocaux, cartes offline et decouvertes intelligentes.",
        "nav_features": "Fonctionnalites",
        "nav_how": "Comment ca marche",
        "nav_pricing": "Tarifs",
        "nav_support": "Support",
        "launch": "Statut du lancement",
        "app_store": "App Store bientot",
        "google_play": "Google Play plus tard",
        "hero_fact": "Nee a Istanbul",
        "hero_fact_strong": "Pensee pour chaque ville",
        "hero_title": "Planifiez mieux,<br>voyagez <em>mieux</em>.",
        "hero_body": "Navitra transforme les lieux que vous aimez en itineraire jour par jour, avec horaires, distances et rythme reel. Votre compagnon de voyage IA, en ligne ou hors ligne.",
        "features_title": "Planifier un voyage ne devrait pas etre complique.",
        "features_accent": "Avec Navitra, vous choisissez.",
        "features_lead": "Navitra gere la logistique pour que vous profitiez du voyage.",
        "features": [
            ("Itineraires IA", "Choisissez vos lieux; l'IA organise chaque jour selon les horaires, les distances et votre rythme."),
            ("Guide vocal IA", "Ecoutez l'histoire de chaque arret dans l'une des langues de narration prises en charge."),
            ("Cartes offline", "Telechargez votre trajet, vos cartes et vos guides avant de partir."),
            ("Decouverte intelligente", "Lieux caches, pauses repas et alternatives arrivent au bon moment."),
        ],
        "route_title": "De la liste d'envies a l'itineraire a pied.",
        "route_body": "Choisissez une ville, gardez ce qui vous plait et laissez Navitra creer un plan qui fonctionne sur place.",
        "route_bullets": [
            ("Horaires respectes", "Ferme le lundi? Ce ne sera pas dans votre lundi."),
            ("Journees groupees par quartier", "Plus d'allers-retours inutiles pour un seul musee."),
            ("Votre hotel inclus", "Chaque jour commence et finit la ou vous dormez."),
            ("Remix a tout moment", "Fatigue, faim ou changement d'envie: le reste de la journee s'adapte."),
        ],
        "steps_title": "Comment ca marche",
        "steps_lead": "Quatre etapes suffisent pour passer de l'idee au plan.",
        "steps": [
            ("Choisissez une ville", "Recherchez une destination ou decrivez votre voyage a l'assistant."),
            ("Selectionnez vos envies", "Musees, marches, points de vue ou street food: gardez ce qui vous attire."),
            ("L'IA construit vos journees", "Le moteur ordonne les arrets selon horaires, distances et energie."),
            ("Explorez avec des histoires", "Suivez la route, ecoutez les guides vocaux et utilisez le tout offline."),
        ],
        "pricing_title": "Un plan adapte a votre voyage.",
        "pricing_lead": "Navitra sera gratuit a telecharger et a utiliser pour planifier au lancement. Premium debloque l'experience complete avec 7 jours d'essai sur l'abonnement annuel.",
        "best_value": "Meilleure valeur",
        "yearly": "Annuel",
        "monthly": "Mensuel",
        "yearly_for": "Pour les voyageurs reguliers.",
        "monthly_for": "Pour le grand voyage.",
        "trial": "7 jours d'essai inclus",
        "all_year": "Premium toute l'annee",
        "month_equiv": "Environ $3.33 par mois",
        "full_access": "Acces Premium complet",
        "voice_guides": "Guides vocaux IA a chaque arret",
        "offline_nav": "Cartes et navigation offline",
        "higher_limits": "Limites IA plus elevees",
        "price_note": "Prix en USD; votre store affiche les prix locaux. Les abonnements se renouvellent automatiquement et peuvent etre annules dans le store.",
        "faq_title": "Questions frequentes",
        "faqs": [
            ("Navitra est-il gratuit?", "Oui. Au lancement, le telechargement et la planification seront gratuits. Premium ajoute guides vocaux, cartes offline et limites IA plus elevees."),
            ("Est-ce vraiment offline?", "Avec Premium, vous telechargez la destination avant de partir. Cartes, routes et guides restent sur l'appareil."),
            ("Comment annuler?", "L'abonnement se gere dans l'App Store ou Google Play et peut etre annule a tout moment."),
        ],
        "final_title": "Le monde vous attend.<br><em>Votre route est prete.</em>",
        "final_lead": "Navitra prepare son lancement iOS; Android suivra plus tard.",
        "tiny": "Gratuit au lancement · 7 jours d'essai annuel · Annulable a tout moment",
        "footer": "Compagnon de voyage IA pour decouvrir, planifier et naviguer.",
    },
    "it": {
        "lang": "it",
        "dir": "ltr",
        "title": "Navitra - Viaggi con IA | Itinerari intelligenti",
        "description": "Navitra trasforma i luoghi che ami in itinerari giornalieri ottimizzati con guide vocali, mappe offline e scoperta intelligente.",
        "nav_features": "Funzioni",
        "nav_how": "Come funziona",
        "nav_pricing": "Prezzi",
        "nav_support": "Supporto",
        "launch": "Stato lancio",
        "app_store": "App Store a breve",
        "google_play": "Google Play piu avanti",
        "hero_fact": "Nata a Istanbul",
        "hero_fact_strong": "Pensata per ogni citta",
        "hero_title": "Pianifica meglio,<br>viaggia <em>meglio</em>.",
        "hero_body": "Navitra trasforma i luoghi che ami in un percorso giorno per giorno, considerando orari, distanze e ritmo reale. Il tuo compagno di viaggio IA, online o offline.",
        "features_title": "Pianificare un viaggio non deve essere complicato.",
        "features_accent": "Con Navitra, scegli e basta.",
        "features_lead": "Navitra gestisce la logistica, tu vivi il viaggio.",
        "features": [
            ("Itinerari con IA", "Scegli i luoghi che ami; l'IA costruisce ogni giornata in base a orari, distanze e ritmo."),
            ("Guida vocale IA", "Ascolta la storia di ogni tappa in una lingua di narrazione supportata."),
            ("Mappe offline", "Scarica viaggio, mappe e guide prima di partire. Anche senza rete, continui."),
            ("Scoperta smart", "Luoghi nascosti, pause pranzo e alternative arrivano al momento giusto."),
        ],
        "route_title": "Dalla lista dei desideri a un percorso a piedi.",
        "route_body": "Scegli una citta, salva cio che ti piace e lascia che Navitra crei un piano realistico.",
        "route_bullets": [
            ("Orari rispettati", "Se e chiuso lunedi, non finira nel tuo lunedi."),
            ("Giornate per zona", "Niente attraversamenti inutili per una sola tappa."),
            ("Hotel incluso", "Ogni giornata parte e torna dove dormi davvero."),
            ("Remix quando vuoi", "Stanco, affamato o fuori programma? Il resto della giornata si adatta."),
        ],
        "steps_title": "Come funziona",
        "steps_lead": "Dall'idea al piano completo in quattro passaggi.",
        "steps": [
            ("Scegli una citta", "Cerca una destinazione o racconta all'assistente il viaggio che immagini."),
            ("Seleziona cio che ami", "Musei, mercati, panorami o street food: tieni cio che ti interessa."),
            ("L'IA costruisce i giorni", "Il motore ordina le tappe per orari, distanze ed energia."),
            ("Esplora con storie", "Segui la rotta, ascolta le guide vocali e usa tutto offline."),
        ],
        "pricing_title": "Un piano per il tuo viaggio.",
        "pricing_lead": "Al lancio Navitra sara gratis da scaricare e usare per pianificare. Premium sblocca l'esperienza completa con 7 giorni di prova sul piano annuale.",
        "best_value": "Miglior valore",
        "yearly": "Annuale",
        "monthly": "Mensile",
        "yearly_for": "Per chi viaggia spesso.",
        "monthly_for": "Per il grande viaggio.",
        "trial": "7 giorni di prova inclusi",
        "all_year": "Premium tutto l'anno",
        "month_equiv": "Circa $3.33 al mese",
        "full_access": "Accesso Premium completo",
        "voice_guides": "Guide vocali IA a ogni tappa",
        "offline_nav": "Mappe e navigazione offline",
        "higher_limits": "Limiti IA piu alti",
        "price_note": "Prezzi in USD; lo store mostra i prezzi locali. Gli abbonamenti si rinnovano automaticamente e si possono annullare nello store.",
        "faq_title": "Domande frequenti",
        "faqs": [
            ("Navitra e gratis?", "Si. Al lancio, download e pianificazione saranno gratuiti. Premium aggiunge guide vocali, mappe offline e limiti IA piu alti."),
            ("Funziona offline?", "Con Premium scarichi la destinazione prima del viaggio. Mappe, rotte e guide restano sul dispositivo."),
            ("Come annullo?", "L'abbonamento si gestisce da App Store o Google Play e si puo annullare quando vuoi."),
        ],
        "final_title": "Il mondo ti aspetta.<br><em>La tua rotta e pronta.</em>",
        "final_lead": "Navitra sta preparando il lancio iOS; Android arrivera piu avanti.",
        "tiny": "Gratis al lancio · 7 giorni di prova annuale · Annulla quando vuoi",
        "footer": "Compagno di viaggio IA per scoprire, pianificare e navigare.",
    },
    "nl": {
        "lang": "nl",
        "dir": "ltr",
        "title": "Navitra - AI Reisplanner | Slimme routes",
        "description": "Navitra zet je favoriete plekken om in geoptimaliseerde dagroutes met spraakgidsen, offline kaarten en slimme ontdekking.",
        "nav_features": "Functies",
        "nav_how": "Zo werkt het",
        "nav_pricing": "Prijzen",
        "nav_support": "Support",
        "launch": "Launchstatus",
        "app_store": "Binnenkort in App Store",
        "google_play": "Google Play later",
        "hero_fact": "Geboren in Istanbul",
        "hero_fact_strong": "Gemaakt voor elke stad",
        "hero_title": "Plan slimmer,<br>reis <em>beter</em>.",
        "hero_body": "Navitra maakt van je favoriete plekken een dag-tot-dag route met openingstijden, afstanden en jouw tempo. Je AI-reismaatje, online of offline.",
        "features_title": "Reizen plannen hoeft niet ingewikkeld te zijn.",
        "features_accent": "Met Navitra kies je gewoon.",
        "features_lead": "Navitra draagt de logistiek; jij verzamelt de herinneringen.",
        "features": [
            ("AI-routeplanning", "Kies wat je mooi vindt; AI bouwt elke dag rond tijden, afstand en tempo."),
            ("AI-spraakgids", "Luister naar het verhaal achter elke stop in een ondersteunde vertelstem."),
            ("Offline kaarten", "Download je reis, kaarten en gidsen vooraf. Geen bereik nodig."),
            ("Slim ontdekken", "Verborgen plekken, eetstops en alternatieven verschijnen precies op tijd."),
        ],
        "route_title": "Van wensenlijst naar looproute.",
        "route_body": "Kies een stad, bewaar wat je leuk vindt en laat Navitra een realistisch dagplan maken.",
        "route_bullets": [
            ("Openingstijden meegewogen", "Maandag dicht? Dan staat het niet op maandag."),
            ("Dagen per buurt gegroepeerd", "Geen onnodig heen-en-weer door de stad."),
            ("Je hotel telt mee", "Elke dag start en eindigt waar je echt slaapt."),
            ("Altijd opnieuw plannen", "Moe, hongerig of spontaan? De rest van de dag past zich aan."),
        ],
        "steps_title": "Zo werkt het",
        "steps_lead": "Van waar beginnen we? naar een plan in vier stappen.",
        "steps": [
            ("Kies een stad", "Zoek een bestemming of vertel de assistent wat voor reis je wilt."),
            ("Bewaar je favorieten", "Musea, markten, uitzichten of streetfood: kies wat past."),
            ("AI bouwt je dagen", "De route-engine ordent stops op tijden, afstanden en energie."),
            ("Ontdek met verhalen", "Volg de route, luister naar spraakgidsen en gebruik alles offline."),
        ],
        "pricing_title": "Een plan voor jouw reis.",
        "pricing_lead": "Navitra is bij lancering gratis te downloaden en te gebruiken voor planning. Premium opent de volledige ervaring met 7 dagen proef in het jaarplan.",
        "best_value": "Beste waarde",
        "yearly": "Jaarlijks",
        "monthly": "Maandelijks",
        "yearly_for": "Voor frequente reizigers.",
        "monthly_for": "Voor de grote reis.",
        "trial": "7 dagen gratis proef",
        "all_year": "Premium het hele jaar",
        "month_equiv": "Ongeveer $3.33 per maand",
        "full_access": "Volledige Premium-toegang",
        "voice_guides": "AI-spraakgidsen bij elke stop",
        "offline_nav": "Offline kaarten en navigatie",
        "higher_limits": "Hogere AI-routelimieten",
        "price_note": "Prijzen in USD; je store toont lokale prijzen. Abonnementen verlengen automatisch en zijn in de store opzegbaar.",
        "faq_title": "Veelgestelde vragen",
        "faqs": [
            ("Is Navitra gratis?", "Ja. Bij lancering zijn downloaden en reizen plannen gratis. Premium voegt spraakgidsen, offline kaarten en hogere AI-limieten toe."),
            ("Werkt het offline?", "Met Premium download je de bestemming vooraf. Kaarten, routes en gidsen blijven op je apparaat."),
            ("Hoe zeg ik op?", "Abonnementen beheer je via App Store of Google Play en kun je daar altijd opzeggen."),
        ],
        "final_title": "De wereld wacht.<br><em>Je route is klaar.</em>",
        "final_lead": "Navitra bereidt de iOS-lancering voor; Android volgt later.",
        "tiny": "Gratis bij lancering · 7 dagen proef op jaarplan · Altijd opzegbaar",
        "footer": "AI-reismaatje om te ontdekken, plannen en navigeren.",
    },
    "pt-br": {
        "lang": "pt-BR",
        "dir": "ltr",
        "title": "Navitra - Planejador de viagem com IA | Rotas inteligentes",
        "description": "Navitra transforma os lugares que voce ama em roteiros otimizados, com guias de voz, mapas offline e descoberta inteligente.",
        "nav_features": "Recursos",
        "nav_how": "Como funciona",
        "nav_pricing": "Precos",
        "nav_support": "Suporte",
        "launch": "Status do lancamento",
        "app_store": "App Store em breve",
        "google_play": "Google Play depois",
        "hero_fact": "Nascido em Istambul",
        "hero_fact_strong": "Feito para cada cidade",
        "hero_title": "Planeje melhor,<br>viaje <em>melhor</em>.",
        "hero_body": "Navitra transforma os lugares que voce ama em um roteiro dia a dia, considerando horarios, distancias e seu ritmo. Seu companheiro de viagem com IA, online ou offline.",
        "features_title": "Planejar uma viagem nao precisa ser complicado.",
        "features_accent": "Com Navitra, voce escolhe.",
        "features_lead": "Navitra cuida da logistica para voce aproveitar a viagem.",
        "features": [
            ("Roteiros com IA", "Escolha os lugares que quer ver; a IA monta cada dia por horarios, distancias e ritmo."),
            ("Guia de voz com IA", "Ouça a história de cada parada em um idioma de narração compatível."),
            ("Mapas offline", "Baixe viagem, mapas e guias antes de sair. Sem sinal, tudo continua."),
            ("Descoberta inteligente", "Lugares escondidos, pausas para comer e alternativas aparecem na hora certa."),
        ],
        "route_title": "Da lista de desejos ao roteiro a pe.",
        "route_body": "Escolha uma cidade, salve o que voce gosta e deixe Navitra montar um plano realista.",
        "route_bullets": [
            ("Horarios respeitados", "Se fecha na segunda, nao entra na sua segunda."),
            ("Dias agrupados por regiao", "Sem atravessar a cidade por uma unica parada."),
            ("Hospedagem no plano", "Cada dia comeca e termina onde voce realmente dorme."),
            ("Remixe quando quiser", "Cansou, ficou com fome ou mudou de ideia? O dia se adapta."),
        ],
        "steps_title": "Como funciona",
        "steps_lead": "Da duvida inicial ao plano pronto em quatro passos.",
        "steps": [
            ("Escolha uma cidade", "Busque um destino ou conte ao assistente o tipo de viagem que voce quer."),
            ("Marque favoritos", "Museus, mercados, mirantes ou comida de rua: escolha o que combina com voce."),
            ("A IA monta os dias", "O motor organiza paradas por horarios, distancias e energia diaria."),
            ("Explore com historias", "Siga a rota, ouça guias de voz e use tudo offline."),
        ],
        "pricing_title": "Um plano para sua viagem.",
        "pricing_lead": "No lancamento, Navitra sera gratis para baixar e planejar. Premium libera a experiencia completa com 7 dias de teste no plano anual.",
        "best_value": "Melhor valor",
        "yearly": "Anual",
        "monthly": "Mensal",
        "yearly_for": "Para quem viaja sempre.",
        "monthly_for": "Para a grande viagem.",
        "trial": "7 dias de teste gratis",
        "all_year": "Premium o ano todo",
        "month_equiv": "Cerca de $3.33 por mes",
        "full_access": "Acesso Premium completo",
        "voice_guides": "Guias de voz com IA em cada parada",
        "offline_nav": "Mapas e navegacao offline",
        "higher_limits": "Limites maiores de rotas com IA",
        "price_note": "Precos em USD; sua loja mostra os valores locais. Assinaturas renovam automaticamente e podem ser canceladas na loja.",
        "faq_title": "Perguntas frequentes",
        "faqs": [
            ("Navitra e gratis?", "Sim. No lancamento, baixar e planejar viagens sera gratis. Premium adiciona guias de voz, mapas offline e limites maiores."),
            ("Funciona offline?", "Com Premium, voce baixa o destino antes da viagem. Mapas, rotas e guias ficam no aparelho."),
            ("Como cancelar?", "A assinatura e gerenciada pela App Store ou Google Play e pode ser cancelada quando quiser."),
        ],
        "final_title": "O mundo espera.<br><em>Sua rota esta pronta.</em>",
        "final_lead": "Navitra prepara o lancamento no iOS; Android vem depois.",
        "tiny": "Gratis no lancamento · 7 dias de teste anual · Cancele quando quiser",
        "footer": "Companheiro de viagem com IA para descobrir, planejar e navegar.",
    },
}

# Reuse Spanish/French/Portuguese structure quality for non-Latin locales with
# concise native copy, kept separate so line length in the template stays sane.
LOCALES.update({
    "ar": {
        "lang": "ar", "dir": "rtl", "title": "Navitra - مخطط سفر ذكي بالذكاء الاصطناعي", "description": "Navitra يحول الأماكن التي تحبها إلى مسارات يومية ذكية مع دليل صوتي وخرائط بلا إنترنت واكتشافات مناسبة لرحلتك.",
        "nav_features": "المزايا", "nav_how": "طريقة العمل", "nav_pricing": "الأسعار", "nav_support": "الدعم", "launch": "حالة الإطلاق", "app_store": "قريبًا على App Store", "google_play": "Google Play لاحقًا",
        "hero_fact": "وُلد في إسطنبول", "hero_fact_strong": "مصمم لكل مدينة", "hero_title": "خطط بذكاء،<br>وسافر <em>أفضل</em>.", "hero_body": "Navitra يحول الأماكن التي تختارها إلى خطة يومية واقعية تراعي ساعات العمل والمسافات ووتيرتك. رفيق سفر ذكي يعمل أونلاين وأوفلاين.",
        "features_title": "تخطيط الرحلة لا يجب أن يكون مرهقًا.", "features_accent": "مع Navitra، اختر فقط.", "features_lead": "Navitra يتولى التفاصيل اللوجستية لتتفرغ للتجربة.",
        "features": [("تخطيط مسار بالذكاء الاصطناعي", "اختر الأماكن التي تعجبك، وسيبني الذكاء الاصطناعي كل يوم حسب الوقت والمسافة والوتيرة."), ("دليل صوتي ذكي", "استمع إلى قصة كل محطة بإحدى لغات السرد المدعومة."), ("خرائط بلا إنترنت", "حمّل رحلتك وخرائطك وأدلتك قبل الانطلاق."), ("اكتشاف ذكي", "أماكن مخفية، توقفات للطعام وبدائل تظهر في الوقت المناسب.")],
        "route_title": "من قائمة أمنيات إلى مسار قابل للمشي.", "route_body": "اختر مدينة، احفظ ما تحبه، ودع Navitra يبني خطة يومية تصلح على أرض الواقع.",
        "route_bullets": [("يراعي ساعات العمل", "المكان المغلق يوم الاثنين لن يظهر في خطة الاثنين."), ("أيام مجمعة جغرافيًا", "لا تنقلات مرهقة عبر المدينة لمحطة واحدة."), ("الفندق داخل الخطة", "كل يوم يبدأ وينتهي حيث تقيم فعليًا."), ("تعديل في أي لحظة", "تعبت أو جعت أو تغيرت الخطة؟ يتكيف باقي اليوم.")],
        "steps_title": "طريقة العمل", "steps_lead": "أربع خطوات من فكرة الرحلة إلى خطة جاهزة.",
        "steps": [("اختر مدينة", "ابحث عن وجهة أو صف للمساعد نوع الرحلة التي تريدها."), ("حدد ما تحبه", "متاحف، أسواق، إطلالات أو طعام شارع؛ اختر ما يناسبك."), ("الذكاء الاصطناعي يبني الأيام", "المحرك يرتب المحطات حسب الوقت والمسافة والطاقة."), ("استكشف مع القصص", "اتبع المسار، استمع للدليل الصوتي واستخدمه بلا إنترنت.")],
        "pricing_title": "خطة تناسب رحلتك.", "pricing_lead": "سيكون تنزيل Navitra والتخطيط به مجانيًا عند الإطلاق. Premium يفتح التجربة الكاملة مع تجربة مجانية 7 أيام في الخطة السنوية.", "best_value": "أفضل قيمة", "yearly": "سنوي", "monthly": "شهري", "yearly_for": "للمسافر المتكرر.", "monthly_for": "للرحلة الكبيرة.", "trial": "تجربة مجانية 7 أيام", "all_year": "Premium طوال العام", "month_equiv": "حوالي $3.33 شهريًا", "full_access": "وصول Premium كامل", "voice_guides": "دليل صوتي ذكي في كل محطة", "offline_nav": "خرائط وتنقل بلا إنترنت", "higher_limits": "حدود أعلى لمسارات الذكاء الاصطناعي", "price_note": "الأسعار بالدولار؛ يعرض المتجر السعر المحلي. الاشتراكات تتجدد تلقائيًا ويمكن إلغاؤها من المتجر.",
        "faq_title": "أسئلة شائعة", "faqs": [("هل Navitra مجاني؟", "نعم. عند الإطلاق سيكون التنزيل والتخطيط مجانيين. Premium يضيف الدليل الصوتي والخرائط offline وحدودًا أعلى."), ("هل يعمل بلا إنترنت؟", "مع Premium يمكنك تنزيل الوجهة قبل السفر؛ تبقى الخرائط والمسارات والأدلة على الجهاز."), ("كيف ألغي الاشتراك؟", "تتم إدارة الاشتراك من App Store أو Google Play ويمكن إلغاؤه في أي وقت.")],
        "final_title": "العالم ينتظر.<br><em>مسارك جاهز.</em>", "final_lead": "Navitra يستعد للإطلاق على iOS، وAndroid لاحقًا.", "tiny": "مجاني عند الإطلاق · تجربة 7 أيام للخطة السنوية · إلغاء في أي وقت", "footer": "رفيق سفر ذكي يساعدك على الاكتشاف والتخطيط والتنقل.",
    },
    "ja": {
        "lang": "ja", "dir": "ltr", "title": "Navitra - AI旅行プランナー | スマートな旅程", "description": "Navitraは、行きたい場所を音声ガイド、オフライン地図、スマートな発見つきの最適な日別ルートに変えます。",
        "nav_features": "機能", "nav_how": "使い方", "nav_pricing": "料金", "nav_support": "サポート", "launch": "公開状況", "app_store": "App Store 近日公開", "google_play": "Google Play は後日",
        "hero_fact": "イスタンブール生まれ", "hero_fact_strong": "あらゆる街のために", "hero_title": "もっと賢く計画し、<br>もっと良く<em>旅する</em>。", "hero_body": "Navitraは、好きな場所を営業時間、距離、あなたのペースに合わせた日別ルートに変えます。オンラインでもオフラインでも使えるAI旅行パートナーです。",
        "features_title": "旅行計画は、複雑である必要はありません。", "features_accent": "Navitraなら、選ぶだけ。", "features_lead": "面倒な調整はNavitraに任せて、旅の時間に集中できます。",
        "features": [("AIルート計画", "行きたい場所を選ぶだけ。AIが営業時間、距離、ペースに合わせて1日を組み立てます。"), ("AI音声ガイド", "対応しているナレーション言語で各スポットの物語を聞けます。"), ("オフライン地図", "出発前に旅程、地図、音声ガイドを保存。通信がなくても続けられます。"), ("スマート発見", "隠れた名所、食事休憩、代替案をちょうど良いタイミングで提案します。")],
        "route_title": "行きたいリストから、歩けるルートへ。", "route_body": "街を選び、気になる場所を保存すると、Navitraが現地で使える日別プランを作ります。",
        "route_bullets": [("営業時間を考慮", "月曜休館なら月曜の予定には入りません。"), ("エリアごとに整理", "一つのスポットのために街を何度も横断しません。"), ("宿泊地も考慮", "毎日、実際に泊まる場所から始まり戻ります。"), ("いつでも再調整", "疲れた、空腹、予定変更。残りの1日を組み直せます。")],
        "steps_title": "使い方", "steps_lead": "どこから始めるか迷う状態から、4ステップで完成したプランへ。",
        "steps": [("街を選ぶ", "目的地を検索するか、理想の旅をアシスタントに伝えます。"), ("好きな場所を選ぶ", "美術館、市場、展望スポット、ローカルフードなどを選択。"), ("AIが日程を作成", "営業時間、移動距離、1日の体力に合わせて順番を組みます。"), ("物語と一緒に探索", "ルートをたどり、音声ガイドを聞き、必要ならオフラインで使えます。")],
        "pricing_title": "旅に合うプラン。", "pricing_lead": "Navitraは公開時、ダウンロードと旅行計画を無料で利用できます。Premiumでは年間プランに7日間の無料トライアルがあります。", "best_value": "おすすめ", "yearly": "年間", "monthly": "月間", "yearly_for": "よく旅する人へ。", "monthly_for": "大きな旅行に。", "trial": "7日間無料トライアル", "all_year": "1年中Premium", "month_equiv": "月あたり約$3.33", "full_access": "Premium機能すべて", "voice_guides": "各スポットでAI音声ガイド", "offline_nav": "オフライン地図とナビ", "higher_limits": "AIルート上限を拡大", "price_note": "価格はUSD表記です。ストアでは現地価格が表示されます。サブスクリプションは自動更新され、ストア設定で解約できます。",
        "faq_title": "よくある質問", "faqs": [("Navitraは無料ですか？", "はい。公開時はダウンロードと旅行計画が無料です。Premiumでは音声ガイド、オフライン地図、上限拡大が使えます。"), ("本当にオフラインで使えますか？", "Premiumなら出発前に目的地を保存できます。地図、ルート、音声ガイドは端末に保存されます。"), ("解約方法は？", "App StoreまたはGoogle Playで管理し、いつでも解約できます。")],
        "final_title": "世界が待っています。<br><em>ルートは準備完了。</em>", "final_lead": "NavitraはiOS公開に向けて準備中です。Androidは後日対応予定です。", "tiny": "公開時無料 · 年間プラン7日間トライアル · いつでも解約", "footer": "発見、計画、移動を支えるAI旅行パートナー。",
    },
    "ko": {
        "lang": "ko", "dir": "ltr", "title": "Navitra - AI 여행 플래너 | 스마트 여행 루트", "description": "Navitra는 좋아하는 장소를 음성 가이드, 오프라인 지도, 스마트 추천이 담긴 최적의 일자별 루트로 바꿉니다.",
        "nav_features": "기능", "nav_how": "사용 방법", "nav_pricing": "가격", "nav_support": "지원", "launch": "출시 상태", "app_store": "App Store 곧 출시", "google_play": "Google Play 추후 공개",
        "hero_fact": "이스탄불에서 시작", "hero_fact_strong": "모든 도시를 위해", "hero_title": "더 똑똑하게 계획하고,<br>더 좋게 <em>여행하세요</em>.", "hero_body": "Navitra는 좋아하는 장소를 영업시간, 거리, 여행 속도에 맞춘 일자별 루트로 정리합니다. 온라인과 오프라인에서 함께하는 AI 여행 동반자입니다.",
        "features_title": "여행 계획은 복잡할 필요가 없습니다.", "features_accent": "Navitra에서는 선택만 하면 됩니다.", "features_lead": "복잡한 동선은 Navitra가 맡고, 당신은 여행에 집중하세요.",
        "features": [("AI 루트 계획", "가고 싶은 곳을 고르면 AI가 시간, 거리, 속도에 맞춰 하루를 구성합니다."), ("AI 음성 가이드", "지원되는 내레이션 언어로 각 장소의 이야기를 들을 수 있습니다."), ("오프라인 지도", "출발 전 여행, 지도, 음성 가이드를 저장하세요. 신호가 없어도 계속됩니다."), ("스마트 발견", "숨은 명소, 식사 시간, 대체 장소를 필요한 순간에 추천합니다.")],
        "route_title": "위시리스트를 걸을 수 있는 루트로.", "route_body": "도시를 고르고 마음에 드는 장소를 저장하면 Navitra가 실제로 움직이기 좋은 일정을 만듭니다.",
        "route_bullets": [("영업시간 반영", "월요일 휴무라면 월요일 일정에 넣지 않습니다."), ("지역별 일정 구성", "한 곳 때문에 도시를 왔다 갔다 하지 않습니다."), ("숙소 반영", "매일 실제 숙소에서 시작하고 돌아옵니다."), ("언제든 재구성", "피곤하거나 배고프거나 계획이 바뀌면 남은 하루를 다시 짭니다.")],
        "steps_title": "사용 방법", "steps_lead": "어디서 시작할지 모르는 순간에서 완성된 계획까지 네 단계입니다.",
        "steps": [("도시 선택", "목적지를 검색하거나 원하는 여행 스타일을 어시스턴트에게 말하세요."), ("좋아하는 곳 선택", "박물관, 시장, 전망대, 길거리 음식까지 마음에 드는 곳을 고릅니다."), ("AI가 하루를 구성", "루트 엔진이 영업시간, 거리, 에너지에 맞춰 정렬합니다."), ("이야기와 함께 탐험", "루트를 따라가고 음성 가이드를 듣고 오프라인에서도 사용하세요.")],
        "pricing_title": "여행에 맞는 플랜.", "pricing_lead": "Navitra는 출시 시 다운로드와 여행 계획이 무료입니다. Premium은 연간 플랜 7일 무료 체험과 함께 전체 경험을 엽니다.", "best_value": "최고 가치", "yearly": "연간", "monthly": "월간", "yearly_for": "자주 여행하는 분께.", "monthly_for": "큰 여행을 위해.", "trial": "7일 무료 체험 포함", "all_year": "일 년 내내 Premium", "month_equiv": "월 약 $3.33", "full_access": "전체 Premium 접근", "voice_guides": "모든 장소의 AI 음성 가이드", "offline_nav": "오프라인 지도와 내비게이션", "higher_limits": "더 높은 AI 루트 한도", "price_note": "가격은 USD 기준이며 스토어에서 현지 가격이 표시됩니다. 구독은 자동 갱신되며 스토어에서 언제든 취소할 수 있습니다.",
        "faq_title": "자주 묻는 질문", "faqs": [("Navitra는 무료인가요?", "예. 출시 시 다운로드와 여행 계획은 무료입니다. Premium은 음성 가이드, 오프라인 지도, 더 높은 한도를 제공합니다."), ("오프라인으로 정말 작동하나요?", "Premium에서는 여행 전 목적지를 다운로드할 수 있습니다. 지도, 루트, 음성 가이드가 기기에 저장됩니다."), ("어떻게 취소하나요?", "구독은 App Store 또는 Google Play에서 관리하며 언제든 취소할 수 있습니다.")],
        "final_title": "세상이 기다립니다.<br><em>루트는 준비됐습니다.</em>", "final_lead": "Navitra는 iOS 출시를 준비 중이며 Android는 추후 공개됩니다.", "tiny": "출시 시 무료 · 연간 플랜 7일 체험 · 언제든 취소", "footer": "발견, 계획, 이동을 돕는 AI 여행 동반자.",
    },
    "ru": {
        "lang": "ru", "dir": "ltr", "title": "Navitra - ИИ-планировщик поездок | Умные маршруты", "description": "Navitra превращает любимые места в оптимальные маршруты по дням с аудиогидами, офлайн-картами и умными рекомендациями.",
        "nav_features": "Функции", "nav_how": "Как работает", "nav_pricing": "Цены", "nav_support": "Поддержка", "launch": "Статус запуска", "app_store": "Скоро в App Store", "google_play": "Google Play позже",
        "hero_fact": "Рождено в Стамбуле", "hero_fact_strong": "Для каждого города", "hero_title": "Планируйте умнее,<br>путешествуйте <em>лучше</em>.", "hero_body": "Navitra превращает выбранные места в маршрут по дням с учетом часов работы, расстояний и вашего темпа. Ваш ИИ-помощник в путешествии онлайн и офлайн.",
        "features_title": "Планирование поездки не должно быть сложным.", "features_accent": "С Navitra вы просто выбираете.", "features_lead": "Navitra берет логистику на себя, а вы наслаждаетесь поездкой.",
        "features": [("ИИ-маршруты", "Выберите места, а ИИ соберет дни по времени работы, расстояниям и вашему темпу."), ("ИИ-аудиогид", "Слушайте истории каждой остановки на одном из поддерживаемых языков озвучки."), ("Офлайн-карты", "Загрузите маршрут, карты и гиды заранее. Связь не обязательна."), ("Умные открытия", "Скрытые места, паузы на еду и альтернативы появляются вовремя.")],
        "route_title": "От списка желаний к маршруту пешком.", "route_body": "Выберите город, сохраните интересные места, и Navitra соберет реалистичный план на каждый день.",
        "route_bullets": [("Учет часов работы", "Если место закрыто в понедельник, его не будет в плане на понедельник."), ("Дни по районам", "Без лишних поездок через весь город ради одной точки."), ("Отель в маршруте", "Каждый день начинается и заканчивается там, где вы живете."), ("Перестройка в любой момент", "Устали, проголодались или изменили планы? День перестраивается.")],
        "steps_title": "Как работает", "steps_lead": "Четыре шага от идеи до готового плана.",
        "steps": [("Выберите город", "Найдите направление или опишите ассистенту желаемую поездку."), ("Отметьте любимое", "Музеи, рынки, виды или уличная еда — выбирайте то, что интересно."), ("ИИ собирает дни", "Движок маршрутов расставляет остановки по времени, расстоянию и энергии."), ("Исследуйте с историями", "Следуйте маршруту, слушайте аудиогиды и пользуйтесь офлайн.")],
        "pricing_title": "План под вашу поездку.", "pricing_lead": "На запуске Navitra будет бесплатна для скачивания и планирования. Premium откроет полный опыт с 7-дневным пробным периодом на годовом плане.", "best_value": "Лучшее предложение", "yearly": "Годовой", "monthly": "Месячный", "yearly_for": "Для частых путешествий.", "monthly_for": "Для большой поездки.", "trial": "7 дней бесплатно", "all_year": "Premium на весь год", "month_equiv": "Около $3.33 в месяц", "full_access": "Полный доступ Premium", "voice_guides": "ИИ-аудиогид на каждой остановке", "offline_nav": "Офлайн-карты и навигация", "higher_limits": "Больше лимитов для ИИ-маршрутов", "price_note": "Цены указаны в USD; магазин покажет локальную цену. Подписки продлеваются автоматически и отменяются в магазине.",
        "faq_title": "Частые вопросы", "faqs": [("Navitra бесплатна?", "Да. На запуске скачивание и планирование будут бесплатными. Premium добавит аудиогиды, офлайн-карты и повышенные лимиты."), ("Работает офлайн?", "С Premium можно заранее загрузить направление. Карты, маршруты и гиды сохраняются на устройстве."), ("Как отменить?", "Подписка управляется через App Store или Google Play и может быть отменена в любое время.")],
        "final_title": "Мир ждет.<br><em>Ваш маршрут готов.</em>", "final_lead": "Navitra готовится к запуску на iOS; Android появится позже.", "tiny": "Бесплатно на запуске · 7 дней пробного годового плана · Отмена в любое время", "footer": "ИИ-спутник для открытия мест, планирования и навигации.",
    },
    "zh-hans": {
        "lang": "zh-Hans", "dir": "ltr", "title": "Navitra - AI旅行规划师 | 智能路线", "description": "Navitra 将你喜欢的地点变成按天优化的旅行路线，包含语音导览、离线地图和智能发现。",
        "nav_features": "功能", "nav_how": "如何使用", "nav_pricing": "价格", "nav_support": "支持", "launch": "上线状态", "app_store": "App Store 即将上线", "google_play": "Google Play 稍后推出",
        "hero_fact": "诞生于伊斯坦布尔", "hero_fact_strong": "为每座城市而做", "hero_title": "更聪明地计划，<br>更好地<em>旅行</em>。", "hero_body": "Navitra 会把你喜欢的地点整理成按天优化的路线，兼顾开放时间、距离和你的节奏。在线或离线，都能陪你旅行。",
        "features_title": "旅行计划不该复杂。", "features_accent": "用 Navitra，只需选择。", "features_lead": "路线和时间交给 Navitra，你专注享受旅程。",
        "features": [("AI路线规划", "选择想去的地方，AI 会按开放时间、距离和节奏安排每天路线。"), ("AI语音导览", "可使用受支持的讲解语言收听每个地点的故事。"), ("离线地图", "出发前下载路线、地图和语音导览，没有网络也能继续。"), ("智能发现", "隐藏景点、用餐停靠和替代方案会在合适时机出现。")],
        "route_title": "从心愿清单到可步行路线。", "route_body": "选择城市，保存喜欢的地点，Navitra 会生成真正适合落地执行的日程。",
        "route_bullets": [("考虑开放时间", "周一关闭的地点不会出现在周一行程里。"), ("按区域组织每天", "不会为了一个地点反复横穿城市。"), ("纳入住宿位置", "每天从真实住宿点开始并返回。"), ("随时重新安排", "累了、饿了或计划变化，剩余行程可重新调整。")],
        "steps_title": "如何使用", "steps_lead": "从不知道从哪开始，到完成计划，只需四步。",
        "steps": [("选择城市", "搜索目的地，或告诉助手你想要什么样的旅行。"), ("标记喜欢的地点", "博物馆、市场、观景点或街头美食，选你真正感兴趣的。"), ("AI安排每天", "路线引擎会按时间、距离和每日精力排序。"), ("带着故事探索", "跟随路线，收听语音导览，需要时离线使用。")],
        "pricing_title": "适合你旅程的计划。", "pricing_lead": "Navitra 上线时可免费下载并免费规划。Premium 解锁完整体验，年度计划含 7 天免费试用。", "best_value": "最划算", "yearly": "年度", "monthly": "月度", "yearly_for": "适合经常旅行的人。", "monthly_for": "适合一次大旅行。", "trial": "含 7 天免费试用", "all_year": "全年 Premium", "month_equiv": "约每月 $3.33", "full_access": "完整 Premium 权限", "voice_guides": "每站 AI 语音导览", "offline_nav": "离线地图和导航", "higher_limits": "更高 AI 路线额度", "price_note": "价格以美元显示；商店会显示本地价格。订阅会自动续订，可在商店设置中取消。",
        "faq_title": "常见问题", "faqs": [("Navitra 免费吗？", "是。上线时下载和规划旅行免费。Premium 会提供语音导览、离线地图和更高 AI 路线额度。"), ("真的可以离线使用吗？", "Premium 用户可在出发前下载目的地。地图、路线和语音导览会保存在设备上。"), ("如何取消？", "订阅由 App Store 或 Google Play 管理，可随时取消。")],
        "final_title": "世界在等你。<br><em>路线已准备好。</em>", "final_lead": "Navitra 正在准备 iOS 上线，Android 将稍后推出。", "tiny": "上线时免费 · 年度计划 7 天试用 · 可随时取消", "footer": "帮助你发现、计划和导航的 AI 旅行伙伴。",
    },
})


def link_tags(current: str) -> str:
    tags = ['    <link rel="alternate" hreflang="x-default" href="https://navitraapp.com/">']
    for code, meta in LANGS.items():
        tags.append(
            f'    <link rel="alternate" hreflang="{meta["hreflang"]}" href="https://navitraapp.com{meta["url"]}">'
        )
    return "\n".join(tags)


def lang_switcher(current: str) -> str:
    anchors = []
    for code, meta in LANGS.items():
        cls = ' class="active"' if code == current else ""
        anchors.append(f'<a{cls} href="{meta["url"]}">{escape(meta["name"])}</a>')
    return "\n".join(anchors)


def render_list(items: list[tuple[str, str]]) -> str:
    return "\n".join(
        f'<li><span>{escape(title)}</span><small>{escape(body)}</small></li>'
        for title, body in items
    )


def render_cards(items: list[tuple[str, str]]) -> str:
    return "\n".join(
        f'<article><h3>{escape(title)}</h3><p>{escape(body)}</p></article>'
        for title, body in items
    )


def render_steps(items: list[tuple[str, str]]) -> str:
    return "\n".join(
        f'<article><b>{idx:02d}</b><h3>{escape(title)}</h3><p>{escape(body)}</p></article>'
        for idx, (title, body) in enumerate(items, 1)
    )


def render_faq(items: list[tuple[str, str]]) -> str:
    return "\n".join(
        f'<details><summary>{escape(q)}</summary><p>{escape(a)}</p></details>'
        for q, a in items
    )


def render_page(code: str, t: dict[str, object]) -> str:
    u = UI_LABELS[code]
    lang = t["lang"]
    direction = t["dir"]
    canonical = f"https://navitraapp.com/{code}/"
    return f"""<!DOCTYPE html>
<html lang="{lang}" dir="{direction}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{escape(t["title"])}</title>
    <meta name="description" content="{escape(t["description"])}">
    <meta property="og:title" content="{escape(t["title"])}">
    <meta property="og:description" content="{escape(t["description"])}">
    <meta property="og:image" content="https://navitraapp.com/og-image.jpg">
    <meta property="og:url" content="{canonical}">
    <meta property="og:type" content="website">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{escape(t["title"])}">
    <meta name="twitter:description" content="{escape(t["description"])}">
    <meta name="twitter:image" content="https://navitraapp.com/og-image.jpg">
    <link rel="canonical" href="{canonical}">
{link_tags(code)}
    <link rel="icon" type="image/png" href="/favicon.png?v=2">
    <link rel="apple-touch-icon" href="/apple-touch-icon.png?v=2">
    <meta name="theme-color" content="#12121F">
    <style>
        :root {{ --night:#12121f; --ink:#20202b; --mut:#6f6d78; --cream:#faf8f1; --paper:#fffaf0; --line:rgba(32,32,43,.13); --sun:#ff5a2e; --sun2:#ff865f; }}
        * {{ box-sizing:border-box; }}
        body {{ margin:0; font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; background:var(--cream); color:var(--ink); }}
        a {{ color:inherit; text-decoration:none; }}
        .wrap {{ width:min(1180px, calc(100% - 40px)); margin:0 auto; }}
        nav {{ position:sticky; top:0; z-index:5; background:rgba(18,18,31,.92); color:white; backdrop-filter:blur(18px); border-bottom:1px solid rgba(255,255,255,.12); }}
        .nav-inner {{ height:72px; display:flex; align-items:center; justify-content:space-between; gap:24px; }}
        .brand {{ display:flex; align-items:center; gap:10px; font-weight:800; font-size:21px; }}
        .brand img {{ width:32px; height:32px; border-radius:9px; }}
        .nav-links {{ display:flex; align-items:center; gap:20px; font-size:13px; font-weight:700; text-transform:uppercase; letter-spacing:.08em; }}
        .nav-links a {{ opacity:.86; }}
        .pill {{ display:inline-flex; align-items:center; justify-content:center; min-height:46px; padding:13px 24px; border-radius:999px; font-weight:800; font-size:13px; letter-spacing:.08em; text-transform:uppercase; background:var(--sun); color:white; box-shadow:0 16px 35px rgba(255,90,46,.25); }}
        .pill.alt {{ background:transparent; color:var(--ink); border:1px solid var(--line); box-shadow:none; }}
        .hero {{ background:radial-gradient(circle at 75% 20%, rgba(255,90,46,.28), transparent 26%), linear-gradient(135deg, #11111f, #272137 58%, #5b2e24); color:white; padding:86px 0 78px; overflow:hidden; }}
        .hero-grid {{ display:grid; grid-template-columns:1.05fr .95fr; gap:54px; align-items:center; }}
        .eyebrow {{ color:var(--sun2); font-size:12px; font-weight:800; letter-spacing:.16em; text-transform:uppercase; }}
        h1 {{ font-size:clamp(3rem, 7vw, 6.4rem); line-height:.94; margin:18px 0 22px; letter-spacing:-.04em; }}
        h1 em, .accent {{ color:var(--sun2); font-style:normal; }}
        .hero p {{ color:rgba(255,255,255,.82); font-size:clamp(1.04rem, 1.7vw, 1.32rem); line-height:1.55; max-width:620px; }}
        .cta-row {{ display:flex; flex-wrap:wrap; gap:12px; margin-top:30px; }}
        .ghost {{ background:rgba(255,255,255,.08); border:1px solid rgba(255,255,255,.28); box-shadow:none; }}
        .visual {{ border-radius:8px; min-height:560px; background:#f4f2ed url('/img/app-route-result.png') center/contain no-repeat; box-shadow:0 34px 80px rgba(0,0,0,.32); }}
        section {{ padding:86px 0; }}
        .section-head {{ max-width:850px; margin-bottom:34px; }}
        h2 {{ font-size:clamp(2.1rem, 4vw, 4.2rem); line-height:1.02; letter-spacing:-.035em; margin:8px 0 16px; }}
        .lead {{ font-size:1.1rem; line-height:1.65; color:var(--mut); max-width:760px; }}
        .grid4 {{ display:grid; grid-template-columns:repeat(4,1fr); gap:16px; }}
        .grid4 article, .plan-card, .price-card, details {{ background:white; border:1px solid var(--line); border-radius:8px; padding:24px; box-shadow:0 14px 42px rgba(30,30,45,.06); }}
        h3 {{ margin:0 0 10px; font-size:1.18rem; }}
        article p, details p, li small {{ color:var(--mut); line-height:1.55; }}
        .route {{ background:var(--paper); }}
        .split {{ display:grid; grid-template-columns:.95fr 1.05fr; gap:40px; align-items:start; }}
        .plan-card ul {{ list-style:none; padding:0; margin:0; display:grid; gap:14px; }}
        .plan-card li {{ display:grid; gap:4px; padding-bottom:14px; border-bottom:1px solid var(--line); }}
        .plan-card li:last-child {{ border-bottom:0; padding-bottom:0; }}
        .plan-card span {{ font-weight:800; }}
        .steps {{ display:grid; grid-template-columns:repeat(4,1fr); gap:16px; counter-reset:step; }}
        .steps b {{ display:inline-grid; place-items:center; width:40px; height:40px; border-radius:50%; background:var(--sun); color:white; margin-bottom:18px; }}
        .pricing {{ background:#171725; color:white; }}
        .pricing .lead {{ color:rgba(255,255,255,.68); }}
        .prices {{ display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:18px; max-width:940px; }}
        .price-card {{ background:#222235; border-color:rgba(255,255,255,.13); color:white; }}
        .price-card.hot {{ background:linear-gradient(160deg, #ff5a2e, #c44324); }}
        .badge {{ display:inline-flex; padding:7px 10px; border-radius:999px; background:rgba(255,255,255,.16); font-size:12px; font-weight:800; margin-bottom:16px; }}
        .amount {{ font-size:2.8rem; font-weight:900; margin:12px 0; }}
        .amount span {{ font-size:1rem; opacity:.72; }}
        .price-card ul {{ margin:18px 0 0; padding-inline-start:20px; line-height:1.8; color:rgba(255,255,255,.82); }}
        .note {{ color:rgba(255,255,255,.62); font-size:.9rem; line-height:1.55; margin-top:20px; }}
        .faq-list {{ display:grid; gap:12px; max-width:860px; }}
        summary {{ cursor:pointer; font-weight:800; }}
        details p {{ margin-bottom:0; }}
        .final {{ text-align:center; background:var(--night); color:white; }}
        .final p {{ color:rgba(255,255,255,.72); }}
        footer {{ background:#0d0d17; color:white; padding:48px 0; }}
        .footer-grid {{ display:grid; grid-template-columns:1.3fr repeat(3,auto); gap:32px; }}
        footer p, footer a {{ color:rgba(255,255,255,.72); }}
        .lang-list {{ display:flex; flex-wrap:wrap; gap:8px; max-width:520px; }}
        .lang-list a {{ border:1px solid rgba(255,255,255,.18); border-radius:999px; padding:7px 11px; font-size:12px; }}
        .lang-list .active {{ background:white; color:var(--night); }}
        html[dir="rtl"] .nav-links, html[dir="rtl"] .cta-row, html[dir="rtl"] .lang-list {{ flex-direction:row-reverse; }}
        @media (max-width:900px) {{ .hero-grid,.split,.prices,.footer-grid {{ grid-template-columns:1fr; }} .grid4,.steps {{ grid-template-columns:1fr 1fr; }} .nav-links {{ display:none; }} .visual {{ min-height:520px; }} }}
        @media (max-width:560px) {{ .grid4,.steps {{ grid-template-columns:1fr; }} h1 {{ font-size:3rem; }} section {{ padding:64px 0; }} }}
    </style>
</head>
<body>
    <nav>
        <div class="wrap nav-inner">
            <a class="brand" href="/"><img src="/logo-white.png" alt="">Navitra</a>
            <div class="nav-links">
                <a href="#features">{escape(t["nav_features"])}</a>
                <a href="#how">{escape(t["nav_how"])}</a>
                <a href="#pricing">{escape(t["nav_pricing"])}</a>
                <a href="/support.html">{escape(t["nav_support"])}</a>
                <a class="pill" href="#download">{escape(t["launch"])}</a>
            </div>
        </div>
    </nav>

    <header class="hero">
        <div class="wrap hero-grid">
            <div>
                <div class="eyebrow">{escape(t["hero_fact"])} · {escape(t["hero_fact_strong"])}</div>
                <h1>{t["hero_title"]}</h1>
                <p>{escape(t["hero_body"])}</p>
                <div class="cta-row">
                    <a class="pill" href="#download">{escape(t["app_store"])}</a>
                    <a class="pill ghost" href="#download">{escape(t["google_play"])}</a>
                </div>
            </div>
            <div class="visual" role="img" aria-label="{escape(u["preview"])}"></div>
        </div>
    </header>

    <main>
        <section id="features">
            <div class="wrap">
                <div class="section-head">
                    <div class="eyebrow">Navitra</div>
                    <h2>{escape(t["features_title"])} <span class="accent">{escape(t["features_accent"])}</span></h2>
                    <p class="lead">{escape(t["features_lead"])}</p>
                </div>
                <div class="grid4">{render_cards(t["features"])}</div>
            </div>
        </section>

        <section class="route">
            <div class="wrap split">
                <div>
                    <div class="eyebrow">{escape(u["route_engine"])}</div>
                    <h2>{escape(t["route_title"])}</h2>
                    <p class="lead">{escape(t["route_body"])}</p>
                </div>
                <div class="plan-card">
                    <ul>{render_list(t["route_bullets"])}</ul>
                </div>
            </div>
        </section>

        <section id="how">
            <div class="wrap">
                <div class="section-head">
                    <div class="eyebrow">{escape(t["nav_how"])}</div>
                    <h2>{escape(t["steps_title"])}</h2>
                    <p class="lead">{escape(t["steps_lead"])}</p>
                </div>
                <div class="steps">{render_steps(t["steps"])}</div>
            </div>
        </section>

        <section class="pricing" id="pricing">
            <div class="wrap">
                <div class="section-head">
                    <div class="eyebrow">{escape(t["nav_pricing"])}</div>
                    <h2>{escape(t["pricing_title"])}</h2>
                    <p class="lead">{escape(t["pricing_lead"])}</p>
                </div>
                <div class="prices">
                    <article class="price-card hot">
                        <span class="badge">{escape(t["best_value"])}</span>
                        <h3>{escape(t["yearly"])}</h3>
                        <p>{escape(t["yearly_for"])}</p>
                        <div class="amount">$39.99 <span>/ {escape(u["year_unit"])}</span></div>
                        <ul>
                            <li>{escape(t["trial"])}</li>
                            <li>{escape(t["all_year"])}</li>
                            <li>{escape(t["month_equiv"])}</li>
                        </ul>
                    </article>
                    <article class="price-card">
                        <h3>{escape(t["monthly"])}</h3>
                        <p>{escape(t["monthly_for"])}</p>
                        <div class="amount">$5.99 <span>/ {escape(u["month_unit"])}</span></div>
                        <ul>
                            <li>{escape(t["full_access"])}</li>
                            <li>{escape(t["voice_guides"])}</li>
                            <li>{escape(t["offline_nav"])}</li>
                            <li>{escape(t["higher_limits"])}</li>
                        </ul>
                    </article>
                </div>
                <p class="note">{escape(t["price_note"])}</p>
            </div>
        </section>

        <section>
            <div class="wrap">
                <div class="section-head">
                    <div class="eyebrow">{escape(u["faq"])}</div>
                    <h2>{escape(t["faq_title"])}</h2>
                </div>
                <div class="faq-list">{render_faq(t["faqs"])}</div>
            </div>
        </section>

        <section class="final" id="download">
            <div class="wrap">
                <h2>{t["final_title"]}</h2>
                <p class="lead" style="margin-inline:auto">{escape(t["final_lead"])}</p>
                <div class="cta-row" style="justify-content:center">
                    <a class="pill" href="#download">{escape(t["app_store"])}</a>
                    <a class="pill ghost" href="#download">{escape(t["google_play"])}</a>
                </div>
                <p>{escape(t["tiny"])}</p>
            </div>
        </section>
    </main>

    <footer>
        <div class="wrap footer-grid">
            <div>
                <a class="brand" href="/"><img src="/logo-white.png" alt="">Navitra</a>
                <p>{escape(t["footer"])}</p>
            </div>
            <div>
                <h3>{escape(t["nav_support"])}</h3>
                <p><a href="/support.html">{escape(u["support"])}</a><br><a href="mailto:support@navitraapp.com">support@navitraapp.com</a></p>
            </div>
            <div>
                <h3>{escape(u["legal"])}</h3>
                <p><a href="/privacy.html">{escape(u["privacy"])}</a><br><a href="/terms.html">{escape(u["terms"])}</a></p>
            </div>
            <div>
                <h3>{escape(u["languages"])}</h3>
                <div class="lang-list">{lang_switcher(code)}</div>
            </div>
        </div>
    </footer>
</body>
</html>
"""


def write_pages() -> None:
    for code, data in LOCALES.items():
        directory = ROOT / code
        directory.mkdir(exist_ok=True)
        (directory / "index.html").write_text(render_page(code, data), encoding="utf-8", newline="\n")


def write_sitemap() -> None:
    urls = [
        ("https://navitraapp.com/", "1.0"),
        ("https://navitraapp.com/support.html", "0.5"),
        ("https://navitraapp.com/privacy.html", "0.5"),
        ("https://navitraapp.com/terms.html", "0.5"),
        ("https://navitraapp.com/delete.html", "0.5"),
        ("https://navitraapp.com/delete/", "0.5"),
    ]
    for code in LOCALES:
        urls.append((f"https://navitraapp.com/{code}/", "0.8"))

    body = "\n".join(
        f"  <url>\n    <loc>{loc}</loc>\n    <lastmod>{LASTMOD}</lastmod>\n    <priority>{priority}</priority>\n  </url>"
        for loc, priority in urls
    )
    (ROOT / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{body}\n</urlset>\n',
        encoding="utf-8",
        newline="\n",
    )


if __name__ == "__main__":
    write_pages()
    write_sitemap()
    print(f"Generated {len(LOCALES)} localized pages.")
