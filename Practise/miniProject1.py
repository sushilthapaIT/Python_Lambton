import random

def roll():
    minVal = 1
    maxVaL = 6
    roll = random.randint(minVal, maxVaL)

    return roll

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Invalid Input!!! Must between (2-4)")
    else:
        print("Invalid! Try Again.")

MAX_SCORE = 50
playerScore = [0 for _ in range(players)]

while max(playerScore) < MAX_SCORE:
    for playerIndex in range(players):
        print(f"Player Number {playerIndex+1} turn has just started! \n")
        print(f"Your total score is {playerScore[playerIndex]} \n")
        currentScore = 0

        while True:
            shoRoll = input("Would you like to roll (y/n)? ")
            if shoRoll.lower() != "y":
                break

            value = roll()

            if value == 1:
                print("You rolled a 1! Turn Done!!!")
                currentScore = 0 
                break
            else:
                currentScore = currentScore + value
                print(f"You rolled a {value}")
            
            print("Your score is: ",currentScore)

        playerScore[playerIndex] = playerScore[playerIndex] + currentScore
        print(f"Your total score is: {playerScore[playerIndex]}")

MAX_SCORE = max(playerScore)
winningIndex = playerScore.index(MAX_SCORE)
print("Player number", winningIndex + 1, "is the winner with a score of: ",MAX_SCORE)