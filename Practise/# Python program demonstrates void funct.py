'''def paint_job_estimator():
    square_feet_per_gallon = 112
    hours_of_labor_per_gallon = 8
    labor_cost_per_hour = 35

    try:
        square_feet = int(input('Enter the square feet of wall space to be painted: '))
        paint_gallon = int(input('Enter the price of the paint per gallon: '))
    except ValueError:
        print('Invalid Input')

    gallons_of_paint_required = square_feet / square_feet_per_gallon
    hours_of_labor_required = gallons_of_paint_required * hours_of_labor_per_gallon
    cost_of_paint = gallons_of_paint_required * paint_gallon
    labor_charges = hours_of_labor_required * labor_cost_per_hour
    total_cost = cost_of_paint + labor_charges

    print('The number of gallons of paint required is: ', gallons_of_paint_required)
    print('The hours of labor required is: ',hours_of_labor_required)
    print('The cost of the paint required is: ',cost_of_paint)
    print('The labor charge is: ',labor_charges)
    print('The total cost of the paint job is: ',total_cost)


paint_job_estimator()'''
'''total_score = 0
def calc_average():
        for i in range(5):
            try:
                test_score = int(input(f"Enter {i+1}s test scores: "))
                total_score += test_score
            except ValueError:
                print("Invalid Input")
            

        print("the sum of 5 test score is: ",total_score)


calc_average()'''

'''total_score = 0  # Initialize total score to zero

for i in range(5):
    try:
        test_score = int(input(f"Enter {i+1}'s test score: "))
        total_score += test_score  # Update total score
    except ValueError:
        print("Invalid Input")

print(f"\nTotal Score: {total_score}")'''

'''def calc_average():
    sum = 0 
    try:
        for i in range(5):
            test_score = int(input(f"Enter {i+1}'s test score: "))
            sum += test_score
    except ValueError:
        print("Invalid Input")

    print('The sum of 5 num is: ', sum)


calc_average()

def determine_grade(calc_average):
    if (calc_average >=90 or calc_average<=100):
        print('You have got grade A')


determine_grade(calc_average)'''

'''def user_test():
    while True:
        user_input = input("Do you want to try again [Y/N]")

        if user_input.lower() != "y":
            print("Thank you for using our program")
        break


def determine_grade():'''

    
'''    if (test_score <= 90 or test_score >= 100):
        print("you got A") '''





'''try:
    loan_amount = float(input("Enter the loan amount: $"))
    annual_interest_rate = float(input("Enter the annual interest rate (as a percentage): "))
    num_of_months = int(input("Enter the desired number of months: "))
except ValueError:
    print("INVALID INPUT")

monthly_interest_rate = annual_interest_rate / 100 / 12
monthly_payment = (monthly_interest_rate * loan_amount) / (1 - (1 + monthly_interest_rate) ** -num_of_months)

print(loan_amount)
print(annual_interest_rate)
print(num_of_months)
print(monthly_interest_rate)
'''



'''def main():
    # Get user input
    loan_amount = float(input("Enter the loan amount: $"))
    annual_interest_rate = float(input("Enter the annual interest rate (as a percentage): "))
    num_of_months = int(input("Enter the desired number of months: "))
    
    # Call the function to calculate the monthly payment
    monthly_payment = calculate_monthly_payment(loan_amount, annual_interest_rate, num_of_months)
    
    # Display the result
    print(f"\nThe monthly payment amount needed to pay off the loan in {num_of_months} months is: ${monthly_payment:.2f}")

def calculate_monthly_payment(loan_amount, annual_interest_rate, num_of_months):
    # Convert annual interest rate to monthly rate
    monthly_interest_rate = annual_interest_rate / 100 / 12
    
    # Calculate monthly payment using the formula
    monthly_payment = (monthly_interest_rate * loan_amount) / (1 - (1 + monthly_interest_rate) ** -num_of_months)
    
    return monthly_payment
if __name__ == "__main__":
    main()
