num1 = int(input("enter 1st no.: "))
num2 = int(input("enter 2nd no.: "))

sum = num1 + num2
print(type(num1))
print("sum of nos is: ", sum)


# Conditionals

day_of_week = input("Enter the day: ").lower()
#print(day_of_week)

if day_of_week == "saturday" or day_of_week == "sunday":
    print("I wont study")
else:
    print("I will study")

#-------------------------------------------------------
# calculator

num1 = int(input("enter 1st no.: "))
num2 = int(input("enter 2nd no.: "))
choice = input("Enter your operation: (Options: +, -, *, /)")


if choice == "+":
    sum = num1 + num2 
    print("addition", sum)
elif choice == "-":
    diff = num1 - num2
    print("subtraction", diff)
elif choice == "*":
    mul = num1 * num2

    print("multiplication of the numbers is: ", mul)
else:
    print("invalid")


