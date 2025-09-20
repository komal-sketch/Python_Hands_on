
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if b == 0:
    raise ValueError("Please dont divide by 0")

print(f"The division is {a / b}")