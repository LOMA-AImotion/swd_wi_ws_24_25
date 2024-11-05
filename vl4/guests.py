gast_befehl = input("Wen einladen? <niemand> zum Beenden")
gaeste = []

while gast_befehl != "niemand":
    gaeste.append(gast_befehl)
    gast_befehl = input("Wen einladen? <niemand> zum Beenden")

print(f"Fertig. Du hast {len(gaeste)} Gäste eingeladen.")