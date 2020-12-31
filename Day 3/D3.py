with open("input.txt", "r") as file:
    lst = file.read().splitlines()


def traj(down, right):
    pos = 0
    nbr = 0
    for index, line in enumerate(lst):
        if index % down == 0:
            if pos > 30:
                pos = pos - 31
            if line[pos] == "#":
                nbr += 1
            pos += right
    return nbr


print(traj(1, 1) * traj(1, 3) * traj(1, 5) * traj(1, 7) * traj(2, 1))
