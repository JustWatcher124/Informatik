import time


def hochfahren(anzahl):
    print('Lift fährt', anzahl, 'Stockwerk(e) nach oben')


def herunterfahren(anzahl):
    print('Lift fährt', anzahl, 'Stockwerk(e) nach unten')


def stockwerkdistanz(wohin, wojetzt, switcher):
    # print(switcher.get(wojetzt)-switcher.get(wohin))
    return switcher.get(wohin)-switcher.get(wojetzt)


print("Willkommen im Aufzug der ZUK-unft AG\n"
"Sie befinden sich im Untergeschoss,\n"
"In diesem Gebäude befinden sich das (U)ntergeschoss, (E)rdgeschoss und das (O)bergeschoss\n"
"Der Aufzug fährt nur mit theorethischer Geschwindigkeit, braucht also für jede Strecke nur 1 Sekunde")
woistaufzug = "U"
unnecessary = 0
switchlist={
    0 : "U",
    1 : "E",
    2 : "O",
    "U": 0,
    "E": 1,
    "O": 2
    }
try:
    while True:
        fahrliste = []
        wohinfahren = input("Bitte geben sie (U)/(E)/(O) für die Stockwerke ein zu denen sie fahren wollen:\n")
        print("\nEs werden erst alle schon eingegebenen Stockwerke angefahren bevor die nächste Eingabe abgefragt wird.\n")
        for stockwerke in wohinfahren:
            if stockwerke in ("U","E","O"):
                fahrliste.append(stockwerke)
        if len(fahrliste) > 0:
            print(fahrliste)
            for fahrplan in fahrliste:
                distanz = stockwerkdistanz(fahrplan, woistaufzug, switchlist)
                if distanz > 0:
                    hochfahren(distanz)
                elif distanz < 0:
                    herunterfahren(abs(distanz))
                else:
                    unnecessary += 1
                woistaufzug = fahrplan
        else:
            print("\nSie haben keine Zulässigen Stockwerke eingegeben!\n")
        print("Der Aufzug hat", unnecessary,"mal unnötig gehalten")
except Exception as e:
    print("SYSTEM ERROR ROOT NOT FOUND")
