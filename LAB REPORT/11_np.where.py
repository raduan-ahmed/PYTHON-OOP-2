import numpy as np

# Sample temperature data for several days
temperatures = np.array([22, 15, 30, 18, 25, 12, 28, 35, 20, 27])

# Define the threshold temperature
threshold = 20
# Define the minimum value to replace low temperatures
min_value = 18

# Find indices where the temperature exceeds the threshold
high_temp_indices = np.where(temperatures > threshold)
print("Indices where temperature exceeds threshold:", high_temp_indices[0])

# Replace temperatures below the threshold with the minimum value
adjusted_temperatures = np.where(temperatures < threshold, min_value, temperatures)
print("Adjusted Temperatures:", adjusted_temperatures)
