import math

# given three floating-point numbers x, y, and z
x = float(input())
y = float(input())
z = float(input())

# calculate x to the power of z
xpowz = x ** z

# calculate x to the power of (y to the power of z)
xpow_ypowz = x ** (y ** z)

# calculate the absolute value of (x - y)
abs_xy = abs(x - y)

# calculate the square root of (x to the power of z)
sqrt_xpowz = math.sqrt(x ** z)

# output x to the power of z, x to the power of (y to the power of z), the absolute value of (x - y), and the square root of (x to the power of z)
print(f'{xpowz:.2f} {xpow_ypowz:.2f} {abs_xy:.2f} {sqrt_xpowz:.2f}')
