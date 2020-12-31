def add(n):
    val = 1
    last = 1
    for _ in range(n):
        val += val + 2 * last
        last *= 2
    return val

print(add(4))

print(sum([1, 2, 3]))
