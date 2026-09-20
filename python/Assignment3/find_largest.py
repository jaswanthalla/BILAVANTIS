# 2. Create a function: find_largest(a, b, c)
# The function should return the largest of the three numbers.
# **Restriction:** Do not use `max()`.
# Example:
# find_largest(25, 10, 18)
# Output: 25


def find_largest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


largest = find_largest(25, 10, 18)
print(largest)
