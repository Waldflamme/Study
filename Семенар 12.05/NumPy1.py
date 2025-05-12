import numpy as np

M = int(input("Введите M: "))

A = np.random.randint(1, 100, size=(M, M))
print(A, '\n')

sums = [int(np.sum(np.diagonal(A, offset=k))) for k in range(M-1, -M, -1)]

print(sums)
