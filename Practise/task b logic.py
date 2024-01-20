def input_1():
    while True:
        try:
            fat = int(input('enter how many floor'))
            print('your number of floor is', fat)
        except ValueError:
            print('enter integer')
        
        user_input = input('do you want to continue [Y/N]')

        if user_input.lower() != "y":
            print('Thanks for using our application')
            break

input_1()