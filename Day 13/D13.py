from math import gcd

with open("input.txt", "r") as file:
    lst = file.read().splitlines()
    timestamp = int(lst[0])
    busses = lst[1].split(",")
    busses = ["x" if elem == "x" else int(elem) for elem in busses]


def q1(busses):
    busses_dict = {}
    for bus in busses:
        if bus != "x":
            busses_dict[bus] = [0]

    for key, value in busses_dict.items():
        lst = [0]
        while True:
            if lst[len(lst) - 1] <= timestamp:
                lst.append(lst[len(lst) - 1] + key)
            else:
                break
        busses_dict[key] = lst

    maximum_lst = []

    for key, value in busses_dict.items():
        maximum_lst.append([key, max(value)])

    return busses_dict, min(maximum_lst)[0] * (min(maximum_lst)[1] - timestamp)


def ppcm(a, b):
    print(a, b)
    return int(a) * int(b) // gcd(int(a), int(b))


def q2(busses):
    ids = []
    for index, elem in enumerate(busses):
        if elem != "x":
            ids.append([elem, index])
    # ids : [[id, rank], ...]
    added = 1
    time = 0
    for k in range(1, len(ids)):
        found = False
        while not found:
            found = True
            for t in range(1 + k):
                if (time + ids[t][1]) % ids[t][0] != 0:
                    found = False
                    break

            if found:
                # On incremente a chaque fois au temps le ppcm du gap precedent avec id actuel -> premiers
                added = ppcm(added, ids[t][0])
                print(f"")
                break
            else:
                time += added

    print(time)


q2(busses)
