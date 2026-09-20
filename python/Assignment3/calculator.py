# 6. Create:calculator(a, b, operator)
# Support:
# +
# -
# *
# /
# %
# **
# Example:
# calculator(10, 3, "%")
# Output:
# 1
# Handle division by zero appropriately.


def calculator(a, b, operator):
    match operator:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            if b == 0:
                return "Division not possible"
            else:
                return a / b
        case "%":
            return a % b
        case "**":
            return a**b


print(calculator(10, 0, "/"))
