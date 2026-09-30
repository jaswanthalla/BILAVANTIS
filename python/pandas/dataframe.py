import pandas as pd

mydataset = {"cars": ["BMW", "Volvo", "Ford"], "passings": [3, 7, 2]}

myvar = pd.DataFrame(mydataset)

print(myvar)

data = {
    "Name": ["lisa", "Babu", "marlie"],
    "Age": [25, 30, 35],
    "City": ["Hyderabad", "Delhi", "Mumbai"],
}

df = pd.DataFrame(data)
print(df)

print(pd.__version__)

print(df.loc[2])
print(df.loc[[0, 1]])
