import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 3, 2],
    [2, 1, 5],
    [3, 4, 1]
])

print(A, '\n')

sorted_indices = A[:, 0].argsort()
A_sorted = A[sorted_indices]

print(A_sorted)