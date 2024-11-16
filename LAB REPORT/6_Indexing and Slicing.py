import numpy as np

# Sample 2D array representing sales data
sales_data = np.array([[100, 150, 200, 250],
                        [120, 180, 240, 300],
                        [130, 160, 210, 260],
                        [140, 170, 220, 270],
                        [150, 190, 230, 280]])

# Sales data for the first three products
first_three_products = sales_data[:3]
print("Sales data for the first three products:\n", first_three_products)

# Sales data for all products in the last two months
last_two_months = sales_data[:, -2:]
print("\nSales data for all products in the last two months:\n", last_two_months)

# Sales data for a specific product and month (2nd product in the 4th month)
specific_product_month = sales_data[1, 3]
print("\nSales data for the 2nd product in the 4th month:\n", specific_product_month)
