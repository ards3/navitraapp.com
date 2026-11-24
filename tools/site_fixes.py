"""Post-launch copy and structured data for the localized landing pages.

The original locale tables in generate_localized_site.py were written before the
App Store launch ("free at launch", "App Store soon"). This module holds the
live-app copy that overrides them, the full six-question FAQ for every locale,
and the JSON-LD (MobileApplication + FAQPage) that search engines and AI
assistants read.
"""

from __future__ import annotations

import json
import re

STORE_URL = "https://apps.apple.com/us/app/navitra-ai-travel-planner/id6779956173"
SAME_AS = [
    "https://x.com/navitratravel",
    "https://www.instagram.com/navitra.travel/",
    "https://www.tiktok.com/@navitra.travel",
    "https://www.youtube.com/@navitraaitravelplanner",
]

# free: hero/CTA chip · gplay: Android pill · tiny: line under the final CTA
# faq: free, route, languages (offline/share/delete come from the existing tables)
LIVE = {
    "tr": {
        "free": "Ücretsiz indir",
        "gplay": "Google Play · Yakında",
        "pricing_lead": "Navitra'yı indirmek ve gezi planlamak ücretsiz. Premium tüm deneyimi açar; aylık ve yıllık seçenekler var, yıllık plan 7 günlük ücretsiz denemeyle başlar.",
        "tiny": "Ücretsiz indir · Yıllık planda 7 gün deneme · İstediğin zaman iptal",
        "free_a": "Evet. Navitra'yı indirmek ve gezi planlamak ücretsiz. Premium; AI sesli rehber, offline haritalar, bütçe planlama ve daha yüksek AI rota limitleri ekler. Güncel aylık ve yıllık fiyatı App Store'da kendi para biriminle görürsün; yıllık plan 7 günlük ücretsiz denemeyle başlar.",
        "route_q": "AI rotamı nasıl oluşturuyor?",
        "route_a": "Navitra'nın rota motoru gezini gerçek bir lojistik problemi gibi ele alır: her yerin açılış saatlerini kontrol eder, yakın durakları aynı güne toplar, yürümeyi en aza indirecek şekilde sıralar ve her durağa gerçekçi süre ayırır. Ardından AI açıklamalar, ipuçları ve yemek önerileri ekler.",
        "lang_q": "Navitra hangi dilleri konuşuyor?",
        "lang_a": "Yedi dili tam olarak: Türkçe, İngilizce, Almanca, İspanyolca, Fransızca, Arapça ve Çince. Arayüz, AI planları ve sesli rehberler senin dilini takip eder.",
    },
    "de": {
        "free": "Kostenloser Download",
        "gplay": "Google Play · Demnächst",
        "pricing_lead": "Navitra ist kostenlos zum Herunterladen und Planen. Premium schaltet die volle Erfahrung frei, mit monatlicher und jährlicher Option; der Jahresplan startet mit 7 Tagen Gratis-Test.",
        "tiny": "Kostenloser Download · 7 Tage Test im Jahresplan · Jederzeit kündbar",
        "free_a": "Ja. Download und Reiseplanung sind kostenlos. Premium ergänzt KI-Sprachguides, Offline-Karten, Budgetplanung und höhere KI-Routenlimits. Den aktuellen Preis siehst du im App Store in deiner Währung; der Jahresplan startet mit 7 Tagen Gratis-Test.",
        "route_q": "Wie erstellt die KI meine Route?",
        "route_a": "Navitras Routenmotor behandelt deine Reise wie ein echtes Logistikproblem: Er prüft Öffnungszeiten, bündelt nahe Orte am selben Tag, ordnet sie für möglichst kurze Wege und plant realistische Zeit pro Stopp ein. Danach ergänzt die KI Beschreibungen, Tipps und Essensvorschläge.",
        "lang_q": "Welche Sprachen spricht Navitra?",
        "lang_a": "Sieben, vollständig: Deutsch, Englisch, Türkisch, Spanisch, Französisch, Arabisch und Chinesisch. Oberfläche, KI-Pläne und Sprachguides folgen deiner Sprache.",
    },
    "es": {
        "free": "Descarga gratis",
        "gplay": "Google Play · Próximamente",
        "pricing_lead": "Descargar Navitra y planificar viajes es gratis. Premium desbloquea la experiencia completa, con opción mensual y anual; el plan anual empieza con 7 días de prueba gratis.",
        "tiny": "Descarga gratis · 7 días de prueba en el plan anual · Cancela cuando quieras",
        "free_a": "Sí. Descargar y planificar es gratis. Premium añade guías de voz con IA, mapas offline, presupuesto y más rutas con IA. Verás el precio actual en tu moneda en el App Store; el plan anual empieza con 7 días de prueba gratis.",
        "route_q": "¿Cómo crea la IA mi ruta?",
        "route_a": "El motor de rutas de Navitra trata tu viaje como un problema logístico real: revisa horarios de apertura, agrupa lugares cercanos en el mismo día, los ordena para caminar lo mínimo y reserva un tiempo realista en cada parada. Después la IA añade descripciones, consejos y sugerencias para comer.",
        "lang_q": "¿Qué idiomas habla Navitra?",
        "lang_a": "Siete, por completo: español, inglés, turco, alemán, francés, árabe y chino. La interfaz, los planes con IA y las guías de voz siguen tu idioma.",
    },
    "fr": {
        "free": "Téléchargement gratuit",
        "gplay": "Google Play · Bientôt",
        "pricing_lead": "Télécharger Navitra et planifier vos voyages est gratuit. Premium débloque l’expérience complète, en mensuel ou en annuel ; l’offre annuelle commence par 7 jours d’essai gratuit.",
        "tiny": "Téléchargement gratuit · 7 jours d’essai sur l’offre annuelle · Résiliable à tout moment",
        "free_a": "Oui. Le téléchargement et la planification sont gratuits. Premium ajoute les guides vocaux IA, les cartes hors ligne, le budget et des limites d’itinéraires IA plus élevées. Le prix actuel s’affiche dans votre devise sur l’App Store ; l’offre annuelle commence par 7 jours d’essai gratuit.",
        "route_q": "Comment l’IA construit-elle mon itinéraire ?",
        "route_a": "Le moteur d’itinéraire de Navitra traite votre voyage comme un vrai problème logistique : il vérifie les horaires d’ouverture, regroupe les lieux proches le même jour, les ordonne pour limiter la marche et prévoit un temps réaliste à chaque étape. L’IA ajoute ensuite descriptions, conseils et idées de repas.",
        "lang_q": "Quelles langues Navitra parle-t-il ?",
        "lang_a": "Sept, entièrement : français, anglais, turc, allemand, espagnol, arabe et chinois. L’interface, les plans IA et les guides vocaux suivent votre langue.",
    },
    "it": {
        "free": "Download gratuito",
        "gplay": "Google Play · In arrivo",
        "pricing_lead": "Scaricare Navitra e pianificare viaggi è gratis. Premium sblocca l’esperienza completa, con opzione mensile e annuale; il piano annuale inizia con 7 giorni di prova gratuita.",
        "tiny": "Download gratuito · 7 giorni di prova sul piano annuale · Annulli quando vuoi",
        "free_a": "Sì. Download e pianificazione sono gratuiti. Premium aggiunge guide vocali IA, mappe offline, budget e limiti più alti per gli itinerari IA. Il prezzo attuale è indicato nella tua valuta sull’App Store; il piano annuale inizia con 7 giorni di prova gratuita.",
        "route_q": "Come costruisce l’IA il mio itinerario?",
        "route_a": "Il motore di Navitra tratta il viaggio come un vero problema logistico: controlla gli orari di apertura, raggruppa i luoghi vicini nello stesso giorno, li ordina per camminare il meno possibile e assegna un tempo realistico a ogni tappa. Poi l’IA aggiunge descrizioni, consigli e suggerimenti per mangiare.",
        "lang_q": "Quali lingue parla Navitra?",
        "lang_a": "Sette, completamente: inglese, turco, tedesco, spagnolo, francese, arabo e cinese. Interfaccia, piani IA e guide vocali seguono la tua lingua.",
    },
    "nl": {
        "free": "Gratis downloaden",
        "gplay": "Google Play · Binnenkort",
        "pricing_lead": "Navitra downloaden en reizen plannen is gratis. Premium ontgrendelt de volledige ervaring, maandelijks of jaarlijks; het jaarplan begint met 7 dagen gratis proberen.",
        "tiny": "Gratis downloaden · 7 dagen proef bij het jaarplan · Altijd opzegbaar",
        "free_a": "Ja. Downloaden en plannen is gratis. Premium voegt AI-audiogidsen, offline kaarten, budgetplanning en hogere AI-routelimieten toe. De actuele prijs zie je in je eigen valuta in de App Store; het jaarplan begint met 7 dagen gratis proberen.",
        "route_q": "Hoe bouwt de AI mijn route?",
        "route_a": "De route-engine van Navitra behandelt je reis als een echt logistiek probleem: hij controleert openingstijden, bundelt plekken die dicht bij elkaar liggen op dezelfde dag, zet ze in een volgorde met zo min mogelijk lopen en plant realistische tijd per stop. Daarna voegt de AI beschrijvingen, tips en eetsuggesties toe.",
        "lang_q": "Welke talen spreekt Navitra?",
        "lang_a": "Zeven, volledig: Engels, Turks, Duits, Spaans, Frans, Arabisch en Chinees. De interface, AI-plannen en audiogidsen volgen jouw taal.",
    },
    "pt-br": {
        "free": "Download grátis",
        "gplay": "Google Play · Em breve",
        "pricing_lead": "Baixar a Navitra e planejar viagens é grátis. O Premium libera a experiência completa, com opção mensal e anual; o plano anual começa com 7 dias de teste grátis.",
        "tiny": "Download grátis · 7 dias de teste no plano anual · Cancele quando quiser",
        "free_a": "Sim. Baixar e planejar é grátis. O Premium adiciona guias de voz com IA, mapas offline, planejamento de orçamento e limites maiores de rotas com IA. O preço atual aparece na sua moeda na App Store; o plano anual começa com 7 dias de teste grátis.",
        "route_q": "Como a IA monta minha rota?",
        "route_a": "O motor de rotas da Navitra trata sua viagem como um problema real de logística: confere horários de funcionamento, agrupa lugares próximos no mesmo dia, ordena para você andar o mínimo e reserva um tempo realista em cada parada. Depois a IA acrescenta descrições, dicas e sugestões de refeição.",
        "lang_q": "Quais idiomas a Navitra fala?",
        "lang_a": "Sete, por completo: inglês, turco, alemão, espanhol, francês, árabe e chinês. A interface, os planos de IA e os guias de voz seguem o seu idioma.",
    },
    "ar": {
        "free": "تنزيل مجاني",
        "gplay": "Google Play · قريبًا",
        "pricing_lead": "تنزيل Navitra وتخطيط الرحلات مجاني. يفتح Premium التجربة الكاملة باشتراك شهري أو سنوي، ويبدأ الاشتراك السنوي بتجربة مجانية لمدة 7 أيام.",
        "tiny": "تنزيل مجاني · تجربة 7 أيام في الخطة السنوية · إلغاء في أي وقت",
        "free_a": "نعم. التنزيل والتخطيط مجانيان. يضيف Premium أدلة صوتية بالذكاء الاصطناعي وخرائط بلا إنترنت وتخطيط الميزانية وحدودًا أعلى للمسارات. يظهر السعر الحالي بعملتك في App Store، وتبدأ الخطة السنوية بتجربة مجانية لمدة 7 أيام.",
        "route_q": "كيف يبني الذكاء الاصطناعي مساري؟",
        "route_a": "يتعامل محرك المسارات في Navitra مع رحلتك كمسألة لوجستية حقيقية: يتحقق من مواعيد الافتتاح، ويجمع الأماكن القريبة في اليوم نفسه، ويرتبها لتقليل المشي، ويخصص وقتًا واقعيًا لكل محطة. بعد ذلك يضيف الذكاء الاصطناعي الأوصاف والنصائح واقتراحات الطعام.",
        "lang_q": "ما اللغات التي يتحدثها Navitra؟",
        "lang_a": "سبع لغات بالكامل: العربية والإنجليزية والتركية والألمانية والإسبانية والفرنسية والصينية. الواجهة وخطط الذكاء الاصطناعي والأدلة الصوتية تتبع لغتك.",
    },
    "ja": {
        "free": "無料ダウンロード",
        "gplay": "Google Play · 近日公開",
        "pricing_lead": "Navitraのダウンロードと旅行計画は無料です。Premiumでは月額・年額プランですべての機能を使え、年額プランは7日間の無料トライアルから始まります。",
        "tiny": "無料ダウンロード · 年額プランは7日間無料 · いつでも解約",
        "free_a": "はい。ダウンロードと旅行計画は無料です。PremiumではAI音声ガイド、オフライン地図、予算管理、AIルート上限の拡大が使えます。最新の料金はApp Storeでお使いの通貨で表示され、年額プランは7日間の無料トライアルから始まります。",
        "route_q": "AIはどうやってルートを作るのですか？",
        "route_a": "Navitraのルートエンジンは旅を実際の物流問題として扱います。各スポットの営業時間を確認し、近い場所を同じ日にまとめ、歩く距離が最短になる順に並べ、各スポットに現実的な滞在時間を確保します。そのうえでAIが説明、ヒント、食事の提案を加えます。",
        "lang_q": "Navitraは何語に対応していますか？",
        "lang_a": "7言語に完全対応しています：英語、トルコ語、ドイツ語、スペイン語、フランス語、アラビア語、中国語。画面、AIプラン、音声ガイドがすべてその言語になります。",
    },
    "ko": {
        "free": "무료 다운로드",
        "gplay": "Google Play · 출시 예정",
        "pricing_lead": "Navitra 다운로드와 여행 계획은 무료입니다. Premium은 월간·연간 옵션으로 모든 기능을 열어 주며, 연간 플랜은 7일 무료 체험으로 시작합니다.",
        "tiny": "무료 다운로드 · 연간 플랜 7일 체험 · 언제든 해지",
        "free_a": "예. 다운로드와 여행 계획은 무료입니다. Premium은 AI 음성 가이드, 오프라인 지도, 예산 관리, 더 높은 AI 루트 한도를 제공합니다. 최신 가격은 App Store에서 현지 통화로 확인할 수 있으며, 연간 플랜은 7일 무료 체험으로 시작합니다.",
        "route_q": "AI는 내 루트를 어떻게 만드나요?",
        "route_a": "Navitra의 루트 엔진은 여행을 실제 물류 문제처럼 다룹니다. 장소별 영업시간을 확인하고, 가까운 곳을 같은 날로 묶고, 걷는 거리가 가장 짧도록 순서를 정하고, 각 장소에 현실적인 시간을 배정합니다. 그다음 AI가 설명, 팁, 식사 추천을 더합니다.",
        "lang_q": "Navitra는 어떤 언어를 지원하나요?",
        "lang_a": "7개 언어를 완전히 지원합니다: 영어, 터키어, 독일어, 스페인어, 프랑스어, 아랍어, 중국어. 화면, AI 계획, 음성 가이드가 모두 선택한 언어를 따릅니다.",
    },
    "ru": {
        "free": "Бесплатно",
        "gplay": "Google Play · Скоро",
        "pricing_lead": "Скачать Navitra и планировать поездки можно бесплатно. Premium открывает все возможности — помесячно или на год; годовой план начинается с 7 бесплатных дней.",
        "tiny": "Бесплатно · 7 дней пробного периода в годовом плане · Отмена в любой момент",
        "free_a": "Да. Скачивание и планирование бесплатны. Premium добавляет AI-аудиогиды, офлайн-карты, планирование бюджета и больше AI-маршрутов. Актуальную цену в вашей валюте показывает App Store; годовой план начинается с 7 бесплатных дней.",
        "route_q": "Как AI строит мой маршрут?",
        "route_a": "Маршрутный движок Navitra решает поездку как настоящую логистическую задачу: проверяет часы работы, объединяет близкие места в один день, выстраивает их так, чтобы ходить как можно меньше, и закладывает реалистичное время на каждую остановку. Затем AI добавляет описания, советы и идеи, где поесть.",
        "lang_q": "Какие языки поддерживает Navitra?",
        "lang_a": "Семь, полностью: английский, турецкий, немецкий, испанский, французский, арабский и китайский. Интерфейс, AI-планы и аудиогиды работают на вашем языке.",
    },
    "zh-hans": {
        "free": "免费下载",
        "gplay": "Google Play · 即将推出",
        "pricing_lead": "下载 Navitra 和规划旅行都是免费的。Premium 提供月度和年度方案，解锁完整体验；年度方案从 7 天免费试用开始。",
        "tiny": "免费下载 · 年度方案 7 天试用 · 随时取消",
        "free_a": "是的。下载和规划旅行都免费。Premium 增加 AI 语音导览、离线地图、预算规划和更高的 AI 路线额度。当前价格会在 App Store 以你的货币显示；年度方案从 7 天免费试用开始。",
        "route_q": "AI 如何生成我的路线？",
        "route_a": "Navitra 的路线引擎把你的旅行当作真实的物流问题来处理：核对每个地点的营业时间，把相近的地点安排在同一天，按步行最少的顺序排列，并为每一站预留合理时间。随后 AI 再补充介绍、小贴士和用餐建议。",
        "lang_q": "Navitra 支持哪些语言？",
        "lang_a": "完整支持七种语言：中文、英语、土耳其语、德语、西班牙语、法语和阿拉伯语。界面、AI 行程和语音导览都会使用你的语言。",
    },
}

