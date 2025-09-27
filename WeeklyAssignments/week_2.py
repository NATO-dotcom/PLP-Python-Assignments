#creating an empty list
my_list=[]

#appending elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

#inserting an element at a specific position
my_list.insert(1,15)
print(my_list)

#extending the list with another list
#list2=[50,60,70]
#my_list.extend(list2)
my_list.extend([50, 60, 70])
print(my_list)

#removing an element from the list
my_list.remove(70)
print(my_list)

#sorting the list
my_list.sort()
print(my_list)

#accessing the index of an element
print(my_list.index(30))  