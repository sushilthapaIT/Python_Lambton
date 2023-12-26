#This program that lets the user play the game of Rock, Paper, Scissors against the computer.

print("**********************************")
print("----Rock, paper, scissors----")
print("**********************************")
print()
print("-------------Welcome------------------")


# import random
# def main(userInput):
#     randomNum = random.randint(1,3)
#     if randomNum == 1:
#         randomNum == "rock"
#     elif randomNum == 2:
#         randomNum == "paper"
#     else:
#         randomNum == "scissors"

#         if (userInput == randomNum):
#             print("Its a tie")
#     print()
#     print(userInput)

# def user_input():
#     userInput = input("Enter your choice rock, paper or scissors: ").lower()
#     while userInput not in ["rock","paper","scissors"]:
#         userInput = input("Invalid Input!!\nEnter your choice rock, paper or scissors: ").lower()

#     print(userInput)

# userInput = user_input()
# main(userInput)


import random
choices = ['rock','paper','scissors']
choice = random.choice(choices)

userChoice = input("Enter your choice:\n rock, paper, scissors: ").lower()
while userChoice not in choices:
    userChoice = input("Invalid Input!!!\nEnter your choice:\n(r) for rock, (p) for paper, (s) for scissor: ").lower()
print()
print(f"Computer choice is: {choice}")
print()

#r>s,s>p,p>r
