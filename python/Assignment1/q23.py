# 23. Create a set of five fruits.
# Perform:
# * Add a new fruit
# * Add multiple fruits
# * Remove a fruit
# * Discard a fruit
# * Check whether a particular fruit exists in the set

fruits = {"mango", "apple", "cherry", "banana", "avacado"}

fruits.add("papaya")
print(fruits)

fruits.update(["watermelon", "kiwi"])
print(fruits)

fruits.pop()
print(fruits)

fruits.remove("mango")
fruits.discard("kiwi")
print(fruits)

print("banana" in fruits)
