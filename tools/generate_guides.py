"""Turkish city guides under /tr/rehber/ (Christmas market routes).

Static pages, generated from the data below so that the copy, the visible FAQ
and the JSON-LD never drift apart. Every date and opening hour must come from a
source listed in the guide's `sources`; re-check them each season.

Run:  python3 tools/generate_guides.py
"""

from __future__ import annotations

import json
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://navitraapp.com"
STORE = "https://apps.apple.com/us/app/navitra-ai-travel-planner/id6779956173"
CHECKED = "2026-11-24"
CHECKED_TR = "24 Kasım 2026"

GUIDES = [
    {
        "slug": "viyana-noel-pazarlari",
        "city": "Viyana",
        "title": "Viyana Noel Pazarları 2026: 4 pazar, tek akşamda yürüyüş rotası",
        "description": "Viyana'nın 4 Noel pazarı (Rathausplatz, Freyung, Am Hof, Stephansplatz) için 2026 tarihleri, açılış saatleri ve yaklaşık 1,5 km'lik tek akşamlık yürüyüş rotası.",
        "h1": "Viyana'da 4 Noel pazarı, tek akşamda",
        "answer": "Viyana'nın merkezindeki dört Noel pazarı (Rathausplatz, Freyung, Am Hof ve Stephansplatz) yaklaşık 1,5 km'lik bir yürüyüşle tek akşamda gezilebilir. Stephansplatz ve Am Hof 21:00'de, Rathausplatz 22:00'de kapandığı için akşam başlıyorsan rotayı Stephansplatz'tan başlatıp Rathausplatz'ta bitir.",
        "markets": [
            ("Stephansplatz (Weihnachtsdorf)", "6 Kasım – 26 Aralık", "Her gün 11:00–21:00", "Katedralin dibinde, küçük ve kalabalık. Rotanın en erken kapanan durağı."),
            ("Am Hof", "13 Kasım – 23 Aralık", "Pzt–Per 11:00–21:00, Cum–Paz 10:00–21:00", "Stephansplatz'tan birkaç dakikalık yürüme. El işi ve sakin bir meydan."),
            ("Freyung (Altwiener Christkindlmarkt)", "14 Kasım – 23 Aralık", "Her gün 10:00–21:00", "Am Hof'un hemen yanında, geleneksel el sanatları."),
            ("Rathausplatz (Wiener Christkindlmarkt)", "13 Kasım – 26 Aralık", "Her gün 10:00–22:00", "En büyüğü: belediye binasının önünde yaklaşık 100 stant. Rotanın son ve en geç kapanan durağı."),
        ],
        "route": [
            "Stephansplatz'tan başla; katedrali gördükten sonra Graben üzerinden kuzeybatıya yürü.",
            "Am Hof'a birkaç dakikada varırsın. Freyung hemen bitişiğinde.",
            "Freyung'dan Schottentor yönüne, oradan Rathausplatz'a geç.",
            "Rathausplatz 22:00'ye kadar açık; akşam yemeğini ve son içeceği burada bitir.",
        ],
        "route_note": "Toplam yürüme yaklaşık 1,5 km. Sabah ya da öğleden sonra başlıyorsan sıra fark etmez; Rathausplatz'tan Stephansplatz'a doğru da yürüyebilirsin.",
        "tips": [
            "Sıcak içecekler depozitolu kupada gelir; depozito genelde 3–5 €. Kupayı aynı pazardaki bir içecek standına geri verirsen paran iade edilir.",
            "Hafta sonu akşamları en kalabalık saatler. Rathausplatz'ı rahat gezmek için hafta içi ya da öğleden önceyi seç.",
            "23 Aralık'tan sonra Am Hof ve Freyung kapanıyor; Noel haftasında gidiyorsan rotan Rathausplatz ve Stephansplatz'a iner.",
        ],
        "faq": [
            ("Viyana Noel pazarları 2026'da ne zaman açılıyor?", "Stephansplatz 6 Kasım'da, Rathausplatz ve Am Hof 13 Kasım'da, Freyung 14 Kasım'da açılıyor. Am Hof ve Freyung 23 Aralık'ta, Rathausplatz ve Stephansplatz 26 Aralık'ta kapanıyor."),
            ("Viyana'daki Noel pazarları kaçta kapanıyor?", "Rathausplatz her gün 22:00'de, Stephansplatz, Am Hof ve Freyung 21:00'de kapanıyor."),
            ("Viyana'daki 4 Noel pazarı tek akşamda gezilir mi?", "Evet. Dördü de şehir merkezinde ve aralarındaki toplam yürüme yaklaşık 1,5 km. En erken kapanan Stephansplatz'tan başlayıp en geç kapanan Rathausplatz'ta bitirmek en rahat sıra."),
            ("Kupa depozitosu ne kadar?", "Genelde 3–5 €. Kupayı aynı pazardaki bir içecek standına iade edersen depozito geri verilir; istersen hatıra olarak saklayabilirsin."),
        ],
        "sources": [
            ("wien.info (Viyana turizm ofisi)", "https://www.wien.info/"),
        ],
    },
    {
        "slug": "dresden-noel-pazarlari",
        "city": "Dresden",
        "title": "Dresden Noel Pazarları 2026: Striezelmarkt ve 3 pazar, tek akşam rotası",
        "description": "Dresden'in Striezelmarkt, Stallhof Orta Çağ pazarı, Frauenkirche ve Augustusmarkt Noel pazarları için 2026 tarihleri, saatleri ve tek akşamlık yürüyüş rotası.",
        "h1": "Dresden'de 4 Noel pazarı, tek akşamda",
        "answer": "Dresden'in Noel pazarları 25 Kasım 2026'da açılıyor. Almanya'nın en eski Noel pazarı Striezelmarkt, Frauenkirche önündeki pazar ve Stallhof'taki Orta Çağ pazarı eski şehirde birbirine yürüme mesafesinde; nehrin karşısındaki Augustusmarkt'la birlikte dördü tek akşamda gezilebilir.",
        "markets": [
            ("Striezelmarkt (Altmarkt)", "25 Kasım – 24 Aralık", "Her gün 10:00–21:00 (24 Aralık 14:00'e kadar)", "1434'ten beri kurulan, Almanya'nın en eski Noel pazarı. Giriş ücretsiz."),
            ("Stallhof Orta Çağ pazarı", "25 Kasım'dan itibaren", "11:00–21:30", "Saray avlusunda Orta Çağ temalı pazar. Giriş güne ve saate göre ücretli olabilir."),
            ("Frauenkirche önü (Neumarkt / Münzgasse)", "25 Kasım – 24 Aralık", "Pzt–Per ve Paz 10:00–21:00, Cum–Cmt 10:00–22:00", "Frauenkirche'nin önünde, eski şehrin en fotojenik pazarı. Giriş ücretsiz."),
            ("Augustusmarkt (Neustadt, Hauptstraße)", "25 Kasım – Ocak başı", "Pzt–Per 11:00–21:00, Cum 11:00–22:00, Cmt 10:00–22:00, Paz 10:00–21:00", "Nehrin karşısında, uluslararası yiyecekler ve dönme dolap. 24–26 Aralık ve 1 Ocak'ta kapalı."),
        ],
        "route": [
            "Altmarkt'taki Striezelmarkt'tan başla; en erken kapanan durak bu (21:00).",
            "Kuzeye yürüyerek Neumarkt'a, Frauenkirche önündeki pazara geç.",
            "Oradan saraya doğru Stallhof'a yürü; pazar 21:30'a kadar açık.",
            "Augustusbrücke'den Elbe'yi geçip Altın Atlı heykelinden başlayan Augustusmarkt'ta bitir; cuma ve cumartesi 22:00'ye kadar açık.",
        ],
        "route_note": "Toplam yürüme yaklaşık 1,5–2 km. Köprü manzarası için Augustusbrücke'yi hava kararmadan geçmeye çalış.",
        "tips": [
            "Stallhof'a giriş güne ve saate göre ücretli olabiliyor; gitmeden pazarın sitesinden kontrol et.",
            "Striezelmarkt 24 Aralık'ta 14:00'te kapanıyor, Noel'den sonra yalnızca Augustusmarkt ve Stallhof'un Noel sonrası etkinliği açık kalıyor.",
            "Sıcak içecekler depozitolu kupayla satılır; kupayı iade edersen depozito geri verilir.",
        ],
        "faq": [
            ("Dresden Noel pazarları 2026'da ne zaman açılıyor?", "Striezelmarkt, Frauenkirche önündeki pazar, Stallhof ve Augustusmarkt 25 Kasım 2026'da açılıyor. Striezelmarkt ve Frauenkirche pazarı 24 Aralık'ta kapanıyor; Augustusmarkt Ocak başına kadar sürüyor."),
            ("Striezelmarkt kaçta açılıp kapanıyor?", "Her gün 10:00–21:00 arası açık; 24 Aralık'ta 14:00'te kapanıyor. Giriş ücretsiz."),
            ("Stallhof Orta Çağ pazarına giriş ücretli mi?", "Giriş, güne ve saate göre ücretli olabiliyor. Diğer üç pazar ücretsiz. Güncel fiyatı pazarın kendi sitesinden kontrol et."),
            ("Dresden'deki Noel pazarları tek akşamda gezilir mi?", "Evet. Striezelmarkt, Frauenkirche pazarı ve Stallhof eski şehirde birkaç dakika arayla; Augustusmarkt köprünün hemen karşısında. Toplam yürüme yaklaşık 1,5–2 km."),
        ],
        "sources": [
            ("Striezelmarkt (Dresden belediyesi)", "https://striezelmarkt.dresden.de/en/"),
            ("Dresden belediyesi – diğer Noel pazarları", "https://www.dresden.de/de/tourismus/sehen/weihnachtszeit/weitere-weihnachtsmaerkte.php"),
            ("Mittelalter-Weihnacht im Stallhof", "https://www.mittelalter-weihnacht.de/"),
        ],
    },
    {
        "slug": "prag-noel-pazarlari",
        "city": "Prag",
        "title": "Prag Noel Pazarları 2026: tarihler, saatler ve yürüyüş rotası",
        "description": "Prag'ın Eski Şehir Meydanı ve Venceslas Meydanı Noel pazarları 28 Kasım 2026 – 6 Ocak 2027 arası her gün 10:00–22:00 açık. Tarihler, rota ve para ipuçları.",
        "h1": "Prag Noel pazarları: 28 Kasım'da açılıyor",
        "answer": "Prag'ın iki ana Noel pazarı, Eski Şehir Meydanı (Staroměstské náměstí) ve Venceslas Meydanı (Václavské náměstí), 28 Kasım 2026 – 6 Ocak 2027 arası her gün 10:00–22:00 açık. İki meydan yaklaşık 10 dakikalık yürüme mesafesinde; dev Noel ağacı açılış akşamı yakılıyor.",
        "markets": [
            ("Eski Şehir Meydanı (Staroměstské náměstí)", "28 Kasım 2026 – 6 Ocak 2027", "Her gün 10:00–22:00", "Dev Noel ağacı ve astronomik saatin önündeki ana pazar."),
            ("Venceslas Meydanı (Václavské náměstí)", "28 Kasım 2026 – 6 Ocak 2027", "Her gün 10:00–22:00", "Eski Şehir Meydanı'na yürüme mesafesinde, bulvar boyunca uzanan pazar."),
            ("Náměstí Míru", "20 Kasım – 24 Aralık", "Pazarın sitesine bak", "Vinohrady'de, daha yerel ve sakin bir pazar."),
            ("Tylovo náměstí", "26 Kasım – 24 Aralık", "Pazarın sitesine bak", "Náměstí Míru'ya yakın, küçük mahalle pazarı."),
        ],
        "route": [
            "Eski Şehir Meydanı'ndan başla; ağacı ve astronomik saati gör.",
            "Havelská ya da Melantrichova sokağından güneye yürüyüp Venceslas Meydanı'na geç (yaklaşık 10 dakika).",
            "Daha yerel bir pazar istersen Venceslas Meydanı'nın üst ucundan Náměstí Míru'ya devam et.",
        ],
        "route_note": "İki ana meydan arası yaklaşık 800 m. Náměstí Míru'yu eklersen rota yaklaşık 2 km olur.",
        "tips": [
            "Kartla ödemede \"kendi para biriminle öde\" (DCC) seçeneği sunulursa reddet ve Çek korunası seç; DCC çoğu zaman yüzde birkaç daha pahalıya gelir.",
            "Jambon ve halušky gibi yiyecekler çoğunlukla 100 gram fiyatıyla yazılır; tartılan porsiyonun fiyatını ödemeden önce sor.",
            "Çekya'da döviz bürosunda banknot değişimi için komisyon alınması yasak ve kötü bir işlemi 3 saat içinde iptal ettirme hakkın var.",
        ],
        "faq": [
            ("Prag Noel pazarları 2026'da ne zaman açılıyor?", "Eski Şehir Meydanı ve Venceslas Meydanı'ndaki ana pazarlar 28 Kasım 2026'da açılıyor ve 6 Ocak 2027'ye kadar sürüyor."),
            ("Prag Noel pazarları kaçta açık?", "Ana pazarlar her gün 10:00–22:00 arası açık."),
            ("Prag'da Noel ağacı ne zaman yakılıyor?", "Eski Şehir Meydanı'ndaki dev ağaç pazarın açılış akşamı yakılıyor."),
            ("Prag Noel pazarında kartla ödeme yaparken nelere dikkat etmeliyim?", "Terminal \"kendi para biriminle öde\" seçeneği sunarsa reddet ve Çek korunası seç. Ağırlıkla satılan yiyeceklerde fiyatın 100 gram için olduğunu unutma."),
        ],
        "sources": [
            ("expats.cz", "https://www.expats.cz/"),
            ("akce.cz", "https://www.akce.cz/"),
        ],
    },
]

