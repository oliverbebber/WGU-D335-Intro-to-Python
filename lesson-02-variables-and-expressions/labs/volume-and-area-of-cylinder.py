import math

r = float(input())
h = float(input())

pi = math.pi

# Calculate volume for cubic inches
cubic_inches = (pi * r**2) * h

# Calculate area for square inches
square_inches = (2 * pi * r * h) + (2 * pi * r * r)

print(f'Volume (cubic inches): {cubic_inches:.2f}')
print(f'Surface area (square inches): {square_inches:.2f}')
