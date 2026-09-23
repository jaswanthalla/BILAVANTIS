class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):  # instance method
        print("Name:", self.name, "Marks:", self.marks)


s = Student("sai", 90)
s.display()
