from copy import deepcopy

with open("input.txt", "r") as file:
    matrix = file.read().splitlines()
    matrix = [[char for char in line] for line in matrix]

new_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]


def count_around(y, x, item):

    lst = []

    try:
        r = 1
        while matrix[y - r][x - r] == ".":
            r += 1
        if y - r >= 0 and x - r >= 0:
            lst.append(matrix[y - r][x - r])
        else:
            raise IndexError
    except IndexError:
        lst.append(0)

    try:
        r = 1
        while matrix[y - r][x + r] == ".":
            r += 1
        if y - r >= 0:
            lst.append(matrix[y - r][x + r])
        else:
            raise IndexError
    except IndexError:
        lst.append(0)

    try:
        r = 1
        while matrix[y][x - r] == ".":
            r += 1
        if x - r >= 0:
            lst.append(matrix[y][x - r])
        else:
            raise IndexError
    except IndexError:
        lst.append(0)

    try:
        r = 1
        while matrix[y][x + r] == ".":
            r += 1

        lst.append(matrix[y][x + r])
    except IndexError:
        lst.append(0)

    try:
        r = 1
        while matrix[y + r][x - r] == ".":
            r += 1
        if x - r >= 0:
            lst.append(matrix[y + r][x - r])
        else:
            raise IndexError
    except IndexError:
        lst.append(0)

    try:
        r = 1
        while matrix[y - r][x] == ".":
            r += 1
        if y - r >= 0:
            lst.append(matrix[y - r][x])
        else:
            raise IndexError
    except IndexError:
        lst.append(0)

    try:
        r = 1
        while matrix[y + r][x] == ".":
            r += 1
        lst.append(matrix[y + r][x])
    except IndexError:
        lst.append(0)

    try:
        r = 1
        while matrix[y + r][x + r] == ".":
            r += 1
        lst.append(matrix[y + r][x + r])
    except IndexError:
        lst.append(0)

    if item == "#":
        return lst.count(item)
    if item == "L":
        return lst.count(item) + lst.count(0)


times = 0
while True:
    change = 0

    for index, line in enumerate(matrix):

        for index2, elem in enumerate(line):

            if elem == "L":
                if count_around(index, index2, "#") == 0:
                    new_matrix[index][index2] = "#"
                    change += 1
                else:
                    new_matrix[index][index2] = "L"
            elif elem == "#":
                if count_around(index, index2, "#") >= 5:
                    new_matrix[index][index2] = "L"
                    change += 1
                else:
                    new_matrix[index][index2] = "#"
            elif elem == ".":
                new_matrix[index][index2] = "."

    matrix = deepcopy(new_matrix)
    times += 1
    if change == 0:
        break

cnt = 0
for line in matrix:
    cnt += line.count("#")

matrix_print = ["".join(k) for k in matrix]

with open("out.txt", "w+") as file:
    file.write("\n".join(matrix_print))

print(cnt)
