import numpy as np

arr1 = np.array([[1, 2, 3], [3, 4, 5]])
arr2 = np.array([[12, 13, 14]])

print(arr1)
print(arr2)

np.concatenate((arr1, arr2),axis=0)
