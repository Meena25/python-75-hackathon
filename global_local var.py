"""
Global and local variables:
Variable n is defined as global
"""
n = 3
  
""" Function func1 uses global variable 'n'
because there is no local variable 'n' """ 
def func1(): 
    print("In function1 variable n is: ", n) 
  
#In function func2 variable 'n' is redefined as local variable
def func2():     
    n = 20
    n = n/10
    print("In function2 variable n is: ",n) 
  
#In function func3 global keyword used to modify global variable 'n' 
def func3():     
    global n 
    n = 50
    print("In function3 variable n is: ",n) 
"""Global scope of variable n""" 
print("global variable: ",n)
func1() 
print("global variable: ",n) 
func2() 
print("global variable: ",n) 
func3() 
print("global variable: ",n) 

'''
OUTPUT:
global variable:  3
In function1 variable n is:  3
global variable:  3
In function2 variable n is:  2.0
global variable:  3
In function3 variable n is:  50
global variable:  50
'''
