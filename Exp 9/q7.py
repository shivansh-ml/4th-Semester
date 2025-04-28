import numpy as np
norm_data = np.random.randn(20)
quartiles = np.percentile(norm_data, [25, 50, 75])
print("Quartiles:", quartiles)