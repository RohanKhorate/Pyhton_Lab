#2. Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.

import numpy as np
arr = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10])
# Reshape the array to a 3x3 matrix
reshaped_array = arr.reshape(3, 3)
print("array:")
print(arr)
print("\nReshaped array:")
print(reshaped_array)


# output:-

# array:
# [ 2  3  4  5  6  7  8  9 10]

# Reshaped array:
# [[ 2  3  4]
#  [ 5  6  7]
#  [ 8  9 10]]