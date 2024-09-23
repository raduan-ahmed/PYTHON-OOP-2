def add_lists(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Both lists must have the same length")
    
    # Add corresponding elements of both lists
    result = [list1[i] + list2[i] for i in range(len(list1))]
    return result

list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]

result_list = add_lists(list1, list2)
print("Resultant List:", result_list)
