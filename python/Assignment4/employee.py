class Employee:
    def __init__(self, name, age=None):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Good morning {self.name}")


obj = Employee("Jayanth", 23)
obj1 = Employee("AJ")
obj.greet()
obj1.greet()
