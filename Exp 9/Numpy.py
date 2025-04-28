import numpy as np
# dir(np)
A = np.array([1,2,3]) # Creation of an Numpy Array (Vector)
type(A) # numpy.ndarray
A.size # 3 elements
A.shape # (3,) #
A.ndim # 1
A.itemsize # 4
A.dtype # default dtype('int32')
# Note that if we put dot after each element , it changes to float.
# Change Data Type
A = np.array([1,2,3],dtype='float32') # User defined datatype
# Altenatively astype() method
A.astype(np.float64)
# Creation of multidimensional Array
A = np.array([[1,2],[2,4]])
# or
B = np.array([(7.8, 9, 10), (45, 5, 6)])
# Alternatively
A = np.array(([1,2],[2,3]),ndmin=2)
# Creation of 3 dimensional Matrix
A = np.array([[[1,2,3],[2,3,4],[4,5,6]],
[[7,8,9],[12,13,14],[14,15,16]],
[[27,28,29],[22,23,24],[24,25,26]]])

# Data Types for Strings
A =np.array(["hello", "world citizen"])
A.dtype # dtype('<U13') 13 characters
# Unique items in an array 7 Counts
A = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])
unique_values = np.unique(A)
print(unique_values)
unique_values, indices_list = np.unique(A, return_index=True)
print(indices_list) # an array of first index positions of unique values

unique_values, occurrence_count = np.unique(A, return_counts=True)
print(occurrence_count) #frequency count of unique values in a NumPy array