num_pizzas = int(input())
cost = 14.99
tax_rate = 0.08

# calculate subtotal
subtotal = (num_pizzas * cost)

# calculate total cost
total_cost = subtotal + (subtotal * tax_rate)

print(f'Pizzas: {num_pizzas}')
print(f'Subtotal: ${subtotal:.2f}')
print(f'Total due: ${total_cost:.2f}')
