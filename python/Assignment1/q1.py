# 1. Create variables to store your name, age, height, and city. Print them in a meaningful format using string formatting methods. 

name = input("enter the name:")
age = int(input("enter the age:"))
height = float(input("enter the height:"))
city = input("enter the city:")

print(f"My name is {name}")
print(f"My age is {age}")
print(f"My height is {height}")
print(f"My city is {city}")

print("my name is {}".format(name))
print("my age is {}".format(age))
print("my height is {}".format(height))
print("my city is {}".format(city))
