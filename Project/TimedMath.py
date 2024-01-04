import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERA = 3
MAX_OPERA = 12
TOTAL_PROBLEMS = 10


def generateProb():
    left = random.randint(MIN_OPERA, MAX_OPERA)
    right = random.randint(MIN_OPERA, MAX_OPERA)

    operator = random.choice(OPERATORS)

    expression = str(left) +  " " +operator + " " + str(right)
    answer = eval(expression)
    return expression, answer

wrong = 0
input("Press enter to start!!!")
print("___________________________")

startTime = time.time()
for i in range(TOTAL_PROBLEMS):
    expression, answer = generateProb()
    while True:
        guess = input("Problem #" + str(i+1) + ": " + expression + " = ")
        if guess == str(answer):
            break
        wrong = wrong + 1

endTime = time.time()
totalTime = endTime - startTime

print("_____________________________")
print(f"Good Job! You finished in {format(totalTime, '.2f')} seconds")