_ICON = (
    '<span class="ic"><svg viewBox="0 0 12 12" fill="none" stroke="currentColor" '
    'stroke-width="1.8" aria-hidden="true"><path d="M6 1v10M1 6h10"/></svg></span>'
)


def faq_items(code: str, locale: dict, extra: dict) -> list[tuple[str, str]]:
    """Six (question, answer-html) pairs in the same order as the English page."""
    live = LIVE[code]
    faqs = locale["faqs"]
    return [
        (faqs[0][0], live["free_a"]),
        (live["route_q"], live["route_a"]),
        (faqs[1][0], faqs[1][1]),
        (live["lang_q"], live["lang_a"]),
        (extra["share_q"], extra["share_a"]),
        (extra["delete_q"], extra["delete_a"]),
    ]


def render_faq_items(items: list[tuple[str, str]], esc) -> str:
    out = []
    for q, a in items:
        out.append(
            '<div class="acc">\n'
            f'                    <button aria-expanded="false">{esc(q)}{_ICON}</button>\n'
            f'                    <div class="panel"><div><p>{a}</p></div></div>\n'
            "                </div>"
        )
    return "\n                ".join(out)


def replace_faq_block(html: str, rendered: str) -> str:
    """Swap every accordion item inside the FAQ section for the localized ones."""
    start = html.index('<section class="faq" id="faq">')
    end = html.index("</section>", start)
    section = html[start:end]
    first = section.index('<div class="acc">')
    # The accordion list ends where the column <div> and the grid <div> close.
    closing = "\n            </div>\n        </div>\n    "
    if not section.endswith(closing):
        raise ValueError("FAQ section layout changed; update replace_faq_block")
    new_section = section[:first] + rendered + closing
    return html[:start] + new_section + html[end:]


