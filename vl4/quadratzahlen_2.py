# Frage nach einem Budget. "Kaufe" solange Quadratzahlen, bis das Budget erschöpft ist.
# Gib die höchste Quadratzahl aus - und wieviel es gekostet hat 

budget = int(input("Welches Budget?"))
aktuelle_zahl = 1
summe = 0

while budget >= aktuelle_zahl * aktuelle_zahl: # solange noch Budget da ist 
    budget = budget - aktuelle_zahl*aktuelle_zahl
    summe = summe + aktuelle_zahl*aktuelle_zahl
    aktuelle_zahl = aktuelle_zahl + 1 
    print(aktuelle_zahl)

print(f"Summe ist {summe}, hoechste Zahl ist {aktuelle_zahl - 1}")