# Define a procedure, abbaize, that takes
# two strings as its inputs, and returns
# a string that is the first input,
# followed by two repetitions of the second input,
# followed by the first input.


def abbaize(first_string, second_string):
    return first_string + second_string + second_string + first_string


# print abbaize('a','b')
# >>> 'abba'

# print abbaize('dog','cat')
# >>> 'dogcatcatdog'

print(abbaize('a', 'b'))

print(abbaize('dog', 'cat'))