def _plain(text: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", text)).strip()


def json_ld(lang: str, page_url: str, description: str, items: list[tuple[str, str]]) -> str:
    app = {
        "@context": "https://schema.org",
        "@type": "MobileApplication",
        "name": "Navitra",
        "url": page_url,
        "inLanguage": lang,
        "downloadUrl": STORE_URL,
        "installUrl": STORE_URL,
        "operatingSystem": "iOS",
        "applicationCategory": "TravelApplication",
        "description": description,
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        "creator": {
            "@type": "Organization",
            "name": "Navitra",
            "url": "https://navitraapp.com/",
            "sameAs": SAME_AS,
        },
    }
    faq = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "inLanguage": lang,
        "mainEntity": [
            {
                "@type": "Question",
                "name": _plain(q),
                "acceptedAnswer": {"@type": "Answer", "text": _plain(a)},
            }
            for q, a in items
        ],
    }
    dump = lambda obj: json.dumps(obj, ensure_ascii=False, indent=4).replace("</", "<\\/")
    return (
        f'<script type="application/ld+json">\n{dump(app)}\n    </script>\n'
        f'    <script type="application/ld+json">\n{dump(faq)}\n    </script>'
    )


def replace_json_ld(html: str, block: str) -> str:
    pattern = re.compile(r'<script type="application/ld\+json">.*?</script>(\s*<script type="application/ld\+json">.*?</script>)?', re.S)
    return pattern.sub(lambda _m: block, html, count=1)


