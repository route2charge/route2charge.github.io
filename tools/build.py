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
# Postanschrift für das Impressum (mehrzeilig mit \n). Leer = kein Impressum.
ADDRESS = ""
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

ICON_PLUG = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2" '
             'stroke-linecap="round" stroke-linejoin="round" d="M9 3v4m6-4v4M6.5 7h11v3.5a5.5 5.5 0 0 1-11 0zM12 16v5"/></svg>')
ICON_HIDE = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2" '
             'stroke-linecap="round" stroke-linejoin="round" d="M3 12s3.5-6.5 9-6.5S21 12 21 12s-3.5 6.5-9 6.5S3 12 3 12z'
             'M12 9.2a2.8 2.8 0 1 0 0 5.6 2.8 2.8 0 0 0 0-5.6M4 20 20 4"/></svg>')
ICON_DETOUR = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2" '
               'stroke-linecap="round" d="M5 19V9a4 4 0 0 1 8 0v6a4 4 0 0 0 6 0V5"/><circle cx="5" cy="19" r="2" '
               'fill="currentColor"/><circle cx="19" cy="5" r="2" fill="currentColor"/></svg>')
ICON_SHIELD = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2" '
               'stroke-linejoin="round" d="M12 3 5 6v5.5c0 4.4 3 8 7 9.5 4-1.5 7-5.1 7-9.5V6z"/><path fill="none" '
               'stroke="currentColor" stroke-width="2" stroke-linecap="round" d="M9 12h6"/></svg>')
ICON_FLAG = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2" '
             'stroke-linecap="round" stroke-linejoin="round" d="M5 21V4m0 0h11l-2 4 2 4H5"/></svg>')
ICON_NEXT = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2" '
             'stroke-linecap="round" stroke-linejoin="round" d="M4 12h13m-5-6 6 6-6 6"/><path fill="currentColor" '
             'd="M20 5h2v14h-2z"/></svg>')
ICON_LOCK = ('<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="5" y="10.5" width="14" height="10" rx="2.5" '
             'fill="none" stroke="currentColor" stroke-width="2"/><path fill="none" stroke="currentColor" stroke-width="2" '
             'd="M8.5 10.5V8a3.5 3.5 0 0 1 7 0v2.5"/></svg>')
