import numpy as np

# Sample 2D NumPy array with string values
data = np.array([['Raduan', '25', '3000.50'],
                 ['Ahamed', '30', '4000.75'],
                 ['Roni', '22', '2500.00']])

# Extract and cast columns
names = data[:, 0]
ages = data[:, 1].astype(int)  # Convert age to integers
salaries = data[:, 2].astype(float)  # Convert salary to floats

# Print converted data
print("Names:", names)
print("Ages:", ages)
print("Salaries:", salaries)
