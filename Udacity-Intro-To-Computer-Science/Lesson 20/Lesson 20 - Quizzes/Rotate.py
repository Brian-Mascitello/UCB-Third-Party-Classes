# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.


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


def rotate(input_string, steps):
    output_string = ''
    for letter in input_string:
        if letter == ' ':
            output_string += letter
        else:
            output_string += shift_n_letters(letter, steps)
    return output_string


print(rotate('sarah', 13))
# >>> 'fnenu'
print(rotate('fnenu', 13))
# >>> 'sarah'
print(rotate('dave', 5))
# >>>'ifaj'
print(rotate('ifaj', -5))
# >>>'dave'
print(rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
              "sv rscv kf ivru kyzj"), -17))
# >>> ???
# if your code works correctly you should be able to read this
