class employee():
    company = "Google"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"The name is {self.name} and the salary is {self.salary}"
        

e = employee("Jack", 2000000)
print(e.name, e.salary)
print(str(e))

