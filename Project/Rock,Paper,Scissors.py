#This program that lets the user play the game of Rock, Paper, Scissors against the computer.

print("**********************************")
print("----Rock, paper, scissors----")
print("**********************************")
print()
print("-------------Welcome------------------")

userInput = "y"
while userInput == "y":
    import random
    choices = ['rock','paper','scissors']
    choice = random.choice(choices)

    userChoice = input("Enter your choice:\n rock, paper, scissors: ").lower()
    while userChoice not in choices:
        userChoice = input("Invalid Input!!!\nEnter your choice:\n(r) for rock, (p) for paper, (s) for scissor: ").lower()
    print()
    print(f"Computer choice is: {choice}")
    print(f"Your choice is: {userChoice}")
    print()

    if choice == userChoice:
        print("Its a tie.")
    elif userChoice == "rock" and choice == "scissors":
        print("You win. Rock smashes scissors.")
    elif userChoice == "scissors" and choice == "paper":
        print("You win. Scissors cuts paper.")
    elif userChoice == "paper" and choice == "rock":
        print("You win. Paper wraps rock.")
    else: 
        print("Computer won!! Better luck next time.")
    
    userInput = input("Do you want to continue? (y/n)").lower()
#r>s,s>p,p>r
