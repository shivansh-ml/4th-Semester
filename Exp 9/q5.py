import numpy as np
A = np.array([1, 2, 3, 4, 5, 6])
B = np.array([7, 8, 9, 10, 12, 17])
mse = np.mean((A - B) ** 2)
print("Mean Square Error:", mse)