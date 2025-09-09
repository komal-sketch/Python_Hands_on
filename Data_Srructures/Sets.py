
'''
sets are :
unordered
unique collections (no duplicates)
'''

s  = {3, 6, 9, 99}
print(s, type(s))

# print(s[2]) # Error: because sets are unordererd.

# set Methods

s.add(32)
print(s)

s.remove(6)
print(s)

s.pop()
print(s) # random  number will be removed


# Set Operations:

a = {33, 55, 66, 999}
b = {333, 555, 999, 666}

c = a.union(b)

print(c)

d = a.intersection(b)
print(d)

e = a.difference(b)
print(e)







