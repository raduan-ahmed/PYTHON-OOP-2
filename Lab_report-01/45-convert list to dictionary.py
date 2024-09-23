def list_to_dict(tuples_list):
    return dict(tuples_list)

tuples_list = [("a", 1), ("b", 2), ("c", 3)]

result_dict = list_to_dict(tuples_list)

print("Converted Dictionary:", result_dict)
