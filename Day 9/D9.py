with open("input.txt", "r") as file:
    lines = file.read().splitlines()
    lines = [int(line) for line in lines]


def q1(lines, preamble):
    valid = []
    all_no_valid = []
    for k in range(preamble, len(lines)):

        tmp_lst = []

        for u in range(k - preamble, k):
            tmp_lst.append(lines[u])

        for elem in tmp_lst:

            if lines[k] - elem in tmp_lst and elem != lines[k] - elem:
                valid.append(lines[k])

    for t in range(preamble, len(lines)):
        if lines[t] not in valid:
            all_no_valid.append(lines[t])

    return all_no_valid


def q2(lines, non_valid):
    for k in range(len(lines) - 1):
        for t in range(1, len(lines) - 1):
            terms = lines[k:t]
            if sum(terms) == non_valid[0] and terms[0] != non_valid[0]:
                return min(terms) + max(terms)


non_valid = q1(lines, 25)
print(f"Q1 : {non_valid[0]}")
print(f"Q2 : {q2(lines, non_valid)}")