CSS = """
:root{--night:#12121F;--navy:#1A1A2E;--cream:#FAFAF7;--cream-warm:#F4F1EA;--ink:#1c1c28;--mut:#5e5e6e;--sunset:#FF5722;--sunset-deep:#E64A19;--line:rgba(28,28,40,.12);--serif:'Crimson Text',Georgia,serif;--sans:'Inter',-apple-system,BlinkMacSystemFont,sans-serif;--pad-x:clamp(20px,4.5vw,64px)}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--cream);color:var(--ink);font:16px/1.65 var(--sans)}
a{color:inherit}
.top{position:sticky;top:0;z-index:5;display:flex;align-items:center;justify-content:space-between;gap:16px;padding:14px var(--pad-x);background:rgba(250,250,247,.92);backdrop-filter:blur(12px);border-bottom:1px solid var(--line)}
.brand{display:flex;align-items:center;gap:10px;text-decoration:none;font:600 22px var(--serif)}
.brand img{width:28px;height:28px;border-radius:7px}
.pill{display:inline-flex;align-items:center;justify-content:center;padding:12px 22px;border-radius:999px;font:600 13px var(--sans);letter-spacing:.06em;text-transform:uppercase;text-decoration:none;white-space:nowrap}
.pill-sunset{background:var(--sunset);color:#fff}.pill-sunset:hover{background:var(--sunset-deep)}
main{max-width:860px;margin:0 auto;padding:40px var(--pad-x) 96px}
.crumbs{font-size:13px;color:var(--mut);margin-bottom:28px}.crumbs a{text-decoration:none}.crumbs a:hover{text-decoration:underline}
.label{display:block;font:600 12px var(--sans);letter-spacing:.14em;text-transform:uppercase;color:var(--sunset);margin-bottom:12px}
h1{font:400 clamp(38px,6vw,60px)/1.05 var(--serif);margin:0 0 20px;letter-spacing:-.01em}
h2{font:400 clamp(28px,4vw,38px)/1.15 var(--serif);margin:56px 0 18px}
.answer{font-size:18px;line-height:1.7;background:var(--cream-warm);border-left:3px solid var(--sunset);border-radius:0 14px 14px 0;padding:20px 24px;margin:0 0 12px}
.meta{font-size:13px;color:var(--mut)}
.table-wrap{overflow-x:auto;border:1px solid var(--line);border-radius:16px;background:#fff}
table{width:100%;border-collapse:collapse;font-size:15px;min-width:620px}
th,td{text-align:left;vertical-align:top;padding:14px 16px;border-bottom:1px solid var(--line)}
th{font:600 12px var(--sans);letter-spacing:.08em;text-transform:uppercase;color:var(--mut);background:var(--cream-warm)}
tr:last-child td{border-bottom:0}td strong{font-weight:600}
ol.route{counter-reset:s;list-style:none;padding:0;margin:0}
ol.route li{counter-increment:s;position:relative;padding:0 0 18px 52px}
ol.route li::before{content:counter(s);position:absolute;left:0;top:-2px;width:34px;height:34px;border-radius:50%;background:var(--navy);color:var(--cream);display:grid;place-items:center;font:600 14px var(--sans)}
ul.tips{padding-left:20px}ul.tips li{margin-bottom:10px}
details{border-top:1px solid var(--line);padding:18px 0}details:last-of-type{border-bottom:1px solid var(--line)}
summary{cursor:pointer;font-weight:600;list-style:none}summary::-webkit-details-marker{display:none}
summary::after{content:'+';float:right;color:var(--sunset);font-weight:400;font-size:20px;line-height:1}
details[open] summary::after{content:'–'}details p{margin:12px 0 0;color:var(--mut)}
.cta{margin-top:64px;background:var(--navy);color:var(--cream);border-radius:24px;padding:36px clamp(24px,4vw,44px)}
.cta h2{margin:0 0 10px;color:var(--cream)}.cta p{margin:0 0 22px;color:rgba(250,250,247,.78)}
.sources{font-size:13px;color:var(--mut);margin-top:40px}.sources a{color:var(--mut)}
.cards{display:grid;gap:16px;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));margin-top:24px}
.card{display:block;text-decoration:none;background:#fff;border:1px solid var(--line);border-radius:18px;padding:24px;transition:transform .3s,box-shadow .3s}
.card:hover{transform:translateY(-3px);box-shadow:0 12px 30px rgba(18,18,31,.08)}
.card .label{margin-bottom:8px}.card h3{font:400 26px/1.15 var(--serif);margin:0 0 8px}.card p{margin:0;color:var(--mut);font-size:15px}
footer{border-top:1px solid var(--line);padding:28px var(--pad-x);font-size:13px;color:var(--mut);display:flex;flex-wrap:wrap;gap:18px;justify-content:space-between}
footer a{text-decoration:none}footer a:hover{text-decoration:underline}
@media (max-width:560px){.top .pill{padding:10px 16px;font-size:12px}}
"""


