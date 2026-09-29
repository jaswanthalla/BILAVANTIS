import numpy as np

a = np.array([1, 2, 3])
print(a)

a1 = np.array([[1, 2], [3, 4], [5, 6]])
print(a1)

a3 = np.array(
    [
        [[1, 2], [3, 4]],
        [[5, 6], [7, 8]],
    ]
)
print(a3)

print(a[2])
print(a1[1,0])
print(a1[1:1])

aa=np.zeros((4,5))
print(aa)
bb=np.zeros((3,3))
print(bb)
cc=np.arange(10,40,1)
print(cc)
dd=np.full((4,4),2)
print(dd)