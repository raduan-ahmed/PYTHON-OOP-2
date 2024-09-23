#Using a Set
my_list = [1, 2, 2, 3, 4, 4, 5]
my_list = list(set(my_list))
print(my_list)  

#Using a Loop
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = []
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)
print(unique_list)  

#Using Dictionary Keys
my_list = [1, 2, 2, 3, 4, 4, 5]
my_list = list(dict.fromkeys(my_list))
print(my_list) 

#Using List Comprehension
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = []
[unique_list.append(item) for item in my_list if item not in unique_list]
print(unique_list)  



