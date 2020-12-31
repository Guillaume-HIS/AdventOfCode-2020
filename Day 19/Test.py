with open("tst.txt", "r") as file:
    v = file.read().split(": ")[1]


print(v[0] == '"')
