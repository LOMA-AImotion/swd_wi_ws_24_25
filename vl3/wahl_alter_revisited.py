# Liest Name und Alter eines Benutzers
# Berechnet wie viele Jahre der Benutzer schon wählen darf
# gibt aus, wie lange Benutzer wählen darf
# - berücksichtigt Erstwähler
# - berücksichtigt noch nicht Wahlberechtigte

name = input("Wie heißt du?")
alter = int(input("Wie alt bist du?")) 

wahl_alter = 18
jahre_waehler = alter - wahl_alter

if alter < wahl_alter:
    print(f"Tut mir Leid {name}, Du bist erst {alter} und musst noch {wahl_alter - alter} Jahre warten")
elif alter == wahl_alter:
    print(f"Gratuliere {name}, du darfst dieses Jahr zum ersten Mal wählen.")
else:
    print(f"{name}, Du darfst seit {jahre_waehler} Jahren wählen.")
