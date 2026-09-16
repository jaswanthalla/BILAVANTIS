# 4. Store a number representing total seconds. Convert it into minutes and Remaining seconds
# Example:
# Input: 367
# Output:
# Minutes = 6
# Seconds = 7

input = int(input("Enter total seconds:"))
minutes = input // 60
seconds = input % 60

print(minutes, "Minutes")
print(seconds, "Seconds")
