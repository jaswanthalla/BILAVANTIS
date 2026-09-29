import csv

with open("abc.csv", "r") as f:
    reader = csv.reader(f)
    for ro in reader:
        print(ro)
