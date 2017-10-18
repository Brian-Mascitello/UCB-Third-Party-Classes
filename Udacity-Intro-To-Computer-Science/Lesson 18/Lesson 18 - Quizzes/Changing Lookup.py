# Change the lookup procedure
# to now work with dictionaries.


# Tried using the one-liner if statement.
def lookup(dictionary, keyword):
    return dictionary[keyword] if keyword in dictionary else None
