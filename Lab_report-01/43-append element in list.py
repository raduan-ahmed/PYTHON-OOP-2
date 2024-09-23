def append_element(my_list, element):
    my_list.append(element)
    return my_list

my_list = [1, 2, 3, 4, 5]

element = 6

updated_list = append_element(my_list, element)

print("Updated List:", updated_list)
