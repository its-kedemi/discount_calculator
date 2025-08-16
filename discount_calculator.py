# Function to calculate discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price

# Prompt user for input
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(price, discount_percent)

# Print the result
if final_price < price:
    print(f"Final price after discount: {final_price}")
else:
    print(f"No discount applied. Original price: {price}")

