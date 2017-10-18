# Creating an Empty Hash Table
# Define a procedure, make_hashtable,
# that takes as input a number, nbuckets,
# and returns an empty hash table with
# nbuckets empty buckets.


def make_hashtable(nbuckets):
    hash_table = []
    while nbuckets > 0:
        hash_table.append([])
        nbuckets -= 1
    return hash_table


print(make_hashtable(1))
print(make_hashtable(3))
print(make_hashtable(5))
