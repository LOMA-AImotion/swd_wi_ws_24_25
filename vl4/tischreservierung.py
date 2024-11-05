# Gib eine Anzahl an Plätzen fest an
plaetze = 10
verfuegbare_plaetze = plaetze

# Nehme Anrufe entgegen solange Platz ist
while verfuegbare_plaetze > 0: 
    name = input("Hallo, wer spricht?")
    gewuenschte_plaetze = int(input("Wie viele Plätze benötigen Sie?"))
    if verfuegbare_plaetze >= gewuenschte_plaetze:
        # Ziehe gewünschte Plätze von verfügbaren Plätzen ab
        verfuegbare_plaetze = verfuegbare_plaetze - gewuenschte_plaetze
        print(f"{name}, wir haben Platz für Sie, es sind jetzt {plaetze - verfuegbare_plaetze}/{plaetze} belegt.")
    else:
        # Gib Info wenn kein Platz mehr ist
        print(f"Es tut mir Leid {name}, wir haben keinen Platz mehr.")
print("Alle Plätze belegt.")
