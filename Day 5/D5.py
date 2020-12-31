with open("input.txt", "r") as file:
    lines = file.read().splitlines()

seats = []

for line in lines:
    dic = {}

    row_str = line.replace("L", "").replace("R", "").replace("F", "0").replace("B", "1")
    dic["row"] = int(row_str, 2)

    column_str = line.replace("F", "").replace("B", "").replace("L", "0").replace("R", "1")
    dic["column"] = int(column_str, 2)

    dic["ID"] = dic["row"] * 8 + dic["column"]

    seat = [line, dic]
    seats.append(seat)

maximum = 0
for t in seats:
    if t[1]["ID"] > maximum:
        maximum = t[1]["ID"]

id_lst = []
for k in seats:
    id_lst.append(k[1]["ID"])

id_free = []
for u in range(0, maximum):
    if u not in id_lst:
        id_free.append(u)

print(id_free)
