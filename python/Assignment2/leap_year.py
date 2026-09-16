# 4. Write a program to determine whether a given year is a leap year.
# Hint: A leap year has a special relationship with divisibility by `4`, `100`, and `400`.

year = int(input("enter the year:"))

if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")