def count_around(y, x, item):
    lst = []
    try:
        if matrix[y - 1][x - 1] == item:
            lst.append(item)
    except:
        lst.append(0)
    try:
        if matrix[y - 1][x] == item:
            lst.append(item)
    except:
        lst.append(0)
    try:
        if matrix[y - 1][x + 1] == item:
            lst.append(item)
    except:
        lst.append(0)
    try:
        if matrix[y][x - 1] == item:
            lst.append(item)
    except:
        lst.append(0)
    try:
        if matrix[y][x + 1] == item:
            lst.append(item)
    except:
        lst.append(0)
    try:
        if matrix[y + 1][x - 1] == item:
            lst.append(item)
    except:
        lst.append(0)
    try:
        if matrix[y + 1][x] == item:
            lst.append(item)
    except:
        lst.append(0)
    try:
        if matrix[y + 1][x + 1] == item:
            lst.append(item)
    except:
        lst.append(0)

    return lst.count(item)

matrix = [[1234]]