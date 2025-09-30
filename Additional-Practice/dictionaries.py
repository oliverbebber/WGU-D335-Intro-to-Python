# Dictionary with branching to find full price, savings, and total cost after savings
purchase = {"bananas": 1.85, "steak": 19.99, "cookies": 4.52, "celery": 2.81, "milk": 4.34}

print("Enter the item to purchase:")
#solution accepts a string input representing an item (dictionary key)
item = input()

#solution accepts an integer input representing the number of items to be purchased
print("Enter the quantity of that item:")
quantity = int(input())

#cost per item: 
    # <10 is full price
    # 10-20 (inclusive) is 5% discount
    # 21+ is 10% discount
if quantity < 10:
    discount = 0
elif 10 <= quantity <= 20:
    discount = 0.05
else:
    discount = 0.10
    
# calculate total with discount
# formula: total = cost per item * qty * (1 - discount)
total = purchase[item] * quantity * (1 - discount)

# calculate full price (no discount)
full_price = purchase[item] * quantity
# print(purchase[item])
# print(full_price)
    
# show total savings
print(f'Savings on this purchase: ${full_price - total:.2f}')

# show paid price
print(f'You paid: ${total:.2f}')

# show full price
print(f'Without your membership, you would have paid: ${full_price:.2f}')

