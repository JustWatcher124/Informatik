import time


def wortPruefen(koffein, schongetrunken, switcher):
    if koffein + schongetrunken > 4:
        return "NEIN"
    else:
        return switcher[koffein + schongetrunken]


## Hauptprogramm:
switchlist ={
"q0" : 0,"q1" : 1, "q2" : 2, "q3" : 3, "q4" : 4,
0 : "q0", 1 : "q1", 2 : "q2", 3 : "q3", 4 : "q4",
"K" : 1, "E" : 2
}
while True:
    schongetrunken = "q0"
    wort = input("Geben Sie ein Wort ein, um zu testen ob es zur Sprache L gehört. Benutzen Sie Großbuchstaben K oder E")
    wort = [i for i in wort if i in ("E", "K")]
    for bestellung in wort:
        isitvalid = wortPruefen(switchlist[bestellung], switchlist[schongetrunken], switchlist)
    if isitvalid != "NEIN":
        print("Bestellung wird zubereitet")
        schongetrunken = isitvalid
    else:
        print("Der Kaffeemüll würde mit dieser Bestellung überfüllt werden.")
        print("Der Kaffemüll wird durch unsere Mitarbeiter geleert. Bitte warten.")
        time.sleep(3)
