#!/usr/bin/env python3
"""Erzeugt die statischen Seiten der Route2Charge-Website (Englisch + Deutsch).

Aufruf:  python3 tools/build.py
Danach liegen index.html, privacy.html, de/index.html, de/datenschutz.html
und 404.html fertig im Hauptordner. Kein Server, kein JavaScript nötig.
"""
from pathlib import Path

# ---------------------------------------------------------------------------
# Einstellungen – hier anpassen
SITE_URL = "https://route2charge.github.io"
OWNER = "Clemens Schweder"
EMAIL = "route2charge@proton.me"
UPDATED_EN = "November 2026"
UPDATED_DE = "November 2026"
# ---------------------------------------------------------------------------

ROOT = Path(__file__).resolve().parent.parent

CSP = ("default-src 'self'; img-src 'self' data:; style-src 'self'; script-src 'none'; "
       "object-src 'none'; base-uri 'none'; form-action 'none'")

ICON_CHECK = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" '
              'stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" d="M5 12.5l4.2 4.2L19 7"/></svg>')
ICON_BOLT = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" '
             'd="M13.5 2 4.8 13.2h5.9L9.6 22l9.6-12.4h-6.1z"/></svg>')
ICON_MAP = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2" '
            'stroke-linejoin="round" d="M9 4 3 6.5v13L9 17l6 2.5 6-2.5v-13L15 6.5 9 4zm0 0v13m6-10.5v13"/></svg>')
ICON_PHONE = ('<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="6.5" y="2.5" width="11" height="19" rx="3" '
              'fill="none" stroke="currentColor" stroke-width="2"/><path stroke="currentColor" stroke-width="2" '
              'stroke-linecap="round" d="M10.5 18.5h3"/></svg>')
ICON_BATTERY = ('<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="2.5" y="7" width="17" height="10" rx="2.5" '
                'fill="none" stroke="currentColor" stroke-width="2"/><rect x="20.5" y="10" width="2" height="4" rx="1" '
                'fill="currentColor"/><rect x="5" y="9.5" width="9" height="5" rx="1.2" fill="currentColor"/></svg>')
ICON_CLOCK = ('<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" '
              'stroke="currentColor" stroke-width="2"/><path fill="none" stroke="currentColor" stroke-width="2" '
              'stroke-linecap="round" d="M12 7v5l3 2"/></svg>')

ROUTE_PATH = "M40 160 C150 160 150 80 260 80 C370 80 370 160 480 160 C590 160 590 80 700 80 C810 80 810 160 920 160"


def route_svg(t):
    """Illustration: Route, Ladefenster, zwei Empfehlungen, Reichweitengrenze."""
    return f"""<svg class="route-svg" viewBox="0 0 960 230" role="img" aria-labelledby="rt rd">
  <title id="rt">{t['svg_title']}</title>
  <desc id="rd">{t['svg_desc']}</desc>
  <defs>
    <filter id="glow" x="-10%" y="-60%" width="120%" height="220%">
      <feGaussianBlur stdDeviation="7" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <path class="r-base" d="{ROUTE_PATH}" fill="none" stroke-width="10" stroke-linecap="round"/>
  <path class="r-window" d="{ROUTE_PATH}" pathLength="100" stroke-dasharray="0 45 30 100" fill="none" stroke-width="10" stroke-linecap="round" filter="url(#glow)"/>
  <text class="r-text-accent r-sm-hide" x="530" y="95" text-anchor="middle">{t['svg_window']}</text>

  <circle class="r-dot" cx="40" cy="160" r="9"/>
  <text class="r-text-strong" x="40" y="205" text-anchor="start">{t['svg_start']}</text>
  <text class="r-text r-sm-hide" x="40" y="225" text-anchor="start">{t['svg_start_sub']}</text>

  <g transform="translate(480 160)">
    <circle class="r-ring" r="27"/>
    <circle class="r-m2" r="18"/>
    <text class="r-num" y="6" text-anchor="middle">2</text>
  </g>
  <text class="r-text" x="480" y="216" text-anchor="middle">150 kW</text>

  <g transform="translate(635 92.5)">
    <circle class="r-ring" r="27"/>
    <circle class="r-m1" r="18"/>
    <text class="r-num" y="6" text-anchor="middle">1</text>
  </g>
  <text class="r-text-strong" x="612" y="44" text-anchor="middle">300 kW</text>

  <g transform="translate(700 80)">
    <rect class="r-flag" x="-2" y="-22" width="4" height="22" rx="2"/>
    <g transform="translate(-25 -52)">
      <rect class="r-batt" x="0" y="0" width="44" height="26" rx="6"/>
      <rect class="r-flag" x="46.5" y="8" width="4.5" height="10" rx="2"/>
      <rect class="r-flag" x="5" y="5" width="9" height="16" rx="2.5"/>
    </g>
  </g>
  <text class="r-text r-sm-hide" x="735" y="44" text-anchor="start">{t['svg_limit']}</text>

  <g transform="translate(920 160)">
    <circle class="r-dot" r="9"/>
  </g>
  <text class="r-text-strong" x="920" y="205" text-anchor="end">{t['svg_dest']}</text>
</svg>"""


