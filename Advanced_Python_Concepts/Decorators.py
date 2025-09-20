# Decorator is a function that takes a function, it creates a new function inside its body(wrapper). Then it returns that new function.


def decorator(func):
    def wrapper():
        print("I am about to execute a function....")
        func()
        print("I have executed this function....")
    return wrapper

@decorator
def say_hello():
    print("Helloo")

say_hello()
# f = decorator(say_hello)
# f()

'''
Decorators with Arguments:
'''

def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return decorator
@repeat(7)
def say_hey(a):
    print(f"Helloo! {a}")

say_hey("Sameer")


            