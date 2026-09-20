# 1. Create a function: check_number(num)
# The function should return:
# * `"Even"` if the number is even.
# * `"Odd"` if the number is odd.
# * `"Zero"` if the number is zero.
# Example:
# check_number(25)
# Output: Odd


def check_num(num):
    if num % 2 == 0:
        return "Even"
    elif num % 2 == 1:
        return "Odd"
    else:
        return "Zero"


a = check_num(25)
print(a)
