import numpy as np

# Sample array of product prices
prices = np.array([10, 25, 30, 45, 60, 15, 50, 75, 20])

# Define the price range
lower_bound = 20
upper_bound = 50

# Use boolean indexing to filter products within the specified price range
filtered_prices = prices[(prices >= lower_bound) & (prices <= upper_bound)]

# Display the filtered prices
print(filtered_prices)
