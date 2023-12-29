#1
print("--------------------------------")
print("Bug Collector")
print("--------------------------------")
print()
total = 0
for i in range(5):
    user_input = int(input(f"How many bugs u collected in {i + 1} days: "))

    total = user_input + total

print(f"Total bugs collected by bounty hunter in 5 days is: {total}")
print()

#3
print("--------------------------------")
print("Lap Times")
print("--------------------------------")
print()

userInput = int(input("Enter the number of times around a lap time: "))
lapTimes = []
for i in range(userInput):
    userInput1 = input(f"Enter the lap time {i+1}: ")
    lapTimes.append(userInput1)

maximum = max(lapTimes)
minimum = min(lapTimes)
average = sum(lapTimes) / userInput

print("The fastest lap is: ",maximum)
print("The slowest lap is: ",minimum)
print("The average lap time is: ",average)


#2
print("--------------------------------")
print("Calories Burned")
print("--------------------------------")
print()

oneMinCal = 4.2

for i in range(10,35,5):
    print(f"The number of calories burned after {i} is {int(i * oneMinCal)}.")


#4
print("--------------------------------")
print("Distance Traveled")
print("--------------------------------")
print()

distance = int(input("What is the speed of the vehicle in mph? \n------------  "))
hour = int(input("How many hours it traveled? \n-------------"))

for i in range(hour):
    print((i+1) * distance)


#5
print("--------------------------------")
print("Average Rainfall")
print("--------------------------------")
print()
numYear = int(input("Enter number of years: "))
rainList = []

for outer in range(numYear):
    # rainList.append(i)
    print(f"Year {outer + 1}")
    for inner in range(12):
        rain = int(input(f"what are the inches of rainfall in {inner + 1}'s month: "))
        rainList.append(rain)

total_rainfall = sum(rainList)
num_months = numYear * 12
average_rainfall = total_rainfall / num_months

print(f"The inches of rainfall is {total_rainfall}.")
print(f"The number of months is {num_months}.")
print(f"the average rainfall is {format(average_rainfall, '.2f')}.")


#6
print("--------------------------------")
print(" Miles to Kilometers Table")
print("--------------------------------")
print()

oneMile = 1.60934

for i in range(10,90,10):
    print(f"The {i} miles is equivalent to: {format((i)*oneMile,'.2f')} km" )

#7
# print("--------------------------------")
# print("Pennies for Pay")
# print("--------------------------------")
# print()

# userInput = int(input("Enter the number of days you will work: "))

# oneDollar = 100

# for i in range(userInput):
#     f


#8
print("--------------------------------")
print("Average word length")
print("--------------------------------")
print()

userInput = input("Enter a word to continue or enter nothing to exit")
lists = []

for i in range(100):
    if userInput == "":
        break
    else:
        userInput = input("Enter a word to continue or enter nothing to exit")
        lists.append(userInput)

average = int(sum(lists) / i)

print(f"Average length of word is {len(average)}")
print("Thank you for using my application")



#12
# print("--------------------------------")
# print("Calculating the factorial of a number")
# print("--------------------------------")
# print()


# userInput = int(input("Enter a non negative integer number: "))
# fact = 0
# if userInput > 0:
#     for i in range(1, userInput + 1):
#         fact = fact * i
#         print(fact)
# else:
#     print("Invalid Input!!")

'''print("Number \t Square")
for i in range(1,11,1):
    print(f"{i} \t {i**2}")'''


#to let user control the loop iteration

print("Square of number starting from 1.")
print("----------------------------------")
print()
userInput = int(input("Enter how high should i go: "))

for i in range(1, userInput + 1):
    print(f"{i} {i*i}")


# to let user control the loop start and end iteration

start = int(input("Enter the starting point of sum of self number: \n"))

end = int(input("Enter the end number of iteration when to stop: \n"))

step = int(input("Enter step number: \n"))
sum=0
print(f"So, the starting point will be from {start} and ending point is {end} and the step will be {step}")
for number in range(start, end+1, step):
    sum = number+sum
    print(number, sum)


for i in range(10,0, -1):
    print(i)


for i in range(0,501,100):
    print(i)


'''for i in range(10,5,-1):
    print(i)'''

total=0
for number in range(5):
    userInput = int(input(f"Enter a number {1+number}'s time: "))
    total = total + userInput
