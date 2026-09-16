# 30. data = "10,20,30,40,50,20,30"
# 1. Convert the string into a list of numbers.
# 2. Convert the list into a set to remove duplicates.
# 3. Convert the set into a tuple.
# 4. Display the final tuple.
# 5. Display the number of unique values.
# 6. Display the maximum and minimum values.
# 7. Display the tuple in reverse using slicing.

data = "10,20,30,40,50,20,30"

data = data.split(",")
print(data)

new_data = []
for i in data:
    new_data.append(int(i))

print(new_data)

data = set(new_data)
print(data)

data = tuple(data)
print(data)

length = len(data)
print(length)

maximum = max(data)
print(maximum)

minimum = max(data)
print(minimum)

data = data[::-1]
print(data)