def english_faq_items(html: str) -> list[tuple[str, str]]:
    start = html.index('<section class="faq" id="faq">')
    end = html.index("</section>", start)
    section = html[start:end]
    return re.findall(
        r'<button aria-expanded="false">(.*?)<span class="ic">.*?<div class="panel"><div><p>(.*?)</p></div></div>',
        section,
        re.S,
    )


# ---------------------------------------------------------------------------
# Visible English leftovers in the localized pages (swipe demo cards and two
# call-to-action paragraphs). Keys are the English source strings.
# card: (country, name, line) for Colosseum, Trevi, Pantheon, Vatican, Trastevere
# ---------------------------------------------------------------------------

CARDS_EN = [
    ("the Colosseum", "Ancient Rome", "The Colosseum", "The arena that defined an empire."),
    ("the Trevi Fountain", "Baroque Rome", "The Trevi Fountain", "Toss a coin, make a wish, come back."),
    ("the Pantheon", "Ancient Rome", "The Pantheon", "A 2,000-year-old dome, still perfect."),
    ("the Vatican Museums", "Vatican City", "The Vatican Museums", "Michelangelo's ceiling, room after room."),
    ("Trastevere", "Neighborhood", "Trastevere", "Cobbled lanes, trattorias, golden light."),
]

DONE_EN = "In the app, Navitra turns your picks into a day-by-day route that respects opening hours, distances and your pace."
CTA_EN = "Navitra is now available on iPhone. Android is coming soon. Premium unlocks voice guides, offline maps and higher route limits, with a 7-day free trial on the yearly plan."
FINAL_EN = 'Navitra is now available on iPhone. Android is coming soon — turn your next "someday" into a day-by-day plan.'

