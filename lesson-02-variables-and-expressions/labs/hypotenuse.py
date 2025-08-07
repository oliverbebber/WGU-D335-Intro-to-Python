a = float(input())
b = float(input())

print(f'Right triangle has side lengths {a:.2f} and {b:.2f}')

# Calculate hypotenuse using Pythagorean's Theorem
hypotenuse = (a**2 + b**2) ** 0.5

# Output the length of the third side (hypotenuse) with 2 digits after the decimal point
print(f'Hypotenuse is {hypotenuse:.2f}')
