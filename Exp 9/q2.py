import numpy as np
coefficients = np.array([[3, 2], [10, -1]])
constants = np.array([5, 3])
solution = np.linalg.solve(coefficients, constants)
print("Solution to equations:", solution)