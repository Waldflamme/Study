import numpy as np

A = np.array([
    [10, 20, 30],
    [5, 25, 35],
    [0, 15, 40]
])

M, N = A.shape

found = 0

for i in range(M):
    row_max = A[i].max()

    for j in range(N):
        if A[i][j] == row_max:
            col_min = A[:, j].min()
            if A[i][j] == col_min:
                found = A[i][j]
                break
    if found:
        break

print(found)