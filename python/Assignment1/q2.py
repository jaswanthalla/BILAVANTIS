# 2. Take two numbers and swap their values without using a third variable.
# Example:
# Before swapping:
# a = 10
# b = 20
# After swapping:
# a = 20
# b = 10

a = int(input("Enter first number:"))
b = int(input("Enter second number: "))

print("Before swapping " + "a is", a, "b is ", b)

a = a + b
b = a - b
a = a - b

print("After swapping " + "a is", a, "b is ", b)
