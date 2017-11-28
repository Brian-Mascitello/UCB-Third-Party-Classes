#
# How many edges in a complete graph on n nodes?
#


def clique(n):
    # Return the number of edges
    # Try to use a mathematical formula...
    edges = sum(range(0, n))
    return edges


for x in range(6):
    print(str(x) + '\t' + str(clique(x)))
