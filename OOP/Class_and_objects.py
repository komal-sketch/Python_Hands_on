
class employee:
    company = "Oracle"

    def get_salary(self):   # self is a way to reference the obj of the class which is being created.
        return 2000000
    
e = employee()   # an obj of class emoloyee is created here
print(e.get_salary()) # employee e's gat salary method is called.

e2 = employee()
print(e.company)
print(e2.get_salary())


