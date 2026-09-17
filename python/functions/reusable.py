def converter(km):
    meters = 0
    meters = km * 1000
    return meters


print(converter(10))
print(converter(2))
print(converter(3))
print(f"15km in meters is {converter(15)} meters")
