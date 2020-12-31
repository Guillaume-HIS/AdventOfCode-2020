with open("input.txt", 'r') as file:
    inp = [int(x) for x in file.read()]


def rnd(cups):

    current, picked = cups[0], cups[1:4]
    cups = cups[4:] + [current]
    current = current - 1 if current > 0 else max(cups) - 1

    while current not in cups:
        current = current - 1 if current > 0 else current + max(cups)

    for k in reversed(picked):
        cups.insert(cups.index(current) + 1, k)

    return cups


def q1(data):

    for z in range(100):
        data = rnd(data)

    ans = data[data.index(1) + 1:] + data[:data.index(1)]
    ans = [str(x) for x in ans]

    return "".join(ans)


print(f"Q1 : {q1(inp)}")
