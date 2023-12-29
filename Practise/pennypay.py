# Get the number of days from the user
try:
    num_days = int(input("Enter the number of days: "))
    if num_days <= 0:
        raise ValueError("Number of days must be a positive integer.")

    total_salary = 0
    print(f"{'Day':<5}{'Salary':<15}")

    for day in range(1, num_days + 1):
        salary = 2 ** (day - 1)  # Calculate salary for the day (doubling each day)
        total_salary += salary

        # Display the salary for each day
        print(f"{day:<5}${salary / 100:<15.2f}")

    # Display the total salary at the end of the period
    print("\nTotal salary for the period: ${:.2f}".format(total_salary / 100))

except ValueError as e:
    print(f"Error: {e}")