TEXT = {
    "en": {
        "lang": "en",
        "prefix": "",
        "home": "index.html",
        "privacy_file": "privacy.html",
        "help_file": "help.html",
        "other_home": "de/index.html",
        "other_privacy": "de/datenschutz.html",
        "other_help": "de/hilfe.html",
        "other_label": "DE",
        "other_name": "Deutsch",
        "title": "Route2Charge – your 2 best charging stops",
        "description": "150 km left? Route2Charge shows the two best fast chargers along your route – right before your range runs low. No account, no tracking, no ads.",
        "nav_how": "How it works",
        "nav_app": "The app",
        "nav_privacy": "Privacy",
        "nav_help": "Help",
        "help_title": "Help &amp; feedback",
        "help_lead": "Found a bug, have a question or an idea? We’d love to hear from you – no form, no account, no tracking. Just an e-mail.",
        "contact_h": "Write to us",
        "contact_text": "Please tell us your start, destination and remaining range if a result looks wrong – that helps us reproduce it.",
        "contact_btn": "Send an e-mail",
        "faq_h": "Frequently asked questions",
        "faq": [
            ("Where does the charging station data come from?", "From Open Charge Map, a free community database, and its data providers. If a charger is missing, closed or shows the wrong power, you can correct it directly at <a href=\"https://openchargemap.org\">openchargemap.org</a> – or simply tell us."),
            ("Why does the app show prices?", "It doesn’t yet. There is no free, open database for charging prices. We’re working on it."),
            ("Why does Apple Maps only navigate to the charger?", "Apple Maps accepts only one destination from other apps. After charging, tap “Continue to destination” or “Find next charging stop from here” in Route2Charge."),
            ("Does the app need my location?", "Only if you start from where you are, and to notice when you’ve arrived at the charger. You can also enter any starting point. Your location is never stored."),
            ("Which cars does it work with?", "Any electric car with a CCS fast-charging plug – that’s almost every EV in Europe. For battery percentage mode, enter your battery size and average consumption in the settings."),
            ("Can I hide Tesla Superchargers?", "Yes – in the settings, switch on “Hide Tesla Superchargers”."),
        ],
        "skip": "Skip to content",
        "eyebrow": "No account · No tracking · No ads",
        "h1": '150&nbsp;km left? <span class="glow">Your 2 best charging stops.</span>',
        "lead": "Tell Route2Charge where you’re going and how far you can still drive. It shows the two best fast chargers along your route – right before your range runs low.",
        "cta": "See how it works",
        "soon": "Coming soon to the App Store",
        "facts": ["Germany &amp; Europe", "CCS fast chargers", "Built for iPhone"],
        "hero_alt": "Route2Charge on iPhone: a route from Karlsfeld to Stuttgart with the charging window highlighted in green and two recommended chargers.",
        "how_kicker": "How it works",
        "how_h2": "Three steps. Two stops. Zero stress.",
        "how_p": "No planning marathon – just the answer you need when the range gets tight.",
        "svg_title": "How Route2Charge picks your stops",
        "svg_desc": "A route from start to destination. Shortly before the range limit, a green charging window is highlighted, containing recommendation 1 and recommendation 2.",
        "svg_window": "Charging window",
        "svg_start": "Start",
        "svg_start_sub": "150 km left",
        "svg_limit": "Range limit (minus buffer)",
        "svg_dest": "Destination",
        "route_caption": "Route2Charge searches the stretch right before your range limit – and picks two real alternatives, a few kilometres apart.",
        "steps": [
            ("Set your destination", "Start from where you are or pick any starting point. Routing runs on Apple Maps."),
            ("Tell it how far you can go", "Enter your remaining range in km, your battery percentage – or simply say: I want to charge around km 150."),
            ("Get your best stops – and more", "Route2Charge checks every fast charger in your charging window and shows the best two plus further options – with real detours, not guesses. Tap one to see your whole trip."),
        ],
        "crit_h": "Ranked by what actually matters",
        "criteria": [
            ("Up to <span>350&nbsp;kW</span>", "Fast chargers first. Less waiting, more driving."),
            ("Minimal <span>detour</span>", "Every candidate is checked with real routing – chargers on the wrong side of the motorway drop out."),
            ("Range, <span>used well</span>", "Charge late enough to make progress, early enough to stay relaxed. Your safety buffer always applies."),
            ("Real <span>choice</span>", "Your second option comes from a different network whenever possible – and you can hide Tesla Superchargers."),
        ],
        "app_kicker": "The app",
        "app_h2": "Clear, calm, made for the road.",
        "app_p": "Your route, the charging window and your best options – with power, detour and the range left on arrival. Pick a charger and see the whole trip, start to destination, right in the app.",
        "shots": [
            ("assets/screens/route.jpg", "Route and charging window at a glance", "The map shows the route, the green charging window and both recommended chargers."),
            ("assets/screens/stops.jpg", "Your two best stops – plus more options", "List of the two recommended chargers with power, charge points, detour and remaining range, followed by further options from other networks."),
            ("assets/screens/trip.jpg", "The whole trip with your charging stop", "Map of the full trip from start via the charging station to the destination, with total distance, driving time and range on arrival."),
        ],
        "priv_kicker": "Privacy",
        "claim": ["No account.", "No tracking.", "No server."],
        "priv_p": "Route2Charge is built to know as little about you as possible. That’s not a feature we added – it’s how the app works.",
        "checks": [
            ("No sign-up, ever", "Open the app and go. There’s nothing to register."),
            ("No ads, no analytics, no trackers", "We don’t know who you are – and we don’t want to."),
            ("Your route stays yours", "Routing runs through Apple Maps. The charger database only sees small map areas around your charging window – never your start, destination or full route."),
            ("Settings stay on your iPhone", "Battery size, consumption and preferences are stored locally only."),
        ],
        "more": "Read the privacy policy →",
        "footer_note": "Route2Charge is an independent project.",
        "contact": "Contact",
        "help": "Help",
        "privacy": "Privacy policy",
        "credits": "Charging station data © Open Charge Map contributors and data providers, licensed under CC BY 4.0. Maps and routing: Apple Maps. Apple, iPhone and App Store are trademarks of Apple Inc. All information without guarantee – availability, power and prices of charging stations may differ.",
        "back": "← Back to Route2Charge",
        "nf_title": "Page not found",
        "nf_text": "This page ran out of range. Let’s get you back on the road.",
    },
    "de": {
        "lang": "de",
        "prefix": "../",
        "home": "index.html",
        "privacy_file": "datenschutz.html",
        "help_file": "hilfe.html",
        "other_home": "../index.html",
        "other_privacy": "../privacy.html",
        "other_help": "../help.html",
        "other_label": "EN",
        "other_name": "English",
        "title": "Route2Charge – deine 2 besten Ladestopps",
        "description": "Noch 150 km? Route2Charge zeigt dir die zwei besten Schnelllader auf deiner Route – kurz bevor es knapp wird. Ohne Account, ohne Tracking, ohne Werbung.",
        "nav_how": "So funktioniert’s",
        "nav_app": "Die App",
        "nav_privacy": "Datenschutz",
        "nav_help": "Hilfe",
        "help_title": "Hilfe &amp; Feedback",
        "help_lead": "Fehler entdeckt, eine Frage oder eine Idee? Schreib uns gern – ohne Formular, ohne Account, ohne Tracking. Einfach per E-Mail.",
        "contact_h": "Schreib uns",
        "contact_text": "Wenn ein Ergebnis komisch aussieht: Schick uns Start, Ziel und Reichweite mit – dann können wir es nachstellen.",
        "contact_btn": "E-Mail schreiben",
        "faq_h": "Häufige Fragen",
        "faq": [
            ("Woher kommen die Ladesäulen-Daten?", "Von Open Charge Map, einer freien Community-Datenbank, und deren Datenlieferanten. Fehlt eine Säule, ist sie geschlossen oder stimmt die Leistung nicht, kannst du das direkt auf <a href=\"https://openchargemap.org\">openchargemap.org</a> korrigieren – oder uns einfach Bescheid geben."),
            ("Zeigt die App Preise an?", "Noch nicht. Für Ladepreise gibt es keine freie, offene Datenbank. Wir arbeiten daran."),
            ("Warum navigiert Apple Karten nur bis zur Säule?", "Apple Karten übernimmt von anderen Apps nur ein Ziel. Nach dem Laden tippst du in Route2Charge auf „Weiter zum Ziel navigieren“ oder „Nächsten Ladestopp ab hier suchen“."),
            ("Braucht die App meinen Standort?", "Nur wenn du an deinem Standort startest und damit die App merkt, dass du an der Ladesäule angekommen bist. Du kannst auch jeden anderen Startpunkt eingeben. Der Standort wird nie gespeichert."),
            ("Mit welchen Autos funktioniert die App?", "Mit jedem E-Auto mit CCS-Schnellladestecker – also fast allen in Europa. Für den Modus „Akku %“ trägst du in den Einstellungen Akkugröße und Durchschnittsverbrauch ein."),
            ("Kann ich Tesla Supercharger ausblenden?", "Ja – in den Einstellungen „Tesla Supercharger ausblenden“ einschalten."),
        ],
        "skip": "Zum Inhalt springen",
        "eyebrow": "Ohne Account · Ohne Tracking · Ohne Werbung",
        "h1": 'Noch 150&nbsp;km? <span class="glow">Deine 2 besten Ladestopps.</span>',
        "lead": "Sag Route2Charge, wohin du fährst und wie weit du noch kommst. Die App zeigt dir die zwei besten Schnelllader auf deiner Route – kurz bevor es knapp wird.",
        "cta": "So funktioniert’s",
        "soon": "Bald im App Store",
        "facts": ["Deutschland &amp; Europa", "CCS-Schnelllader", "Für iPhone"],
        "hero_alt": "Route2Charge auf dem iPhone: Route von Karlsfeld nach Stuttgart mit grün markiertem Ladefenster und zwei empfohlenen Ladesäulen.",
        "how_kicker": "So funktioniert’s",
        "how_h2": "Drei Schritte. Zwei Stopps. Null Stress.",
        "how_p": "Kein Planungsmarathon – nur die Antwort, die du brauchst, wenn die Reichweite knapp wird.",
        "svg_title": "So wählt Route2Charge deine Ladestopps",
        "svg_desc": "Eine Route vom Start zum Ziel. Kurz vor der Reichweitengrenze ist ein grünes Ladefenster markiert, darin Empfehlung 1 und Empfehlung 2.",
        "svg_window": "Ladefenster",
        "svg_start": "Start",
        "svg_start_sub": "noch 150 km",
        "svg_limit": "Reichweite (minus Puffer)",
        "svg_dest": "Ziel",
        "route_caption": "Route2Charge sucht im Abschnitt kurz vor deiner Reichweitengrenze – und wählt zwei echte Alternativen, ein paar Kilometer auseinander.",
        "steps": [
            ("Ziel eingeben", "Start am aktuellen Standort oder an einem beliebigen Ort. Die Route berechnet Apple Karten."),
            ("Reichweite angeben", "Restreichweite in km, Akkustand in % – oder einfach: Ich will bei ca. km 150 laden."),
            ("Die besten Stopps bekommen – und mehr", "Route2Charge prüft alle Schnelllader im Ladefenster und zeigt die zwei besten plus weitere Optionen – mit echtem Umweg statt Schätzung. Antippen zeigt dir die ganze Fahrt."),
        ],
        "crit_h": "Ausgewählt nach dem, was zählt",
        "criteria": [
            ("Bis <span>350&nbsp;kW</span>", "Schnelllader zuerst. Weniger warten, mehr fahren."),
            ("Kleinster <span>Umweg</span>", "Jeder Kandidat wird echt nachgerechnet – Säulen auf der falschen Autobahnseite fliegen raus."),
            ("Reichweite <span>clever genutzt</span>", "Spät genug laden, um voranzukommen, früh genug, um entspannt zu bleiben. Dein Sicherheitspuffer gilt immer."),
            ("Echte <span>Auswahl</span>", "Die zweite Empfehlung kommt möglichst von einem anderen Anbieter – und Tesla Supercharger kannst du ausblenden."),
        ],
        "app_kicker": "Die App",
        "app_h2": "Klar, ruhig, gemacht für unterwegs.",
        "app_p": "Deine Route, das Ladefenster und deine besten Optionen – mit Leistung, Umweg und Reichweite bei Ankunft. Säule antippen und die ganze Fahrt vom Start bis zum Ziel direkt in der App sehen.",
        "shots": [
            ("../assets/screens/route.jpg", "Route und Ladefenster auf einen Blick", "Die Karte zeigt die Route, das grüne Ladefenster und beide empfohlenen Ladesäulen."),
            ("../assets/screens/stops.jpg", "Die zwei besten Stopps – plus weitere Optionen", "Liste der zwei empfohlenen Ladesäulen mit Leistung, Ladepunkten, Umweg und Restreichweite, darunter weitere Optionen anderer Anbieter."),
            ("../assets/screens/trip.jpg", "Die ganze Fahrt mit Ladestopp", "Karte der ganzen Fahrt vom Start über die Ladesäule zum Ziel, mit Gesamtstrecke, Fahrzeit und Reichweite bei Ankunft."),
        ],
        "priv_kicker": "Datenschutz",
        "claim": ["Kein Account.", "Kein Tracking.", "Kein Server."],
        "priv_p": "Route2Charge ist so gebaut, dass es so wenig wie möglich über dich weiß. Das ist kein Zusatz-Feature – so funktioniert die App.",
        "checks": [
            ("Keine Anmeldung, niemals", "App öffnen und los. Es gibt nichts zu registrieren."),
            ("Keine Werbung, keine Analyse, keine Tracker", "Wir wissen nicht, wer du bist – und wollen es auch nicht."),
            ("Deine Route bleibt deine", "Die Route berechnet Apple Karten. Die Ladesäulen-Datenbank sieht nur kleine Kartenausschnitte rund um dein Ladefenster – nie Start, Ziel oder die ganze Route."),
            ("Einstellungen bleiben auf dem iPhone", "Akkugröße, Verbrauch und Vorlieben werden nur lokal gespeichert."),
        ],
        "more": "Zur Datenschutzerklärung →",
        "footer_note": "Route2Charge ist ein unabhängiges Projekt.",
        "contact": "Kontakt",
        "help": "Hilfe",
        "privacy": "Datenschutzerklärung",
        "credits": "Ladesäulen-Daten © Open Charge Map und Datenlieferanten, Lizenz CC BY 4.0. Karten und Routen: Apple Karten. Apple, iPhone und App Store sind Marken der Apple Inc. Alle Angaben ohne Gewähr – Verfügbarkeit, Leistung und Preise der Ladesäulen können abweichen.",
        "back": "← Zurück zu Route2Charge",
        "nf_title": "Seite nicht gefunden",
        "nf_text": "Dieser Seite ist der Akku ausgegangen. Zurück auf die Strecke:",
    },
}


