# 22. Create two sets:
# A = {10, 20, 30, 40, 50}
# B = {40, 50, 60, 70, 80}
# Display:
# * Union
# * Intersection
# * Difference of A
# * Difference of B
# * Symmetric difference


A = {10, 20, 30, 40, 50}
B = {40, 50, 60, 70, 80}

#|
union = A.union(B)
print(union)

#&
intersection = A.intersection(B)
print(intersection)

#-
diff_a = A.difference(B)
print(diff_a)

diff_b = B.difference(A)
print(diff_b)

#^
syn_diff = A.symmetric_difference(B)
print(syn_diff)
