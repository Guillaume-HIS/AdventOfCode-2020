with open("input.txt", "r") as file:
    lst = file.read().splitlines()

correct_pswrd = []

for index, elem in enumerate(lst):
    lst[index] = elem.split()
    lst[index][0] = lst[index][0].split("-")
    lst[index][1] = lst[index][1].replace(":", "")

print(lst)

for k in lst:
    if int(k[0][0]) <= k[2].count(k[1]) <= int(k[0][1]):
        correct_pswrd.append(k[2])
    else:
        continue

correct_pswdr2 = []

for k in lst:

    valid = 0

    if len(k[2]) < int(k[0][1]) - 1 and k[2][int(k[0][0]) - 1] == k[1]:
        valid += 1

    elif k[2][int(k[0][0]) - 1] == k[1] and k[2][int(k[0][1]) - 1] != k[1]:
        valid += 1

    elif k[2][int(k[0][0]) - 1] != k[1] and k[2][int(k[0][1]) - 1] == k[1]:
        valid += 1

    if valid == 1:
        correct_pswdr2.append(k[2])

print(lst)
print(correct_pswrd)
print(len(correct_pswrd))
print(len(correct_pswdr2))