ICON_GEAR = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2" '
             'stroke-linecap="round" d="M4 6h16M4 12h16M4 18h16"/><circle cx="9" cy="6" r="2.4" fill="#06090d" '
             'stroke="currentColor" stroke-width="2"/><circle cx="15.5" cy="12" r="2.4" fill="#06090d" stroke="currentColor" '
             'stroke-width="2"/><circle cx="7" cy="18" r="2.4" fill="#06090d" stroke="currentColor" stroke-width="2"/></svg>')

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
            ("Can I also see regular 11 or 22 kW chargers?", "Yes. In the settings, set the minimum power to 11 or 22&nbsp;kW and switch off “CCS plug only”. These Type&nbsp;2 chargers are marked in the results – they charge much more slowly than fast chargers."),
            ("Is the app available in English?", "Yes. Route2Charge follows your iPhone’s language: German or English."),
        ],
        "skip": "Skip to content",
        "eyebrow": "No account · No tracking · No ads",
        "h1": '150&nbsp;km left? <span class="glow">Your 2 best charging stops.</span>',
        "lead": "Tell Route2Charge where you’re going and how far you can still drive. It shows the two best fast chargers along your route – right before your range runs low.",
        "cta": "See how it works",
        "soon": "Coming soon to the App Store",
        "facts": ["Germany &amp; Europe", "CCS fast chargers", "Built for iPhone"],
        "hero_img": "route-en.jpg",
        "hero_alt": "Route2Charge on iPhone: a route from Munich to Bitterfeld with the charging window highlighted in green and two recommended chargers.",
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
            ("assets/screens/route-en.jpg", "Route and charging window at a glance", "The map shows the route, the green charging window and both recommended chargers."),
            ("assets/screens/stops-en.jpg", "Your two best stops – plus more options", "List of the two recommended chargers with power, charge points, detour and remaining range, followed by further options from other networks."),
            ("assets/screens/trip-en.jpg", "The whole trip with your charging stop", "Map of the full trip from start via the charging station to the destination, with total distance, driving time and range on arrival."),
        ],
        "nav_opts": "Options",
        "opt_kicker": "Make it yours",
        "opt_h2": "Your car. Your rules.",
        "opt_p": "Enter your range the way your car shows it – and set once what a good charger means to you.",
        "range_h": "Range – the way your car shows it",
        "modes": [
            ("km", "Range", "150&nbsp;km", "Type in the remaining range from your dashboard – anywhere from 10 to 600&nbsp;km."),
            ("pct", "Battery %", "35&nbsp;%", "Enter your battery level. With your battery size and consumption, Route2Charge works out the range."),
            ("at", "At km", "km&nbsp;150", "You know where you want to stop? Pick the kilometre on your route and get the best chargers up to 20&nbsp;km before or after it."),
        ],
        "extras": [
            ("shield", "Safety buffer", "Keep 0–100&nbsp;km in reserve – 20&nbsp;km by default. Your stops always come before it."),
            ("flag", "No stop needed?", "Then the app tells you – including the range left when you arrive."),
            ("next", "After charging", "Continue to your destination or search for the next stop from the charger – with your new range in km or %."),
        ],
        "set_h": "Settings – set once, done",
        "settings": [
            ("bolt", "Minimum power", "11, 22, 50, 100 or 150&nbsp;kW – only chargers at least this fast make the cut. 50&nbsp;kW by default."),
            ("plug", "CCS only", "The fast-charging plug of almost every EV in Europe. Switch it off to also see regular Type&nbsp;2 chargers with 11 or 22&nbsp;kW."),
            ("hide", "Hide Tesla Superchargers", "Often pricier for other cars or only usable with the Tesla app – one switch and they’re gone."),
            ("detour", "Max. distance from the route", "0.5 to 10&nbsp;km. Stay right on the motorway or allow a short hop for a better charger."),
            ("battery", "Battery &amp; consumption", "Usable capacity and average consumption – used for battery % mode."),
        ],
        "set_note": "All settings are stored on your iPhone only.",
        "opt_shots": [
            ("input-en.jpg", "Route2Charge on iPhone: route from Munich to Bitterfeld, range options Range, Battery % and At km, remaining range 150 km and a 20 km safety buffer."),
            ("settings-en.jpg", "Route2Charge settings: minimum power, CCS only, hide Tesla Superchargers, maximum distance from the route, battery size and consumption."),
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
            ("Kann ich auch normale 11- oder 22-kW-Lader sehen?", "Ja. In den Einstellungen die Mindestleistung auf 11 oder 22&nbsp;kW stellen und „Nur CCS-Stecker“ ausschalten. Diese Typ-2-Lader sind in den Ergebnissen markiert – sie laden deutlich langsamer als Schnelllader."),
            ("Gibt es die App auch auf Englisch?", "Ja. Route2Charge richtet sich nach der Sprache deines iPhones: Deutsch oder Englisch."),
        ],
        "skip": "Zum Inhalt springen",
        "eyebrow": "Ohne Account · Ohne Tracking · Ohne Werbung",
        "h1": 'Noch 150&nbsp;km? <span class="glow">Deine 2 besten Ladestopps.</span>',
        "lead": "Sag Route2Charge, wohin du fährst und wie weit du noch kommst. Die App zeigt dir die zwei besten Schnelllader auf deiner Route – kurz bevor es knapp wird.",
        "cta": "So funktioniert’s",
        "soon": "Bald im App Store",
        "facts": ["Deutschland &amp; Europa", "CCS-Schnelllader", "Für iPhone"],
        "hero_img": "route.jpg",
        "hero_alt": "Route2Charge auf dem iPhone: Route von München nach Bitterfeld mit grün markiertem Ladefenster und zwei empfohlenen Ladesäulen.",
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
        "nav_opts": "Optionen",
        "opt_kicker": "Einstellbar",
        "opt_h2": "Dein Auto. Deine Regeln.",
        "opt_p": "Gib die Reichweite so ein, wie dein Auto sie anzeigt – und leg einmal fest, was für dich eine gute Ladesäule ist.",
        "range_h": "Reichweite – so, wie dein Auto sie zeigt",
        "modes": [
            ("km", "Reichweite", "150&nbsp;km", "Restreichweite vom Display ablesen und eintragen – von 10 bis 600&nbsp;km."),
            ("pct", "Akku %", "35&nbsp;%", "Akkustand eingeben. Mit Akkugröße und Verbrauch rechnet Route2Charge die Reichweite aus."),
            ("at", "Bei km", "km&nbsp;150", "Du weißt schon, wo du laden willst? Kilometer auf der Route wählen – und die besten Säulen bis 20&nbsp;km davor oder danach bekommen."),
        ],
        "extras": [
            ("shield", "Sicherheitspuffer", "0 bis 100&nbsp;km Reserve – standardmäßig 20&nbsp;km. Deine Stopps liegen immer davor."),
            ("flag", "Kein Stopp nötig?", "Dann sagt dir die App das – samt Reichweite bei Ankunft."),
            ("next", "Nach dem Laden", "Weiter zum Ziel oder ab der Säule den nächsten Stopp suchen – mit neuer Reichweite in km oder %."),
        ],
        "set_h": "Einstellungen – einmal setzen, fertig",
        "settings": [
            ("bolt", "Mindestleistung", "11, 22, 50, 100 oder 150&nbsp;kW – nur so schnelle Säulen kommen in Frage. Standard: 50&nbsp;kW."),
            ("plug", "Nur CCS-Stecker", "Der Schnellladestecker fast aller E-Autos in Europa. Ausschalten, um auch normale Typ-2-Lader mit 11 oder 22&nbsp;kW zu sehen."),
            ("hide", "Tesla Supercharger ausblenden", "Für andere Autos oft teurer oder nur mit der Tesla-App nutzbar – ein Schalter, und sie sind weg."),
            ("detour", "Max. Abstand zur Route", "0,5 bis 10&nbsp;km. Direkt an der Autobahn bleiben oder für eine bessere Säule kurz abfahren."),
            ("battery", "Akku &amp; Verbrauch", "Nutzbare Kapazität und Durchschnittsverbrauch – für den Modus „Akku %“."),
        ],
        "set_note": "Alle Einstellungen bleiben nur auf deinem iPhone.",
        "opt_shots": [
            ("input.jpg", "Route2Charge auf dem iPhone: Route von München nach Bitterfeld, Reichweiten-Modi Reichweite, Akku % und Bei km, Restreichweite 150 km und 20 km Sicherheitspuffer."),
            ("settings.jpg", "Einstellungen von Route2Charge: Mindestleistung, nur CCS-Stecker, Tesla Supercharger ausblenden, maximaler Abstand zur Route, Akkugröße und Verbrauch."),
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
      <a class="hide-md" href="#options">{t['nav_opts']}</a>
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
    imprint = ""
    if ADDRESS.strip():
        imprint = f"""<a href="{IMPRINT[t['lang']]['file']}">{IMPRINT[t['lang']]['title']}</a>
        """
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="footer-top">
      <span>© 2026 {OWNER} · {t['footer_note']}</span>
      <nav class="footer-links" aria-label="Footer">
        <a href="{t['help_file']}">{t['help']}</a>
        <a href="{t['privacy_file']}">{t['privacy']}</a>
        <a href="{TECH[t['lang']]['file']}">{TECH[t['lang']]['title']}</a>
        {imprint}        <a href="mailto:{EMAIL}">{t['contact']}</a>
        <a href="{t['other_home']}" hreflang="{'de' if t['lang']=='en' else 'en'}">{t['other_name']}</a>
      </nav>
    </div>
    <p class="credits">{t['credits']}</p>
  </div>
</footer>
</body>
</html>
"""


OPT_ICONS = {
    "shield": ICON_SHIELD, "flag": ICON_FLAG, "next": ICON_NEXT, "bolt": ICON_BOLT,
    "plug": ICON_PLUG, "hide": ICON_HIDE, "detour": ICON_DETOUR, "battery": ICON_BATTERY,
}


def options_section(t):
    p = t["prefix"]
    modes = "\n".join(
        f"""<article class="mode mode-{key}"><span class="mode-tag">{tag}</span><div class="mode-val">{val}</div>"""
        f"""<span class="meter" aria-hidden="true"><i></i></span><p>{d}</p></article>"""
        for key, tag, val, d in t["modes"]
    )
    extras = "\n".join(
        f"""<li>{OPT_ICONS[k]}<div><strong>{h}</strong><span>{d}</span></div></li>""" for k, h, d in t["extras"]
    )
    settings = "\n".join(
        f"""<li>{OPT_ICONS[k]}<div><strong>{h}</strong><span>{d}</span></div></li>""" for k, h, d in t["settings"]
    )
    (in_src, in_alt), (set_src, set_alt) = t["opt_shots"]
    return f"""<section id="options" class="options-section">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">{t['opt_kicker']}</span>
      <h2>{t['opt_h2']}</h2>
      <p>{t['opt_p']}</p>
    </div>
    <div class="opt-row">
      <div class="opt-text">
        <h3 class="opt-h">{ICON_BATTERY}{t['range_h']}</h3>
        <div class="modes">
{modes}
        </div>
        <ul class="checklist compact">
{extras}
        </ul>
      </div>
      <div class="opt-phone"><div class="phone"><img src="{p}assets/screens/{in_src}" alt="{in_alt}" width="1206" height="2622" loading="lazy"></div></div>
    </div>
    <div class="opt-row opt-row-rev">
      <div class="opt-text">
        <h3 class="opt-h">{ICON_GEAR}{t['set_h']}</h3>
        <ul class="checklist compact">
{settings}
        </ul>
        <p class="opt-note">{ICON_LOCK}{t['set_note']}</p>
      </div>
      <div class="opt-phone"><div class="phone"><img src="{p}assets/screens/{set_src}" alt="{set_alt}" width="1206" height="2622" loading="lazy"></div></div>
    </div>
  </div>
</section>
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
    <div class="phone"><img src="{p}assets/screens/{t['hero_img']}" alt="{t['hero_alt']}" width="1206" height="2622"></div>
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

{options_section(t)}
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
<p>If you contact us by e-mail, we use your message only to answer it and delete it when it is no longer needed. E-mails are received via Proton Mail (Proton AG, Switzerland), which stores them encrypted. The legal basis is Art. 6(1)(f) GDPR.</p>
<p>An overview of every service and tool involved – and which data each one sees – is on the page <a href="legal.html">Technology &amp; legal</a>.</p>

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
<p>Wenn du uns per E-Mail kontaktierst, verwenden wir deine Nachricht nur zur Beantwortung und löschen sie, sobald sie nicht mehr benötigt wird. E-Mails empfangen wir über Proton Mail (Proton AG, Schweiz), dort werden sie verschlüsselt gespeichert. Rechtsgrundlage ist Art. 6 Abs. 1 lit. f DSGVO.</p>
<p>Eine Übersicht aller beteiligten Dienste und Werkzeuge – und welche Daten jeder sieht – findest du auf der Seite <a href="technik-recht.html">Technik &amp; Recht</a>.</p>

<h2>4. Deine Rechte</h2>
<p>Nach der DSGVO hast du das Recht auf Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung, Datenübertragbarkeit und Widerspruch. Schreib dafür einfach eine E-Mail. Außerdem hast du das Recht, dich bei einer Datenschutz-Aufsichtsbehörde zu beschweren.</p>

<h2>5. Änderungen</h2>
<p>Wenn sich die App oder diese Website so ändern, dass deine Daten betroffen sind, wird diese Erklärung entsprechend angepasst.</p>
"""


# ---------------------------------------------------------------------------
# Technik & Recht: alle Werkzeuge, Dienste, Lizenzen und rechtlichen Hinweise
# Aufbau je Eintrag: (Name, Anbieter, wofür, welche Daten)
TECH = {
    "en": {
        "file": "legal.html",
        "title": "Technology &amp; legal",
        "lead": "Everything Route2Charge is built with and runs on – which company is behind each part, what it does and which data it sees. Plus licences, disclaimer and trademarks.",
        "summary": "<strong>In short:</strong> Route2Charge is an independent project by {owner}. The app has no server of its own, no account and no tracking. It talks to exactly two services: Apple Maps and Open Charge Map. This website is plain HTML and CSS on GitHub Pages – no JavaScript, no cookies.",
        "data_label": "Data",
        "who_h": "Who is behind Route2Charge",
        "who": "Developer and contact: {owner}, e-mail <a href=\"mailto:{email}\">{email}</a>. Route2Charge is not affiliated with Apple, Tesla, Open Charge Map or any charging network.",
        "imprint_link": "Legal notice (Impressum) →",
        "app_h": "The app",
        "app_p": "Requires an iPhone with iOS 17 or later. Written in Swift.",
        "app": [
            ("Swift &amp; SwiftUI", "Apple", "Programming language and user interface.", "Runs on your iPhone only – no data leaves the device."),
            ("Apple Maps (MapKit)", "Apple Inc.", "Map, place search, routes and detour calculation.", "Search terms, start, destination and the positions of suggested chargers are sent to Apple. <a href=\"https://www.apple.com/legal/privacy/\">Apple privacy policy</a>"),
            ("Open Charge Map API", "Open Charge Map (community project)", "Charging station data: location, power, plugs, operator.", "Only small rectangular map areas around your charging window and the minimum power. Never your start, destination or route; no device ID. Your IP address is technically transmitted. <a href=\"https://openchargemap.org\">openchargemap.org</a>"),
            ("Core Location", "Apple", "Your current location – only if you start “from here”, once per search, and to notice when you have arrived at the charger.", "Stays on your iPhone; passed to Apple Maps for routing. Never stored, never sent to us."),
            ("UserDefaults (iOS)", "Apple", "Stores your settings such as battery size or minimum power.", "Only on your iPhone. Deleted together with the app."),
            ("Mail app (iOS)", "Apple or your mail provider", "Feedback – only when you tap “Report a bug”.", "Whatever you write; app and iOS version are visible in the message and can be deleted before sending."),
        ],
        "app_none": "Not included: analytics, crash-reporting SDKs, advertising, tracking, third-party libraries or a server of our own.",
        "web_h": "This website",
        "web": [
            ("GitHub Pages", "GitHub, Inc. (USA)", "Hosting of this website.", "Your IP address and technical request data are processed by GitHub to deliver the pages. <a href=\"https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement\">GitHub Privacy Statement</a>"),
            ("HTML &amp; CSS", "Built in-house", "The pages are plain, static HTML and CSS, generated by a small Python script.", "No JavaScript, no cookies, no external fonts, no third-party content. A Content Security Policy blocks scripts and foreign content."),
        ],
        "web_src": "The website’s source code is public: <a href=\"https://github.com/route2charge/route2charge.github.io\">github.com/route2charge/route2charge.github.io</a>",
        "mail_h": "Contact by e-mail",
        "mail": [
            ("Proton Mail", "Proton AG (Switzerland)", "Receives e-mails sent to {email}.", "Your e-mail address and message. Used only to reply and deleted when no longer needed. <a href=\"https://proton.me/legal/privacy\">Proton privacy policy</a>"),
        ],
        "dev_h": "Development tools",
        "dev_p": "Used to build the app and the website. They never see any data from users.",
        "dev": [
            ("Xcode, Simulator &amp; Swift Testing", "Apple", "Building, testing and screenshots."),
            ("XcodeGen", "Open source (MIT licence)", "Generates the Xcode project from a short text file."),
            ("Git &amp; GitHub", "GitHub, Inc.", "Version control; the app’s source code is kept in a private repository."),
            ("Python &amp; Playwright", "Open source", "Builds this website and checks how it looks on different screens."),
            ("Claude", "Anthropic", "AI assistant used for programming, texts and design."),
        ],
        "lic_h": "Licences &amp; sources",
        "lic": [
            "Charging station data © Open Charge Map contributors and data providers, licensed under <a href=\"https://creativecommons.org/licenses/by/4.0/\">CC BY 4.0</a>. The app names the data provider for each recommended charger.",
            "Maps, routes and place search: Apple Maps. The map’s own legal notice can be opened in the app from the map (“Legal”).",
            "Icons in the app: SF Symbols by Apple, used under Apple’s licence for apps on Apple platforms.",
            "App icon, logo, website design and texts: © 2026 {owner}.",
        ],
        "disc_h": "Disclaimer",
        "disc": [
            "All information is provided without guarantee. Charging station data comes from a community database and its providers – a charger may be occupied, out of order, closed, or have different power, access rules or prices.",
            "Range and arrival estimates are approximations. Temperature, speed, elevation and your driving style change your real range. Always keep a reserve – that’s what the safety buffer is for.",
            "Please don’t operate your phone while driving. Plan your stop before you set off or let a passenger do it.",
            "We are not responsible for the content of external websites we link to.",
        ],
        "tm_h": "Trademarks",
        "tm": "Apple, iPhone, Apple Maps, App Store, Xcode, Swift and SwiftUI are trademarks of Apple Inc. Tesla and Supercharger are trademarks of Tesla, Inc. GitHub is a trademark of GitHub, Inc. Proton and Proton Mail are trademarks of Proton AG. Claude is a trademark of Anthropic, PBC. All other names belong to their respective owners. Their use here only describes compatibility or the services used.",
        "sec_h": "Security",
        "sec": [
            "No account means there is nothing to sign in to and no user data with us that could leak.",
            "All connections of the app and this website are encrypted (HTTPS).",
            "Secret keys are not part of any public source code.",
            "Found a security issue? Please write to <a href=\"mailto:{email}\">{email}</a> – thank you!",
        ],
    },
    "de": {
        "file": "technik-recht.html",
        "title": "Technik &amp; Recht",
        "lead": "Alles, womit Route2Charge gebaut ist und worauf es läuft – welche Firma dahintersteht, wofür es da ist und welche Daten es sieht. Dazu Lizenzen, Haftungsausschluss und Marken.",
        "summary": "<strong>Kurz gesagt:</strong> Route2Charge ist ein unabhängiges Projekt von {owner}. Die App hat keinen eigenen Server, keinen Account und kein Tracking. Sie spricht mit genau zwei Diensten: Apple Karten und Open Charge Map. Diese Website ist reines HTML und CSS auf GitHub Pages – ohne JavaScript, ohne Cookies.",
        "data_label": "Daten",
        "who_h": "Wer steckt hinter Route2Charge",
        "who": "Entwickler und Kontakt: {owner}, E-Mail <a href=\"mailto:{email}\">{email}</a>. Route2Charge ist weder mit Apple, Tesla oder Open Charge Map noch mit einem Ladenetz verbunden.",
        "imprint_link": "Impressum →",
        "app_h": "Die App",
        "app_p": "Läuft auf dem iPhone ab iOS 17. Geschrieben in Swift.",
        "app": [
            ("Swift &amp; SwiftUI", "Apple", "Programmiersprache und Benutzeroberfläche.", "Läuft nur auf deinem iPhone – keine Daten verlassen das Gerät."),
            ("Apple Karten (MapKit)", "Apple Inc.", "Karte, Ortssuche, Routen und Umweg-Berechnung.", "Suchbegriffe, Start, Ziel und die Positionen vorgeschlagener Ladesäulen gehen an Apple. <a href=\"https://www.apple.com/de/legal/privacy/\">Datenschutzrichtlinie von Apple</a>"),
            ("Open Charge Map API", "Open Charge Map (Community-Projekt)", "Ladesäulen-Daten: Ort, Leistung, Stecker, Betreiber.", "Nur kleine rechteckige Kartenausschnitte rund um dein Ladefenster und die Mindestleistung. Nie Start, Ziel oder Route, keine Gerätekennung. Technisch wird deine IP-Adresse übertragen. <a href=\"https://openchargemap.org\">openchargemap.org</a>"),
            ("Core Location", "Apple", "Dein aktueller Standort – nur wenn du „ab hier“ startest, einmal pro Suche, und um zu merken, dass du an der Säule angekommen bist.", "Bleibt auf dem iPhone, geht für die Route an Apple Karten. Nie gespeichert, nie an uns übertragen."),
            ("UserDefaults (iOS)", "Apple", "Speichert deine Einstellungen wie Akkugröße oder Mindestleistung.", "Nur auf deinem iPhone. Wird mit der App gelöscht."),
            ("Mail-App (iOS)", "Apple bzw. dein Mail-Anbieter", "Feedback – nur wenn du auf „Fehler melden“ tippst.", "Was du schreibst; App- und iOS-Version stehen sichtbar in der Mail und können vor dem Senden gelöscht werden."),
        ],
        "app_none": "Nicht enthalten: Analyse-Tools, Absturz-SDKs, Werbung, Tracking, Bibliotheken von Drittanbietern oder ein eigener Server.",
        "web_h": "Diese Website",
        "web": [
            ("GitHub Pages", "GitHub, Inc. (USA)", "Hosting dieser Website.", "Deine IP-Adresse und technische Abrufdaten verarbeitet GitHub, um die Seiten auszuliefern. <a href=\"https://docs.github.com/de/site-policy/privacy-policies/github-general-privacy-statement\">Datenschutzerklärung von GitHub</a>"),
            ("HTML &amp; CSS", "Eigenbau", "Die Seiten sind reines, statisches HTML und CSS, erzeugt von einem kleinen Python-Skript.", "Kein JavaScript, keine Cookies, keine externen Schriften, keine Inhalte Dritter. Eine Content Security Policy blockiert Skripte und fremde Inhalte."),
        ],
        "web_src": "Der Quellcode der Website ist öffentlich: <a href=\"https://github.com/route2charge/route2charge.github.io\">github.com/route2charge/route2charge.github.io</a>",
        "mail_h": "Kontakt per E-Mail",
        "mail": [
            ("Proton Mail", "Proton AG (Schweiz)", "Empfängt E-Mails an {email}.", "Deine E-Mail-Adresse und Nachricht. Nur zur Antwort genutzt und gelöscht, sobald nicht mehr nötig. <a href=\"https://proton.me/de/legal/privacy\">Datenschutzerklärung von Proton</a>"),
        ],
        "dev_h": "Entwicklungswerkzeuge",
        "dev_p": "Damit werden App und Website gebaut. Sie sehen nie Daten von Nutzern.",
        "dev": [
            ("Xcode, Simulator &amp; Swift Testing", "Apple", "Bauen, Testen und Screenshots."),
            ("XcodeGen", "Open Source (MIT-Lizenz)", "Erzeugt das Xcode-Projekt aus einer kurzen Textdatei."),
            ("Git &amp; GitHub", "GitHub, Inc.", "Versionsverwaltung; der Quellcode der App liegt in einem privaten Repository."),
            ("Python &amp; Playwright", "Open Source", "Bauen diese Website und prüfen, wie sie auf verschiedenen Bildschirmen aussieht."),
            ("Claude", "Anthropic", "KI-Assistent für Programmierung, Texte und Design."),
        ],
        "lic_h": "Lizenzen &amp; Quellen",
        "lic": [
            "Ladesäulen-Daten © Open Charge Map und Datenlieferanten, Lizenz <a href=\"https://creativecommons.org/licenses/by/4.0/deed.de\">CC BY 4.0</a>. Die App nennt bei jeder empfohlenen Säule den Datenlieferanten.",
            "Karten, Routen und Ortssuche: Apple Karten. Die rechtlichen Hinweise der Karte lassen sich in der App direkt auf der Karte öffnen („Rechtliches“).",
            "Symbole in der App: SF Symbols von Apple, genutzt im Rahmen der Apple-Lizenz für Apps auf Apple-Plattformen.",
            "App-Icon, Logo, Website-Design und Texte: © 2026 {owner}.",
        ],
        "disc_h": "Haftungsausschluss",
        "disc": [
            "Alle Angaben ohne Gewähr. Die Ladesäulen-Daten stammen aus einer Community-Datenbank und von deren Lieferanten – eine Säule kann belegt, defekt oder geschlossen sein oder andere Leistung, Zugangsregeln oder Preise haben.",
            "Reichweite und Ankunftswerte sind Schätzungen. Temperatur, Tempo, Höhenmeter und Fahrstil verändern die echte Reichweite. Plane immer eine Reserve ein – dafür gibt es den Sicherheitspuffer.",
            "Bitte bediene das Handy nicht während der Fahrt. Plane den Stopp vor dem Losfahren oder lass Beifahrer tippen.",
            "Für Inhalte externer Websites, auf die wir verlinken, sind deren Betreiber verantwortlich.",
        ],
        "tm_h": "Marken",
        "tm": "Apple, iPhone, Apple Karten, App Store, Xcode, Swift und SwiftUI sind Marken der Apple Inc. Tesla und Supercharger sind Marken der Tesla, Inc. GitHub ist eine Marke der GitHub, Inc. Proton und Proton Mail sind Marken der Proton AG. Claude ist eine Marke der Anthropic, PBC. Alle anderen Namen gehören ihren jeweiligen Inhabern. Sie werden hier nur genannt, um Kompatibilität oder genutzte Dienste zu beschreiben.",
        "sec_h": "Sicherheit",
        "sec": [
            "Kein Account heißt: Es gibt keine Anmeldung und bei uns keine Nutzerdaten, die abhandenkommen könnten.",
            "Alle Verbindungen von App und Website sind verschlüsselt (HTTPS).",
            "Geheime Schlüssel sind nicht Teil von öffentlichem Quellcode.",
            "Sicherheitslücke gefunden? Bitte schreib an <a href=\"mailto:{email}\">{email}</a> – danke!",
        ],
    },
}

# Impressum: wird erst erzeugt und verlinkt, wenn ADDRESS ausgefüllt ist
IMPRINT = {
    "en": {"file": "imprint.html", "title": "Legal notice",
           "body": "<p>Information pursuant to § 5 DDG (German Digital Services Act)</p><p>{owner}<br>{address}</p><h2>Contact</h2><p>E-mail: <a href=\"mailto:{email}\">{email}</a></p><h2>Responsible for content</h2><p>{owner}, address as above</p>"},
    "de": {"file": "impressum.html", "title": "Impressum",
           "body": "<p>Angaben gemäß § 5 DDG</p><p>{owner}<br>{address}</p><h2>Kontakt</h2><p>E-Mail: <a href=\"mailto:{email}\">{email}</a></p><h2>Verantwortlich für den Inhalt nach § 18 Abs. 2 MStV</h2><p>{owner}, Anschrift wie oben</p>"},
}


def fill(text):
    return text.format(owner=OWNER, email=EMAIL, address=ADDRESS.replace("\n", "<br>"))


def tool_cards(items, data_label):
    out = []
    for item in items:
        name, vendor, what = item[:3]
        data = f'<p class="tool-data"><b>{data_label}:</b> {fill(item[3])}</p>' if len(item) > 3 else ""
        out.append(f"""<div class="tool"><h3>{name} <span>{vendor}</span></h3><p>{fill(what)}</p>{data}</div>""")
    return '<div class="tools">' + "\n".join(out) + "</div>"


def tech_body(lang):
    c = TECH[lang]
    imprint = ""
    if ADDRESS.strip():
        imprint = f'<p><a class="more" href="{IMPRINT[lang]["file"]}">{c["imprint_link"]}</a></p>'
    bullets = lambda items: "<ul>" + "".join(f"<li>{fill(x)}</li>" for x in items) + "</ul>"
    return f"""
<p class="lead">{c['lead']}</p>
<div class="summary"><p>{fill(c['summary'])}</p></div>

<h2>{c['who_h']}</h2>
<p>{fill(c['who'])}</p>
{imprint}
<h2>{c['app_h']}</h2>
<p>{c['app_p']}</p>
{tool_cards(c['app'], c['data_label'])}
<p class="note">{c['app_none']}</p>

<h2>{c['web_h']}</h2>
{tool_cards(c['web'], c['data_label'])}
<p>{c['web_src']}</p>

<h2>{c['mail_h']}</h2>
{tool_cards(c['mail'], c['data_label'])}

<h2>{c['dev_h']}</h2>
<p>{c['dev_p']}</p>
{tool_cards(c['dev'], c['data_label'])}

<h2>{c['lic_h']}</h2>
{bullets(c['lic'])}

<h2>{c['disc_h']}</h2>
{bullets(c['disc'])}

<h2>{c['tm_h']}</h2>
<p>{c['tm']}</p>

<h2>{c['sec_h']}</h2>
{bullets(c['sec'])}
"""


def legal(t, title, body, canonical, alt_en, alt_de, lang_target=None):
    html = head(t, f"{title} – Route2Charge", t["description"], canonical, alt_en, alt_de)
    other = (alt_de if t["lang"] == "en" else "../" + alt_en) if lang_target is None else lang_target
    html += header(t, other, show_nav=False)
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
    write("legal.html", legal(TEXT["en"], TECH["en"]["title"], tech_body("en"), "legal.html", "legal.html", "de/technik-recht.html"))
    write("de/technik-recht.html", legal(TEXT["de"], TECH["de"]["title"], tech_body("de"), "de/technik-recht.html", "legal.html", "de/technik-recht.html"))
    if ADDRESS.strip():
        for lang, other in (("en", "de/impressum.html"), ("de", "../imprint.html")):
            c = IMPRINT[lang]
            rel = c["file"] if lang == "en" else "de/" + c["file"]
            write(rel, legal(TEXT[lang], c["title"], fill(c["body"]), rel, "imprint.html", "de/impressum.html", other))
    write("404.html", not_found())
