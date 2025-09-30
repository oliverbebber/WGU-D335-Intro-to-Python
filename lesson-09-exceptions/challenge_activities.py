# 9.1.2
# Add a try block to read an integer manufacture_year from input
# and outputs 'Manufacture year is ' followed by the value of manufacture_year

try:
    manufacture_year = int(input())
    print(f'Manufacture year is {manufacture_year}')

except:
    print('Error: The manufacture year entered is invalid')


# Add an except block to handle an exception 
# and outputs "Error: Bad input value for shaft's height"
try:
    shaft_height = int(input())
    print(f"Shaft's height (in cm) is {shaft_height}")

except:
  print('Error: Bad input value for shaft\'s height')



# Add an except block in the while loop to handle an exception
# and outputs "Bad input for color intensity is discarded"
has_read = 0
carry_on = True

while carry_on:
    try:
        color_intensity = int(input())
        if color_intensity == -100:
            print(f'Processed {has_read} valid input values')
            carry_on = False
        else:
            print(f'Color intensity: {color_intensity}')
            has_read = has_read + 1
    except:
        print('Bad input for color intensity is discarded')



# 9.3.1 Exception handling
try:
    user_age = int(input())

    if user_age < 0:
        raise ValueError('Invalid age')

    # Source: https://www.heart.org/en/healthy-living/fitness
    avg_max_heart_rate = 220 - user_age

    print(f'Avg: {avg_max_heart_rate}')

except ValueError as excpt:
    print(f'Error: {excpt}')

# input: 70
# output: Avg: 150
#

try:
    user_age = int(input())

    if user_age < 0:
        raise ValueError('Invalid age')

    # Source: https://www.heart.org/en/healthy-living/fitness
    avg_max_heart_rate = 220 - user_age

    print(f'Avg: {avg_max_heart_rate}')

except ValueError as excpt:
    print(f'Error: {excpt}')

# input: -30
# output: Error: Invalid age
#


valid_password = False

while valid_password == False:
    try:
        password = input()

        if len(password) < 8:
            raise ValueError('Invalid')

        valid_password = True
        print('Accepted')

    except ValueError as excpt:
        print(f'Error: {excpt}')

# input: apples107
# output: Accepted
#


valid_password = False

while valid_password == False:
    try:
        password = input()

        if len(password) < 8:
            raise ValueError('Invalid')

        valid_password = True
        print('Accepted')

    except ValueError as excpt:
        print(f'Error: {excpt}')

# input: red59
#     yellow62
# output: Error: Invalid
# Accepted
#
