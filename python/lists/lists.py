list = [1, 2, 3, 5, "rajesh", "ramesh", "suresh", "rajesh", {1: "a", 2: "b"}]
print(type(list))

list.append("hello")
print(list)

x = list.copy()
print(x)

count = list.count("rajesh")
print(count)

bilvantis = [2, 2, 4]
list.extend(bilvantis)
print(bilvantis)

a = list.index(3)
print(a)

length = len(list)
print(length)

x = []
x = list[1:6:1]
print(x)

print(list[8][1])
list = ["apple", "banana", "cherry"]
print(list[-1])

if "bilavantis" in list:
    print("yes")
else:
    print("no")

lists = [2]

print(lists)

a = 500 * 90
print(a)


newlist = []

for x in list:
    if "a" in x:
        newlist.append(x)
print(newlist)


b = [1, 2, 3, 4, [123, 3, 34, 5, [1, 2]]]
print(b[4][4])
