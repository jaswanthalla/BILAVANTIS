# The self parameter is a reference to the current instance of the class.

# It is used to access properties and methods that belong to the class.


class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Good morning {self.name}")


obj = student("Jaswanth", 23)
obj1 = student("AJ",32)
obj.greet()
obj1.greet()