LEFTOVERS = {
    "tr": {
        "cards": [
            ("Antik Roma", "Kolezyum", "Bir imparatorluğu tanımlayan arena."),
            ("Barok Roma", "Trevi Çeşmesi", "Bir bozuk para at, dilek tut, geri gel."),
            ("Antik Roma", "Pantheon", "2.000 yıllık kubbe, hâlâ kusursuz."),
            ("Vatikan", "Vatikan Müzeleri", "Salon salon Michelangelo'nun tavanı."),
            ("Mahalle", "Trastevere", "Arnavut kaldırımı, trattoriler, altın ışık."),
        ],
        "done": "Uygulamada Navitra seçtiklerini açılış saatlerine, mesafelere ve temposuna uyan günlük bir rotaya dönüştürür.",
        "cta": "Navitra artık iPhone'da. Android yakında. Premium; sesli rehber, offline harita ve daha yüksek rota limitlerini açar, yıllık planda 7 gün ücretsiz deneme var.",
        "final": "Navitra artık iPhone'da, Android yakında. Bir gün gideceğin yeri bugünden günlük bir plana dönüştür.",
    },
    "de": {
        "cards": [
            ("Antikes Rom", "Kolosseum", "Die Arena, die ein Weltreich prägte."),
            ("Barockes Rom", "Trevi-Brunnen", "Münze werfen, etwas wünschen, wiederkommen."),
            ("Antikes Rom", "Pantheon", "Eine 2.000 Jahre alte Kuppel, noch immer perfekt."),
            ("Vatikanstadt", "Vatikanische Museen", "Michelangelos Decke, Saal für Saal."),
            ("Viertel", "Trastevere", "Kopfsteinpflaster, Trattorien, goldenes Licht."),
        ],
        "done": "In der App macht Navitra aus deiner Auswahl eine Tagesroute, die Öffnungszeiten, Wege und dein Tempo berücksichtigt.",
        "cta": "Navitra ist jetzt fürs iPhone verfügbar, Android folgt bald. Premium schaltet Sprachguides, Offline-Karten und höhere Routenlimits frei, mit 7 Tagen Gratis-Test im Jahresplan.",
        "final": "Navitra ist jetzt fürs iPhone verfügbar, Android folgt bald. Mach aus deinem nächsten „irgendwann“ einen Plan für jeden Tag.",
    },
    "es": {
        "cards": [
            ("Roma antigua", "El Coliseo", "La arena que definió un imperio."),
            ("Roma barroca", "La Fontana di Trevi", "Lanza una moneda, pide un deseo, vuelve."),
            ("Roma antigua", "El Panteón", "Una cúpula de 2.000 años, aún perfecta."),
            ("Ciudad del Vaticano", "Museos Vaticanos", "El techo de Miguel Ángel, sala tras sala."),
            ("Barrio", "Trastevere", "Calles empedradas, trattorias, luz dorada."),
        ],
        "done": "En la app, Navitra convierte tus elecciones en una ruta día a día que respeta horarios, distancias y tu ritmo.",
        "cta": "Navitra ya está disponible en iPhone. Android llegará pronto. Premium desbloquea guías de voz, mapas offline y más rutas, con 7 días de prueba gratis en el plan anual.",
        "final": "Navitra ya está disponible en iPhone y pronto en Android. Convierte tu próximo «algún día» en un plan día a día.",
    },
    "fr": {
        "cards": [
            ("Rome antique", "Le Colisée", "L’arène qui a défini un empire."),
            ("Rome baroque", "La fontaine de Trevi", "Lancez une pièce, faites un vœu, revenez."),
            ("Rome antique", "Le Panthéon", "Une coupole de 2 000 ans, toujours parfaite."),
            ("Cité du Vatican", "Les musées du Vatican", "Le plafond de Michel-Ange, salle après salle."),
            ("Quartier", "Trastevere", "Ruelles pavées, trattorias, lumière dorée."),
        ],
        "done": "Dans l’app, Navitra transforme vos choix en itinéraire jour par jour qui respecte horaires, distances et votre rythme.",
        "cta": "Navitra est disponible sur iPhone, Android arrive bientôt. Premium débloque les guides vocaux, les cartes hors ligne et plus d’itinéraires, avec 7 jours d’essai gratuit sur l’offre annuelle.",
        "final": "Navitra est disponible sur iPhone, Android arrive bientôt. Transformez votre prochain « un jour » en plan jour par jour.",
    },
    "it": {
        "cards": [
            ("Roma antica", "Il Colosseo", "L’arena che ha definito un impero."),
            ("Roma barocca", "Fontana di Trevi", "Lancia una moneta, esprimi un desiderio, torna."),
            ("Roma antica", "Il Pantheon", "Una cupola di 2.000 anni, ancora perfetta."),
            ("Città del Vaticano", "Musei Vaticani", "Il soffitto di Michelangelo, sala dopo sala."),
            ("Quartiere", "Trastevere", "Vicoli acciottolati, trattorie, luce dorata."),
        ],
        "done": "Nell’app, Navitra trasforma le tue scelte in un itinerario giorno per giorno che rispetta orari, distanze e il tuo ritmo.",
        "cta": "Navitra è disponibile su iPhone, Android arriverà presto. Premium sblocca guide vocali, mappe offline e più itinerari, con 7 giorni di prova gratuita sul piano annuale.",
        "final": "Navitra è disponibile su iPhone, presto su Android. Trasforma il tuo prossimo «prima o poi» in un piano giorno per giorno.",
    },
    "nl": {
        "cards": [
            ("Het oude Rome", "Het Colosseum", "De arena die een rijk bepaalde."),
            ("Barok Rome", "De Trevifontein", "Gooi een munt, doe een wens, kom terug."),
            ("Het oude Rome", "Het Pantheon", "Een koepel van 2.000 jaar, nog steeds perfect."),
            ("Vaticaanstad", "Vaticaanse Musea", "Michelangelo’s plafond, zaal na zaal."),
            ("Wijk", "Trastevere", "Keienstraatjes, trattoria’s, gouden licht."),
        ],
        "done": "In de app maakt Navitra van je keuzes een dagroute die rekening houdt met openingstijden, afstanden en jouw tempo.",
        "cta": "Navitra is nu beschikbaar op iPhone, Android volgt binnenkort. Premium ontgrendelt audiogidsen, offline kaarten en meer routes, met 7 dagen gratis proberen bij het jaarplan.",
        "final": "Navitra is nu beschikbaar op iPhone, Android volgt binnenkort. Maak van je volgende ‘ooit’ een plan per dag.",
    },
    "pt-br": {
        "cards": [
            ("Roma antiga", "O Coliseu", "A arena que definiu um império."),
            ("Roma barroca", "A Fontana di Trevi", "Jogue uma moeda, faça um pedido, volte."),
            ("Roma antiga", "O Panteão", "Uma cúpula de 2.000 anos, ainda perfeita."),
            ("Cidade do Vaticano", "Museus do Vaticano", "O teto de Michelangelo, sala após sala."),
            ("Bairro", "Trastevere", "Ruas de pedra, trattorias, luz dourada."),
        ],
        "done": "No app, a Navitra transforma suas escolhas em uma rota dia a dia que respeita horários, distâncias e o seu ritmo.",
        "cta": "A Navitra já está disponível no iPhone. Android em breve. O Premium libera guias de voz, mapas offline e mais rotas, com 7 dias de teste grátis no plano anual.",
        "final": "A Navitra já está no iPhone e em breve no Android. Transforme o seu próximo “um dia” em um plano dia a dia.",
    },
    "ar": {
        "cards": [
            ("روما القديمة", "الكولوسيوم", "الساحة التي صنعت إمبراطورية."),
            ("روما الباروكية", "نافورة تريفي", "ارمِ عملة، تمنَّ أمنية، وعُد."),
            ("روما القديمة", "البانثيون", "قبة عمرها 2000 عام وما زالت مثالية."),
            ("مدينة الفاتيكان", "متاحف الفاتيكان", "سقف مايكل أنجلو، قاعة بعد قاعة."),
            ("حيّ", "تراستيفيري", "أزقة مرصوفة ومطاعم صغيرة وضوء ذهبي."),
        ],
        "done": "في التطبيق، يحوّل Navitra اختياراتك إلى مسار يومي يراعي مواعيد الافتتاح والمسافات وإيقاعك.",
        "cta": "Navitra متاح الآن على iPhone، وقريبًا على Android. يفتح Premium الأدلة الصوتية والخرائط بلا إنترنت وحدودًا أعلى للمسارات، مع تجربة مجانية لمدة 7 أيام في الخطة السنوية.",
        "final": "Navitra متاح الآن على iPhone وقريبًا على Android. حوّل «يومًا ما» القادم إلى خطة يومًا بيوم.",
    },
    "ja": {
        "cards": [
            ("古代ローマ", "コロッセオ", "帝国を象徴した円形闘技場。"),
            ("バロックのローマ", "トレヴィの泉", "コインを投げて願えば、また戻ってこられる。"),
            ("古代ローマ", "パンテオン", "2000年前のドームが今も完璧なまま。"),
            ("バチカン市国", "バチカン美術館", "部屋ごとに続くミケランジェロの天井画。"),
            ("街並み", "トラステヴェレ", "石畳、トラットリア、黄金色の光。"),
        ],
        "done": "アプリでは、選んだ場所をNavitraが営業時間、距離、あなたのペースに合わせた日別ルートにします。",
        "cta": "NavitraはiPhoneで利用できます。Androidは近日公開。Premiumでは音声ガイド、オフライン地図、ルート上限の拡大が使え、年額プランは7日間無料で試せます。",
        "final": "NavitraはiPhoneで利用でき、Androidも近日公開。いつか行きたい場所を、日ごとのプランに。",
    },
    "ko": {
        "cards": [
            ("고대 로마", "콜로세움", "제국을 상징한 원형 경기장."),
            ("바로크 로마", "트레비 분수", "동전을 던지고 소원을 빌면 다시 오게 돼요."),
            ("고대 로마", "판테온", "2,000년 된 돔, 여전히 완벽해요."),
            ("바티칸 시국", "바티칸 박물관", "방마다 이어지는 미켈란젤로의 천장화."),
            ("동네", "트라스테베레", "자갈길, 트라토리아, 황금빛 햇살."),
        ],
        "done": "앱에서 Navitra는 고른 장소를 영업시간, 거리, 여행 속도에 맞춘 일별 루트로 만들어 줍니다.",
        "cta": "Navitra는 지금 iPhone에서 사용할 수 있고 Android는 곧 출시됩니다. Premium은 음성 가이드, 오프라인 지도, 더 많은 루트를 제공하며 연간 플랜은 7일 무료 체험으로 시작합니다.",
        "final": "Navitra는 지금 iPhone에서, 곧 Android에서도 만날 수 있어요. 언젠가의 여행을 일별 계획으로 바꿔 보세요.",
    },
    "ru": {
        "cards": [
            ("Древний Рим", "Колизей", "Арена, ставшая символом империи."),
            ("Барочный Рим", "Фонтан Треви", "Бросьте монету, загадайте желание, вернитесь."),
            ("Древний Рим", "Пантеон", "Куполу 2000 лет, и он всё так же совершенен."),
            ("Ватикан", "Музеи Ватикана", "Потолок Микеланджело, зал за залом."),
            ("Район", "Трастевере", "Брусчатка, траттории, золотой свет."),
        ],
        "done": "В приложении Navitra превращает ваш выбор в маршрут по дням с учётом часов работы, расстояний и вашего темпа.",
        "cta": "Navitra уже доступна на iPhone, Android скоро. Premium открывает аудиогиды, офлайн-карты и больше маршрутов, а годовой план начинается с 7 бесплатных дней.",
        "final": "Navitra уже на iPhone и скоро на Android. Превратите своё «когда-нибудь» в план по дням.",
    },
    "zh-hans": {
        "cards": [
            ("古罗马", "罗马斗兽场", "定义一个帝国的竞技场。"),
            ("巴洛克罗马", "特雷维喷泉", "投一枚硬币，许个愿，还会再来。"),
            ("古罗马", "万神殿", "两千年的穹顶，依旧完美。"),
            ("梵蒂冈", "梵蒂冈博物馆", "米开朗基罗的天顶画，一厅接一厅。"),
            ("街区", "特拉斯提弗列", "石板小巷、小餐馆和金色的光。"),
        ],
        "done": "在应用里，Navitra 会把你选中的地方变成兼顾营业时间、距离和你节奏的每日路线。",
        "cta": "Navitra 现已登陆 iPhone，Android 版即将推出。Premium 解锁语音导览、离线地图和更多路线，年度方案可免费试用 7 天。",
        "final": "Navitra 现已登陆 iPhone，Android 版即将推出。把下一个“总有一天”变成每日计划。",
    },
}

