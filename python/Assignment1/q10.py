# 10. Username Generator
# full_name = "John Smith"
# Create a username using slicing and string methods.
# Expected format:
# john_smith

full_name = "John Smith"
parts = full_name.split()
print(parts)

first = parts[0].lower()
print(first)

second = parts[1].lower()
print(second)

username = f"{first}_{second}"

print(username)

a="bilavantis"
print(a.split())