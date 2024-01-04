import random
import time

MIN = 1
MAX = 10
calcC = ["*", "-"] 
calc = ["+", "-", "*"]
TOTAL_PROBLEM = 10

def genNum():
    num = random.choice(calc)
    numC = random.choice(calcC)
    num1 = random.randint(MIN, MAX)
    num2 = random.randint(MIN, MAX)
    num3 = random.randint(MIN,MAX)

    number = str(num1) + str(num) + str(num2)
    ans = eval(number)
    return number, ans

start = time.time()
wrong = 0
input("Press enter to play!!!")
print("_________________________")

for i in range(TOTAL_PROBLEM):
    number, ans = genNum()
    while True:
        user = input(f"{number} = ")
        user = int(user)
        if ans == user:
            break
        wrong = wrong + 1

print("_________________________")
end = time.time()
total = end - start
print(f"Wow!!! You solved in {format(total, '.2f')} seconds\nAnd you got {wrong} times wrong")