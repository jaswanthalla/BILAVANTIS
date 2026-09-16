# 27. email = "student@example.com"
# Using string methods and slicing, extract:
# Username: student
# Domain: example.com
# Do not manually create the output strings.

email = "student@example.com"

a = email.index("@")
print(a)

username = email[:7]
print(f"username:{username}")

domain = email[8:]
print(f"Domain:{domain}")

