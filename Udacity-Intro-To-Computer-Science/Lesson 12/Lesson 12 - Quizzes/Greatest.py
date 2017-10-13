# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.


def greatest(list_of_numbers):
    maximum = 0
    for number in list_of_numbers:
        if maximum < number:
            maximum = number
    return maximum


# print greatest([4,23,1])
# >>> 23
# print greatest([])
# >>> 0

print(greatest([4, 23, 1]))

print(greatest([]))
