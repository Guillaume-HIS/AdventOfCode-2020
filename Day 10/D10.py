with open("input.txt", "r") as file:
    lines = file.read().splitlines()
    lines = [int(elem) for elem in lines]


adaptators = lines.copy()
last = 0
difs = []
for _ in range(len(adaptators)):
    difs.append(min(adaptators) - last)
    last = min(adaptators)
    adaptators.remove(last)
difs.append(3)

print(difs.count(1) * difs.count(3))

dico = {0: 1}
for line in sorted(lines):
    dico[line] = 0
    if line - 1 in dico:
        dico[line] += dico[line - 1]
    if line - 2 in dico:
        dico[line] += dico[line - 2]
    if line - 3 in dico:
        dico[line] += dico[line - 3]

print(dico)
print(dico[max(lines)])
