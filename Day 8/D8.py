from copy import deepcopy

with open("input.txt", "r") as file:
    lines = file.read().splitlines()
    lines = [line.split() for line in lines]


def q1(lines):
    accumulator = 0
    current_index = 0
    deja_vu_index = []
    sol_valide = True
    while True:
        if len(lines) - 1 == current_index:
            sol_valide = False
        if current_index in deja_vu_index:
            return accumulator, False
        deja_vu_index.append(current_index)
        if lines[current_index][0] == "nop":
            current_index += 1
        elif lines[current_index][0] == "acc":
            accumulator += int(lines[current_index][1])
            current_index += 1
        elif lines[current_index][0] == "jmp":
            current_index += int(lines[current_index][1])

        if not sol_valide:
            return accumulator, True


def q2(lines):

    new_lines = lines.copy()

    for current_index in range(len(new_lines)):

        command = lines[current_index][0]
        value = int(lines[current_index][1])

        if command == "jmp":
            command = "nop"
        elif command == "nop":
            command = "jmp"

        new_lines = lines.copy()
        new_lines[current_index] = [command, str(value)]
        accumulator, valid = q1(new_lines)

        if valid:
            return accumulator


print(lines)
print(q1(lines)[0])
print(q2(lines))
