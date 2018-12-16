"""
Classes and objects
"""
#to create class use keyword class
class val:
    a = 10
    
#to create an object obj for class val and print value of a
obj = val()
print("Value of a is : ",obj.a)

#Class student use __init__() function to assign values for name and regno
#classes have init function which is executed when class is initiated
class Student:
    def __init__(self,name,regno):
        self.name = name
        self.regno = regno
obj1 = Student("Jenny", 59787)
print("Student name : ",obj1.name)
print("Student register number : ",obj1.regno)
#self parameter-reference to class instance itself & used to access variables that belongs to the class

#create a method myname in class that is accessed by the object
class Student:
    def __init__(self,name,regno):
        self.name = name
        self.regno = regno
    def myname(self):
        print("Hello,this is",self.name,"and my regno is",self.regno)
obj1 = Student("Jenny", 59787)
obj1.myname()

#Modify object
#modify the regno of ob1 to 59866
obj1.regno = 59866
print("Modified object regno : ",obj1.regno)

#Delete the name property from object
del obj1.name
#print(obj1.name)
#AttributeError: 'Student' object has no attribute 'name'

#to delete object
del obj1
#print(obj1)
#NameError: name 'obj1' is not defined

'''
OUTPUT:
Value of a is :  10
Student name :  Jenny
Student register number :  59787
Hello,this is Jenny and my regno is 59787
Modified object regno :  59866
'''

