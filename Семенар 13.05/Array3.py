import numpy as np

A = np.array([
    [10, 3, 15],
    [2, 20, 5],
    [4, 8, 6]
])

M, N = A.shape
B = A.copy()

for i in range(M):
    for j in range(N):
        near = []
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                ni, nj = i + di, j + dj
                if 0 <= ni < M and 0 <= nj < N:
                    if not (ni == i and nj == j):
                        near.append(A[ni][nj])
        if all(A[i][j] > n for n in near):
            B[i][j] = -A[i][j]

print(B)