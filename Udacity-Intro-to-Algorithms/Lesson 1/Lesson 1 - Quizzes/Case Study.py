# Just multiplies a * b
def naive(a, b):
    x = a
    y = b
    z = 0
    while x > 0:
        z = z + y
        x = x - 1
    return z


print(naive(1, 2))  # 2
print(naive(2, 3))  # 6
print(naive(3, 4))  # 12
print(naive(4, 5))  # 20
