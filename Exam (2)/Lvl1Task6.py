import numpy as np

N = 1000

x = np.linspace(0, 5, N)
y = np.linspace(0, 5, N)
X, Y = np.meshgrid(x, y)

Z = X * Y * np.sin(X) * np.cos(Y)

mask = Z > 0.25

area_fraction = np.mean(mask)

print(f"{area_fraction:.4f}")
