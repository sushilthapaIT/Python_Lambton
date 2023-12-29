import random

pick = ['rock', 'paper', 'scissors']
choices = random.choice(pick)
userInput = input("Enter your choice\n 'rock', 'paper','scissors'").lower()
print()
while userInput not in pick:
    userInput = input("Invalid Input. Please enter: \n 'rock', 'paper' , 'scissors'\n ").lower()

if userInput == choices:
    print("Its a tie.")
elif (userInput == "rock" and choices == "scissors") or (userInput == "scissors" and choices == "paper") or (userInput == "paper" and choices == "rock"):
    print("Congratulation, you win!")
else:
    print("Oops, you loose.")
    
    #r>s, s>p, p>r
print()
print(f"Your choice is {userInput}\nComputer choice is {choices}")