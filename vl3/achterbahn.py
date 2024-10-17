# Frage Nutzer nach Körpergröße
# Überprüfe ob Nutzer größer als 150 ist - dann darf er fahren, sonst nicht
groesse = int(input("Wie groß bist du?"))

if groesse > 150:
    print("Du darfst fahren!")
    print("Macht 3 €")
    print("Per Paypal bezahlen?")
else:
    print(f"Leider nein, du bist {150 - groesse} cm zu klein.")