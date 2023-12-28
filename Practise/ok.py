import random

pick = ['rock', 'paper', 'scissors']
choices = random.choice(pick)
userInput = input("Enter your choice\n 'rock', 'paper','scissors'")
print()
while userInput not in pick:
    userInput = input("Invalid Input. Please enter: \n 'rock', 'paper' , 'scissors' ")

print(f"Your choice is {userInput} \n Computer choice is {choices}")