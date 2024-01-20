# Get the number of packages purchased from the user
quantity = int(input("Enter the number of packages purchased: "))

# Define the package price
package_price = 99  # $99 per package

# Initialize discount and total variables
discount = 0
total_amount = 0

# Check the quantity and calculate the discount
if quantity >= 10 and quantity <= 19:
    discount = 0.10
elif quantity >= 20 and quantity <= 49:
    discount = 0.20
elif quantity >= 50 and quantity <= 99:
    discount = 0.30
elif quantity >= 100:
    discount = 0.40

# Calculate the total amount after applying the discount
discounted_price = package_price * (1 - discount)
total_amount = quantity * discounted_price

# Display the discount and total amount
print(f"Discount: {discount * 100}%")
print(f"Total amount after discount: ${total_amount:.2f}")
