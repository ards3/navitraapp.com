from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCALES = "tr de es fr it nl pt-br ar ja ko ru zh-hans".split()
PAGES = [ROOT / "index.html", *[ROOT / code / "index.html" for code in LOCALES]]
STORE = "https://apps.apple.com/us/app/navitra-ai-travel-planner/id6779956173"

failed = []
for page in PAGES:
    text = page.read_text(encoding="utf-8")
    checks = {
        "collaboration section": 'id="collaborate"' in text,
        "collaboration email": "mailto:support@navitraapp.com?subject=" in text,
        "canonical App Store links": text.count(STORE) >= 6,
        "no old App Store URL": "apps.apple.com/app/id6779956173" not in text,
        "no launch-status CTA": ">Launch status<" not in text,
        "Twitter profile": text.count("https://x.com/navitratravel") == 2,
        "Instagram profile": text.count("https://instagram.com/navitra.travel") == 2,
        "TikTok profile": text.count("https://tiktok.com/@navitra.travel") == 2,
        "no old social handles": not any(old in text for old in ("twitter.com/navitraapp", "twitter.com/navitra.travel", "instagram.com/navitraapp", "tiktok.com/@navitraapp")),
    }
    errors = [name for name, passed in checks.items() if not passed]
    print(f"{page.relative_to(ROOT)}: AppStore={text.count(STORE)}, collab=yes, " + ("PASS" if not errors else f"FAIL {errors}"))
    failed.extend((page, error) for error in errors)

if failed:
    raise SystemExit(1)
print(f"PASS: {len(PAGES)} language pages validated")
