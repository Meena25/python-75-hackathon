"""
Module - same as a code library
create a module save the code in file demomodule.py
demomodule.prime(n) computes given number prime or not
"""
import demomodule

print("Enter a number : ")
x = int(input())
demomodule.prime(x)

#Renaming a module
#creating alias for demomodule as dx

import demomodule as dx
print("Enter a number : ")
x = int(input())
dx.prime(x)

"""
OUTPUT :
RESTART: C:/Users/Meenu/AppData/Local/Programs/Python/Python36/py programs/py75/modules.py 
Enter a number : 
56
56 is not a prime number
Enter a number : 
17
17 is a prime number
"""
