# Define a function, hash_string,
# that takes as inputs a keyword
# (string) and a number of buckets,
# and returns a number representing
# the bucket for that keyword.


def hash_string(keyword, buckets):
    hash_value = 0
    for letter in keyword:
        hash_value += ord(letter)  # add up the ordinal value of all letters in keyword
    hash_value %= buckets  # find remainder of hash_value with respect to buckets
    return hash_value


# print hash_string('a',12)
# >>> 1

# print hash_string('b',12)
# >>> 2

# print hash_string('a',13)
# >>> 6

# print hash_string('au',12)
# >>> 10

# print hash_string('udacity',12)
# >>> 11

print(hash_string('a', 12))
# >>> 1

print(hash_string('b', 12))
# >>> 2

print(hash_string('a', 13))
# >>> 6

print(hash_string('au', 12))
# >>> 10

print(hash_string('udacity', 12))
# >>> 11
