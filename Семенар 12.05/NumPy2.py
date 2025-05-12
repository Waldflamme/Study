import numpy as np

M = int(input('Введите М: '))

A = np.random.randint(1, 100, size=(M, M))
print(A, '\n')

A = np.rot90(A,1)

print(A)