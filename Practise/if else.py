# all = float(input("EnTER 1ST NUM"))
# inn = float(input("EnTER 2nd NUM"))

# if (all == inn):
#     print("They are equal")
# else:
#     print("They are not equal")


# all = float(input("EnTER your salary to know if you qualify for loan or not: "))
# inn = float(input("EnTER 2nd NUM"))

# if(all >= 50000):

#     if(inn >= 2):
#         print('you are qualify for loan')
    
# else:
#     print('you are not qualified for loan.')

# all = float(input("EnTER your salary to know if you qualify for loan or not: "))
# inn = float(input("EnTER 2nd NUM"))
# if (all >= 50000 and inn >= 2):
#      print('you are qualify for loan')
# else:
#  print('you are not qualified for loan.')


# i = 1

# while i <= 5:
#    print('hello' , i)
#    i=i+1
















# i=1
# j = 1

# while (j <= 5):
#    print('i')
#    j=j+1
#    while(i <=5):
#       print('h')
#       i=i+1


# name = input('enter your name?')

# while name == "":
#    print('you did not enter anything!!')
#    name = input('enter your name?')
#    print('your name is' ,name)


# a = input('enter a number!!')

# if (a <= 2):
#     a == 90
#     print(a)
    

'''a = input('enter your 1st score')

b = input('enter your 2nd score')

c = input('enter your 3rd score')

d = input('enter your 4th score')

e = input('enter your 5th score')

total_score = a + b + c + d + e


if total_score >= 63 :
    print('you earned a bonus')
else:
    print('you did not earned a bonus')'''


# user_inputs = []

# # Use a while loop to repeatedly get input
# while True:
#     user_input = input("Enter something (or 'done' to exit): ")
    
#     if user_input.lower() == 'done':
#         break  # Exit the loop if the user enters 'done'
    
def main():
    upper_section = [0] * 6  # Initialize an array to store scores for each number (ones to sixes)
    
    # Ask the user for input for each number
    for i in range(1, 7):
        while True:
            try:
                num_rolled = int(input(f"How many {i}s did you score? (1-5): "))
                if 1 <= num_rolled <= 5:
                    upper_section[i - 1] = i * num_rolled
                    break
                else:
                    print("Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a valid number between 1 and 5.")

    # Calculate the subtotal
    subtotal = sum(upper_section)
    
    # Check if the user scored 63 or more for the bonus
    if subtotal >= 63:
        bonus = 35
    else:
        bonus = 0
    
    # Calculate the total score
    total_score = subtotal + bonus
    
    # Display the results
    print(f"Your subtotal is {subtotal}")
    if bonus > 0:
        print("You earned a bonus")
    else:
        print("You did not earn a bonus")
    print(f"Your total is {total_score}")

if __name__ == "__main__":
    main()
