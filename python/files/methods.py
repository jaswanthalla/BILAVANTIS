# 1. Create and write to a file
with open("demo.txt", "w") as f:
    f.write("First line\n")
    f.write("Second line\n")

# 2. Append new content
with open("demo.txt", "a") as f:
    f.write("Appended line\n")

# 3. Read the entire file
with open("demo.txt", "r") as f:
    print("Read all:", f.read())

# 4. Read line by line
with open("demo.txt", "r") as f:
    print("Readline:", f.readline())  # Reads first line
    print("Readlines:", f.readlines())  # Reads remaining lines into a list

# 5. Check file properties
with open("demo.txt", "r") as f:
    print("File name:", f.name)
    print("Mode:", f.mode)
    print("Closed?", f.closed)

# 6. Using tell() and seek()
with open("demo.txt", "r") as f:
    print("Initial position:", f.tell())
    print("First 5 chars:", f.read(5))
    print("Position after read:", f.tell())
    f.seek(0)  # Move back to start
    print("After seek, first line again:", f.readline())

# 7. Closing explicitly
f = open("demo.txt", "r")
print("Manual close example:", f.read())
f.close()
print("Closed after manual close?", f.closed)
