# Write a procedure, count_words, which takes as input a string
# and returns the number of words in the string. You may consider words
# as strings of characters separated by spaces.


def count_words(input_string):
    words_in_string = 0
    for item in input_string.split():
        words_in_string += 1
    return words_in_string


passage = ("The number of orderings of the 52 cards in a deck of cards "
           "is so great that if every one of the almost 7 billion people alive "
           "today dealt one ordering of the cards per second, it would take "
           "2.5 * 10**40 times the age of the universe to order the cards in every "
           "possible way.")

print(count_words(passage))  # 56

message = ("As Professor Evans would say, 'Stay Udacious!'")

print(count_words(message))  # 7
