while True:
    try:
        book = int(input('enter the number u have purchased this month: '))

        if (book == 0):
            print('You have earned 0 points.')
        elif (book == 2):
            print('You have earned 5 points.')
        elif (book == 4):
            print('You have earned 15 points.')
        elif (book == 6):
            print('You have earned 30 points.')
        elif (book == 8 or book > 8):
            print('You have earned 60 points.')
        else:
            print('Points 0')
    except ValueError:
        print('Invalid Input')

    user_input = input('Do you want to try this program again [y/n]?')
    if user_input.lower() != "n":
        book = int(input('enter the number u have purchased this month: '))
        break

