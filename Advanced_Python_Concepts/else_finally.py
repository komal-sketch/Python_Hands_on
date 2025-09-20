# Program 1.
# you print something when there is no error

# try:
#     a = 345/10

# except Exception as e:
#     print(e)

# # below block will be executed when there is no error
# else:
#     print("Hey! I am good")

# program 2.

a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

try:
    c = a/b
    print(c)

except Exception as e:
    print(e)

finally:
    print("This is always executed")

'''
output:
Enter number one: 46
Enter number two: 0
division by zero
This is always executed
'''    