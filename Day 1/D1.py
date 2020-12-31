with open("input.txt", "r") as file:
    lst = file.read().splitlines()

for elem in lst:

    for elem2 in lst:

        if int(elem) + int(elem2) == 2020:
            print(f"Q1 : {int(elem2) * int(elem)}")

        for elem3 in lst:
            if int(elem) + int(elem2) + int(elem3) == 2020:
                print(f"Q2 : {int(elem) * int(elem2) * int(elem3)}")
