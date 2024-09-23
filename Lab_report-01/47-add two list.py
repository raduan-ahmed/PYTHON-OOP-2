#Using the + Operator
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list1 + list2
print(result) 

#Using List Comprehension
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = [x + y for x, y in zip(list1, list2)]
print(result) 

#Using the extend() Method
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)  

#Using a Loop
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = []
for i in range(len(list1)):
    result.append(list1[i] + list2[i])
print(result)  

