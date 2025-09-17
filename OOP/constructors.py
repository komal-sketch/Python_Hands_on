# constructor is used to initialize an object

class employee():

    def __init__(self, salary, name, bond):
        self.salary = salary  # create an instance attribute of name salary and assign it with salery
        self.name = name
        self.bond = bond

    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"The name of the employee is {self.name}. Salary is {self.salary}. The bond is for {self.bond} years")

e1 = employee(2000000, "Sameer", 2)
e1.get_info()

