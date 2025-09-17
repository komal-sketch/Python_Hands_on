
class Animal:  # Parent class (Super class)
    location = "Austria"
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Speaking now...")

class Dog(Animal): # This in inheritance
    def speak(self):
        super().speak()  # We are using the speak function of the parent class.
        print("Woof!")

d = Dog("Bruno")
d.speak()
print(d.location)


    
