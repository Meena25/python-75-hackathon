"""
RANGE:
3 parameters [start,stop,step]
Code to print the odd integers in the specified range
from 5 to -10 by assigning negative step value 
"""
start = 5
stop = -10
step = -2
print("Odd numbers from 5 to -10 are: ")
for num in range(start,stop,step):
    print(num)

'''
OUTPUT:
Odd numbers from 5 to -10 are: 
5
3
1
-1
-3
-5
-7
-9
'''
