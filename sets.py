"""
Set :
Collection which is unordered or unindexed
"""

set1 = {"java","python","c++"}
print("Set : ",set1)

#Adding items to a set
set1.add("c")
print("Added set :",set1)

#Adding multiple items to the set
set1.update(["unix", "linux", "c#"])
print("Updated set : ",set1)

#Length of the set
print("Length of the set : ",len(set1))

#Removing items from the set
set1.remove("unix")
set1.remove("linux")
print("After removing items from set : ",set1)

#Remove the last element by pop(), since sets are unordered we will not know which item will be removed
p = set1.pop()
print("Poped element is : "+p)
print("Set : ",set1)

#To empty the set clear() used
set1.clear()
print(set1)

# to delete the set completely del() used
del set1
print(set1)

'''
OUTPUT:
Set :  {'java', 'python', 'c++'}
Added set : {'java', 'c', 'python', 'c++'}
Updated set :  {'c', 'python', 'c++', 'c#', 'unix', 'java', 'linux'}
Length of the set :  7
After removing items from set :  {'c', 'python', 'c++', 'c#', 'java'}
Poped element is : c
Set :  {'python', 'c++', 'c#', 'java'}
set()
Traceback (most recent call last):
  File "C:/Users/Meenu/AppData/Local/Programs/Python/Python36/py programs/py75/sets.py", line 36, in <module>
    print(set1)
NameError: name 'set1' is not defined
'''
