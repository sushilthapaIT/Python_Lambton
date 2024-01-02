import random

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
    print(f"{expression}\n{answer}")
    return expression, answer


for i in range(TOTAL_PROBLEMS):
    