# The app speaks 7 languages; these site locales are not among them.
APP_LANG_NOTICE = {
    "it": "L’app Navitra è disponibile in inglese, turco, tedesco, spagnolo, francese, arabo e cinese. L’italiano non è ancora tra le lingue dell’app.",
    "nl": "De Navitra-app is beschikbaar in het Engels, Turks, Duits, Spaans, Frans, Arabisch en Chinees. Nederlands wordt in de app nog niet ondersteund.",
    "pt-br": "O app Navitra está disponível em inglês, turco, alemão, espanhol, francês, árabe e chinês. O português ainda não está entre os idiomas do app.",
    "ja": "Navitraアプリは英語、トルコ語、ドイツ語、スペイン語、フランス語、アラビア語、中国語に対応しています。日本語にはまだ対応していません。",
    "ko": "Navitra 앱은 영어, 터키어, 독일어, 스페인어, 프랑스어, 아랍어, 중국어를 지원합니다. 한국어는 아직 앱에서 지원하지 않습니다.",
    "ru": "Приложение Navitra доступно на английском, турецком, немецком, испанском, французском, арабском и китайском. Русский язык в приложении пока не поддерживается.",
}


def fix_leftovers(code: str, html: str, esc) -> str:
    data = LEFTOVERS[code]
    for (data_name, country, name, line), (l_country, l_name, l_line) in zip(CARDS_EN, data["cards"]):
        html = html.replace(f'data-name="{data_name}"', f'data-name="{esc(l_name)}"', 1)
        html = html.replace(
            f'<span class="sd-country">{country}</span><h3>{name}</h3><p>{line}</p>',
            f'<span class="sd-country">{esc(l_country)}</span><h3>{esc(l_name)}</h3><p>{esc(l_line)}</p>',
            1,
        )
    html = html.replace(f"<p>{DONE_EN}</p>", f"<p>{esc(data['done'])}</p>", 1)
    html = html.replace(f'<p class="lede">{CTA_EN}</p>', f'<p class="lede">{esc(data["cta"])}</p>', 1)
    html = html.replace(f'<p class="reveal">{FINAL_EN}</p>', f'<p class="reveal">{esc(data["final"])}</p>', 1)
    return html


