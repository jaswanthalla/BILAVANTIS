import pandas as pd

df = pd.read_csv("sample.csv")

df = pd.read_csv("sample.csv", na_values=["NaN", "not_available"])

# new_df = df.dropna()
# print(new_df)

# df.dropna(inplace=True)
# print(df)

print("Before fillna:")
print(df)

df.fillna(22, inplace=True)

print("\nAfter fillna:")
print(df)
