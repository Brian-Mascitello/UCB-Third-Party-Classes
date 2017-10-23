"""
Author:         Brian Mascitello
Date:           10/22/2017
Websites:       https://classroom.udacity.com/courses/cs101/
Info:           Python 2 print to Python 3 print()
Description:    While the class is almost over, this may be useful in the future. It will take a large, multi-line
    string of Python 2 code and convert all print statements to Python 3 print() syntax. Also it will remove hashtags
    from print lines, but maintain them for expected print results.
"""

import pyperclip  # pip install pyperclip


def get_multi_line_input():
    print("Enter the commented test code block.")
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    text = '\n'.join(lines)
    return text


python_2_code = """
# print stirling(1,1)
# >>> 1
# print stirling(2,1)
# >>> 1
# print stirling(2,2)
# >>> 1
# print stirling(2,3)
# >>> 0

# print stirling(3,1)
# >>> 1
# print stirling(3,2)
# >>> 3
# print stirling(3,3)
# >>> 1

# print stirling(4,1)
# >>> 1
# print stirling(4,2)
# >>> 7
# print stirling(4,3)
# >>> 6
# print stirling(4,4)
# >>> 1

# print stirling(5,1)
# >>> 1
# print stirling(5,2)
# >>> 15
# print stirling(5,3)
# >>> 25
# print stirling(5,4)
# >>> 10
# print stirling(5,5)
# >>> 1

# print stirling(20,15)
# >>> 452329200

# print bell(1)
# >>> 1
# print bell(2)
# >>> 2
# print bell(3)
# >>> 5
# print bell(4)
# >>> 15
# print bell(5)
# >>> 52
# print bell(15)
# >>> 1382958545
"""

python_2_code = get_multi_line_input()

copy_string = ''
for line in python_2_code.splitlines():
    if line.find('>>> ') != -1:
        line = line.replace('>>> ', '')
    elif line.startswith('#') and line.find('print') != -1:
        if line.startswith('#'):
            line = line.replace('#', '', 1)
        elif line.startswith('# '):
            line = line.replace('# ', '', 1)

    if line.find('print') != -1:
        line = line.replace('print ', 'print(', 1)
        line = line.replace(')', '))', 1)
    copy_string += line + '\n'
    print(line)

# Copies the copy_string to my clipboard so I can easy paste into Word.
# https://automatetheboringstuff.com/chapter18/
pyperclip.copy(copy_string)
