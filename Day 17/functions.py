def find_around(point):

    around = [(point[0] + dx, point[1] + dy, point[2] + dz)
              for dx in range(-1, 2)
              for dy in range(-1, 2)
              for dz in range(-1, 2)
              if not (dx == 0 and dy == 0 and dz == 0)]

    return around


def count_active_around(point, space):

    act_around = []
    for pnt in find_around(point):
        if space.get(pnt, None) == "#":
            act_around.append(pnt)

    return len(act_around)


def cycle(space):

    new_space = {}

    for point, state in space.items():

        cnt_ar = count_active_around(point, space)

        if state == "#":
            if cnt_ar == 2 or cnt_ar == 3:
                new_space[point] = "#"
            else:
                new_space[point] = "."

            ar = find_around(point)
            for pnt in ar:
                if pnt not in space:
                    if count_active_around(pnt, space) == 3:
                        new_space[pnt] = "#"

        elif state == ".":
            if cnt_ar == 3:
                new_space[point] = "#"
            else:
                new_space[point] = "."

    return new_space


def find_around_4d(point):

    around = [(point[0] + dx, point[1] + dy, point[2] + dz, point[3] + dw)
              for dx in range(-1, 2)
              for dy in range(-1, 2)
              for dz in range(-1, 2)
              for dw in range(-1, 2)
              if not (dx == 0 and dy == 0 and dz == 0 and dw == 0)]

    return around


def count_active_around_4d(point, space):

    act_around = []
    for pnt in find_around_4d(point):
        if space.get(pnt, None) == "#":
            act_around.append(pnt)

    return len(act_around)


def cycle4d(space):

    new_space = {}

    for point, state in space.items():

        cnt_ar = count_active_around_4d(point, space)

        if state == "#":
            if cnt_ar == 2 or cnt_ar == 3:
                new_space[point] = "#"
            else:
                new_space[point] = "."
            ar = find_around_4d(point)
            for pnt in ar:
                if pnt not in space:
                    if count_active_around_4d(pnt, space) == 3:
                        new_space[pnt] = "#"

        elif state == ".":
            if cnt_ar == 3:
                new_space[point] = "#"
            else:
                new_space[point] = "."

    return new_space
