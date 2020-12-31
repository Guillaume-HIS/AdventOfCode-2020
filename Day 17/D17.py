from functions import *

with open("input", "r") as file:
    lines = file.read().splitlines()


def q1(lines):
    space = {(x, y, 0): lines[y][x]
             for x in range(len(lines[0]))
             for y in range(len(lines))}

    for _ in range(6):
        space = cycle(space)

    return list(space.values()).count("#")


def q2(lines):
    space = {(x, y, 0, 0): lines[y][x]
             for x in range(len(lines[0]))
             for y in range(len(lines))}

    for _ in range(6):
        space = cycle4d(space)

    return list(space.values()).count("#")


print(f"Q1 : {q1(lines)}")
print(f"Q2 : {q2(lines)}")
