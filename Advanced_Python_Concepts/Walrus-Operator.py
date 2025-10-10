def any_func():
    print("Something....")
    print("Something....")
    print("Something....")
    print("Something....")
    print("Something....")
    return 70

# a = any_func()

if((a:=any_func())>10):
    print(a)

else:
    print("It is not greater than 10")

#----------------------------------------------------------

while(data:=input("Enter the value: ")):
    print(data)
    if data == "q":
        break


