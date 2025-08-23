# write an assignment statement for the following equation
# y = (1/3)x + (x/4) + 2x

x = int(input())

y = (1.0 / 3) * x + (x / 4.0) + 2 * x  # ( / ) for floating point division

print(round(y, 5))


# originally tried the following
# x = int(input())

# y = ((1/3) * x) + (x / 4) + (2 * x)

# print(round(y, 5))

# to ensure floating-point division, regardless of what Python version is being uses and to avoid any surprises, it's best to change 1/3 to 1.0 / 3
# x / 4 to x / 4.0
# this explicitly ensures both pieces of the equation are floating-point division
