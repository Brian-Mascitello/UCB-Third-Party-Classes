# Write a program that returns the number of edges
# in a star network that has `n` nodes


def star_network(n):
    # return number of edges
    if n < 2:
        return 0
    return n - 1


for x in range(5):
    print(x, star_network(x))
