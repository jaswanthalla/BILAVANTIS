with open("mynewfile.txt", "w") as g:
    g.write("this is the first line\n")
    g.write("this is the second line of this file\n")

with open("mynewfile.txt") as g:
    print(g.read())
