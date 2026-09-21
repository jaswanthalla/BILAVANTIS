# 4. Rectangle Geometry
# Problem Statement:
# Design a Rectangle class with attributes length and width. Add methods area() and perimeter() to calculate respective values. Create multiple rectangle objects and display their area and perimeter.


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# Creating objects
r1 = Rectangle(10, 5)
r2 = Rectangle(7, 3)

print("Area:", r1.area(), "Perimeter:", r1.perimeter())
print("Area:", r2.area(), "Perimeter:", r2.perimeter())
