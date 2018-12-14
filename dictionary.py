"""
Dictionary
"""
dict1={ "regno" : 59767,
        "name" : "Merlin",
        "score" : 75
    }
print("Dictionary consists of ",dict1)

#Accessing elements in dictionary
x = dict1["name"]
print("Name is : ",x)
#Accessing using get() method
x = dict1.get("regno")
print("Register number is : ",x)

#Changing values - changung score to 85
dict1["score"] = 85
print("After changing score dict1 : ",dict1)

#Loop through both keys and values of dictionary
print("Keys and values of dictionary :")
for x,y in dict1.items():
    print(x, y)

#values() function to return values of dictionary
print("Values of dictionary :")
for x in dict1.values():
    print(x)

#Length of dictionary
print("Length of dict1 : ",len(dict1))

#Adding items to dictionary
dict1["dept"] = "cse"
print("Dict1 after adding an item : ",dict1)

'''
OUTPUT:
Dictionary consists of  {'regno': 59767, 'name': 'Merlin', 'score': 75}
Name is :  Merlin
Register number is :  59767
After changing score dict1 :  {'regno': 59767, 'name': 'Merlin', 'score': 85}
Keys and values of dictionary :
regno 59767
name Merlin
score 85
Values of dictionary :
59767
Merlin
85
Length of dict1 :  3
Dict1 after adding an item :  {'regno': 59767, 'name': 'Merlin', 'score': 85, 'dept': 'cse'}
'''
