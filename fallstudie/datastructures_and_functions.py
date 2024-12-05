# Nehmen wir an: Automobilzulieferer für Autoinnenausstattung 

# Datenstrukturen 

# Tupel
t = ("item1", "item2", "item3")
t1, t2, t3 = t

# Set 
s = {"item1", "item2", "item3", "item3"}
print(s)

if "item1" in s:
    print("yes")

# Dictionary
d = {"item1": 1, "item2": 2, "item3": 3}
print(d["item3"])


# Idea: save inventory in CSV

# radio_knopf_100stk = ["Radioknopf (100er Packung)", 5]
# fussraumteppich_in_m = ["Fußraumteppich (m)", 70]
# fensterheber_in_100stk = ["Fensterheber (100er Packung)", 4]
# lenkrad_knopf_100stk = ["Lenkradknopf (100er Packung)", 6]

# inventar = [radio_knopf_100stk, fussraumteppich_in_m, fensterheber_in_100stk, lenkrad_knopf_100stk]

def transfer_from_inventory_to_cart(inventar, bestellung, menge, einkaufswagen):
    aktueller_bestand = inventar.get(bestellung, None)
    
    if aktueller_bestand is None:
        return None
    
    einheit = inventar[bestellung][1]


    if aktueller_bestand >= menge:
        inventar[bestellung][0] -= menge
        einkaufswagen.append(f"{menge} {einheit} von {bestellung}")
        return inventar, einkaufswagen
    else:
        return None


inventar = {"Radioknopf": [5, "100er Packung"], "Fußraumteppich": [70, "meter"], "Fensterheber": [4, "100er Packung"], "Lenkradknopf": [6, "100er Packung"]}


print(f"Hallo lieber Kunde, hier ist unser Inventar: {inventar}")

bestellung = input("Bitte Produktcode für Bestellung eingeben (stop zum abbrechen): ")

einkaufswagen = []

while not bestellung == "stop":
    menge = int(input("Bitte zu bestellende Menge eingeben: "))

    result = transfer_from_inventory_to_cart(inventar, bestellung, menge, einkaufswagen)

    if result is None:
        print("Entschuldigung! Wir konnten Ihre Bestellung leider nicht erfüllen... :(")
    else: 
        inventar, einkaufswagen = result 

    bestellung = input("Bitte Produktcode für Bestellung eingeben (stop zum abbrechen): ")

           
print(f"Ihre bestätigte Bestellung: {einkaufswagen}")
print(f"Aktueller Inventar: {inventar}")
