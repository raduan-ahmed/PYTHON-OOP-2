import numpy as np

# Sample 1D array representing sensor data
sensor_data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Desired shape (rows = num_sensors, cols = num_timestamps)
num_sensors = 2
num_timestamps = 5

# Reshape or pad/truncate data
total_elements = num_sensors * num_timestamps
if len(sensor_data) < total_elements:
    sensor_data = np.pad(sensor_data, (0, total_elements - len(sensor_data)))
reshaped_data = sensor_data[:total_elements].reshape((num_sensors, num_timestamps))

print("Reshaped Data:")
print(reshaped_data)