def head(t, title, description, canonical, alt_en, alt_de):
    p = t["prefix"]
    return f"""<!doctype html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta http-equiv="Content-Security-Policy" content="{CSP}">
<meta name="referrer" content="no-referrer">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="theme-color" content="#06090d">
<meta name="color-scheme" content="dark">
<link rel="canonical" href="{SITE_URL}/{canonical}">
<link rel="alternate" hreflang="en" href="{SITE_URL}/{alt_en}">
<link rel="alternate" hreflang="de" href="{SITE_URL}/{alt_de}">
<link rel="alternate" hreflang="x-default" href="{SITE_URL}/{alt_en}">
<link rel="icon" href="{p}assets/icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{p}assets/apple-touch-icon.png">
<link rel="stylesheet" href="{p}assets/style.css">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{SITE_URL}/{canonical}">
<meta property="og:image" content="{SITE_URL}/assets/og-{t['lang']}.png">
<meta name="twitter:card" content="summary_large_image">
</head>
<body>
<a class="skip" href="#main">{t['skip']}</a>
"""


def header(t, lang_target, show_nav=True):
    p = t["prefix"]
    nav = ""
    if show_nav:
        nav = f"""<a class="hide-sm" href="#how">{t['nav_how']}</a>
      <a class="hide-sm" href="#app">{t['nav_app']}</a>
      <a class="hide-sm" href="#privacy">{t['nav_privacy']}</a>
      <a href="{t['help_file']}">{t['nav_help']}</a>
      """
    home = t["home"]
    return f"""<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{home}" aria-label="Route2Charge – Start">
      <img src="{p}assets/icon.svg" alt="" width="32" height="32">
      <span>Route<b>2</b>Charge</span>
    </a>
    <nav class="nav" aria-label="Main">
      {nav}<a class="lang" href="{lang_target}" hreflang="{'de' if t['lang']=='en' else 'en'}" lang="{'de' if t['lang']=='en' else 'en'}" title="{t['other_name']}">{t['other_label']}</a>
    </nav>
  </div>
</header>
"""


