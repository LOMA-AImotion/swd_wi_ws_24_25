# Nehmen wir an: Automobilzulieferer für Autoinnenausstattung 


radio_knopf_100stk = 5
fussraumteppich_in_m = 70
fensterheber_in_100stk = 4

print("Radioknopf (in 100er Packungen): Code 1, Fußraumteppich (in Meter): Code 2, Fensterheber (in 100er Packungen): Code 3")

bestellung = input("Bitte Produktcode für Bestellung eingeben: ")
menge = float(input("Bitte zu bestellende Menge eingeben: "))

einkaufswagen = None

if bestellung == "1":
    if radio_knopf_100stk >= menge:
        radio_knopf_100stk = radio_knopf_100stk - menge
        einkaufswagen = f"{menge} von Radioknöpfen (100 Stk.)"
    else:
        print("Leider haben wir nicht ausreichend viel Bestand :(")
if bestellung == "2":
    if fussraumteppich_in_m >= menge:
        fussraumteppich_in_m = fussraumteppich_in_m - menge
        einkaufswagen = f"{menge} von Fußraumteppich (m)"
    else:
        print("Leider haben wir nicht ausreichend viel Bestand :(")
if bestellung == "3":
    if fensterheber_in_100stk >= menge:
        fensterheber_in_100stk = fensterheber_in_100stk - menge
        einkaufswagen = f"{menge} von Fensterheber (100 Stk.)"
    else:
        print("Leider haben wir nicht ausreichend viel Bestand :(")
         
           
print(f"Ihre bestätigte Bestellung: {einkaufswagen}")
