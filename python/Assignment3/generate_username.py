# 8. Create: generate_username(first_name, last_name)
# The function should:
# 1. Remove unnecessary spaces.
# 2. Convert the names to lowercase.
# 3. Take the first three characters of the first name.
# 4. Take the first three characters of the last name.
# 5. Join them to create a username.
# Example:
# First name: Rahul
# Last name: Sharma
# Output:
# rahsha
# Use string methods and slicing.


def genarate_username(first_name, last_name):
    first = first_name.strip().lower()
    last = last_name.strip().lower()
    a = first[:3]
    b = last[:3]
    username = a + b
    return username


username = genarate_username("  ajs ", " aajdjJJJdfgh")
print(username)
