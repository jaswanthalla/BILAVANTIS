# 18.numbers = (10, 20, 30, 20, 40, 20, 50)
# * How many times `20` occurs
# * The index of `40`
# * The first four elements
# * The tuple in reverse

numbers = (10, 20, 30, 20, 40, 20, 50)
print(numbers.count(20))

print(numbers.index(40))

print(numbers[:4])

print(numbers[::-1])
