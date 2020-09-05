def hochfahren(anzahl):
    print('Lift fährt', anzahl, 'Stockwerk(e) nach oben')


def herunterfahren(anzahl):
    print('Lift fährt', anzahl, 'Stockwerk(e) nach unten')


def ZustandWechseln(eingabe, zustand):
    '''Funktion, die das Wechseln des Stockwerks simuliert
    Parameter: eingabe = String
    Rückgabewert: zustand = String'''
    switcherZustand = {
    "Lift im EG": eingabefunk(eingabe, "EG"),
    "Lift im UG": eingabefunk(eingabe, "UG"),
    "Lift im OG": eingabefunk(eingabe, "OG")
    }
    return switcherZustand.get(zustand, "Bitte erneut Taste drücken")


def eingabefunk(eingabe, zustandstockwerk):
    wvstockwerke = stockwerksanzahl(eingabe, zustandstockwerk)
    print("Der Lift fährt", wvstockwerke)
    switcher={
    "UG": "Lift im UG" ,
    "EG": "Lift im EG",
    "OG": "Lift im OG"
    }
    return switcher.get(eingabe)

def stockwerksanzahl(eingabe, zustand):
    switcher={
    "UG":  ,
    "EG": "Lift im EG",
    "OG": "Lift im OG"
    }
stockwerk = "Lift im UG"
print(stockwerk)
while wahl != False:
    wahl = input('Wählen Sie ein Stockwerk UG, EG oder OG')
    stockwerk = ZustandWechseln(wahl, stockwerk)
