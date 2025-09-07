Why Python?
Python is a high-level, interpreted programming language known for its simplicity and readability.
It is widely used in:
 -Web Development (Django, Flask)
 -Data Science and Machine Learning (Pandas, NumPy, TensorFlow)
 -Automation and Scripting
 -Game Development (Pygame)
 -Python has a large community and extensive libraries, making it beginner-friendly.
--------------------------------------------------------------------------------------------------------------------------------
Install Python:
Run the installer and ensure you check the box to Add Python to PATH (important for running Python from the command line).
Verify Installation:
 python --version
--------------------------------------------------------------------------------------------------------------------------------
*Understanding Python Syntax and Basics
 1. Python Syntax Rules
Indentation: Python uses indentation (spaces or tabs) to define blocks of code.
Whitespace: Python is sensitive to whitespace. Ensure consistent indentation to avoid errors. Ideally, use 4 spaces for indentation.
Statements: Each line of code is a statement. You can write multiple statements on one line using a semicolon (; ), but this is not recommended.
Comments:
1. Use # for single-line comments.
2. Use''' or """ for multi-line comments.

---------------------------------------------------------------------------------------------------------------------------------
                                                      Python Fundamentals:
Variables and Data Types in Python:
*What are Variables?
Variables are used to store data that can be used and manipulated in a program. A variable is created when you assign a value to it using the = operator.
Example:
 name = "Alice"
 age = 25
 height = 5.6

*Variable Naming Rules
Variable names can contain letters, numbers, and underscores. 
Variable names must start with a letter or underscore. 
Variable names are case-sensitive. 
Avoid using Python keywords as variable names (e.g., print, if, else)

*Best Practices  
Use descriptive names that reflect the purpose of the variable.
Use lowercase letters for variable names. 
Separate words using underscores for readability (e.g., first_name , total_amount ).
----------------------------------------------------------------------------------------------------------------------------------------------------------------

# 🐍 Functions and Modules in Python

## Table of Contents
1. [Defining Functions](#1-defining-functions-in-python)
2. [Function Arguments & Return Values](#2-function-arguments--return-values)
3. [Lambda Functions](#3-lambda-functions-in-python)
4. [Recursion](#4-recursion-in-python)
5. [Modules and Pip](#5-modules-and-pip---using-external-libraries)
6. [Function Scope and Lifetime](#6-function-scope-and-lifetime)
7. [Docstrings](#7-docstrings---writing-function-documentation)
8. [Summary](#summary)

---

## 1. Defining Functions in Python
Functions help in reusability and modularity in Python.

**Syntax:**
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!

Key Points:

-Defined using the def keyword.
-Function name should be meaningful.
-Use return to send a value back.

2. Function Arguments & Return Values
Functions can take parameters and return values.
# Types of Arguments:
i. Positional Arguments

def add(a, b):
    return a + b

print(add(5, 3))  # Output: 8

ii. Default Arguments:

def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet())  # Output: Hello, Guest!

iii. Keyword Arguments

def student(name, age):
    print(f"Name: {name}, Age: {age}")

student(age=20, name="Bob")

3. Lambda Functions in Python: Lambda functions are anonymous, inline functions.
square = lambda x: x * x
print(square(4))  # Output: 16

numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16]

4. Recursion in Python: A function calling itself to solve a problem.
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))  # Output: 120

Important Notes:
                -Must have a base case to avoid infinite recursion.
                -Used in algorithms like Fibonacci, Tree Traversals.

5. Modules and Pip - Using External Libraries:
Importing Modules:
                   import math
                   print(math.sqrt(16))  # Output: 4.0
Creating Your Own Module:
                         def greet(name):
                          return f"Hello, {name}!"
Import in another file:
                       import mymodule
                       print(mymodule.greet("Alice"))  # Output: Hello, Alice!
Installing External Libraries with pip:
                                       pip install requests

6. Function Scope and Lifetime: Variables in Python have scope (where they can be accessed) and lifetime (how long they exist).
Types of Scope:
               -Local Scope: Variables declared inside a function, accessible only within it.
               -Global Scope: Variables declared outside any function, accessible everywhere.
Example: Local vs Global Scope:
                               x = 10  # Global variable

                               def my_func():
                                  x = 5  # Local variable
                                  print(x)  # Output: 5

                               my_func()
                               print(x)  # Output: 10
Using the global Keyword:
                         x = 10  # Global variable

                         def modify_global():
                             global x
                             x = 5

                          modify_global()
                          print(x)  # Output: 5
Note: Excessive use of global variables is discouraged.

7. Docstrings - Writing Function Documentation: Docstrings document functions, classes, and modules. Written in triple quotes and accessible via __doc__.
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

print(add.__doc__)  # Output: Returns the sum of two numbers.

Proper Docstring Format:
def add(a, b):
    """
    Returns the sum of two numbers.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The sum of the two numbers.
    """
    return a + b

Summary
•	Functions help in reusability and modularity.
•	Functions can take arguments and return values.
•	Lambda functions are short, inline functions.
•	Recursion is a technique where a function calls itself.
•	Modules help in organizing code and using external libraries.
•	Scope and lifetime of variables decide their accessibility.
•	Docstrings are used to document functions, classes, and modules.










 
 


