numbers = [1, 2, 3, 4, 45, 21]

def square(x):
    return x * x

new = list(map(square, numbers))
print(new)


# filter

def is_greater_than_9(x):
    if x>9:
        return True
    else:
        return False
    
a = [1, 3, 5, 234, 34, 23, 6543, 21, 6, 43]

new = list(filter(is_greater_than_9, a))
print(new)


# reduce

from functools import reduce

numberss = [1, 2, 3, 4, 5, 6] 

def sum(a, b):
    return a + b

c = reduce(sum, numberss)
print(c)


