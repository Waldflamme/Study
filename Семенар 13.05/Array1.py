import numpy as np

A = np.array([
    [1, 2, 3, 4],
    [5, 2, 6, 7],
    [8, 9, 3, 0]
])

M, N = A.shape

count = 0

for j in range(N):
    col = A[:, j]
    if len(np.unique(col)) == M:
        count += 1

print(count)