print(f"The sum of all number is {total}")
step = 10
mul = 1
inp = int(input("Enter which multiplication u want: "))
for i in range(inp):
    mul = mul * inp

    print(mul)

#auto multiplication
for i in range(1,11):
    print(f"The table of {2} * {i} : {2*i}")

# taking input from user multiplication
whichNum = int(input("Enter which number multiplication u want to do? \n"))
whereTo = int(input("Enter where to u want a multiplication?\n"))
start = int(input("Enter where to start the multiplication?\n"))

for i in range(start,whereTo):
    print(f"The multiplication of {whichNum} is: \n {whichNum} * {i} = {whichNum*i}")



print("Enter the property lot number \n or enter O to end")
while userInput != "O".lower():
    user = int(input("Enter the property tax: \n"))
    tax = 0.13 / user
    print(f"Property tax is {tax}")

    userInput = input("Enter O to end")


#13

startNum = int(input("Starting number of organisms:\n"))
avgInc = 1 + int(input("Average daily increase: \n")) /100
dayMul = int(input("Number of days to multiply: \n"))
print()
print("Day Approximate \t Population")
predicted = startNum
for i in range(dayMul):
    predicted = avgInc * predicted
    print(f"{i+1} \t\t\t {round(predicted, 2)}")


# for i in range(6,0,-1):
#     for j in range(i):
#         print('*', end="")
#     print()


facNum = int(input("Enter a non-negative number:\n"))

if facNum < 0:
    print("Invalid Num!!")
else:
        result = 1
        for i in range(2, facNum + 1):
            result *= i
            print(result)



for i in range(6,0,-1):
    for j in range(i):
        print(5 , end=" ")
    print()

for i in range(3): # Outer loop
    for j in range(2): # Inner loop
        print(i, j )


ok = "i am small and I AM BIG. NOW, SEE THE CHANGE"
ok = ok.swapcase()
print(ok)



while True:
    user = int(input("Enter how many days u hunt bounty: "))
    sum = 0
    for num in range(user):
        bounty = int(input(f"In day {num+1}'s how much you earned: "))

        sum = sum + bounty
    print(f"Total you have earned so far is {sum}")
    userInput = input("Do you want to continue").lower()
    if userInput != "y":
        break
    print("Thank you for using our application!!")


def twoDiv():
    for num in range(100, 500 +1):
        if (num % 11 == 0) and (num % 2 != 0):
            print(num)

twoDiv()



def main(user,rang):
    for num in range(1,rang+1):
        print(f"{user} * {num} = {user * num}")
    thankYou()

def table():
    welcome()
    userInp = int(input("Which number table you like to print: \n"))
    rang = int(input("Up to where: \n"))
    print()
    return userInp, rang
    
def welcome():
    print("--------------------------------------------")
    print("Welcome to table calculator.")
    print("--------------------------------------------")
    print()

def thankYou():
    print("******************************")
    print("Thank you for using table calculation program!")
    print("******************************")


def again():
    while True:
        userINput = input("Do you wan tot try again[y/n]: ")
        if userINput != "y":
            break

tables = table()
main(*tables)



while True:
    number =[]
    userInp = int(input("Enter a num: "))
    if userInp == 0:
        break
    number.append(userInp)

    if not number:
        print("No number entered")
    else:
        total = sum(number)
        average = total / len(number)

        print(total)
        print(average)

def lapTimes():
    inn = []

    userLap = int(input("Enter number of lap\n"))
    print()
    for out in range(userLap):
        lap = int(input(f"Enter {out + 1}'s lap:\n"))
        inn.append(lap)

    average = sum(inn) / len(inn)
    print()

    print(f"The fastest to complete the lap time is: {max(inn)}")
    print(f"The slowest to complete the lap time is: {min(inn)}")
    print(f"The average to complete the lap time is: {format(average,'.2f')}")

lapTimes()

def main(name, age):
    welcome()
    name, age = userInput()
    output(name,age)
    thankyou()

def welcome():
    print("***********************************")
    print("Welcome to my function.")
    print("***********************************")
    print()

def thankyou():
    print()
    print("***********************************")
    print("Thank you for using my function.")
    print("***********************************")

def userInput():
    name = input("Enter a name: ")
    age = input("Enter your age: ")
    return name, age

def output(name, age):
    print (f"Your name is {name} \n Your are {age} years old.")


result = main(None,None)

print(result)