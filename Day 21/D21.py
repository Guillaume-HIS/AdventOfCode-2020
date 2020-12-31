with open("input.txt", "r") as file:
    lines = file.read().splitlines()

alrgns_dic = {}
how_often = {}

for line in lines:

    ingredients = line.split(' (')[0].split(' ')
    alergens = line.split('(contains ')[1][:-1].split(', ')

    for ingr in ingredients:
        if ingr not in how_often:
            how_often[ingr] = 0
        how_often[ingr] += 1

    for aler in alergens:
        if aler not in alrgns_dic:
            alrgns_dic[aler] = set(ingredients)
        else:
            alrgns_dic[aler] = alrgns_dic.get(aler).intersection(set(ingredients))
print(how_often)
deja_vu = []
for _ in range(len(lines)):

    for k, v in alrgns_dic.items():
        if len(v) == 1:
            val, = v
            if val in deja_vu:
                continue

            deja_vu.append(val)

            for key, value in alrgns_dic.items():
                if len(value) > 1 and val in value:
                    value.remove(val)

print(alrgns_dic)
gevaarlijk = {}
for v in alrgns_dic.values():
    for vv in v:
        gevaarlijk[vv] = 1

n = 0
for k, v in how_often.items():
    if k in gevaarlijk:
        continue
    n += v

print("Q1 : ", n)


def q2(inp):
    a, = inp
    return a


print(sorted(list(alrgns_dic.items())))
print("Q2 : ", ",".join([q2(v[1]) for v in sorted(list(alrgns_dic.items()))]))
