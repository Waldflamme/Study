import numpy as np

arr = np.random.uniform(0,20,(4,7))

min = arr.min()
max = arr.max()
a = 1/(max-min)
b = min*-a
arr1 = arr*a+b

print(arr)
print(min,max)
print(a,b)
print(arr1)