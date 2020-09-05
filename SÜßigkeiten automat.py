import time


def geldeinwurf(geld):
    try:
        geldeingeworfen = input("Wie viel wollen sie einwerfen?(In €)")
        if geldeingeworfen in ("a", "A", "Abort", "abort"):
            return 2147483648
        return geld + float(geldeingeworfen)
    except TypeError:
        print("Nur Zahlen sind erlaubt!")
        return(geldeinwurf(geld))



def isitvalid(geld, wunschliste):
    if wunschliste.count(2) * 0.2 + wunschliste.count(1) * 0.1 > geld:
        print("Ihnen fehlt", wunschliste.count(2) * 0.2 + wunschliste.count(1) * 0.1 - geld,"€\n"
        "Sie haben für ihren Wunscheinkauf zu wenig Geld eingeworfen!\n"
        "Sie können ihren Geldbetrag nun erhöhen.\n"
        "Wenn sie ihre Bestellung abbrechen wollen drücken sie (A)bort\n")
        return False
    return True


def startmessage():
    print("Willkommen beim Süß-Sauer Bonbon Automat3000\n"
            "Sie können ein Süßes oder ein Saures Bonbon für\n"
            "jeweils für 0.10€ bzw. 0.20€ kaufen\n"
            "Akzeptiert werden alle gültigen Euro Wertstückelungen\n"
            "Süße Bonbons  (1)\n"
            "Saure Bonbons (2)\n"
            "Zutaten: Zucker, Glucosesirup, Verdickungsmittel Xanthan, blablabla (Wollen sie nicht wissen)\n")
    return

# Main
global geld
geld = 0
startmessage()
try:
    while True:
        geld = geldeinwurf(geld)
        if geld != 2147483648:
            bestellung = input("Für den Kauf bitte 1 oder 2 eingeben.\n"
             "Für 'größere' Mengen die Zahlen mit einem (,) abtrennen!")
            kaufliste = []
            for bonbonwunsch in bestellung:
                if bonbonwunsch in ("1","2"):
                    kaufliste.append(int(bonbonwunsch))
            # Simulierter Kauf
            while not isitvalid(geld, kaufliste):
                geld = geldeinwurf(geld)
            if geld != 2147483648:
                ausgegeben = kaufliste.count(1) * 0.1 + kaufliste.count(2) * 0.2
                print("Ihr Rückgeld beträgt:", geld-ausgegeben, "€\n"
                "Sie haben\n",
                kaufliste.count(1),"Süße Bonbons und\n",
                kaufliste.count(2),"Saure Bonbons gekauft\n")
                time.sleep(3)
                print("Viel Spaß mit ihren Süßigkeiten, und bitte weiterempfehlen!\n"
                " BITTE WARTEN\n\n BITTE WARTEN\n\n BITTE WARTEN\n\n BITTE WARTEN\n")
                time.sleep(10)
                startmessage()
        else:
            print("RESTARTING")
            time.sleep(10)
            startmessage()
        geld = 0
        kaufliste = []
except:
    print("INTERNAL ERROR SYSTEM ROOT NOT DETECTED")
