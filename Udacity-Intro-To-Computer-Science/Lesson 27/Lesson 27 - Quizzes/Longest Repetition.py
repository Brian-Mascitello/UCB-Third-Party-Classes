# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a
# list, and returns the element in the list that has the most
# consecutive repetitions. If there are multiple elements that
# have the same number of longest repetitions, the result should
# be the one that appears first. If the input list is empty,
# it should return None.


def longest_repetition(input_list):
    if not input_list:
        return None
    else:
        chain = 0
        element = input_list[0]
        max_chain = 0
        max_element = input_list[0]
        for item in input_list:
            if element == item:
                chain += 1
                if chain > max_chain:
                    max_chain = chain
                    max_element = element
            else:
                chain = 1
                element = item
        return max_element


# For example,

print(longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1]))
# 3

print(longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd']))
# b

print(longest_repetition([1, 2, 3, 4, 5]))
# 1

print(longest_repetition([]))
# None
