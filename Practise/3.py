def yes_no():
    while True:
        try:
            inp = int(input('enter the number or you will get invalid input'))
            for num in range(inp):
                    ok = int(input('enter the number for sum of all number'))
                    sum = ok + ok
            print('the sum of the number is: ' , sum)
            
            user_input = input('want to try again [y/n]')
            if user_input.lower() == "y":
                 inp = int(input('enter the number or you will get invalid input'))
            break
            
        except ValueError:
            print('Invalid Input')

yes_no()

                    
