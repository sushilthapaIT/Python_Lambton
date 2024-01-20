# x = 2 ** 

# print(x)

# print(format(1235.6789, '.2e'))

def calculate_compound_interest(principal, rate, compounding_frequency, time):
    # Convert the annual rate to a decimal and calculate the number of compounding periods
    rate_decimal = rate / 100
    n = compounding_frequency * 1.0
    t = time * 1.0

    # Calculate the future value using the compound interest formula
    future_value = principal * (1 + rate_decimal / n)**(n * t)

    return future_value

# Input values
principal_amount = float(input("Enter the principal amount: "))
annual_interest_rate = float(input("Enter the annual interest rate (%): "))
compounding_frequency = int(input("Enter the compounding frequency per year: "))
investment_time_years = float(input("Enter the number of years: "))

# Calculate compound interest
result = calculate_compound_interest(
    principal_amount, annual_interest_rate, compounding_frequency, investment_time_years)

# Print the result
print(f"The future value of your investment is: ${result:.2f}")'''


