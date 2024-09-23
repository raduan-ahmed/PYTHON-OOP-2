#Using the join() Method
my_list = ['apple', 'banana', 'cherry']
my_string = ', '.join(my_list)
print(my_string)  

#Using List Comprehension and join()
my_list = ['apple', 'banana', 'cherry', 20, True, 3.14]
my_string = ', '.join([str(item) for item in my_list])
print(my_string) 

#Using a Loop
my_list = ['apple', 'banana', 'cherry']
my_string = ''
for item in my_list:
    my_string += str(item) + ', '
my_string = my_string[:-2] 
print(my_string) 

#Using map() and join()
my_list = ['apple', 'banana', 'cherry', 20, True, 3.14]
my_string = ', '.join(map(str, my_list))
print(my_string)  

