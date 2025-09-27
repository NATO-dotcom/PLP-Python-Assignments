def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    If discount_percent >= 20, applies the discount.
    Otherwise, returns the original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price

# Prompt user for input
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(original_price, discount_percent)

# Print the result
print(f"The final price is: ${final_price:.2f}")
