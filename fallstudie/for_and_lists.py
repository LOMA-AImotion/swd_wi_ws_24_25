# Nehmen wir an: Automobilzulieferer für Autoinnenausstattung 


# Idea: save inventory in CSV

radio_knopf_100stk = ["Radioknopf (100er Packung)", 5]
fussraumteppich_in_m = ["Fußraumteppich (m)", 70]
fensterheber_in_100stk = ["Fensterheber (100er Packung)", 4]
lenkrad_knopf_100stk = ["Lenkradknopf (100er Packung)", 6]

inventar = [radio_knopf_100stk, fussraumteppich_in_m, fensterheber_in_100stk, lenkrad_knopf_100stk]


for i in range(len(inventar)):
    print(f"{inventar[i][0]} -> Code {i} ({inventar[i][1]} verfügbar)")

bestellung = int(input("Bitte Produktcode für Bestellung eingeben: "))
menge = float(input("Bitte zu bestellende Menge eingeben: "))

einkaufswagen = None

aktueller_bestand = inventar[bestellung][1]

if aktueller_bestand >= menge:
    einkaufswagen = f"{menge} von {inventar[bestellung][0]}" 
    inventar[bestellung][1] -= menge
else:
    print("Bestellung kann leider nicht erfüllt werden :(") 
           
print(f"Ihre bestätigte Bestellung: {einkaufswagen}")
