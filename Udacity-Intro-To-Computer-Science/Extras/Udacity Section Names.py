"""
Author:         Brian Mascitello
Date:           10/10/2017
Websites:       https://classroom.udacity.com/courses/cs101/
Info:           Udacity Section Names
Description:    While going through the cs101 course for my UC Berkeley application, I have been making notes with
    Microsoft Word. I have been manually labeling each section before taking notes in case I want to refer back to them,
    however the section names are a bit lengthy. I decided to save the raw html from chrome to my downloads folder as a
    text file, and I am attempting to parse out each section, so I just need to type the notes from lesson 10 onwards.
"""

import pyperclip  # pip install pyperclip
import re

# File location on Windows.
raw_path = r'C:\Users\Brian\Downloads\HTML.txt'

# Modified slashes so the path could be opened by Python.
fixed_path = raw_path.replace('\\', '/')

# Open the file, read it's contents, and convert to text to make regex easier.
file = open(fixed_path, encoding='utf8')
content = file.read()

# Positive Lookbehind (?<=a title=\") finds the start of the anchor titles of the sections.
# 1st Capturing Group (\d+\.\s) gets the digit, period, and space, which I am grouping to separate.
# 2nd Capturing Group (.*?) gets the information about the section. This is what I want.
# Positive Lookahead (?=\") makes sure the regex finds everything before the second quotation mark.
regex = r'(?<=a title=\")(\d+\.\s)(.*?)(?=\")'

# Finds all possible sections within the HTML.txt file contents.
matches = re.findall(regex, content)

# Creates a string that stores all of second group in the matches list, and separates by a line for pasting into Word.
copy_string = ''
for each_match in matches:
    copy_string += each_match[1] + '\n'
print(copy_string)

# Copies the copy_string to my clipboard so I can easy paste into Word.
# https://automatetheboringstuff.com/chapter18/
pyperclip.copy(copy_string)