'''


'''
# Constants
GALLON_PER_SQUARE_FEET = 1 / 112  # One gallon covers 112 square feet
LABOR_HOURS_PER_SQUARE_FEET = 8  # Eight hours of labor per 112 square feet
LABOR_COST_PER_HOUR = 35.00  # Labor cost per hour

# User input
square_feet = float(input("Enter the square feet of wall space to be painted: "))
paint_price_per_gallon = float(input("Enter the price of paint per gallon: $"))

# Calculations
gallons_of_paint = square_feet * GALLON_PER_SQUARE_FEET
hours_of_labor = square_feet / 112 * LABOR_HOURS_PER_SQUARE_FEET
paint_cost = gallons_of_paint * paint_price_per_gallon
labor_cost = hours_of_labor * LABOR_COST_PER_HOUR
total_cost = paint_cost + labor_cost

# Display the results
print("\nResults:")
print(f"Number of gallons of paint required: {gallons_of_paint:.2f} gallons")
print(f"Hours of labor required: {hours_of_labor:.2f} hours")
print(f"Cost of paint: ${paint_cost:.2f}")
print(f"Labor charges: ${labor_cost:.2f}")
print(f"Total cost of the paint job: ${total_cost:.2f}")'''


'''sum = 0 
for i in range(5):
    test_score = int(input(f"Enter {i+1}'s test score: "))
    sum += test_score

print('The sum of 5 num is: ', sum)'''

'''
def calculate_monthly_payment(loan_amount, annual_interest_rate, num_months):
    # Convert annual interest rate to monthly and decimal
    monthly_interest_rate = (annual_interest_rate / 100) / 12

    # Calculate monthly payment using the formula provided
    monthly_payment = loan_amount * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -num_months)

    return monthly_payment

def main():
    # Get user input
    loan_amount = float(input("Enter the loan amount: "))
    annual_interest_rate = float(input("Enter the annual interest rate (as a percentage): "))
    num_months = int(input("Enter the number of months: "))

    # Call the function to calculate the monthly payment
    monthly_payment = calculate_monthly_payment(loan_amount, annual_interest_rate, num_months)

    # Display the result
    print(f"The monthly payment amount necessary is: {monthly_payment:.2f}")

# Run the program
if __name__ == "__main__":
    main()
'''

'''# Get user input
loan_amount = float(input("Enter the loan amount: "))
annual_interest_rate = float(input("Enter the annual interest rate (as a percentage): "))
num_months = int(input("Enter the number of months: "))

# Convert annual interest rate to monthly and decimal
monthly_interest_rate = (annual_interest_rate / 100) / 12

# Calculate monthly payment using the formula
monthly_payment = loan_amount * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -num_months)

# Display the result
print(f"The monthly payment amount necessary is: {monthly_payment:.2f}")
'''


'''state_sale_tax = 5 / 100
country_sale_tax = 2.5 / 100

total_sales = int(input("Enter the total sales for the month: "))

amt_state_sale = (total_sales * state_sale_tax)
amt_country_sale = (total_sales * country_sale_tax)
total_sales = amt_state_sale + amt_state_sale

print("The amount of country sales tax is: ", format(amt_country_sale, '.2f'))
print("The amount of state sales tax: ", format(amt_state_sale, '.2f'))
print("The total sales tax is: ", format(total_sales, '.2f'))'''


'''# Constants for tax rates
state_tax_rate = 0.05  # 5%
county_tax_rate = 0.025  # 2.5%

# Get user input for total sales
total_sales = float(input("Enter the total sales for the month: $"))

# Calculate taxes
state_sales_tax = total_sales * state_tax_rate
county_sales_tax = total_sales * county_tax_rate
total_sales_tax = state_sales_tax + county_sales_tax

# Display results
print(f"\nAmount of County Sales Tax: ${county_sales_tax:.2f}")
print(f"Amount of State Sales Tax: ${state_sales_tax:.2f}")
print(f"Total Sales Tax: ${total_sales_tax:.2f}")'''

import random

def generate_random_value():
    # Generate a random number between 1 and 3
    random_number = random.randint(1, 3)

    return random_number

# Example usage
random_value = generate_random_value()
print(random_value)

