"""
Lambda function in python is a small anonymous function
It can take any number of arguments, but can have only one expression
"""

# Syntax is lambda arguments : expression
# With one argument n
x = lambda n : n + 50
print("When x=5 result is: ",x(5))

# lambda function that multiplies two arguments
x = lambda a, b : a*b
print("Product is : ",x(8,5))

# To sum 3 arguments a,b,c
x = lambda a, b, c : a + b + c
print("Sum is : ",x(4, 13, 3))

#Lambda function is inside another function that computes power
def power(n):
    return lambda a : a ** n
#power(2) computes the square of a number
square = power(2)
#power(3) computes the cube of a number
cube = power(3)
print("Enter the number to be squared : ")
x = int(input())
print("Square of the number is : ",square(x))
print("Enter the number to be cubed : ")
x = int(input())
print("Cube of the number is : ",cube(x))

'''
OUTPUT :
When x=5 result is:  55
Product is :  40
Sum is :  20
Enter the number to be squared : 
12
Square of the number is :  144
Enter the number to be cubed : 
7
Cube of the number is :  343
'''

