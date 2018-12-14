"""
Writing to a file
Creating a new file and writing into it

"x" - will create a file
f = open("python.txt", "x") # a new empty file is created
"""

# "w" -write mode will create a file if it does not exist
f = open("python.txt", "w")

"""After creating now writing to an
   existing file """
# "a" - will append to the end of the file
f = open("pyhton.txt","a")
f.write("Python 75 Challenge - Remote Hackathon - Pilot")
f.write("Procedure:")
f.write("1. Fork this code: https://github.com/teamtact/python-75-hackathon")
f.write("2. Start coding and commit often")
f.write("3. Update your github repository link in the challenge input")
f.close()

"""
OUTPUT Document file :
C:\Users\Meenu\AppData\Local\Programs\Python\Python36\py programs\py75\python.txt
Python 75 Challenge - Remote Hackathon - Pilot
Procedure:
1. Fork this code: https://github.com/teamtact/python-75-hackathon
2. Start coding and commit often
3. Update your github repository link in the challenge input
"""
# "w" method will overwrite the entire file
f = open("python.txt","w")
f.write("Woops! I have deleted the content!!!!!")
f.close()

'''
OUTPUT:
C:\Users\Meenu\AppData\Local\Programs\Python\Python36\py programs\py75\python.txt
Woops! I have deleted the content!!!!!
'''
