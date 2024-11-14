# Frage Nutzer nach einer Zahl k
# Bilde Tupel wie z.B. (1, "x") oder (2, "xx")
# Füge diese Tupel in eine Menge (set) ein.

k = int(input("Zahl k?"))

menge = set()
for i in range(1, k+1): 
    menge.add( (i, "x"*i) )

print(menge)

# über Set-Comprehension
menge2 = { (i, "x"*i) for i in range(1, k+1) }
print(menge2)

print(menge == menge2)