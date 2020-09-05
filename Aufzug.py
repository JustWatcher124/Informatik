### Zustandsbasierte Implementierung eines Aufzugs



def hochfahren(anzahl):
    print('Lift fährt', anzahl, 'Stockwerk(e) nach oben')

def herunterfahren(anzahl):
    print('Lift fährt', anzahl, 'Stockwerk(e) nach unten')

def ZustandWechseln(eingabe, zustand):
    '''Funktion, die das Wechseln des Stockwerks simuliert
    Parameter: eingabe = String
    Rückgabewert: zustand = String'''
    if zustand == 'Lift im UG':
        if eingabe == 'EG':
            hochfahren(1)
            zustand = 'Lift im EG'
            print(zustand)
        elif eingabe == 'OG':
            hochfahren(2)
            zustand = 'Lift im OG'
            print(zustand)
        else:
            print('Bitte erneut Taste drücken')
    if zustand == 'Lift im EG':
        if eingabe == 'OG':
            hochfahren(1)
            zustand = 'Lift im OG'
            print(zustand)
        elif eingabe == 'UG':
            herunterfahren(1)
            zustand = 'Lift im UG'
            print(zustand)
        else:
            print('Bitte erneut Taste drücken')
    if zustand == 'Lift im OG':
        if eingabe == 'EG':
            herunterfahren(1)
            zustand = 'Lift im EG'
            print(zustand)
        elif eingabe == 'UG':
            herunterfahren(2)
            zustand = 'Lift im UG'
            print(zustand)
        else:
            print('Bitte erneut Taste drücken')
    return zustand


# Hauptprogramm:
print('Herzlich Willkommen in unserem Aufzug.')
stockwerk = 'Lift im UG'
print(stockwerk)
wahl = True
while wahl != False:
    wahl = input('Wählen Sie ein Stockwerk UG, EG oder OG')
    stockwerk = ZustandWechseln(wahl, stockwerk)
