class employee():
    company = "HP"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Instance Method (default)
    def print_info(self):
        info = f"The name is {self.name} and the salary is {self.salary}"
        print(info)

    # static method : it doesn't need self parameter.
    @staticmethod
    def sum(a, b):
        return a+b
    
    # class method
    @classmethod
    def print_company(cls):
        print(cls.company)

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company


e1 = employee("Jack", 2000000)
e2 = employee("Ryan", 3000000)

e1.print_info()
e2.print_info()

print(e2.sum(5, 23)) # static method

e1.print_company()  #Class Method

e1.change_company("Acer")
e1.print_company()







        