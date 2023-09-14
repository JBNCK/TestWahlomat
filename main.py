# Ein einfacher Wahl-O-Mat in Python

# Die Parteien und ihre Positionen zu 10 Themen
parteien = {
    "AfD": [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
    "CDU": [1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    "SPD": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    "FDP": [0, 0, 0, 0, 1, -1, -1, -1, -1, -1],
    "Grüne": [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    "Linke": [2, 2, 2, 2, -1, -1, -1, -1,-1,-1]
}

# Die Fragen und die möglichen Antworten
fragen = [
    "Sind Sie für eine Erhöhung des Mindestlohns?",
    "Sind Sie für eine stärkere Regulierung des Finanzmarktes?",
    "Sind Sie für eine Erhöhung der Verteidigungsausgaben?",
    "Sind Sie für eine stärkere Zusammenarbeit mit der EU?",
    "Sind Sie für einen schnelleren Ausstieg aus der Kohleenergie?",
    "Sind Sie für eine Legalisierung von Cannabis?",
    "Sind Sie für eine Abschaffung der GEZ-Gebühren?",
    "Sind Sie für eine Verschärfung des Asylrechts?",
    "Sind Sie für eine Einführung einer CO2-Steuer?",
    "Sind Sie für eine Lockerung des Datenschutzes?"
]

antworten = [
    ["Ja", "Nein", "Weiß nicht"],
    ["Ja", "Nein", "Weiß nicht"],
    ["Ja", "Nein", "Weiß nicht"],
    ["Ja", "Nein", "Weiß nicht"],
    ["Ja", "Nein", "Weiß nicht"],
    ["Ja", "Nein", "Weiß nicht"],
    ["Ja", "Nein", "Weiß nicht"],
    ["Ja", "Nein", "Weiß nicht"],
    ["Ja", "Nein", "Weiß nicht"],
    ["Ja", "Nein", "Weiß nicht"]
]

# Die Punkte für jede Antwort
punkte = {
    "Ja": 2,
    "Nein": -2,
    "Weiß nicht": 0
}

# Eine Funktion zum Stellen einer Frage und zum Erhalten einer Antwort
def frage_stellen(nummer):
    print(f"Frage {nummer + 1}: {fragen[nummer]}")
    print(f"Mögliche Antworten: {', '.join(antworten[nummer])}")
    antwort = input("Ihre Antwort: ")
    while antwort not in antworten[nummer]:
        print("Bitte geben Sie eine gültige Antwort ein.")
        antwort = input("Ihre Antwort: ")
    return antwort

# Eine Funktion zum Berechnen der Übereinstimmung mit jeder Partei
def uebereinstimmung_berechnen(antworten):
    uebereinstimmung = {}
    for partei in parteien:
        punktzahl = 0
        for i in range(len(antworten)):
            punktzahl += punkte[antworten[i]] * parteien[partei][i]
        uebereinstimmung[partei] = punktzahl
    return uebereinstimmung

# Eine Funktion zum Sortieren der Parteien nach Übereinstimmung
def parteien_sortieren(uebereinstimmung):
    sortiert = sorted(uebereinstimmung.items(), key=lambda x: x[1], reverse=True)
    return sortiert

# Eine Funktion zum Anzeigen der Ergebnisse
def ergebnisse_anzeigen(sortiert):
    print("Ihre Übereinstimmung mit den Parteien ist:")
    for partei in sortiert:
        print(f"{partei[0]}: {partei[1]} Punkte")

# Das Hauptprogramm
print("Willkommen beim Wahl-O-Mat!")
print("Sie werden 10 Fragen zu verschiedenen Themen beantworten.")
print("Am Ende werden Sie sehen, welche Parteien am besten zu Ihnen passen.")
antworten = []
for i in range(len(fragen)):
    antwort = frage_stellen(i)
    antworten.append(antwort)
uebereinstimmung = uebereinstimmung_berechnen(antworten)
sortiert = parteien_sortieren(uebereinstimmung)
ergebnisse_anzeigen(sortiert)
