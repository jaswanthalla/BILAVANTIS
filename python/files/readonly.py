with open("file.txt") as f:
    print(f.readline())
    print(f.readline())
    print(f.readline())


with open("file.txt") as d:
    for x in d:
        print(x)
