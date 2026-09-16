# 29. Shopping Cart
# Create:
# items = ["Laptop", "Mouse", "Keyboard"]
# prices = [50000, 1000, 2500]
# Display:
# * First item and its price
# * Last item and its price
# * Total price
# * Number of items
# * Items in reverse order.

items = ["Laptop", "Mouse", "Keyboard"]
prices = [50000, 1000, 2500]

print(f"first Item {items[0]} and its price {prices[0]}")

print(f"last Item {items[-1]} and its price {prices[-1]}")

total_price = sum(prices)
print(total_price)


no_of_items = len(items)
print(no_of_items)

reverse = items[::1]
print(reverse)
