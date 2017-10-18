# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be positive,
# negative or zero.


def create_alphabet_dictionary():
    alphabet = dict()
    for letter in range(ord('a'), ord('z')):
        alphabet[chr(letter)] = chr(letter + 1)
    alphabet['z'] = 'a'
    return alphabet


def shift_n_letters(letter, n):
    alphabet = create_alphabet_dictionary()
    while n > 0:
        letter = alphabet[letter]
        n -= 1
    while n < 0:
        if letter == 'b':
            letter = alphabet['z']
        elif letter == 'a':
            letter = alphabet['y']
        else:
            letter = alphabet[chr(ord(letter) - 2)]
        n += 1
    return letter


print(shift_n_letters('s', 1))
# >>> t
print(shift_n_letters('s', 2))
# >>> u
print(shift_n_letters('s', 10))
# >>> c
print(shift_n_letters('s', -10))
# >>> i
