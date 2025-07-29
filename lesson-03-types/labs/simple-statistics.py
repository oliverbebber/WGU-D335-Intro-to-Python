# Given 4 floating-point numbers
num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

# Calculate product of 4 floating-point numbers
product = num1 * num2 * num3 * num4

# Calculate the average of 4 floating-point numbers
average = (num1 + num2 + num3 + num4) / 4

# Output each rounded integer 
print(f'{product:.0f} {average:.0f}')

# Output each floating-point value with 3 digits after the decimal point
print(f'{product:.3f} {average:.3f}')
