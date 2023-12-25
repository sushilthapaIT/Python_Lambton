#CIS-1232-02
#Assignment 4
#Sushil Thapa
#October 11, 2023

print('Assignment 4 Question Number 1')
print()

#Prompting the user for the number they scored
score_one = int(input('How many 1s did you score?'))
score_two = int(input('How many 2s did you score?'))
score_three = int(input('How many 3s did you score?'))
score_four = int(input('How many 4s did you score?'))
score_five = int(input('How many 5s did you score?'))
score_six = int(input('How many 6s did you score?'))

#Calculating the total score
total_one = score_one * 1
total_two = score_one * 2
total_three = score_one * 3
total_four = score_one * 4
total_five = score_one * 5
total_six = score_one * 6

#Calculating the total score by adding up the scores for all numbers
total = total_one + total_two + total_three + total_four + total_five + total_six

#Printing the subtotal
print('Your subtotal is:',total)

#Checking if the total is 63 or higher to determine if the user earns a bonus
if(total >= 63):
    bonus = total + 35
    #Printing the bonus and the total score
    print('You earned a bonus',bonus)
    print('Your Total is:',bonus)
else:
    #Printing a message indicating the user didn't earn a bonus and the total score
    print('Your did not earned a bonus.')
    print('Your total is:',total)



    


print('Assignment 4 Question Number 2')
print()

#Prompting the user for the grade percentage to convert to GPA
grade_per = int(input('Enter your grade percentage to convert it into GPA and point! '))

#Checking and displaying grade points according to the grade percentage entered by the user
if (grade_per > 100):
    print('The number is to high.')

elif (grade_per < 0):
    print('The number cannot be negative.')

elif (grade_per <=0 or grade_per <= 49):
    print('Your GPA is 0.')

elif (grade_per <= 50 or grade_per <= 59):
    print('Your GPA is 1.')

elif (grade_per <=60 or grade_per <= 62):
    print('Your GPA is 1.7.')

elif (grade_per <= 63 or grade_per <= 66):
    print('Your GPA is 2.')

elif (grade_per <=67 or grade_per <= 69):
    print('Your GPA is 2.3.')

elif (grade_per <= 70 or grade_per <= 72):
    print('Your GPA is 2.7')

elif (grade_per <=73 or grade_per <= 76):
    print('Your GPA is 3.')

elif (grade_per <= 77 or grade_per <= 79):
    print('Your GPA is 3.2.')

elif (grade_per <= 80 or grade_per <= 86):
    print('Your GPA is 3.5.')

elif (grade_per <= 87 or grade_per <= 93):
    print('Your GPA is 3.7.')

elif (grade_per <=94 or grade_per <= 100):
    print('Your GPA is 4.')