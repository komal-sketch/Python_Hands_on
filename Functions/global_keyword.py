def sum(a, b):
    c = a + b
    print("Hello Python")
    global z # telling python inerpreter to modify global z
    z = 0  # This will refer to global z and not create a local variable.

    return c

z = 8
print(sum(2, 3))
print(z)


'''output: 
Hello Python
5
0
'''

