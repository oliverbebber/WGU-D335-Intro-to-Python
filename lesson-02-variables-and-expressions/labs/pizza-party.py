import math

# Read number of people attending the event from user input
people = int(input())

# Calculate the number of slices needed (2 slices per person)
total_slices = people * 2

# Calculate the number of pizzas needed, rounding up
pizzas_needed = math.ceil(total_slices / 12)

# Calculate the total cost
cost = pizzas_needed * 14.95

# Output results for number of people, pizzas needed and cost for the number of pizzas necessary for the event
print(f'People: {people}')
print(f'Pizza(s): {pizzas_needed}')
print(f'Cost for {pizzas_needed} pizza(s): ${cost:.2f}')
