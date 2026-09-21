# 14. Create: analyze_number(num)
# The function should determine:
# * Whether the number is positive, negative, or zero.
# * Whether it is even or odd.
# * Whether it is divisible by both 3 and 5.
# Return/display all the results.
# Example:
# Number: 30
# Positive
# Even
# Divisible by both 3 and 5


def analyze_number(num):
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")

    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

    if num % 3 == 0 and num % 5 == 0:
        print("Divisible by both 3 and 5")


analyze_number(30)
