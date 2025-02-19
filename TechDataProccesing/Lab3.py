import numpy as np

v1 = np.array((2,3))
v2 = np.array((1,4))
sq = np.square(v1-v2)
dist = np.sqrt(np.sum(sq))
print(dist)