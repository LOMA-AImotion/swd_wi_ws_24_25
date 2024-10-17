# Notenberechnung
max_punkte = 70
erreichte_punkte = int(input("Punkte erreicht?"))

prozent_satz = erreichte_punkte / max_punkte

if prozent_satz > 0.9:
    print("Mit 1,0 bestanden")
elif prozent_satz > 0.8:
    print("Mit 2,0 bestanden")
elif prozent_satz > 0.7:
    print("Mit 3,0 bestanden")
elif prozent_satz > 0.5:
    print("Mit 4,0 bestanden")
else:
    print("Nicht bestanden")