# Bärn hilft

Eine Seite, ein Zweck: wenn jemand in Bern zusammenbricht, soll das Telefon in der Hand
den Takt geben und sagen, was zu tun ist. Ohne App, ohne Konto, ohne Tracking.

Live: https://claude.ai/artifact/BGbdRF2PYbgn2tzojxHJPZ (privat, bis der Besitzer sie teilt)

## Was die Seite kann

- **144 gross und kopierbar** mit dem Satz, den die Notrufzentrale braucht (WO zuerst).
- **Reanimations-Metronom**: 110 Schläge pro Minute (ERC 2021: 100–120), Zähler 1–30,
  Modus «30 Drücken : 2 Beatmen» mit 5-Sekunden-Beatmungsfenster oder «Nur Drücken».
  Ton (WebAudio), Vibration wo möglich, Bildschirm bleibt an (Wake Lock, wo erlaubt),
  Zeit und Gesamtzahl der Drücke, Hinweis zum Abwechseln alle 2 Minuten, AED-Hinweis.
- **Vier Schritte** der Basisreanimation nach ERC 2021.
- **Fünf Kurzanleitungen**: bewusstlos aber atmend (Seitenlage), Ersticken (5 Schläge / 5 Stösse),
  Schlaganfall (Gesicht, Arme, Sprache, Zeit), Herzinfarkt, starke Blutung.
- **Schweizer Notrufnummern**: 144, 112, 117, 118, 145, 1414, 143, 147.
- **Vier Sprachen**: DE (Schweizer Schreibweise, kein ß), FR, IT, EN. Sprache wird nur
  lokal im Gerät gemerkt.

## Quellen der Inhalte

Basic Life Support nach European Resuscitation Council Guidelines 2021, in der Schweiz vom
Swiss Resuscitation Council (SRC) angewendet: Frequenz 100–120/min, Tiefe 5–6 cm,
Verhältnis 30:2, Atemkontrolle höchstens 10 s, Beatmungspause unter 10 s, AED sofort wenn
verfügbar, Helferwechsel alle 2 min. Ersticken: 5 Rückenschläge / 5 Oberbauchstösse
abwechselnd, bei Bewusstlosigkeit Reanimation. Schlaganfall: FAST-Schema.

Die Seite ersetzt keinen Kurs. Kurse: https://www.resuscitation.ch · nächster AED: https://www.defikarte.ch

## Technik

Eine Datei, `index.html`, ohne Build und ohne externe Skripte. Einzige externe Ressource
sind zwei Schriften von Google Fonts (Atkinson Hyperlegible für Lesbarkeit unter Stress,
Archivo Black für die Zahlen), mit System-Fallback. Alles andere ist inline.
Dark Mode folgt dem Gerät. Texte werden ausschliesslich über `textContent` gesetzt.

## Für eine andere Stadt anpassen

1. Notrufnummern im Objekt `I18N[lang].nums` ändern (und 144 im Anruf-Block, falls anders).
2. `tagline`, `call_where` und den Titel anpassen.
3. Fertig. Lizenz: frei nutzbar (CC0). Keine Gewähr, siehe Fusszeile der Seite.

## Offen

- Karte «nächster Defibrillator / Trinkwasserbrunnen / WC» für Bern aus OpenStreetMap:
  braucht Zugriff auf `overpass-api.de` beim Bauen (im Erstellungs-Container gesperrt).
  Die Daten würden statisch in die Seite eingebettet, damit sie offline funktioniert.
- Ein öffentliches Git-Repository, damit andere Städte forken können.
