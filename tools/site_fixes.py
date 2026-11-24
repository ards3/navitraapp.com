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
