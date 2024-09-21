# Initial list of customers
customers = ["Alice", "Bob", "Charlie", "David", "Eve"]

# _Access the third customer in the list and print their name
third_customer = customers[2]
print(" ")
print(f"The third customer is: {third_customer}")

# b_Change the name of the second customer to "Ben"
customers[1] = "Ben"

# c_Add a new customer named "Frank" to the end of the list
customers.append("Frank")

# d_Remove the customer "David" from the list
if "David" in customers:
    customers.remove("David")

# e_Sort the customer names alphabetically and print the final list
customers.sort()
print("Final sorted list of customers:", customers)
print(" ")
