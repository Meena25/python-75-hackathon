"""
In this demo.py prime function is defined
This demo is imported as a in module in modules.py
"""

def prime(n):
    if n > 1:
        # check for factors
        for i in range(2,n):
            if (n % i) == 0:
                print(n,"is not a prime number")
                break
        else:
            print(n,"is a prime number")
    else:
        print(n,"is not a prime number")
