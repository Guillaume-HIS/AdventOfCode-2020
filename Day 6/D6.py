with open("input.txt", "r") as file:
    lst = file.read().splitlines()

lst.append("")

group_lst = []
group_str = ""
tot_cnt = 0

for k in lst:
    if k == "":
        comm_ans = []
        for t in group_str:
            if all(t in ans for ans in group_lst) and t not in comm_ans:
                comm_ans.append(t)

        tot_cnt += len(comm_ans)
        group_lst = []
        group_str = ""
    else:
        group_lst.append(k)
        group_str += k

print(tot_cnt)
