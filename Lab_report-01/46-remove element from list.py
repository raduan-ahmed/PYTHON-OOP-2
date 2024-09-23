# Method 1: Using the remove() method
def remove_element_by_value(my_list, value):
    try:
        my_list.remove(value)
    except ValueError:
        print(f"Value {value} not found in the list.")
    return my_list

# Method 2: Using the pop() method
def remove_element_by_index(my_list, index):
    try:
        my_list.pop(index)
    except IndexError:
        print(f"Index {index} is out of range.")
    return my_list

# Method 3: Using the del statement
def remove_element_by_del(my_list, index):
    try:
        del my_list[index]
    except IndexError:
        print(f"Index {index} is out of range.")
    return my_list

# Initial list
my_list = [1, 2, 3, 4, 5, 6]

# Remove element by value
print("Original List:", my_list)
my_list = remove_element_by_value(my_list, 3)
print("After removing value 3:", my_list)

# Remove element by index using pop()
my_list = remove_element_by_index(my_list, 2)
print("After removing element at index 2:", my_list)

# Remove element by index using del
my_list = remove_element_by_del(my_list, 1)
print("After removing element at index 1:", my_list)
