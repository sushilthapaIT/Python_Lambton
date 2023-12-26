#This program ask user to enter number between 1 to 10 and display if the user choice is too high or too low or it match.

print("**********************************")
print("----Random Number Guessing Game----")
print("**********************************")
print()
print("Enter number between 1 to 10.")

def randomNum():
    import random
    gen = random.randint(1,10)
    count = 0
    while True:
        userInput = int(input("Guess a number: "))

        if (userInput > gen):
            print("You guess is too high!!!")
        elif (userInput < gen):
            print("Your guess is to low!!!")
        elif (gen == userInput):
            print(f"Congratulation, you have guessed the number correctly.\n The hidden number was {gen}")
            break
        count = count + 1

    print()
    print(f"You have guessed correctly in {count+1} times.")


randomNum()