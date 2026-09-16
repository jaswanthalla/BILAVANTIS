# 12. String Methods Challenge
# input= "   python programming is fun   "
# Create a program that displays:
# 1. The string without leading/trailing spaces
# 2. The string in uppercase
# 3. The string in lowercase
# 4. The string in title case
# 5. The number of times `"p"` occurs
# 6. The position of `"programming"`
# 7. The string after replacing `"fun"` with `"powerful"`

input = "   python programming is fun   "
without_spacing = input.strip()
print(without_spacing)

upper_case = input.upper()
print(upper_case)

lower_case = input.lower()
print(lower_case)

title_case = input.title()
print(title_case)

count = input.count("p")
print(count)

words = input.split()
print(words)

word = "programming"
print(words.index(word))

replace = input.replace("fun", "powerful")
print(replace)
