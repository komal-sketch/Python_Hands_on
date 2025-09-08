''' Why docstrings?
we sometimes want to attach information.
'''




def sum(a, b):
    ''' This will give sum of 2 numbers''' # it should be right after defining function.
    c = a + b
    return c

print(sum.__doc__)

# output : This will give sum of 2 numbers