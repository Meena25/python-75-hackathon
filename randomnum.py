"""
Random numbers:
"""
import random

""" randrange function
syntax : random.randrange(stop)
stop- boundary value of the range for generating random number """
r = random.randrange(25)
print("Random number using randrange(25) is : ",r)

# Generating random even numbers between 30 and 50
a=random.randrange(30, 50, 2)
print("Random even number between 30 and 50 : ",a) 

#Using randint(lowvalue,highvalue) to generate random number
b = random.randint(1,10)
print("Random number using randint(1,10) :",b)

#Using random.uniform(lower,upper)
c = random.uniform(60,90)
print("Random number using uniform() : ",c)

'''
OUTPUT:
Random number using randrange(25) is :  10
Random even number between 30 and 50 :  48
Random number using randint(1,10) : 2
Random number using uniform() :  84.58832305117737
'''
