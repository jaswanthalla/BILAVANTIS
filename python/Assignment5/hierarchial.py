# Parent class
class Shape:
    def draw(self):
        print("Drawing a generic shape")


# Child class 1
class Circle(Shape):
    def draw(self):
        print("Drawing a circle")


# Child class 2
class Square(Shape):
    def draw(self):
        print("Drawing a square")


# Child class 3
class Triangle(Shape):
    def draw(self):
        print("Drawing a triangle")


c = Circle()
s = Square()
t = Triangle()

c.draw()
s.draw()
t.draw()
