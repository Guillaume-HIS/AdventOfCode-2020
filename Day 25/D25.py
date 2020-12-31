with open("input.txt", "r") as file:
    data = file.read().splitlines()
    card_pub = int(data[0])
    door_pub = int(data[1])

SUBJ_NBR = 7
DIVIDER = 20201227


def loop_size(pub_key):
    loopsize = 0
    tmp = 1
    while tmp != pub_key:
        tmp = (tmp * SUBJ_NBR) % DIVIDER
        loopsize += 1
    return loopsize


def enc_key(pub_key, loopsize):
    tmp = 1
    for _ in range(loopsize):
        tmp = (tmp * pub_key) % DIVIDER
    return tmp


if __name__ == "__main__":
    print(enc_key(door_pub, loop_size(card_pub)))
