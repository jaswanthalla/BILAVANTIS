n = int(input("enter the number of elements:"))
list = []

for i in range(n):
    elements = int(input("enter the number:"))
    list.append(elements)
print(list)

list.reverse()
print(list)
reverse = []

reverse = list[::-1]
print(reverse)
