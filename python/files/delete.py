import os

if os.path.exists("mynewfile.txt"):
    os.remove("mynewfile.txt")
else:
    print("The file does not exist")
