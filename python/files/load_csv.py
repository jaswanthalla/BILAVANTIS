import pandas as pd
import csv

with open("sample.csv", "r") as f:
    reader = csv.reader(f)
    for ro in reader:
        print(ro)

df = pd.read_csv("sample.csv")
print(df.head())
