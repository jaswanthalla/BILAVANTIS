# 11. Create: calculate_discount(amount, membership)
# Discount rules:
# Amount >= 10000 → 20%
# Amount >= 5000  → 10%
# Amount >= 2000  → 5%
# Below 2000      → No discount
# If the customer is a member, provide an **additional 5% discount**.
# Return the final amount after applying the discount.
# Example:
# calculate_discount(6000, True)


def calculate_discount(amount, membership):
    if amount >= 10000:
        discount = 0.20
    elif amount >= 5000:
        discount = 0.10
    elif amount >= 2000:
        discount = 0.05
    else:
        discount = 0.0

    if membership:
        discount += 0.05

    final_amount = amount - (amount * discount)
    return final_amount


print(calculate_discount(6000, True))
