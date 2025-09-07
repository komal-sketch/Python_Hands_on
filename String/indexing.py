# Each character in a string has an index:

name = "Python"
print(name[0]) # 0 means 1st character will be printed
print(name[5])

''' P   y   t   h   o   n
    0   1   2   3   4   5
   -6  -5  -4  -3  -2  -1  Negative indexing

To convert -ve indexing to +ve indexing add length of the string to that number.
ex: -3+6 = 3 '''
 
print(name[-6])


