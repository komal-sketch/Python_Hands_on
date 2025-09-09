'''Tuples are ordered but immutable collections(cannot be changed after creation).
We use tuples where we dont want our list to change accidently'''

# Tuples:

tuple = (3, 5, 9)
single_element = (3, ) # Tuple with one element (comma required)

print(single_element)

# Unpacking of Tuples:

tu = (33, 55, 99)
a, b, c = tu

print(a, b, c)

# Tuple Methods:

t = (4, 9, 8, 9, 10, 11)

print(t.count(9))  # number of occurances of 9
print(t.index(9))  # index of forst occurance of 9 which is 1


'''
Why use Tuples?
* Faster than lists(since they are immutable)
* Used as Dictionary keys (since they are hashable)
* Safe from unintended modifications
'''