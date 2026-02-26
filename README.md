Ein relativ simples Programm

User hat im Menu die Auswahl wie sein Passwort aussehen soll
Dann kann User entscheiden wie sein PW geschützt werden sollen:
- Sehr alt Modisch: gespeichert als PLAIN text
- weniger alt modisch, aber nicht heutiger standard: SHA-256 + SALT
(DO-TO: moderner Techniken einfügen, z.B. scrypt-Funktionen)







wikipedia:

SHA-256 ist eine Hashfunktion.
Eigenschaften:
Wandelt beliebige Eingaben in eine feste Länge um (256 Bit / 64 Hex-Zeichen)
Einwegfunktion:
Hash berechnen: einfach
Original zurückrechnen: praktisch unmöglich
Systeme speichern nicht das Passwort, sondern nur den Hash.

z.B. hello123 --> ef92b778bafe771e89245b89ecbc8a44

Ein Salt ist ein zufälliger Zusatzwert, der vor dem Hashen angehängt wird.
hash = SHA256(salt + password)

Ohne Salt:
Zwei Nutzer mit gleichem Passwort → gleicher Hash
Angreifer können Rainbow Tables verwenden (vorgefertigte Hash-Listen)

Mit Salt:
Jeder Hash ist einzigartig
Vorgefertigte Tabellen funktionieren nicht
Angreifer muss für jeden Nutzer separat brute-forcen






Mein PC schafft fast 5 Millionen-Rechnungen pro Sekunde (deutlich mehr wenn ich den blöden Laufzeit entferne)
"Nur Zahlen" hat 10 Symbole --> 	10⁶ = 1.000.000 --> in 0.2s geknackt
"Zahlen + Kleinbuchstaben" hat 36 Symbole -->	36⁶ ≈ 2,2 Milliarden --> höchsten 5 minuten
+ Großbuchstaben -->	62⁶ ≈ 56 Milliarden --> 4 Stunden
+ Symbole (~80)	--> 80⁶ ≈ 262 Milliarden --> 3 Tage
  (PROBLEM: Mein Rechner hat garnicht den RAM und zweitens ist Python nicht gedacht um solche Hacker Programme zu erstellen --> In C wäre das DEUTLICH effizienter)
