import pandas as pd

data = {
    "Name": ["anya", "rakesh", "yash"],
    "Age": [25, 30, 35],
    "City": ["Hyderabad", "Delhi", "Mumbai"],
}
df = pd.DataFrame(data, index=["a", "b", "c"])

print("DataFrame:")
print(df)

print(df.iloc[0])  # First row (position 0)
# print(df.iloc[0, 0])  # First cell (row 0, col 0)
# print(df.iloc[:, 2])  # Third column (position 2)
