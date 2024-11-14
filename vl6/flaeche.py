def flaeche(breite: int, hoehe: int) -> int:
    a = breite * hoehe
    kosten = kosten_pro_m2 * a
    return a, kosten

print("Im Hauptprogramm")
meine_breite = int(input("Breite?"))
meine_hoehe = int(input("Höhe?"))
kosten_pro_m2 = 100

meine_flaeche, meine_kosten = flaeche(meine_breite, meine_hoehe)
# print(kosten) gilt nur innerhalb der Funktion "flaeche"

print(f"Die Fläche ist {meine_flaeche} und kostet {meine_kosten}.")