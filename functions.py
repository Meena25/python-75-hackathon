"""
Function:
In functions we can pass mutable and immutable parameters
Immutable parameter every time when we change its value
new object is created and old object is discarded
"""
def add(x):
    x += 10
    return x

x = 5
print("Value of x: ",x)
print("ID of x: ",id(x))
x = add(x)
print("Value of x: ",x)
print("ID of x: ",id(x))

'''
OUTPUT:
Value of x:  5
ID of x:  1745579168
Value of x:  15
ID of x:  1745579488
'''
