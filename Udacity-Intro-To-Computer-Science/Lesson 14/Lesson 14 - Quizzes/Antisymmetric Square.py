# By Dimitris_GR from forums
# Modify Problem Set 31's (Optional) Symmetric Square to return True
# if the given square is antisymmetric and False otherwise.
# An nxn square is called antisymmetric if A[i][j]=-A[j][i]
# for each i=0,1,...,n-1 and for each j=0,1,...,n-1.


def antisymmetric(list_matrix):
    if not list_matrix:
        return True
    if len(list_matrix) != len(list_matrix[0]):
        return False
    for index in range(0, len(list_matrix)):
        for j_index in range(0, len(list_matrix)):
            if list_matrix[index][j_index] != -list_matrix[j_index][index]:
                return False
    return True


# Test Cases:

print(antisymmetric([[0, 1, 2],
                     [-1, 0, 3],
                     [-2, -3, 0]]))
# >>> True

print(antisymmetric([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]))
# >>> True

print(antisymmetric([[0, 1, 2],
                     [-1, 0, -2],
                     [2, 2, 3]]))
# >>> False

print(antisymmetric([[1, 2, 5],
                     [0, 1, -9],
                     [0, 0, 1]]))
# >>> False
