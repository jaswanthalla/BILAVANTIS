import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 3])
arr3 = np.array([1, 2, 3])
print(np.equal(arr1, arr2))
print(np.equal(arr1, arr3))
print(np.array_equal(arr1, arr2))


print(np.sum(arr2))
 