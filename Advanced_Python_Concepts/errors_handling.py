# program 1.
# this will be infinite loop
while True:
    try:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        print(f"The sum is {a + b}")

    except:
        print("Some error occurred!")

'''
output: Enter the first number: 5
Enter the second number: h
Some error occurred!
'''
# program 2.

while True:
    try:
        a = int(input("Enter the 1st number: "))
        b = int(input("Enter the 2nd number: "))
        print(f"The multiply is {a * b}")

    except Exception as e:
        print("Some error occured!", e)

'''
output: Enter the 1st number: 7
Enter the 2nd number: k
Some error occured! invalid literal for int() with base 10: 'k'
'''

# Program 3. named errors

while True:
    try:
        a = int(input("Enter number one: "))
        b = int(input("Enter number two: "))
        print(f"The division is {a / b}")

    except ValueError:
        print("Please don't perform bad typecasts")

    except ZeroDivisionError:
        print("Hey! don't divide by 0")

    except Exception as e:
        print("Unknown error occured!", e)

