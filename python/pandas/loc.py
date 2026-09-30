import pandas as pd

data = {
    "Name": ["anya", "rakesh", "yash"],
    "Age": [25, 30, 35],
    "City": ["Hyderabad", "Delhi", "Mumbai"],
}
df = pd.DataFrame(data, index=["a", "b", "c"])

print("DataFrame:")
print(df)

print(df.loc["a"])  # Row with index label "a"
print(df.loc["a", "Name"])  # Specific cell by label
print(df.loc[:, "City"])  # Entire "City" column
