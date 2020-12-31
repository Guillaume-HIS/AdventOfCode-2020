with open("input.txt", "r") as file:
    tiles_lst = file.read().splitlines()


def q1(tiles, system):

    blacks = []

    for tile in tiles:

        # On cree un liste avec tous les moves
        i = 0
        moves = []
        while i < len(tile):
            if tile[i] == "s" or tile[i] == "n":
                moves.append(tile[i: i+2])
                i += 2

            else:
                moves.append(tile[i])
                i += 1

        # Calcul coords du tile selon le systeme de coords
        x = 0
        y = 0
        for move in moves:
            x += system[move][0]
            y += system[move][1]

        # Retournement du tile
        if (x, y) not in blacks:
            blacks.append((x, y))
        else:
            blacks.remove((x, y))

    return len(blacks), blacks


def q2(blacks, system, days, size):

    day = 0
    while day < days:
        black_cpy = blacks.copy()
        for k in range(-size, size):
            if k % 2 == 0:
                poses = [x for x in range(-size - 2, size + 2, 2)]
            else:
                poses = [x for x in range(-size - 1, size + 2, 2)]

            for t in poses:

                # Compte les tiles noires autour de celle au coords (k, t)
                blck_around = 0
                for key in system:
                    x = system[key][0]
                    y = system[key][1]
                    if (k + x, t + y) in blacks:
                        blck_around += 1

                # On transforme en blanc si tile est noir et que soit pas de voisin noir soit plus de 2 voisins noirs
                if (k, t) in blacks and (blck_around == 0 or blck_around > 2):
                    black_cpy.remove((k, t))
                elif (k, t) not in blacks and blck_around == 2:
                    black_cpy.add((k, t))

        blacks = black_cpy.copy()
        day += 1

    return len(blacks)


# Creation du systeme de coordonnees
coord_sys = {"e": (2, 0), "w": (-2, 0), "nw": (-1, 1), "ne": (1, 1), "sw": (-1, -1), "se": (1, -1)}

# Qustion 1
q1_ans, black_tiles = q1(tiles_lst, coord_sys)
print(f"Q1 : {q1_ans}")

# Question 2
black_tiles = set(black_tiles)
q2_ans = q2(black_tiles, coord_sys, 100, 200)
print(f"Q2 : {q2_ans}")