def footer(t):
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="footer-top">
      <span>© 2026 {OWNER} · {t['footer_note']}</span>
      <nav class="footer-links" aria-label="Footer">
        <a href="{t['help_file']}">{t['help']}</a>
        <a href="{t['privacy_file']}">{t['privacy']}</a>
        <a href="mailto:{EMAIL}">{t['contact']}</a>
        <a href="{t['other_home']}" hreflang="{'de' if t['lang']=='en' else 'en'}">{t['other_name']}</a>
      </nav>
    </div>
    <p class="credits">{t['credits']}</p>
  </div>
</footer>
</body>
</html>
"""


def landing(t):
    p = t["prefix"]
    facts = "\n".join(
        f"<li>{icon}{text}</li>" for icon, text in zip([ICON_MAP, ICON_BOLT, ICON_PHONE], t["facts"])
    )
    steps = "\n".join(
        f"""<article class="card"><div class="step-num">{i}</div><h3>{h}</h3><p>{d}</p></article>"""
        for i, (h, d) in enumerate(t["steps"], 1)
    )
    criteria = "\n".join(
        f"""<article class="card"><div class="big">{h}</div><p>{d}</p></article>""" for h, d in t["criteria"]
    )
    shots = "\n".join(
        f"""<figure><div class="phone"><img src="{src}" alt="{alt}" width="1206" height="2622" loading="lazy"></div><figcaption>{cap}</figcaption></figure>"""
        for src, cap, alt in t["shots"]
    )
    checks = "\n".join(
        f"""<li>{ICON_CHECK}<div><strong>{h}</strong><span>{d}</span></div></li>""" for h, d in t["checks"]
    )
    canonical = "" if t["lang"] == "en" else "de/"
    html = head(t, t["title"], t["description"], canonical, "", "de/")
    html += header(t, t["other_home"])
    html += f"""<main id="main">
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <span class="eyebrow">{ICON_BATTERY}{t['eyebrow']}</span>
      <h1>{t['h1']}</h1>
      <p class="lead">{t['lead']}</p>
      <div class="cta-row">
        <a class="btn btn-primary" href="#how">{t['cta']}</a>
        <span class="pill">{ICON_CLOCK}{t['soon']}</span>
      </div>
      <ul class="facts">
{facts}
      </ul>
    </div>
    <div class="phone"><img src="{p}assets/screens/route.jpg" alt="{t['hero_alt']}" width="1206" height="2622"></div>
  </div>
