import numpy as np

a1 = np.arange(20)
print(a1)

c = np.split(a1, 4)
print(c)
print(np.array_split(a1, 6))
