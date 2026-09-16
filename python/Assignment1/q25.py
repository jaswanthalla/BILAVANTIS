# 25.
# student = {
#     "name": "Rahul",
#     "age": 20,
#     "course": "Python",
#     "marks": 85
# }
# Use appropriate dictionary methods to display:
# * All keys
# * All values
# * All key-value pairs
# * Value of `"name"` using `get()`
# * Remove `"age"`
# * Add `"city"`

student = {"name": "Rahul", "age": 20, "course": "Python", "marks": 85}

keys = student.keys()
values = student.values()

print(keys)
print(values)

items = student.items()
print(items)

name = student.get("name")
print(name)

student.pop("age")
print(student)

student["city"] = "Hyderabd"

print(student)
