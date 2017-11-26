# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]


def create_node_list(graph):
    """
    Creates a list of all the unique nodes found inside graph.
    :param graph:
    :return:
    """
    node_list = list()
    for item in graph:
        for node in item:
            if node not in node_list:
                node_list.append(node)
    node_list.sort()
    return node_list


def find_eulerian_tour(graph):
    """
    Finds an Eulerian Tour within the given graph.
    :param graph:
    :return:
    """

    # It is not perfect, as it should be able to find the tour no matter the starting point on a valid graph, but the
    # idea was if for whatever reason a starting node did not work, it would try the next one in the graph and hopefully
    # find a valid tour. The flaw comes with having an optimized for loop always taking the first traversable edge,
    # rather than building a queue of possible paths and iterating through them. Still going to upload this version, but
    # maybe tackle it properly in the future.

    tour = list()

    # Loops that will change the starting node in the tour.
    for edge in graph:
        for node in edge:
            # Copy the graph and remove the edge in use.
            temp_graph = list(graph)  # graph.copy()  # changed for Udacity interpreter

            # node is where we start!
            tour.append(node)

            # Add second node to tour.
            if node == edge[0]:
                location = edge[1]
                tour.append(location)
            else:
                location = edge[0]
                tour.append(location)
            temp_graph.remove(edge)

            last_size = len(temp_graph) + 1  # last_size ensures while loop does not iterate over the same nodes.
            while 0 < len(temp_graph) < last_size:
                last_size = len(temp_graph)  # helped in test 2, first try with node 0 got stuck with last 4 edges.
                for temp_edge in temp_graph:
                    if location in temp_edge:
                        if location == temp_edge[0]:
                            location = temp_edge[1]
                            tour.append(location)
                        else:
                            location = temp_edge[0]
                            tour.append(location)
                        temp_graph.remove(temp_edge)
            if not temp_graph:
                return tour
            else:
                tour = list()  # tour.clear()  # changed for Udacity interpreter
    return tour


def test():
    graph = [(1, 2), (2, 3), (3, 1)]
    return find_eulerian_tour(graph)


def test_2():
    graph = [(0, 1), (1, 5), (1, 7), (4, 5), (4, 8), (1, 6), (3, 7), (5, 9), (2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]
    return find_eulerian_tour(graph)


def test_3():
    graph = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (0, 6)]
    return find_eulerian_tour(graph)


def test_4():
    graph = [(1, 13), (1, 6), (6, 11), (3, 13), (8, 13), (0, 6), (8, 9), (5, 9), (2, 6), (6, 10), (7, 9), (1, 12),
             (4, 12), (5, 14), (0, 1), (2, 3), (4, 11), (6, 9), (7, 14), (10, 13)]
    return find_eulerian_tour(graph)


def test_5():
    graph = [(8, 16), (8, 18), (16, 17), (18, 19), (3, 17), (13, 17), (5, 13), (3, 4), (0, 18), (3, 14), (11, 14),
             (1, 8), (1, 9), (4, 12), (2, 19), (1, 10), (7, 9), (13, 15), (6, 12), (0, 1), (2, 11), (3, 18), (5, 6),
             (7, 15), (8, 13), (10, 17)]
    return find_eulerian_tour(graph)


print(test())

# Verified in Wolfram that it is possible. Looked good by hand wanted to be sure.
# 0 <-> 4, 4 <-> 2, 2 <-> 5, 5 <-> 9, 9 <-> 8, 8 <-> 4, 4 <-> 5, 5 <-> 1, 1 <-> 6, 6 <-> 3, 3 <-> 7, 7 <-> 1, 1 <-> 0
print(test_2())

print(test_3())

print(test_4())

print(test_5())
