#3
onePound = 0.454

userInput = int(input("Enter the mass of an object in pounds then i will convert it into kg for u: "))

convert = userInput * onePound

print(f"so {userInput} pound  = {convert} kg")
print()
print()
print()

#5
distanceSix = 70 * 6
distanceTen = 70 * 10
distanceFiveteen = 70 * 15

print("The distance the car will travel in 6 hours ",distanceSix)
print("The distance the car will travel in 6 hours ",distanceTen)
print("The distance the car will travel in 6 hours ",distanceFiveteen)
print()
print()
print()
#8
foodInput = int(input("Enter the charge of the food: "))

tipAmount = (18/100) * foodInput
saleTax = (7/100) * foodInput
total = foodInput + tipAmount + saleTax

print(f"The 18 percent tip amount is {tipAmount}")
print("The sales tax charge is: ",format(saleTax, '.2f'))
print("The total amount is: ",total)
print()
print()
print()


#10
sugar = 1.5 / 48
butter = 1 / 48
flour = 2.75 / 48

userInput = int(input("Enter how many cookies u want to make i'll provide u recipe: "))

newSugar = userInput * sugar
newButter = userInput * butter
newFlour = userInput * flour

print(f"To make {userInput} cookies you need \n Amount of sugar: {format(newSugar, '.2f')} \n Amount of Butter: {format(newButter, '.2f')} \n Amount of Flour: {format(newFlour, '.2f')}")
print()
print()
print()


#13
r = int(input("Enter length of row in feet: "))
e = int(input("Enter the amount of space used by an end-post assembly in feet: "))
s = int(input("Enter the amount of space between the vines, in feet: "))

v = (r - (2*e) ) / s

print("The number of grapevines that will fit in the row: ",v)