</section>

<section id="how">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">{t['how_kicker']}</span>
      <h2>{t['how_h2']}</h2>
      <p>{t['how_p']}</p>
    </div>
    <div class="route-card">
      {route_svg(t)}
      <p class="route-caption">{t['route_caption']}</p>
    </div>
    <div class="steps">
{steps}
    </div>
  </div>
</section>

<section class="criteria-section" aria-labelledby="crit">
  <div class="wrap">
    <div class="section-head"><h2 id="crit">{t['crit_h']}</h2></div>
    <div class="criteria">
{criteria}
    </div>
  </div>
</section>

<section id="app">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">{t['app_kicker']}</span>
      <h2>{t['app_h2']}</h2>
      <p>{t['app_p']}</p>
    </div>
    <div class="screens">
{shots}
    </div>
  </div>
</section>

<section id="privacy" class="privacy-band">
  <div class="wrap privacy-grid">
    <div>
      <span class="kicker">{t['priv_kicker']}</span>
      <p class="claim">{''.join(f'<span>{c}</span>' for c in t['claim'])}</p>
      <p>{t['priv_p']}</p>
      <a class="more" href="{t['privacy_file']}">{t['more']}</a>
    </div>
    <ul class="checklist">
{checks}
    </ul>
  </div>
</section>
</main>
"""
    html += footer(t)
    return html


PRIVACY_EN = f"""
<p class="meta">Last updated: {UPDATED_EN}</p>
<div class="summary"><p><strong>In short:</strong> Route2Charge has no user accounts, no tracking, no advertising and no analytics. The developer does not receive or store any personal data about you. To work, the app uses Apple Maps (routes and place search) and Open Charge Map (charging station data).</p></div>

