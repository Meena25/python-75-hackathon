import random
dict1 = {'Abirami':'CSE',
         'Sujitha':'Civil',
         'Pragathi':'IT',
         'Sri Vidhya':'Mech'}

key=list(dict1)
#print(key)

temp=dict1.values()

val=list(temp)
#print(val)

stud=random.choice(key)

print("Guess "+stud+"'s department:")

i = 1
while i < 65535:
    print("choice ",i," : ")
    guess = input()
    if guess.lower() == dict1[stud].lower():
        print("Your Guess is correct after ",i," choices")
        break
    i += 1

'''
Output :
Your Guess Pragathi's department:
choice  1  : 
cse
choice  2  : 
civil
choice  3  : 
mech
choice  4  : 
it
Guess is correct after  4  choices
'''
