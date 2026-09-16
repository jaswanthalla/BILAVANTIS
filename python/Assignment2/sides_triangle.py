# 6. Accept three sides of a triangle. First check whether the three sides can form a valid triangle. If valid, determine whether it is:

# * Equilateral
# * Isosceles
# * Scalene

# Hint: A triangle is valid only when the sum of any two sides is greater than the third side.

a = float(input("enter side a :"))
b = float(input("enter side b :"))
c = float(input("enter side c :"))

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
