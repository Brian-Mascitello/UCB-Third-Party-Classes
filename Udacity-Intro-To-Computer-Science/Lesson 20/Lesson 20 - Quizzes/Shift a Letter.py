# Write a procedure, shift, which takes as its input a lowercase letter,
# a-z and returns the next letter in the alphabet after it, with 'a'
# following 'z'.

alphabet = dict()
for letter in range(ord('a'), ord('z')):
    alphabet[chr(letter)] = chr(letter + 1)
alphabet['z'] = 'a'


def shift(letter):
    return alphabet[letter]


print(shift('a'))
# >>> b
print(shift('n'))
# >>> o
print(shift('z'))
# >>> a
