import numpy as np

A = np.array([
    [1, 2, 3, 4],
    [4, 3, 2, 1],
    [1, 2, 3, 4],
    [1, 3, 2, 4]
])

first_row_set = set(A[0])

count_similar_rows = sum(set(A[i]) == first_row_set for i in range(len(A)))

print(count_similar_rows)