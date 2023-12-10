#CSD-1233-01
#Assignment 3
#Sushil Thapa
#September 27, 2023

#Multiple choice question
print('Review Question Answer of Chapter 2 from 14-22')

#question 14 answer
print('Question 14: a')

#question 15 answer
print('Question 15: a')

#question 16 answer
print('Question 16: c')

#question 17 answer
print('Question 17: a')

#question 18 answer
print('Question 18: b')

#question 19 answer
print('Question 19: a')

#question 20 answer
print('Question 20: b')

#question 21 answer
print('Question 21: b')

#question 22 answer
print('Question 22: b')
print('\r')
#True or False
#question 3 answer
print('True or False answer of 2')
print('Question 2: True')
print('\r')
#programming assignment 1
print('Programming assignment 1')

#Setting the variable equal to the amount of square feet in one hector 
one_hector = 10000
#This gets the number of square feet in the user's tract of land and casting the value integer
total_square = float(input('Enter the total square meters in a tract of land?'))
# This calculates the land size in acres
hec_num = (1 / one_hector)*total_square
#Displays the result to the user.
print('The number of hectares in the tract', format(hec_num, '.2f'))

print('\r')
#programming assignment 2
print('Programming assignment 2')

#taking user input and casting the value float
food_charge = float(input('Enter the total amount of a meal purchased at a restaurant?'))
#formula to calculate tip amount
tip_amount = (18/100)*food_charge
#formula to calculate hst amount
hst_amount = (13/100)*food_charge
#formula to calculate total amount
total_amount = food_charge + tip_amount + hst_amount
#Displays the tip amount to the user
print('Your Tip Amount is: ', format(tip_amount, '.2f'))
#Displays the HST amount to the user
print('Your HST amount is: ', format(hst_amount, '.2f'))
#Displays the Total amount to the user
print('Your Total amount including food charge, tips and HST is: ', format(total_amount, '.2f'))


print('\r')
#programming assignment 3
print('Programming assignment 3')
#taking user input and casting the value float
principal = float(input('Enter the amount of principal deposited into the account?'))
#taking user input and casting the value int
interest = int(input('Enter the annual interest rate?'))
#taking user input and casting the value int
num_times =  int(input('Enter the number of times per year?'))
#taking user input and casting the value int
num_years = int(input('Enter number of years the account will be left to earn interest?'))
#converting float to percentage
interest_rate = float(interest/100)
#calculating compound interest
compound_interest = principal*(1+(interest_rate/num_times))**(num_years*num_times)
#Displays the amount of money in the account after the specified number of years
print("the amount of money in the account after the specified number of years:", format(compound_interest, '.2f'))