<h2>1. Who is responsible</h2>
<p>{OWNER}<br>E-mail: <a href="mailto:{EMAIL}">{EMAIL}</a></p>

<h2>2. The Route2Charge app</h2>
<h3>Location</h3>
<p>If you start a route from your current location, the app asks for permission to use your location while you use the app. Your location is used on your iPhone to start the route and is passed to Apple Maps for routing. It is not sent to us and not stored by the app. You can also choose a different starting point and decline location access.</p>
<h3>Routes and place search (Apple Maps)</h3>
<p>Search terms, start, destination and the positions of suggested charging stations are processed by Apple Maps to search places and calculate routes and detours. Apple’s privacy policy applies: <a href="https://www.apple.com/legal/privacy/">apple.com/legal/privacy</a>.</p>
<h3>Charging station data (Open Charge Map)</h3>
<p>To find charging stations, the app requests data for small rectangular map areas around your charging window from Open Charge Map. Your start, destination or full route are not transmitted, and no account or device identifier is used. As with any internet request, your IP address is technically transmitted to the provider’s servers. Information: <a href="https://openchargemap.org">openchargemap.org</a>.</p>
<h3>Settings</h3>
<p>Your settings (for example battery size, consumption, minimum charging power) are stored only locally on your device and are deleted when you delete the app.</p>
<h3>No tracking</h3>
<p>The app contains no advertising, no analytics or tracking tools and no third-party SDKs. If you have chosen in iOS to share analytics with app developers, Apple may provide anonymised crash reports to the developer; this is controlled entirely in your iOS settings.</p>

