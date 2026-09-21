# 10. Create: triangle_type(a, b, c)
# First determine whether the three sides form a valid triangle.
# If valid, return:
# Equilateral
# Isosceles
# Scalene
# If invalid, return:
# Invalid Triangle
# Example:
# triangle_type(10, 10, 10)
# Output:
# Equilateral


def triangle_type(a, b, c):
    if (a + b > c) and (b + c > a) and (a + c > b):
        print("valid triangle")
        if a == b == c:
            print("Equilateral triangle")
        elif a != b != c:
            print("Scalene")
        else:
            print("Isosceles")
    else:
        print("invalid triangle")


a = float(input("enter side a :"))
b = float(input("enter side b :"))
c = float(input("enter side c :"))

triangle_type(a, b, c)
