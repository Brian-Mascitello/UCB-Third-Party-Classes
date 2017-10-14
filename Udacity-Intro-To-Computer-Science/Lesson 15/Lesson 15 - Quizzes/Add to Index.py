# Define a procedure, add_to_index,
# that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

# If the keyword is already
# in the index, add the url
# to the list of urls associated
# with that keyword.

# If the keyword is not in the index,
# add an entry to the index: [keyword,[url]]

index = []


def add_to_index(index, keyword, url):
    added = False  # could have used return instead
    for element in index:
        if element[0] == keyword:
            element[1].append(url)
            added = True
            break
    if not added:
        index.append([keyword, [url]])


# add_to_index(index,'udacity','http://udacity.com')
# add_to_index(index,'computing','http://acm.org')
# add_to_index(index,'udacity','http://npr.org')
# print index
# >>> [['udacity', ['http://udacity.com', 'http://npr.org']],
# >>> ['computing', ['http://acm.org']]]

add_to_index(index, 'udacity', 'http://udacity.com')
add_to_index(index, 'computing', 'http://acm.org')
add_to_index(index, 'udacity', 'http://npr.org')

print(index)
