with open("input", 'r') as file:
    lines = file.read().splitlines()


def make(pos):
    made = []
    cnt = 1
    for elem in lines:
        if elem == "":
            cnt += 1
        else:
            if cnt == pos:
                made.append(elem)
    return made


# nbrs : tous les nombres valides
valid_nbrs = []
conditions = make(1)
for elem in conditions:
    rngs = elem.split(": ")[1].split(" or ")
    for rng in rngs:
        rn = rng.split("-")
        for nbr in range(int(rn[0]), int(rn[1]) + 1):
            if nbr not in valid_nbrs:
                valid_nbrs.append(nbr)

# -----------------------
my_ticket0 = make(2)[1:]
my_ticket = []
for nbr in my_ticket0[0].split(","):
    my_ticket.append(nbr)

# -----------------------
nearby_tickets0 = make(3)[1:]
nearby_tickets = []
for ticket in nearby_tickets0:
    nearby_tickets.append(ticket.split(","))

# -----------------------
non_valid = []
nearby_tickets2 = []
for ticket in nearby_tickets:
    good = True
    for nbr in ticket:
        if int(nbr) not in valid_nbrs:
            good = False
            non_valid.append(int(nbr))
    if good:
        nearby_tickets2.append(ticket)

print(f"Q1 : {sum(non_valid)}")

dic_condition = {}
for cond in conditions:
    lst = []
    for rng in cond.split(": ")[1].split(" or "):
        rn = rng.split("-")
        for nbr in range(int(rn[0]), int(rn[1]) + 1):
            if nbr not in lst:
                lst.append(nbr)
    dic_condition[cond.split(": ")[0]] = lst

dic_position = {x: [] for x in dic_condition.keys()}
for ticket in nearby_tickets2:
    for i, nbr in enumerate(ticket):
        for key, value in dic_condition.items():
            if int(nbr) in value:
                dic_position[key].append(i)

for k, v in dic_position.items():
    max_occur = []
    for elem in v:
        if v.count(elem) == len(nearby_tickets2) and elem not in max_occur:
            max_occur.append(elem)
    dic_position[k] = max_occur

dic_pos2 = {}
deja_vu = []
for k in range(1, len(nearby_tickets2[0]) + 1):
    for key, v in dic_position.items():
        if len(v) == k:
            for nbr in v:
                if nbr not in deja_vu:
                    deja_vu.append(nbr)
                    dic_pos2[key] = nbr

ans = 1
for key, value in dic_pos2.items():
    if "departure" in key:
        ans *= int(my_ticket[value])

print(ans)
