import numpy as np

arr = np.random.randint(0,10,(8,10))
arrs = arr.sum(axis=1)

print(arr)
print(arrs)
print(arrs.argmin(),arr[arrs.argmin()])