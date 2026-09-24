# 1. Default Arguments
def add(a, b=0, c=0):
    return a * b * c


print("Default Args:")
print(add(5))  # 5
print(add(5, 10))  # 15
print(add(5, 10, 15))  # 30
print("-" * 40)
