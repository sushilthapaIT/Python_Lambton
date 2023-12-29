# a = p * (1 + (r/n))**(n*t)

#1
# Get user input
userInput = int(input("Enter an integer: "))

# Check if the number is positive, negative, or zero
if userInput > 0:
    print("Positive")
elif userInput < 0:
    print("Negative")
else:
    print("Zero")

# Check if the number is even or odd
if userInput % 2 == 0:
    print("Even")
else:
    print("Odd")



#3
userInput = int(input("Enter the number between 1 and 12: "))

if (userInput >= 1 and userInput <= 12):
    if(userInput >=1 and userInput <= 3):
        print("The month is first quarter.")
    elif(userInput >= 4 and userInput <= 6):
        print("The month is second quarter.")
    elif(userInput >= 7 and userInput <= 9):
        print("The month is third quarter.")
    elif(userInput >= 10 and userInput <= 12):
        print("The month is fourth quarter.")
else:
    print('Invalid Error!!!')



#7
test = 25
exam = 50
print("---------------------------------------------")
print("Welcome  to grade  Calculator.")
print("---------------------------------------------")
print()
mainTest1 = int(input("Enter your marks for main test1: "))
mainTest2 = int(input("Enter your marks for main test2: "))
mainExam = int(input("Enter your marks for main exam: "))

total = mainTest1 + mainExam + mainTest2
print()
if (mainTest1 >= 0 and mainTest1 <= 25) and (mainTest1 >= 0 and mainTest1 <= 25) and (mainExam >= 0 and mainExam <= 50):
    if(total <= 50 and mainExam <= 25):
        print("Sorry, You Fail!")
    elif(total >= 50 and total <= 59):
        print("Congratulation, You Pass")
    elif(total > 60 and total <80):
        print("Congratulation, Your grade is Credit")
    elif(total >= 80 and total <= 100):
        print("Congratulation, Your grade is Distinction")
else:
    print('Invalid Input')



#9
print("---------------------------------------------")
print("Welcome  to Roulette Wheel Colors.")
print("---------------------------------------------")

userInput = int(input("Enter a number from (0-36): "))

if (userInput >= 0 and userInput <= 36):
    if(userInput == 0):
        print("Green")
    elif(userInput >= 1 and userInput <= 10):
        if(userInput % 2 == 0):
            print("black")
        else:
            print("red")
    elif(userInput >= 11 and userInput >= 18):
        if(userInput % 2 == 0):
            print("red")
        else:
            print("Black")
    elif(userInput >=19 and userInput <= 28):
        if(userInput % 2 == 0):
            print("black")
        else:
            print("red")
    elif(userInput >=29 and userInput <= 36):
        if(userInput % 2 == 0):
            print("Red")
        else:
            print("black")
else:
    print("Invalid Input!!!")



#14
print("---------------------------------------------")
print("Welcome to Body Mass Index.")
print("---------------------------------------------")

userWeight = int(input("Enter your weight: "))
userHeight = int(input("Enter your height: "))

bmi = userWeight * 703 / (userHeight**2)

if (bmi >= 18.5 and bmi <= 25):
    print("You weight is considered as optimal")
elif (bmi < 18.5):
    print("You are considered as underweight!!!")
elif(bmi > 25):
    print("You are considered as overweight!!!")




#15
print("---------------------------------------------")
print("Welcome to Time Calculator.")
print("---------------------------------------------")

'''oneMin = 60
oneHour = 3600
oneDay = 86400

userInput = int(input("Enter a number a seconds: "))

if (userInput<60):
    print("You have entered ",userInput)
elif (userInput > 60):'''

#error cant solve 2023/12/15
    

#16
print("---------------------------------------------")
print("Welcome to February Days.")
print("---------------------------------------------")

userInput = int(input("Enter a year: "))

if (userInput % 400 == 0) or (userInput % 100 != 0 and userInput % 4 == 0):
    print(f"In {userInput} February has 29 days")
else:
    print(f"In {userInput} February has 28 days")