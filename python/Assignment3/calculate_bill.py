# 5. Create:calculate_bill(units)
# Calculate the electricity bill using:
# First 100 units  → ₹2/unit
# 101–200          → ₹3/unit
# Above 200        → ₹5/unit
# The function should return the final bill.
# **Important:** Calculate the bill progressively.
# For example, for `250` units:
# First 100  → 100 × 2
# Next 100   → 100 × 3
# Remaining  → 50 × 5


def calculate_bill(units):
    if units > 0 and units <= 100:
        units = units * 2
    elif units > 100 and units <= 200:
        units = (100 * 2) + (units - 100) * 3
    else:
        units = (100 * 2) + (100 * 3) + (units - 200) * 5

    return units


units = int(input("enter the number of electricity units:"))
print(calculate_bill(units))
