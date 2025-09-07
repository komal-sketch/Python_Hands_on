name = "Python12345"
print(name[0:3]) # it will go from 0 to n-1 i.e 3-1=2

# output : Pyt

print(name[2:-5]) # same as [2:1]

# output : thon
#---------------------------------------------------

# slicing in steps
# print(name[0:10:n])  Skip n-1 characters

print(name[0:10:1]) #Skip 0 characters output : Python1234
print(name[0:10:2])  # output : Pto13
print(name[0:11:4]) # output : Po3

print(name[:5]) #replace the first empty number with 0
print(name[0:]) # replace the last empty with string length, output : Python12345

