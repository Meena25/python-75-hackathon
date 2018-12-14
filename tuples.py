# TUPLES:
#2 tuples are created
tuple1 = ('tact','python')
tuple2 = (1,2,3,4)

print("tup1[0]: ",tuple1[0])
print("tup2[1:3]: ",tuple2[1:3])

""" OUTPUT:
tup1[0]:  tact
tup2[1:3]:  (2, 3) """

#Updating tuple1
tuple1 = ('python','challenge')
tuple3 = tuple1 + tuple2   # Concatenation of tuple1 and tuple2
print("tuple3 : ",tuple3)

""" OUTPUT :
tuple3 :  ('python', 'challenge', 1, 2, 3, 4) """

#Comparing elements of two tuples cmp(tup1,tup2)

#Length of a tuple
print("Length of tuple3 is : ",len(tuple3))

""" OUTPUT:
Length of tuple3 is :  6 """

#Max and min value of a tuple
print("Maximum value of tup2 : ",max(tuple2))
print("Minimum value of tup2 : ",min(tuple2))

"""
OUTPUT:
Maximum value of tup2 :  4
Minimum value of tup2 :  1
"""
    
