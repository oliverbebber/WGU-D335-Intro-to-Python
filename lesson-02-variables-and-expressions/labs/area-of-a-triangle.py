import math

a = float(input())
b = float(input())
c = float(input())

# half of the triangle's perimeter
s = (a + b + c) / 2

# area = sqrt of s * (s-a) * (s-b) * (s-c)
area = math.sqrt(s * (s - a) * (s - b) * (s - c))  # remember to use math module before sqrt function

# output the floating-point value of the area with 2 digits after the decimal point
print(f'Triangle area = {area:.2f}')
