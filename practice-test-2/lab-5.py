# solution accepts five integer inputs
# solution outputs three sums of input values; convert before calculating sum
# first output: the sum of the five inputs as an integer value
# second output: the sum of the five inputs after converting each input to a float value
# third output: the concatenation of the five inputs after converting each input to a string
# accept five integer inputs
print("Enter 1st number:")
num1 = int(input())
print("Enter 2nd number:")
num2 = int(input())
print("Enter 3rd number:")
num3 = int(input())
print("Enter 4th number:")
num4 = int(input())
print("Enter 5th number:")
num5 = int(input())

sum5 = num1 + num2+ num3 + num4 + num5
floatsum = float(sum5)
string = str(num1) + str(num2) + str(num3) + str(num4) + str(num5)

print(f'Integer: {sum5}')
print(f'Float: {floatsum}')
print(f'String: {string}')