NOTICE_CSS = (
    "<style>.app-lang-note{margin-top:16px;max-width:46ch;font-size:12.5px;line-height:1.5;"
    "color:rgba(250,250,247,.82)}</style>"
)


def add_app_lang_notice(code: str, html: str, esc) -> str:
    """Small note under the hero buttons on locales the app itself does not speak."""
    note = APP_LANG_NOTICE.get(code)
    if not note:
        return html
    hero = html.index('<header class="hero">')
    ctas = html.index('<div class="hero-ctas', hero)
    close = html.index("</div>", ctas) + len("</div>")
    html = html[:close] + f'\n                <p class="app-lang-note" role="note">{esc(note)}</p>' + html[close:]
    return html.replace("</head>", NOTICE_CSS + "\n</head>", 1)


# ---------------------------------------------------------------------------
# Turkish homepage extras: "Rehberler" nav link, an app demo inside
# "Nasıl çalışır", and a Christmas-route band (social proof + guide links).
# Turkish only: the videos and the guides are in Turkish.
# ---------------------------------------------------------------------------

IG_VIENNA_REEL = "https://www.instagram.com/reel/DgDPOmtjneF/"

TR_EXTRA_CSS = """<style>
.how .step:nth-last-of-type(2){border-bottom:1px solid var(--line-light)}
.how-demo{max-width:1280px;margin:clamp(56px,7vw,96px) auto 0;display:grid;grid-template-columns:1fr auto;gap:clamp(32px,6vw,96px);align-items:center}
.how-demo .label{display:block;margin-bottom:16px}
.how-demo h3{font-family:var(--serif);font-weight:400;font-size:clamp(1.9rem,3.4vw,3rem);letter-spacing:-.015em;color:var(--cream);margin-bottom:14px}
.how-demo p{color:var(--mut-light);max-width:46ch;font-size:15px}
.phone{position:relative;width:clamp(220px,24vw,290px);aspect-ratio:9/16;border-radius:34px;overflow:hidden;background:#0b0b14;border:1px solid rgba(250,250,247,.14);box-shadow:0 30px 80px rgba(0,0,0,.45),0 0 0 8px rgba(250,250,247,.04)}
.phone video,.phone img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block}
.routes-band{padding:var(--sec-y) var(--pad-x);background:var(--cream-warm)}
.routes-inner{max-width:1280px;margin:0 auto;display:grid;grid-template-columns:auto 1fr;gap:clamp(40px,6vw,96px);align-items:center}
.routes-proof{display:grid;justify-items:center;gap:18px}
.routes-proof .phone{border-color:var(--line);box-shadow:0 30px 70px rgba(18,18,31,.18)}
.routes-proof{margin:0}
.reel .reel-top{position:absolute;left:0;right:0;top:0;display:flex;align-items:center;gap:9px;padding:16px 16px 28px;color:#fff;font:600 13px var(--sans);background:linear-gradient(rgba(0,0,0,.45),transparent)}
.reel .reel-top img{position:static;width:28px;height:28px;border-radius:50%;border:1.5px solid rgba(255,255,255,.85);object-fit:cover}
.reel .reel-top svg{width:20px;height:20px;margin-left:auto;opacity:.95}
.reel .reel-plays{position:absolute;left:14px;bottom:14px;display:flex;align-items:center;gap:5px;color:#fff;font:600 14px var(--sans);text-shadow:0 1px 6px rgba(0,0,0,.55)}
.reel .reel-plays svg{width:15px;height:15px;filter:drop-shadow(0 1px 4px rgba(0,0,0,.5))}
.reel-stats{display:grid;grid-template-columns:repeat(3,auto);gap:clamp(18px,2.4vw,30px);margin:6px 0 0;padding:0}
.reel-stats div{display:grid;justify-items:center;gap:2px}
.reel-stats strong{font-family:var(--serif);font-weight:400;font-size:clamp(1.6rem,2.4vw,2.1rem);line-height:1;color:var(--ink)}
.reel-stats span{font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--mut)}
.reel-link{font-size:13px;font-weight:600;color:var(--ink);text-decoration:none;border-bottom:1px solid var(--line);padding-bottom:2px}
.reel-link:hover{color:var(--sunset);border-color:var(--sunset)}
.routes-copy .label{display:block;margin-bottom:18px}
.routes-copy .sec-head{margin-bottom:18px}
.routes-copy .lede{color:var(--mut);max-width:52ch;margin-bottom:28px}
.route-links{list-style:none;margin:0 0 30px;padding:0;border-top:1px solid var(--line)}
.route-links a{display:flex;justify-content:space-between;align-items:baseline;gap:20px;padding:18px 0;border-bottom:1px solid var(--line);text-decoration:none;color:var(--ink)}
.route-links .city{font-family:var(--serif);font-size:clamp(1.5rem,2.4vw,2rem)}
.route-links .meta{font-size:13px;color:var(--mut);text-align:right}
.route-links a:hover .city{color:var(--sunset)}
@media (max-width:880px){.how-demo,.routes-inner{grid-template-columns:1fr}.how-demo .phone{justify-self:center}.routes-proof{order:2}}
</style>"""

