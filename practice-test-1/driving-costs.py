# write a program with a car's gas mileage (miles/gallon) and the cost of gas (dollars/gallon) as floating-point input
miles_per_gallon = float(input())
dollars_per_gallon = float(input())

# define distances
dist_a = 20
dist_b = 75
dist_c = 500

# output the gas cost for 20 miles, 75 miles, and 500 miles
cost_a = ((dist_a / miles_per_gallon) * dollars_per_gallon)
cost_b = ((dist_b / miles_per_gallon) * dollars_per_gallon)
cost_c = ((dist_c / miles_per_gallon) * dollars_per_gallon)

# output each floating-point value with two digits after the decimal point
print(f'{cost_a:.2f} {cost_b:.2f} {cost_c:.2f}')





# this problem could also be solved using a dictionary and for loop
miles_per_gallon = float(input())
dollars_per_gallon = float(input())

# define distances in a dictionary for loop
distances = {
  "dist_a": 20,
  "dist_b": 75,
  "dist_c": 500
}

# initialize costs as an empty list to have calculations stored in
costs = []
# for each distance in dictionary
for dist in distances.values():
  # calculate the cost by dividing distance by mph and multiply by the dollars per gallon
  cost = (dist / miles_per_gallon) * dollars_per_gallon
  # add the value of cost to the end of the empty costs list
  costs.append(cost)

# output each floating-point value with two digits after the decimal point
print(f'{costs[0]:.2f} {costs[1]:.2f} {costs[2]:.2f}')
