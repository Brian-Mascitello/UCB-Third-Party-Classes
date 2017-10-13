# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.


def symmetric(list_matrix):
    if not list_matrix:
        return True
    if len(list_matrix) != len(list_matrix[0]):
        return False
    for index in range(0, len(list_matrix)):
        for j_index in range(0, len(list_matrix)):
            if list_matrix[index][j_index] != list_matrix[j_index][index]:
                return False
    return True


print(symmetric([[1, 2, 3],
                 [2, 3, 4],
                 [3, 4, 1]]))

print(symmetric([["cat", "dog", "fish"],
                 ["dog", "dog", "fish"],
                 ["fish", "fish", "cat"]]))

print(symmetric([["cat", "dog", "fish"],
                 ["dog", "dog", "dog"],
                 ["fish", "fish", "cat"]]))

print(symmetric([[1, 2],
                 [2, 1]]))

print(symmetric([[1, 2, 3, 4],
                 [2, 3, 4, 5],
                 [3, 4, 5, 6]]))

print(symmetric([[1, 2, 3],
                 [2, 3, 1]]))
