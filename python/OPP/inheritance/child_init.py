class Parent:
    def __init__(self, name):
        self.name = name


class Child(Parent):  # Inherits from Parent
    def __init__(self, name, age):
        super().__init__(name)  # Call Parent's __init__
        self.age = age



c = Child("Bob", 12)
print(c.name)  
print(c.age)  
