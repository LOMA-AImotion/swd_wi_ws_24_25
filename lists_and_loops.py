früchte = ["apple", "birne", "banana"]

früchte_mit_a = [frucht for frucht in früchte if "a" in frucht]

print(früchte_mit_a)

früchte_mit_a = []

for frucht in früchte:
    if "a" in frucht:
        früchte_mit_a.append(frucht)

print(früchte_mit_a)
