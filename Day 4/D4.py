with open("input.txt", "r") as file:
    lst2 = file.read().splitlines()

lst2.append("")

lst = []
for k in lst2:
    if k != "":
        k2 = k.split()
    else:
        k2 = [""]
    for t in k2:
        lst.append(t)

dic = {}
nbr = 0

for elem in lst:
    if elem == "":
        gets = [dic.get("byr", None), dic.get("iyr", None), dic.get("eyr", None), dic.get("hgt", None),
                dic.get("hcl", None), dic.get("ecl", None), dic.get("pid", None), dic.get("cid", 5)]

        # False if fiels are missing
        if None not in gets:

            # False if any date out of range
            if 1920 <= int(gets[0]) <= 2002 and 2010 <= int(gets[1]) <= 2020 and 2020 <= int(gets[2]) <= 2030:

                # False if height in wrong unit or out of range
                if ("cm" in gets[3] and 150 <= int(gets[3].replace("cm", "")) <= 193) or \
                        ("in" in gets[3] and 59 <= int(gets[3].replace("in", "")) <= 76):

                    # False if hcl wrong
                    if len(gets[4]) == 7 or gets[4][0] == "#":
                        with open("chars.txt", "r") as file:
                            chars = file.read().splitlines()
                        for k in gets[4]:
                            if k not in chars:
                                dic = {}
                                continue

                        if gets[5] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:

                            if len(gets[6]) == 9:
                                for k in gets[6]:
                                    if k not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                                        dic = {}
                                        continue
                                nbr += 1
        dic = {}
    else:
        dic[elem.split(":")[0]] = elem.split(":")[1]

print(nbr)
