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
df = df.rename(columns={"ID": "id"})
print(df)

df = df.drop(columns=["Email"])
print(df)
df["Age"] = pd.to_numeric(df["Age"], errors="coerce").fillna(0).astype(int)
df["Age"] = df["Age"].apply(lambda x: x + 1)

print(df)
