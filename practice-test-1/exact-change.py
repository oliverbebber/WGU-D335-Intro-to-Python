# helper function to print denominations based on singular / plural
def print_change(count, name):
  if count > 0:
    if name == "Penny":
      print(f"{count} Penn{'ies' if count > 1 else 'y'}")
    else:
      print(f"{count} {name}{'s' if count > 1 else ''}")

# Read integer input for total change amount
total_change = int(input())

# If the amount is less than or equal to 0, print "No change" and stop the program
if total_change <= 0:
  print('No change')
  exit()

# Otherwise:

# 1. Calculate how many whole dollars fit into the total
dollars = total_change // 100
# 2. Update the remaining cents after subtracting dollars
remaining = total_change % 100

# Print "1 Dollar" if exactly one, otherwise "x Dollars" if more than one
print_change(dollars, "Dollar")

# 3. Calculate how many quarters (25¢) fit into the remaining amount
quarters = remaining // 25
# 4. Update the remaining cents after subtracting quarters
remaining %= 25

# Print "1 Quarter" or "x Quarters" as appropriate
print_change(quarters, "Quarter")

# 5. Calculate how many dimes (10¢) fit into the remaining amount
dimes = remaining // 10
# 6. Update the remaining cents after subtracting dimes
remaining %= 10

#  Print "1 Dime" or "x Dimes"
print_change(dimes, "Dime")

# 7. Calculate how many nickels (5¢) fit into the remaining amount
nickels = remaining // 5
# 8. Update the remaining cents after subtracting nickels
remaining %= 5

#  Print "1 Nickel" or "x Nickels"
print_change(nickels, "Nickel")

# 9. The remainder after nickels are pennies
pennies = remaining

#  Print "1 Penny" or "x Pennies"
print_change(pennies, "Penny")
