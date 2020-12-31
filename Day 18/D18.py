with open("input2.txt", "r") as file:
    lines = file.read().splitlines()


def calcul1(line, start, stop):

    current = start
    ans = 0
    add = True

    while current < stop:

        if line[current] == "+":
            add = True

        elif line[current] == "*":
            add = False

        # Si parenthese ouverte
        elif line[current] == "(":

            stopper = 1
            end_par = current + 1

            while stopper > 0:
                if line[end_par] == ")":
                    stopper -= 1
                elif line[end_par] == "(":
                    stopper += 1
                end_par += 1

            end_par -= 1

            # Recursion, on remplace la parenthese par sa val et par recurtion si parentheses imbriquees
            if add:
                ans += calcul1(line, current + 1, end_par)
            else:
                ans *= calcul1(line, current + 1, end_par)

            current = end_par

        # aka si int
        elif line[current] != " ":
            if add:
                ans += int(line[current])
            else:
                ans *= int(line[current])

        # Incrementation pour boucle while
        current += 1

    return ans


def calcul2(line, start, stop):

    current = start
    ans = []
    current_ans = 0

    while current < stop:

        if line[current] == "*":
            ans.append(current_ans)
            current_ans = 0

        # Si parenthese ouverte debut = a calcul1
        elif line[current] == "(":
            stopper = 1
            end_par = current + 1

            while stopper > 0:
                if line[end_par] == ")":
                    stopper -= 1
                elif line[end_par] == "(":
                    stopper += 1
                end_par += 1

            end_par -= 1

            current_ans += calcul2(line, current + 1, end_par)
            current = end_par

        # AKA si on a un bete int
        elif line[current] != " " and line[current] != "+":
            current_ans += int(line[current])

        # Incrementation pour boucle while
        current += 1

    ans.append(current_ans)

    prod = 1
    for elem in ans:
        prod *= elem

    return prod


def q1(lines):
    sum = 0

    for line in lines:
        sum += calcul1(line, 0, len(line))

    return sum


def q2(lines):
    sum = 0

    for line in lines:
        sum += calcul2(line, 0, len(line))

    return sum


print(f"Q1 : {q1(lines)}")
print(f"Q2 : {q2(lines)}")
