import numpy as np

A = np.array([[-1,2,4],[-3,1,2,],[-3,0,1]])
B = np.array([[3,-1],[2,1]])
C = np.array([[7,21],[11,8],[8,4]])
X = np.linalg.inv(A)@-C@np.linalg.inv(B)
M=A@X@B
print(X)
print(M)