with open("input.txt", "r") as file:
    all_lines = file.read().split("\n\n")
    all_lines = [line.splitlines() for line in all_lines]
    all_lines.remove([])
    dic_lines = {}
    for line in all_lines:
        dic_lines[line[0].split()[1][:-1]] = line[1:]

print(dic_lines)