TR_HOW_DEMO = """
        <div class="how-demo reveal">
            <div>
                <span class="label">Uygulamada</span>
                <h3>Prag'da 3 gün, tek rotada.</h3>
                <p>Yerleri seçersin; Navitra mesafeleri, açılış saatlerini ve yürüme süresini hesaba katıp günlere böler.</p>
            </div>
            <div class="phone">
                <video data-autoplay muted loop playsinline preload="none" poster="/img/video/demo-prag.jpg" aria-label="Navitra ile Prag'da 3 günlük rota oluşturma">
                    <source src="/img/video/demo-prag.mp4" type="video/mp4">
                </video>
            </div>
        </div>
"""

TR_ROUTES_BAND = f"""
    <!-- ───────────── NOEL PAZARI ROTALARI ───────────── -->
    <section class="routes-band" id="rehberler">
        <div class="routes-inner">
            <figure class="routes-proof reveal">
                <div class="phone reel">
                    <video data-autoplay muted loop playsinline preload="none" poster="/img/video/viyana-reel.jpg" aria-label="Viyana'da 4 Noel pazarı rotası animasyonu">
                        <source src="/img/video/viyana-reel.mp4" type="video/mp4">
                    </video>
                    <div class="reel-top" aria-hidden="true">
                        <img src="/apple-touch-icon.png" alt="" width="28" height="28">
                        <span>navitra.travel</span>
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="3" width="18" height="18" rx="5"/><path d="M3 8.5h18M8.5 3l3 5.5M14 3l3 5.5"/><path d="M10 12.5v4.5l4-2.25z" fill="currentColor" stroke="none"/></svg>
                    </div>
                    <div class="reel-plays" aria-hidden="true">
                        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M7 4.5v15l12.5-7.5z"/></svg>20 B
                    </div>
                </div>
                <figcaption class="reel-stats">
                    <div><strong>20 B+</strong><span>izlenme</span></div>
                    <div><strong>600+</strong><span>paylaşım</span></div>
                    <div><strong>600+</strong><span>kaydetme</span></div>
                </figcaption>
                <a class="reel-link" href="{IG_VIENNA_REEL}" target="_blank" rel="noopener">Instagram'da izle <span aria-hidden="true">→</span></a>
            </figure>
            <div class="routes-copy reveal">
                <span class="label">Noel Pazarı Rotası</span>
                <h2 class="sec-head">Avrupa'nın Noel pazarları, <em>tek akşamda.</em></h2>
                <p class="lede">Şehir şehir tarihler, açılış saatleri ve yürüyüş rotaları. Bilgiler resmî kaynaklardan kontrol edilir, sezon boyunca güncellenir.</p>
                <ul class="route-links">
                    <li><a href="/tr/rehber/viyana-noel-pazarlari/"><span class="city">Viyana</span><span class="meta">4 pazar · ~1,5 km</span></a></li>
                    <li><a href="/tr/rehber/dresden-noel-pazarlari/"><span class="city">Dresden</span><span class="meta">Striezelmarkt + 3 pazar</span></a></li>
                    <li><a href="/tr/rehber/prag-noel-pazarlari/"><span class="city">Prag</span><span class="meta">28 Kasım'da açılıyor</span></a></li>
                </ul>
                <a href="/tr/rehber/" class="pill pill-ink">Tüm rehberler</a>
            </div>
        </div>
    </section>
"""

TR_VIDEO_SCRIPT = """<script>
(function(){
  var vids=document.querySelectorAll('video[data-autoplay]');
  if(!vids.length) return;
  var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if(reduce||!('IntersectionObserver' in window)){vids.forEach(function(v){v.setAttribute('controls','');});return;}
  var io=new IntersectionObserver(function(entries){entries.forEach(function(e){var v=e.target;
    if(e.isIntersecting){if(v.preload==='none'){v.preload='auto';v.load();}var p=v.play();if(p&&p.catch)p.catch(function(){});}
    else{v.pause();}});},{threshold:0.35});
  vids.forEach(function(v){io.observe(v);});
})();
</script>"""


def add_tr_extras(html: str) -> str:
    # Nav and mobile menu: "Rehberler" before "Destek".
    html = html.replace(
        '<a href="#collaborate">Bizimle çalışın</a>\n            <a href="/support.html">Destek</a>',
        '<a href="#collaborate">Bizimle çalışın</a>\n            <a href="/tr/rehber/">Rehberler</a>\n            <a href="/support.html">Destek</a>',
        1,
    )
    html = html.replace(
        '<a href="#collaborate">Bizimle çalışın</a>\n        <a href="/support.html">Destek</a>',
        '<a href="#collaborate">Bizimle çalışın</a>\n        <a href="/tr/rehber/">Rehberler</a>\n        <a href="/support.html">Destek</a>',
        1,
    )
    # Demo phone at the end of "Nasıl çalışır".
    start = html.index('<section class="how" id="how">')
    end = html.index("</section>", start)
    html = html[:end] + TR_HOW_DEMO + "    " + html[end:]
    # Routes band right before the FAQ.
    faq_section = html.index('<section class="faq" id="faq">')
    faq = html.rindex("    <!--", 0, faq_section)
    html = html[:faq] + TR_ROUTES_BAND + "\n" + html[faq:]
    html = html.replace("</head>", TR_EXTRA_CSS + "\n</head>", 1)
    html = html.replace("</body>", TR_VIDEO_SCRIPT + "\n</body>", 1)
    return html
