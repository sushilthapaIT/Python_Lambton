'''userInput = "y"

while userInput == "y":
    one = int(input("Enter number of sales: "))
    two = int(input("With Tax: "))

    mul = one + (13/100 * two)

    print(f"Total is {float(mul)}")

    userInput = input("Do you want to continue!!!")'''



'''userInput = "y".lower()

while userInput == "y":
    one = int(input("Enter how many sum number u want: "))
    sum = 0
    for i in range(one):
        sum = sum + i
    print(f"The total sum of {one} is: {sum}")
    
    userInput = input("Do you want to continue? (y/n)")'''



'''userIn = int(input("How many floor do u have in your house?\n"))

for outer in range(userIn):
    print(f"Number of floor {outer + 1}")

    userInR = int(input(f"How many rooms do u have in {outer+1} floor: "))
    for inner in range(userInR):
        roomsInput = str(input(f"What is the shape of {inner + 1} room: "))'''


        
'''#input invalid loop

inp = int(input("Enter positive number\n"))

while inp <0:
    print("Invalid Input!!")
    inp = int(input("Enter positive number\n"))'''




# for i in range(10):
#     print(2 * (i+1))




def user():
    dis = int(input("Enter a distance in kilometers to convert in miles: "))
    mil = dis * 0.6214
    return f"{dis} km = {mil} m"

result = user()

print(result)

