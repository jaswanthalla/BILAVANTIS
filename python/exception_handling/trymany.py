def divide_numbers(a, b):
    try:
        result = a / b
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed")
    except TypeError:
        print("Error: Invalid type, please use numbers")
    except Exception as e:
        print("Unexpected error:", e)


divide_numbers(10, 2)
divide_numbers(5, 0)
divide_numbers("ten", 2)
