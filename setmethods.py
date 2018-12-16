"""
Set Methods:
union,intersection,difference
"""

# Set union() method
a = {"c++","java","python"}
b = {"windows","python","linux"}
u = a.union(b)
print("Union of two sets : ",u)

# Intersection() method - returns similarity among the sets
i = a.intersection(b)
print("Intersection of two sets : ",i)

#Difference() method - returned set contains items that exist only in the first set, and not in both sets.
d = a.difference(b)
print("Difference between sets (a-b) : ",d)

d = b.difference(a)
print("Difference between sets (b-a) : ",d)

'''
OUTPUT :
Union of two sets :  {'c++', 'linux', 'python', 'windows', 'java'}
Intersection of two sets :  {'python'}
Difference between sets (a-b) :  {'c++', 'java'}
Difference between sets (b-a) :  {'linux', 'windows'}
'''


