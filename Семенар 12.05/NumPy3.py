import numpy as np

M = int(input('Введите M: '))

A = np.random.randint(1, 100, size=(M, M))
print(A, '\n')

for i in range(M):
    for j in range(M - i - 1):
        A[i + j + 1][M - 1 - j] = 0

print(A)
