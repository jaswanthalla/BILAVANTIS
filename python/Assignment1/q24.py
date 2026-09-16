# 24.Create a dictionary containing:
# Name
# Age
# Course
# Marks
# City
# Display each value using its corresponding key.
# Then:
# * Update the marks
# * Add a new key called `"Grade"`
# * Display the final dictionary

dict = {
    "Name": "jaswanth",
    "Age": 23,
    "Course": "Databricks",
    "Marks": 87,
    "city": "Hyderabad",
}
k = dict.keys()
print(k)

v = dict.values()
print(v)

for keys, values in dict.items():
    print(f"{keys}:{values}")

city = dict.get("city")
print(city)
marks = dict.get("Marks")
print(marks)


dict.update({"Marks": 90})
dict["Marks"] = 98

dict["Grade"] = "A"

print(dict)
