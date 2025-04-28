import numpy as np 
rand_int_matrix = np.random.randint(2, 101, (5, 5))
boolean_mask = (rand_int_matrix >= 20) & (rand_int_matrix <= 70)
print("Boolean Matrix:\n", boolean_mask)