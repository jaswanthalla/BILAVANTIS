with open("file.txt", "a") as f:
    f.write(
        "this is the appended line and this is added to the text in the end of the file\n"
    )
with open("file.txt") as f:
    context = f.read()
    print(context)

with open("file.txt") as f:
    for x in f:
        print(x)


f = open("file.txt")
print(f.read())
