a = int(input("Enter a number between 1 to 10: "))

match a:
    case 1:
        print("You won a Fridge")
    case 3:
        print("You won a mobile charger")
    case 8:
        print("You won a car")
    case _:
        print("Better luck next time")
