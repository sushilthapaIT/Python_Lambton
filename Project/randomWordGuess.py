#This program ask user to enter number between a to z and display if the user choice is wrong it let user to choose again and count the number of guess or it match.


import random

ran = ['a','b','c','d','e']
pick = random.choice(ran)
user = input("Enter your choice from [a,b,c,d,e]:\n").lower()
while user not in ran:
    user = input("Invalid Input!! Enter your choice from [a,b,c,d,e]:\n").lower()
    
if user in ran:
    print("Wow, you guessed!!")
else:
    print("Oops, try again.")

