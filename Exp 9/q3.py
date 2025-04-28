import numpy as  np
random_matrix = np.random.rand(5, 5)
print("Max:", np.max(random_matrix, axis=1))
print("Min:", np.min(random_matrix, axis=1))
print("Mean:", np.mean(random_matrix, axis=1))
print("Variance:", np.var(random_matrix, axis=1))