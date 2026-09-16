# 16. Create a list of numbers containing some duplicate values.
# Perform:
# * `append()`
# * `insert()`
# * `remove()`
# * `pop()`
# * `count()`
# * `index()`
# * `sort()`
# * `reverse()`
# Display the list after the operations.

numbers = [1, 2, 3, 2, 4, 5, 3, 6, 1]
print(numbers)

numbers.append(11)
print(numbers)

numbers.insert(3, 200)
print(numbers)

numbers.remove(200)
print(numbers)

numbers.pop(1)
print(numbers)

count = numbers.count(1)
print(count)

print(numbers.index(11))

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)