def head(title: str, description: str, url: str, ld: list[dict]) -> str:
    ld_html = "\n".join(
        '<script type="application/ld+json">\n'
        + json.dumps(obj, ensure_ascii=False, indent=2).replace("</", "<\\/")
        + "\n</script>"
        for obj in ld
    )
    return f"""<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{escape(title)}</title>
<meta name="description" content="{escape(description)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Navitra">
<meta property="og:locale" content="tr_TR">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(description)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@navitratravel">
<meta name="apple-itunes-app" content="app-id=6779956173">
<link rel="icon" type="image/png" href="/favicon.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Crimson+Text:ital,wght@0,400;0,600;1,400&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>{CSS}</style>
{ld_html}
</head>
<body>
<header class="top">
  <a href="/tr/" class="brand"><img src="/logo.png" alt="" width="28" height="28">Navitra</a>
  <a class="pill pill-sunset" href="{STORE}">Uygulamayı indir</a>
</header>
"""


FOOTER = f"""<footer>
  <span>© 2026 Navitra · İstanbul'da doğdu.</span>
  <span><a href="/tr/">Ana sayfa</a> · <a href="/tr/rehber/">Rehberler</a> · <a href="/support.html">Destek</a> · <a href="/privacy.html">Gizlilik</a></span>
</footer>
</body>
</html>
"""


