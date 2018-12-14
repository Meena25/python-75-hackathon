"""
String operations
"""
str1 = "hello python!!"
#Slicing for substrings, ":" is used
print("slicing substring str[0:5]",str1[0:5])
print("str[6:13]",str1[6:13])

print("string capitalize : ",str.capitalize(str1))

#count() method - returns number of occurances of substring in range[start,end]
#Syntax : str.count(sub,start=0,end=len(str))
sub = "o"
print("str.count(substr,2,15) : ",str1.count(sub,2,15))
sub = "python"
print("str.count(sub)",str1.count(sub))

#find function str.find(str,beg,end)
#Returns index if found otherwise -1
str2 = "python"
print("Finding python in string 1: ",str1.find(str2))
print("Finding python in string 1 from 10th position: ",str1.find(str2,10))

'''
OUTPUT:
slicing substring str[0:5] hello
str[6:13] python!
string capitalize :  Hello python!!
str.count(substr,2,15) :  2
str.count(sub) 1
Finding python in string 1:  6
Finding python in string 1 from 10th position:  -1
'''
