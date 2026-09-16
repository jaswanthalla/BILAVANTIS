# 15. Modify a List Using Slicing
# numbers = [10, 20, 30, 40, 50]
# Use slice assignment to replace:
# 20, 30
# with:
# 200, 300, 400
# Display the final list.

numbers = [10, 20, 30, 40, 50]
numbers[1:2] = [200, 300, 400]
print(numbers)
