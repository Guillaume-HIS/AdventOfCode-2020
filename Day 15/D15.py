import time

with open("input", "r") as file:
    spoken = file.read().splitlines()
    spoken = [int(line) for line in spoken]


def q1_and_2(max):
    deja_vu = {x: i + 1 for i, x in enumerate(spoken)}
    last = spoken[-1]
    for k in range(len(spoken) + 1, max + 1):
        if last in deja_vu.keys():
            current = k - 1 - deja_vu[last]
        else:
            current = 0
        deja_vu[last] = k - 1
        last = current

    return last


print(f"Q1 : {q1_and_2(2020)}")
ping = time.time()
print(f"Q2 : {q1_and_2(30_000_000)}")
pong = time.time()
print(pong - ping)
