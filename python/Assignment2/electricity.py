# 5. Accept the number of electricity units consumed and calculate the bill using these rates:

# | Units           | Rate        |
# |  | -- |
# | First 100 units | ₹2 per unit |
# | Next 100 units  | ₹3 per unit |
# | Above 200 units | ₹5 per unit |

# Write a program using conditional statements to calculate the total bill.

# Example:
# Units consumed: 250

units = int(input("enter the no of electricity units consumed:"))

if units > 0 and units <= 100:
    units = units * 2
    print(units)
elif units > 100 and units <= 200:
    units = (100 * 2) + (units - 100) * 3
    print(units)
else:
    units = (100 * 2) + (100 * 3) + (units - 200) * 5
    print(units)
