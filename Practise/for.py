# grade = int(input('Enter your grade?'))

# if (grade <= 90):
#     print('Nice')
# else:
#     print('try again')

# char1 = float(input('enter 1st num'))

# char2 = float(input('enter 2nd num'))

# if (char1 == char2):
#     print('they are same')
# else:
#     print('they are not same')

# salary = int(input('Enter your salary'))
# job = int(input('enter job year'))

# if (salary >= 50000 or job >= 2):
#     print('You are qualify for the loan.')
# else:
#     print('You are not qualify for the loan.')

# grade = int(input('enter grade'))

# if (grade < 0  or grade > 100):
#     print('invalid')
# else:
#     print('hurray')

# x = 100

# if (x > 20):
#     print('it is true that the number is greater than 100')

# string1 = "joe"
# string2 = "joe"

# if (string1 == string2):
#     print('they are same')

# num1 = str(input('Enter one name'))

# num2 = str(input('enter second name'))

# if (num1 == num2):
#     print('they are same')
# else:
#     print('they are not same')

# wages = 9
# hours = int(input('enter your working hour'))

# if (hours >40):
#     wages = 1.5 * wages
#     print(wages)
# else:
#     wages = 1 * wages
#     print(wages)

# i = 0

# while (i<=30):
#     print(i)
#     i=i+3

# number = str("number")
# while (number <= 5):
#     print('hello')
#     number = number + 1

while True:
    try:
        user_input = int(input('Enter positive integer number: '))
        if user_input > 0:
            break
        else:
            print("please enter positive integer.")
    except ValueError:
        print("Invalid error: Please enter positive integer.")

print(f'you entered a valid positive integer:{user_input}')