<h2>3. This website</h2>
<p>This website is hosted on GitHub Pages, a service of GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, USA. When you visit the site, GitHub processes technical data such as your IP address to deliver the pages and to keep the service secure. Data may be processed in the USA. Details: <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement">GitHub Privacy Statement</a>. The legal basis is our legitimate interest in providing a secure website (Art. 6(1)(f) GDPR).</p>
<p>The website itself uses no cookies, no tracking, no analytics, no JavaScript and no external fonts or third-party content.</p>
<p>If you contact us by e-mail, we use your message only to answer it and delete it when it is no longer needed.</p>

<h2>4. Your rights</h2>
<p>Under the GDPR you have the right to access, rectification, erasure, restriction of processing, data portability and to object to processing. To exercise these rights, simply send an e-mail. You also have the right to lodge a complaint with a data protection supervisory authority.</p>

<h2>5. Changes</h2>
<p>If the app or this website changes in a way that affects your data, this policy will be updated accordingly.</p>
"""

PRIVACY_DE = f"""
<p class="meta">Stand: {UPDATED_DE}</p>
<div class="summary"><p><strong>Kurz gesagt:</strong> Route2Charge hat keine Nutzerkonten, kein Tracking, keine Werbung und keine Analyse-Tools. Der Entwickler erhält und speichert keine personenbezogenen Daten über dich. Damit die App funktioniert, nutzt sie Apple Karten (Routen und Ortssuche) und Open Charge Map (Ladesäulen-Daten).</p></div>

<h2>1. Verantwortlicher</h2>
<p>{OWNER}<br>E-Mail: <a href="mailto:{EMAIL}">{EMAIL}</a></p>

<h2>2. Die App Route2Charge</h2>
<h3>Standort</h3>
<p>Wenn du eine Route an deinem aktuellen Standort startest, fragt die App nach der Erlaubnis, deinen Standort während der Nutzung zu verwenden. Der Standort wird auf deinem iPhone für den Start der Route verwendet und für die Routenberechnung an Apple Karten übergeben. Er wird nicht an uns übertragen und von der App nicht gespeichert. Du kannst stattdessen auch einen anderen Startpunkt wählen und den Standortzugriff ablehnen.</p>
<h3>Routen und Ortssuche (Apple Karten)</h3>
<p>Suchbegriffe, Start, Ziel und die Positionen vorgeschlagener Ladesäulen werden von Apple Karten verarbeitet, um Orte zu finden sowie Routen und Umwege zu berechnen. Es gilt die Datenschutzrichtlinie von Apple: <a href="https://www.apple.com/de/legal/privacy/">apple.com/de/legal/privacy</a>.</p>
<h3>Ladesäulen-Daten (Open Charge Map)</h3>
<p>Um Ladesäulen zu finden, ruft die App bei Open Charge Map Daten für kleine rechteckige Kartenausschnitte rund um dein Ladefenster ab. Start, Ziel oder die gesamte Route werden dabei nicht übertragen, und es wird weder ein Konto noch eine Gerätekennung verwendet. Wie bei jeder Internetverbindung wird dabei technisch deine IP-Adresse an die Server des Anbieters übermittelt. Informationen: <a href="https://openchargemap.org">openchargemap.org</a>.</p>
<h3>Einstellungen</h3>
<p>Deine Einstellungen (zum Beispiel Akkugröße, Verbrauch, Mindestladeleistung) werden ausschließlich lokal auf deinem Gerät gespeichert und beim Löschen der App entfernt.</p>
<h3>Kein Tracking</h3>
<p>Die App enthält keine Werbung, keine Analyse- oder Tracking-Werkzeuge und keine Software-Bausteine von Drittanbietern. Wenn du in iOS zugestimmt hast, Analysedaten mit App-Entwicklern zu teilen, kann Apple dem Entwickler anonymisierte Absturzberichte bereitstellen; das steuerst du ausschließlich in deinen iOS-Einstellungen.</p>

