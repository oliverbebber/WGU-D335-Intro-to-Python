# given three input values representing nickels, dimes, and quarters
nickels = int(input())
dimes = int(input())
quarters = int(input())

# output the total amount as dollars and cents
dollars = (nickels * 0.05) + (dimes * 0.10) + (quarters * 0.25)

# output each floating-point value with two digits after the decimal point
print(f'Amount: ${dollars:.2f}')
