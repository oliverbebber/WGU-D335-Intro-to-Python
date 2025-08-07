# Accept user input in integers for current price & last months price
current_price = int(input())
last_months_price = int(input())

# Calculate the change in price
price_change = current_price - last_months_price

# Calculate the estimated monthly mortgage
est_monthly_mortgage = (current_price * 0.051) / 12

# Output a summary listing the price, change in price, and estimated monthly mortgage
print(f'This house is ${current_price}. The change is ${price_change} since last month.')
print(f'The estimated monthly mortgage is ${est_monthly_mortgage:.2f}.')