<h2>3. Diese Website</h2>
<p>Diese Website wird über GitHub Pages bereitgestellt, einen Dienst der GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, USA. Beim Aufruf verarbeitet GitHub technische Daten wie deine IP-Adresse, um die Seiten auszuliefern und den Dienst abzusichern. Dabei können Daten in den USA verarbeitet werden. Details: <a href="https://docs.github.com/de/site-policy/privacy-policies/github-general-privacy-statement">Datenschutzerklärung von GitHub</a>. Rechtsgrundlage ist unser berechtigtes Interesse an einer sicheren Bereitstellung der Website (Art. 6 Abs. 1 lit. f DSGVO).</p>
<p>Die Website selbst verwendet keine Cookies, kein Tracking, keine Analyse, kein JavaScript und keine externen Schriftarten oder Inhalte Dritter.</p>
<p>Wenn du uns per E-Mail kontaktierst, verwenden wir deine Nachricht nur zur Beantwortung und löschen sie, sobald sie nicht mehr benötigt wird.</p>

<h2>4. Deine Rechte</h2>
<p>Nach der DSGVO hast du das Recht auf Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung, Datenübertragbarkeit und Widerspruch. Schreib dafür einfach eine E-Mail. Außerdem hast du das Recht, dich bei einer Datenschutz-Aufsichtsbehörde zu beschweren.</p>

<h2>5. Änderungen</h2>
<p>Wenn sich die App oder diese Website so ändern, dass deine Daten betroffen sind, wird diese Erklärung entsprechend angepasst.</p>
"""


def legal(t, title, body, canonical, alt_en, alt_de):
    html = head(t, f"{title} – Route2Charge", t["description"], canonical, alt_en, alt_de)
    html += header(t, t["other_privacy"], show_nav=False)
    html += f"""<main id="main" class="legal">
  <div class="wrap">
    <a href="{t['home']}">{t['back']}</a>
    <h1>{title}</h1>
{body}
  </div>
</main>
"""
    html += footer(t)
    return html


def help_page(t, canonical, alt_en, alt_de):
    subject = "Route2Charge%20Feedback"
    faq = "\n".join(
        f"""<details class="faq"><summary>{q}</summary><p>{a}</p></details>""" for q, a in t["faq"]
    )
    html = head(t, f"{t['nav_help']} – Route2Charge", t["description"], canonical, alt_en, alt_de)
    html += header(t, t["other_help"], show_nav=False)
    html += f"""<main id="main" class="legal">
  <div class="wrap">
    <a href="{t['home']}">{t['back']}</a>
    <h1>{t['help_title']}</h1>
    <p class="lead">{t['help_lead']}</p>
    <div class="contact-card">
      <h2>{t['contact_h']}</h2>
      <p><a class="mail" href="mailto:{EMAIL}?subject={subject}">{EMAIL}</a></p>
      <p class="meta">{t['contact_text']}</p>
      <p><a class="btn btn-primary" href="mailto:{EMAIL}?subject={subject}">{t['contact_btn']}</a></p>
    </div>
    <h2>{t['faq_h']}</h2>
{faq}
  </div>
</main>
"""
    html += footer(t)
    return html


def not_found():
    t = TEXT["en"]
    html = head(t, "404 – Route2Charge", t["description"], "404.html", "", "de/")
    html = html.replace('href="assets/', f'href="{SITE_URL}/assets/')
    html += f"""<main id="main" class="notfound">
  <div class="wrap">
    <h1>404</h1>
    <p>{TEXT['en']['nf_text']}<br>{TEXT['de']['nf_text']}</p>
    <p><a class="btn btn-primary" href="{SITE_URL}/">Route2Charge</a></p>
  </div>
</main>
</body>
</html>
"""
    return html


def write(rel, content):
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print("geschrieben:", rel)


if __name__ == "__main__":
    write("index.html", landing(TEXT["en"]))
    write("de/index.html", landing(TEXT["de"]))
    write("privacy.html", legal(TEXT["en"], "Privacy policy", PRIVACY_EN, "privacy.html", "privacy.html", "de/datenschutz.html"))
    write("de/datenschutz.html", legal(TEXT["de"], "Datenschutzerklärung", PRIVACY_DE, "de/datenschutz.html", "privacy.html", "de/datenschutz.html"))
    write("help.html", help_page(TEXT["en"], "help.html", "help.html", "de/hilfe.html"))
    write("de/hilfe.html", help_page(TEXT["de"], "de/hilfe.html", "help.html", "de/hilfe.html"))
    write("404.html", not_found())
