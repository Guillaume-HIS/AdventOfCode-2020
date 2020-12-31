from copy import deepcopy

with open("input.txt.txt.txt", "r") as file:
    matrix = file.read().splitlines()
    matrix = [[char for char in line] for line in matrix]

new_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]


def count_around(y, x, item):
    lst = []
    try:
        r = 1
        while matrix[y - r][x - r] == ".":
            if y - r == 0:
                raise IndexError
            if x - r == 0:
                raise IndexError
            r += 1
            if matrix[y - r][x - r] == item:
                lst.append(item)

    except:
        lst.append(0)

    try:
        r = 1
        while matrix[y - r][x + r] == ".":
            if y - r == 0:
                raise IndexError
            r += 1
            if matrix[y - r][x + r] == item:
                lst.append(item)
    except:
        lst.append(0)

    try:
        r = 1
        while matrix[y][x - r] == ".":
            if x - r == 0:
                raise IndexError
            r += 1
            if matrix[y][x - r] == item:
                lst.append(item)
    except:
        lst.append(0)

    try:
        r = 1
        while matrix[y][x + r] == ".":
            r += 1
            if matrix[y][x + r] == item:
                lst.append(item)
    except:
        lst.append(0)

    try:
        r = 1
        while matrix[y + r][x - r] == ".":
            if x - r == 0:
                raise IndexError
            r += 1
            if matrix[y + r][x - r] == item:
                lst.append(item)
    except:
        lst.append(0)

    try:
        r = 1
        while matrix[y - r][x] == ".":
            if y - r == 0:
                raise IndexError
            r += 1
            if matrix[y - r][x] == item:
                lst.append(item)
    except:
        lst.append(0)
    try:
        r = 1
        while matrix[y + r][x] == ".":
            r += 1
            if matrix[y + r][x] == item:
                lst.append(item)
    except:
        lst.append(0)
    try:
        r = 1
        while matrix[y + r][x + r] == ".":
            r += 1
            if matrix[y + r][x + r] == item:
                lst.append(item)
    except:
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

print(new_matrix)
print(times)
print(cnt)
