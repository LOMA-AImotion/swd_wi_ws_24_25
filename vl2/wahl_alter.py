# Liest Name und Alter eines Benutzers
# Berechnet wie viele Jahre der Benutzer schon wählen darf
# gibt aus, wie lange Benutzer wählen darf

name = input("Wie heißt du?")
alter = int(input("Wie alt bist du?")) 
#alter = int(alter)

print(name)
print(alter)

wahl_alter = 16
jahre_waehler = alter - wahl_alter
#print("Hallo", name, "Du darfst seit", jahre_waehler, "Jahren wählen.")
print(f"Hallo {name}, Du darfst seit {jahre_waehler} Jahren wählen.")
