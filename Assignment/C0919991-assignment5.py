# Sushil Thapa
# C0919991
# 2023/10/18
print('Assignment 5')
print('Question 14')
print()

# Defining the number of rows in the pattern
rows = 7

# Outer loop to iterate from rows to 1
for i in range(rows, 0, -1):
    # Inner loop to print asterisks
    for j in range(0, i):
        print("*", end="")
    # Moving to the next line after each row to print in new line
    print()


print('Question 12')
#Taking input from the user
num = int(input("Enter a nonnegative integer: "))

#Checking if the input is nonnegative
if num < 0:
    print("Please enter a nonnegative integer.")
else:
    result = 1
    for i in range(1, num + 1):
        result *= i
    print(f"{num}! = {result}")

print()
print('Question 10')
#Initiating tuition amount
tuition = 8000  # $8,000 per semester

#Number of years to project tuition
years = 5

#Calculating and displaying tuition for the next 5 years using loop
for year in range(1, years + 1):
    tuition = tuition + (tuition * 0.03)  # Increase tuition by 3%
    print(f"Year {year}: Semester Tuition = ${tuition:.2f}")

