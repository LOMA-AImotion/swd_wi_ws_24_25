# gegeben messzeitpunkte, liefere mir die Abstände
messzeitpunkte = [0, 1, 4, 5, 7, 8]
# Bestimme Differenzen, soll [1, 3, 1, 2, 1]

differenzen = []
for i in range(1, len(messzeitpunkte)):
    differenzen.append(messzeitpunkte[i] - messzeitpunkte[i-1])

print(differenzen)

## über List comprehensions
diffs = [messzeitpunkte[i] - messzeitpunkte[i-1] for i in range(1, len(messzeitpunkte))]
print(diffs)