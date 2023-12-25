#CSD-1233-01
#Assignment 6
#C0919991
#Sushil Thapa
#November 08,2023

# Function to display menu and handle user choice
def menu():
    print("Menu:")
    print("1. Calculate total meal amount")
    print("2. Calculate hectares in a tract of land")
    print("3. Calculate compound interest")
    choice = input("Enter your choice (1, 2, or 3): ")
    while choice not in ['1', '2', '3']:
        print("Invalid choice. Please enter 1, 2, or 3.")
        choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        tract_hector()
    elif choice == '2':
        calculate_total_meal_amount()
    elif choice == '3':
        calculate_compound_interest()


def tract_hector():
    #Setting the variable equal to the amount of square feet in one hector 
    one_hector = 10000
    #This gets the number of square feet in the user's tract of land and casting the value integer
    total_square = float(input('Enter the total square meters in a tract of land?'))
    # This calculates the land size in acres
    hec_num = (1 / one_hector)*total_square
    #Displays the result to the user.
    print('The number of hectares in the tract', format(hec_num, '.2f'))

def calculate_total_meal_amount():
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

def calculate_compound_interest():
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

# Function to display menu and handle user choice
def menu():
    print("Menu:")
    print("1. Calculate total meal amount")
    print("2. Calculate hectares in a tract of land")
    print("3. Calculate compound interest")
    choice = input("Enter your choice (1, 2, or 3): ")
    while choice not in ['1', '2', '3']:
        print("Invalid choice. Please enter 1, 2, or 3.")
        choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        tract_hector()
    elif choice == '2':
        calculate_total_meal_amount()
    elif choice == '3':
        calculate_compound_interest()


# Main function
def main():
    while True:
        menu()
        another_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if another_calculation.lower() != 'yes':
            print("Thank you for using the program. Goodbye!")
            break


# Call the main function
if __name__ == "__main__":
    main()