# counting steps in naive as a function of a


def naive(a, b):
    x = a
    y = b
    z = 0
    while x > 0:
        z = z + y
        x = x - 1
    return z


def time(a):
    # The number of steps it takes to execute naive(a, b)
    # as a function of a
    steps = 2 * a + 3
    return steps


print(naive(10, 10))

print(time(10))
