class employee:
    company = "Asus"  # This is class attribute.

    def __init__(self, salary, name, bond, company):
        self.salary = salary
        self.name = name
        self.bond = bond
        self.company = company

    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"The name of the employee is {self.name}. His salary is {self.salary}. The bond is for {self.bond} years")

e1 = employee(2000000, "Sameer", 2, "Tesla")
e1.get_info()
print(e1.company) # will always print instance attribute whenvever present
    

# Object introspection : to fins out all methods and attributes an object has in Python

print(dir(e1))
print(employee.company) # this will print the class attribute