def crumbs_ld(items: list[tuple[str, str]]) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i, "name": name, "item": url}
            for i, (name, url) in enumerate(items, 1)
        ],
    }


def guide_page(g: dict) -> str:
    url = f"{BASE}/tr/rehber/{g['slug']}/"
    article = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": g["title"],
        "description": g["description"],
        "inLanguage": "tr",
        "mainEntityOfPage": url,
        "datePublished": CHECKED,
        "dateModified": CHECKED,
        "image": f"{BASE}/og-image.jpg",
        "author": {"@type": "Organization", "name": "Navitra", "url": f"{BASE}/"},
        "publisher": {"@type": "Organization", "name": "Navitra", "logo": {"@type": "ImageObject", "url": f"{BASE}/logo.png"}},
        "about": {"@type": "City", "name": g["city"]},
    }
    faq = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "inLanguage": "tr",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in g["faq"]
        ],
    }
    crumbs = crumbs_ld([("Navitra", f"{BASE}/tr/"), ("Rehberler", f"{BASE}/tr/rehber/"), (g["city"], url)])

    rows = "\n".join(
        f"<tr><td><strong>{escape(n)}</strong></td><td>{escape(d)}</td><td>{escape(h)}</td><td>{escape(note)}</td></tr>"
        for n, d, h, note in g["markets"]
    )
    route = "\n".join(f"<li>{escape(step)}</li>" for step in g["route"])
    tips = "\n".join(f"<li>{escape(t)}</li>" for t in g["tips"])
    faqs = "\n".join(
        f"<details><summary>{escape(q)}</summary><p>{escape(a)}</p></details>" for q, a in g["faq"]
    )
    sources = " · ".join(f'<a href="{escape(u)}" rel="nofollow noopener" target="_blank">{escape(n)}</a>' for n, u in g["sources"])

    return head(g["title"], g["description"], url, [article, faq, crumbs]) + f"""<main>
  <nav class="crumbs" aria-label="İçerik yolu"><a href="/tr/">Navitra</a> › <a href="/tr/rehber/">Rehberler</a> › {escape(g['city'])}</nav>
  <span class="label">Noel Pazarı Rotası · {escape(g['city'])}</span>
  <h1>{escape(g['h1'])}</h1>
  <p class="answer">{escape(g['answer'])}</p>
  <p class="meta">Tarih ve saatler {CHECKED_TR} tarihinde kontrol edildi. Gitmeden önce pazarın kendi sitesinden son durumu kontrol et.</p>

  <h2>Pazarlar, tarihler ve saatler</h2>
  <div class="table-wrap"><table>
    <thead><tr><th>Pazar</th><th>Tarih (2026)</th><th>Saat</th><th>Not</th></tr></thead>
    <tbody>
{rows}
    </tbody>
  </table></div>

  <h2>Tek akşamlık yürüyüş rotası</h2>
  <ol class="route">
{route}
  </ol>
  <p class="meta">{escape(g['route_note'])}</p>

  <h2>İpuçları</h2>
  <ul class="tips">
{tips}
  </ul>

  <h2>Sık sorulan sorular</h2>
{faqs}

  <section class="cta">
    <h2>Bu rotayı kendi otelinden başlat</h2>
    <p>{escape(g['city'])}'da görmek istediğin yerleri seç; Navitra açılış saatlerine uyan, yürümeyi en aza indiren günlük rotanı saniyeler içinde çıkarsın.</p>
    <a class="pill pill-sunset" href="{STORE}">Navitra'yı ücretsiz indir</a>
  </section>

  <p class="sources">Kaynaklar: {sources}</p>
</main>
""" + FOOTER


