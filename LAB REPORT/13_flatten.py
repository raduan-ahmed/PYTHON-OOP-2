# Flattening a 3D NumPy array

import numpy as np

# Sample 3D array
data = np.array([[[1, 2, 3], [4, 5, 6]], 
                  [[7, 8, 9], [10, 11, 12]], 
                  [[13, 14, 15], [16, 17, 18]]])

# Flatten the array into a 1D array
flattened_data = data.flatten()

print(flattened_data)
