with open("input.txt", "r") as file:
    lines = file.read().replace(".", "").splitlines()
    lines = [line.rstrip() for line in lines]


for index, elem in enumerate(lines):
    lines[index] = elem.strip().split("contain")
    lines[index][1] = lines[index][1].strip().split(",")
    lines[index][0] = lines[index][0].strip()
    lines[index][1] = [lst.strip() for lst in lines[index][1]]

dic = {}
for index, elem in enumerate(lines):
    bag_dic = {}
    for index2, elem2 in enumerate(elem[1]):
        if elem2 == "no other bags":
            nbr = 0
        else:
            nbr = elem2[0]
        name = ""
        for k in range(2, len(elem2)):
            name += elem2[k]
        bag_dic[name.replace(" bags", "").replace(" bag", "")] = nbr
    dic[elem[0].replace(" bags", "").replace(" bag", "")] = bag_dic


def is_in(all_bags, target, current):
    if current == target:
        return 1
    elif all_bags.get(current, None) is None:
        return 0
    else:
        counter = []
        for key, value in all_bags[current].items():
            counter.append(is_in(all_bags, target, key))
        return max(counter)


def q1(dic_all, my_bag):
    bag_nbr = 0
    for key, value in dic_all.items():
        if key != my_bag:
            bag_nbr += is_in(dic_all, my_bag, key)
    return bag_nbr


# Q2
bags_content = {}
for key, value in dic.items():
    lst_content = []
    for key2, value2 in value.items():
        for _ in range(int(value2)):
            lst_content.append(key2)
    bags_content[key] = lst_content


def nbr_in(all_bags_content, target):
    if target == "other" or all_bags_content.get(target) is None:
        return 0
    cnt1 = len(all_bags_content[target])
    cnt_tot = []
    for elem in all_bags_content[target]:
        cnt_tot.append(nbr_in(all_bags_content, elem))
    return cnt1 + sum(cnt_tot)


with open("out.txt", "w+") as file:
    file.write(str(bags_content))


print(bags_content)
print(dic)
print(q1(dic, "shiny gold"))
print(nbr_in(bags_content, "shiny gold"))
