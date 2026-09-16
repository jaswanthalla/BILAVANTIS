# 13. Create a list containing five shopping items.
# Perform the following operations:
# * Add one item to the end
# * Add one item at a specific position
# * Remove one item
# * Display the first item
# * Display the last item
# * Display the first three items
# * Display the list in reverse

# n = 5
# if 1 < n:
#     items_list = []
#     for i in range(5):
#         items = input(f"Enter shopping item no {i + 1}:")
#         items_list.append(items)
# print(items_list)


list = ["belt", "shoes", "laptop", "mobile", "pendrive"]
print(list)

list.append("socks")
print(list)

list.insert(4, "bottle")
print(list)

list.pop()
print(list)

first_three = list[:3]
print(first_three)

reverse_list = list[::-1]
print(reverse_list)
