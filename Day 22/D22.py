with open("input.txt", "r") as file:
    l_players = file.read().split("\n\n")
    player1 = l_players[0].splitlines()
    player1.pop(0)
    player1 = [int(elem) for elem in player1]
    player2 = l_players[1].splitlines()
    player2.pop(0)
    player2 = [int(elem) for elem in player2]

player1_2 = player1.copy()
player2_2 = player2.copy()


def rnd_q1(p1, p2):

    if len(p1) == 0 or len(p2) == 0:
        return False

    if p1[0] > p2[0]:
        p1.append(p1[0])
        p1.append(p2[0])
        p1.pop(0)
        p2.pop(0)

    elif p1[0] < p2[0]:
        p2.append(p2[0])
        p2.append(p1[0])
        p1.pop(0)
        p2.pop(0)

    return p1, p2


def score_calc(player):
    player.reverse()
    score = 0
    for i, v in enumerate(player):
        score += (i + 1) * v

    return score


def q1(play1, play2):

    while len(play1) > 0 and len(play2) > 0:
        play1, play2 = rnd_q1(play1, player2)

    to_cnt = play1 if len(play1) > 0 else play2

    return "Player 1" if to_cnt == play1 else "Player 2", score_calc(to_cnt)


def recursive_q2(p1, p2, deja_vu):

    while len(p1) > 0 and len(p2) > 0:

        if (tuple(p1), tuple(p2)) in deja_vu:
            return 1, p1

        deja_vu.append((tuple(p1), tuple(p2)))

        p1_c = p1.pop(0)
        p2_c = p2.pop(0)

        if len(p1) >= p1_c and len(p2) >= p2_c:
            winner, _ = recursive_q2(p1[:p1_c], p2[:p2_c], [])
        else:
            winner = 1 if p1_c > p2_c else 2

        if winner == 1:
            p1.append(p1_c)
            p1.append(p2_c)

        else:
            p2.append(p2_c)
            p2.append(p1_c)

    return (1, p1) if len(p1) > 0 else (2, p2)


ans_q1 = q1(player1, player2)
print(f"Q1 : Winner is {ans_q1[0]} with {ans_q1[1]} points")

ans_q2 = recursive_q2(player1_2, player2_2, [])
print(f"Q2 : Winner is Player {ans_q2[0]} with {score_calc(ans_q2[1])} points")
