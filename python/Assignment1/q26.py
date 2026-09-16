# 26. Create a dictionary for a product containing:
# product_name
# price
# quantity
# category
# Calculate the total cost using the price and quantity stored in the dictionary.

product = {"product_name": "brush", "price": 40, "quantity": 5, "catogory": "tool"}
total_cost = product["price"] * product["quantity"]
print(total_cost)
