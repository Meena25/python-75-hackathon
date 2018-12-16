"""
Variables - python has no command for declaring variable
variable need not to be declared with any particular type
"""
a = 20
b = "python"
print("Variable a is : ",a)
print("Variable b is : "+b)

a = 20
# a is of type int
a = 'Hello' #String can be defined in single or double quotes
#now a is of type str
print("Value of a :"+a)
d = a + " " + b
print("The combined string is : "+d)

a = 20
c = 5
print("sum is : ",a + c) #mathematical operation for variables
# a + b error - since we try to combine number and string
# unsupported operand type(s) for +: 'int' and 'str'

# floating point numbers can be defined in any one of the way
f = 6.0
print("Floating point number : ",f)
f = float(6)
print("Floating point number :",f)

c = 3j
#type of the variables
print("type of a :",type(a))
print("type of b :",type(b))
print("type of f :",type(f))
print("type of c :",type(c))

'''
OUTPUT :
Variable a is :  20
Variable b is : python
Value of a :Hello
The combined string is : Hello python
sum is :  25
Floating point number :  6.0
Floating point number : 6.0
type of a : <class 'int'>
type of b : <class 'str'>
type of f : <class 'float'>
type of c : <class 'complex'>
'''

