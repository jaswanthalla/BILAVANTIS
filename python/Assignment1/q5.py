# 5. Store the length and breadth of a rectangle. Calculate Area and Perimeter
# Then determine the result using appropriate arithmetic operators.

length = int(input("enter the length of the Rectangle:"))
breadth = int(input("enter the breadth of the Rectangle:"))

area = length * breadth
perimeter = 2 * (length + breadth)

print("The area of rectangle is ", area)
print("The perimeter of rectangle is ", perimeter)
