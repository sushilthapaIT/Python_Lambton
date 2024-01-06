print("---------------------\nMini Calculator\n--------------------")

coll = [1,2,3,4]
while True:
    num1 = input("Enter 1st number: ")
    if num1.isdigit():
        break

while True:   
    num2 = input("Enter 2nd number: ")
    if num2.isdigit():
        break
print()
print("Enter:\n1 for addition\n2 for subtraction \n3 for multiplication\n4 for division")
print()
while True:
    userInput = input("Enter your choice: ")
    if userInput.isdigit():
        userInput = int(userInput)
        if userInput in coll:
            break
    else:
        print("Invalid Input")

# try:
num1 = float(num1)
num2 = float(num2)
if userInput == 1:
    add = num1 + num2
    print(f"The addition of {num1} + {num2} = {add}")
elif userInput == 2:
    sub = num1 - num2
    print(f"The subtraction of {num1} - {num2} = {sub}")
elif userInput == 3:
    mul = num1 * num2
    print(f"The addition of {num1} * {num2} = {mul}")
elif userInput == 4:
    if num2 != 0:
        div = num1 / num2
        print(f"The addition of {num1} / {num2} = {div}")
    else:
        print("Zero Division Error")
# except ZeroDivisionError as g:
#     print(g)


