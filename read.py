"""
Reading a file in python
"""
#Open a file to read
fp = open("readinput.txt","r")
print("The file contents are :")
print(fp.read())
print()

# if you want to return first 6 characters of the file
fp = open("readinput.txt","r")
print("The first 6 characters in the file :")
print(fp.read(6))
print()

# if you want to return one line of the file
fp = open("readinput.txt","r")
print("The first line in the file :")
print(fp.readline())

# if you want to return first three lines of the file
fp = open("readinput.txt","r")
print("The first three lines in the file :")
print(fp.readline())
print(fp.readline())
print(fp.readline())

#reading file line by line using looping
fp = open("readinput.txt","r")
print("Reading file line by line :")
for i in fp:
    print(i)

'''
OUTPUT :
The file contents are :
Python 75 Challenge - Remote Hackathon - Pilot
Procedure:
1. Fork this code: https://github.com/teamtact/python-75-hackathon
2. Start coding and commit often
3. Update your github repository link in the challenge input

The first 6 characters in the file :
Python

The first line in the file :
Python 75 Challenge - Remote Hackathon - Pilot

The first three lines in the file :
Python 75 Challenge - Remote Hackathon - Pilot

Procedure:

1. Fork this code: https://github.com/teamtact/python-75-hackathon

Reading file line by line :
Python 75 Challenge - Remote Hackathon - Pilot

Procedure:

1. Fork this code: https://github.com/teamtact/python-75-hackathon

2. Start coding and commit often

3. Update your github repository link in the challenge input
'''
    