def index_page() -> str:
    url = f"{BASE}/tr/rehber/"
    title = "Noel Pazarı Rotaları 2026 | Navitra Gezi Rehberleri"
    description = "Viyana, Dresden ve Prag Noel pazarları için 2026 tarihleri, açılış saatleri ve tek akşamlık yürüyüş rotaları."
    item_list = {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": "Noel Pazarı Rotaları 2026",
        "itemListElement": [
            {"@type": "ListItem", "position": i, "url": f"{url}{g['slug']}/", "name": g["title"]}
            for i, g in enumerate(GUIDES, 1)
        ],
    }
    crumbs = crumbs_ld([("Navitra", f"{BASE}/tr/"), ("Rehberler", url)])
    cards = "\n".join(
        f'<a class="card" href="/tr/rehber/{g["slug"]}/"><span class="label">Noel Pazarı Rotası</span><h3>{escape(g["city"])}</h3><p>{escape(g["description"])}</p></a>'
        for g in GUIDES
    )
    return head(title, description, url, [item_list, crumbs]) + f"""<main>
  <nav class="crumbs" aria-label="İçerik yolu"><a href="/tr/">Navitra</a> › Rehberler</nav>
  <span class="label">Gezi rehberleri</span>
  <h1>Noel pazarı rotaları 2026</h1>
  <p class="answer">Avrupa'nın Noel pazarlarını tek akşamda gezmek için şehir şehir tarihler, açılış saatleri ve yürüyüş rotaları. Her rehberdeki bilgiler resmî kaynaklardan kontrol edilir ve sezon boyunca güncellenir.</p>
  <div class="cards">
{cards}
  </div>
  <section class="cta">
    <h2>Kendi rotanı saniyeler içinde oluştur</h2>
    <p>Görmek istediğin yerleri seç, Navitra açılış saatlerine uyan günlük rotanı çıkarsın.</p>
    <a class="pill pill-sunset" href="{STORE}">Navitra'yı ücretsiz indir</a>
  </section>
</main>
""" + FOOTER


def main() -> None:
    out = ROOT / "tr" / "rehber"
    out.mkdir(parents=True, exist_ok=True)
    (out / "index.html").write_text(index_page(), encoding="utf-8", newline="\n")
    for g in GUIDES:
        d = out / g["slug"]
        d.mkdir(exist_ok=True)
        (d / "index.html").write_text(guide_page(g), encoding="utf-8", newline="\n")
    print(f"Generated {len(GUIDES)} guides + index.")


if __name__ == "__main__":
    main()
