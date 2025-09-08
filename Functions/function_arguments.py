# Default Arguments are optional, you can pass value to override it

def add(a, b, plus=0):
    x = a + b + plus
    return x

c = add(3, 5)
print(c)

# pass value
d = add(3, 5, 2)
print(d)


# Keyword Arguments: can change the order of arguments paasing with parameter name.
e = add(b=5, a=2)
print(e)
