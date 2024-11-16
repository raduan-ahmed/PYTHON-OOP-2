import numpy as np

# Create a 2D NumPy array
data = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

# Create a view of the second row
row_view = data[1, :]

# Create a deep copy of the first column
column_copy = data[:, 0].copy()

# Modify the view
row_view[0] = 100

# Modify the copy
column_copy[0] = 200

# Print the original array, view, and copy
print("Original Array:\n", data)
print("Row View:\n", row_view)
print("Column Copy:\n", column_copy)
