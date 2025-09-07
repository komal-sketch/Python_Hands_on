#defining a function

def average(a, b, c):
    d = (a + b +c)/3.0
    print(d)

#calling the function and passing values to the function
average(5, 4, 1)
average(1, 2, 3)

o1 = average(5, 4, 1)
o2 = average(1, 2, 3)
print(o1)            # output = none

# if i want to give value of d to o1 thn i have to return the value and not print.

def average(k, p, f):
    s = (k + p + f)/3.0
    return s             # return is a reserved keyword in Python

average(1, 2, 3)

a1 = average(1, 2, 3)
print(f"avg is", a1)

