"""
Lists
"""
list1 = [1,2,3,4,5]
list2 = ["a","b","c","d"]
print("List1: ",list1)
print("List2: ",list2)

#Accessing values in list
print("list1[1] : ",list1[1])
print("list2[3] : ",list2[3])

#Updating values in list
list1[0] = 0
print("Updated list1: ",list1)

#deleting elements in list
del list2[1]
print("after deleting b in list2: ",list2)

#Length of the list
print("Length of the list1: ",len(list1))

#Adding elements to the end of the list
list2.append("e")
print("List after appending e: ",list2)

#Adding element "b" to the second position
list2.insert(1,"b")
print("After inserting b in 2nd position : ",list2)

#Removing element 3 from list1
list1.remove(3)
print("List1 after removing 3: ",list1)

'''
OUTPUT:
List1:  [1, 2, 3, 4, 5]
List2:  ['a', 'b', 'c', 'd']
list1[1] :  2
list2[3] :  d
Updated list1:  [0, 2, 3, 4, 5]
after deleting b in list2:  ['a', 'c', 'd']
Length of the list1:  5
List after appending e:  ['a', 'c', 'd', 'e']
After inserting b in 2nd position :  ['a', 'b', 'c', 'd', 'e']
List1 after removing 3:  [0, 2, 4, 5]
'''



