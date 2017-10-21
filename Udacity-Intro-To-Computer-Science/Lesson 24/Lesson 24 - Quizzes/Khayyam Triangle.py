# Double Gold Star

# Khayyam Triangle

# The French mathematician, Blaise Pascal, who built a mechanical computer in
# the 17th century, studied a pattern of numbers now commonly known in parts of
# the world as Pascal's Triangle (it was also previously studied by many Indian,
# Chinese, and Persian mathematicians, and is known by different names in other
# parts of the world).

# The pattern is shown below:

#                    1
#                   1 1
#                  1 2 1
#                 1 3 3 1
#                1 4 6 4 1
#                   ...

# Each number is the sum of the number above it to the left and the number above
# it to the right (any missing numbers are counted as 0).

# Define a procedure, triangle(n), that takes a number n as its input, and
# returns a list of the first n rows in the triangle. Each element of the
# returned list should be a list of the numbers at the corresponding row in the
# triangle.


def generate_row_data(previous_row):
    new_row_data = list()
    new_row_data.append(1)  # add 1 to start of new_row_data
    for x in range(0, len(previous_row) - 1):
        new_row_data.append(previous_row[x] + previous_row[x + 1])  # add inner part of new_row_data
    new_row_data.append(1)  # add 1 to end of new_row_data
    return new_row_data


def triangle(n):
    pascals_triangle = list()
    if n > 0:
        pascals_triangle.append([1])
    if n > 1:
        pascals_triangle.append([1, 1])
    row = 2
    while row < n:
        pascals_triangle.append(generate_row_data(pascals_triangle[-1]))
        row += 1
    return pascals_triangle


# For example:

# print triangle(0)
# >>> []

# print triangle(1)
# >>> [[1]]

# print triangle(2)
# >> [[1], [1, 1]]

# print triangle(3)
# >>> [[1], [1, 1], [1, 2, 1]]

# print triangle(6)
# >>> [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]

print(triangle(0))

print(triangle(1))

print(triangle(2))

print(triangle(3))

print(triangle(6))
