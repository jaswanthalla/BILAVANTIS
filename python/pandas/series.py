import pandas as pd

df = pd.read_csv("data.csv")

id = df["Restaurant ID"]
print(id)

# Create a Series from a Python list
numbers = [10, 20, 30, 40, 50]
s = pd.Series(numbers)

print(s)

print(s[0])