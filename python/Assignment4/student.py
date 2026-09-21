# 1. Student Management System
# Problem Statement:
# Create a Student class with attributes name and age. Add a method greet() that prints a personalized greeting. Instantiate multiple student objects and call their methods.


class Student:
    def __init__(self, name, age):  # initialises attribute
        self.name = name
        self.age = age

    # instance method
    def greet(self):
        print(f"hello {self.name}")


# creating objects
obj1 = Student("Rajesh", 34)
obj2 = Student("Ramesh", 32)
obj3 = Student("Rakesh", 31)
obj1.greet()
obj2.greet()
obj3.greet()
