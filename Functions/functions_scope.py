# function scope and lifetime

''' A variable is destroyed as soon as a function halts means:
In Python, when you define a variable inside a function, it is 
called a local variable. Local variables only exist while the 
function is running. As soon as the function finishes executing, 
those variables are destroyed and their memory is released.
'''
def sum(a, b):
    # a and b are local variables accessible inside the function.
    c = a + b
    return c

print(sum(4, 5))
print(c) 

''' not defined error because after print(sum(4, 5))  values of a, b, c are returned and wiped out after. which means function only keeps variables until it returns
'''

# Global variables

def sum(c, d):
    e = c + d
    print(z)
    return e

z = 8             # z is a global variable
print(sum(2, 3))



