import numpy as np

# Sample data for two branches
branch_a = np.array([100, 200, 300])
branch_b = np.array([150, 250, 350])

# Join arrays horizontally
horizontal_join = np.column_stack((branch_a, branch_b))
print("Horizontal Join:\n", horizontal_join)

# Join arrays vertically
vertical_join = np.vstack((branch_a, branch_b))
print("Vertical Join:\n", vertical_join)

