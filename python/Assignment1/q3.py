# 3. Store marks of five subjects in five variables. then Calculate and display:
# * Total marks
# * Average marks

a = int(input("Enter marks of first subject:"))
b = int(input("Enter marks of second subject:"))
c = int(input("Enter marks of third subject:"))
d = int(input("Enter marks of fourth subject:"))
e = int(input("Enter marks of fifth subject:"))

sum = a + b + c + d + e
avg = sum / 5

print("Total marks:", sum)
print("Average marks:", avg)
