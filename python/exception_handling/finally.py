def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed")
    except TypeError:
        print("Error: Invalid type, please use numbers")
    else:
        print("Division successful, result:", result)
    finally:
        print("Execution finished, cleaning up...")


divide(10, 2)
divide(5, 0)
divide("ten", 2)
print("hi")
