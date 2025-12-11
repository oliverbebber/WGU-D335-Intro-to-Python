# 9.1.1
try:
    number1 = int(input())
    print(number1 * 2)

    number2 = int(input())    # causes the exception as K is not an int
    print(number2 * 2)
except:
    print('x')
print('e')

# input: 
# 3
# K

# output:
# 6
# x
# e
#


user_input = input()
while user_input != 'q':    # q causes the program to skip the entire try/except blocks
    try:
        number = int(user_input)
        print(number * 3)
    except:
        print('x')
    user_input = input()
print('e')

# input:
# 5
# 6
# q

# output:
# 15
# 18
# e
#


user_input = input()
while user_input != 'q':
    try:
        number = int(user_input)
        print(number * 4)
    except:
        print('x')
    user_input = input()
print('e')

# input:
# 3
# L
# 7
# q

# output:
# 12
# x
# 28
# e
#





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




# 9.2.1
user_input = input()
while user_input != 'end':
    try:
        # Possible ValueError
        divisor = int(user_input)
        # Possible ZeroDivisionError
        print(60 // divisor) # Truncates to an integer
    except ValueError:
        print('v')
    except ZeroDivisionError:
        print('z')
    user_input = input()
print('OK')

# input:
# 0
# 1
# 3
# four
# end

# output:
# z
# 60
# 20
# v
# OK
#


numbers = [2, 4, 5, 8]
user_input = input()
while user_input != 'end':
    try:
        num_val = int(user_input)
        if num_val < 0:
            # Possible IndexError if num_val is less than 0
            print(numbers[num_val])
        else:
            # Possible ZeroDivisionError
            print(20 // num_val)          # Truncates to an integer
    except ZeroDivisionError:
        print('r')
    except IndexError:
        print('s')
    user_input = input()
print('OK')

# input:
# 20
# -6
# 0
# end

# output:
# 1
# s
# r
# OK
#


user_input = input()
while user_input != 'end':
    try:
        # Possible ValueError
        divisor = int(user_input)
        if divisor < 0:
            # Possible NameError because
            # compute() is not defined
            print(compute(divisor))
        else:
            # Possible ZeroDivisionError
            print(20 // divisor)     # Truncates to an integer
    except ValueError:
        print('v')
    except ZeroDivisionError:
        print('z')
    except:
        print('x')
    user_input = input()
print('OK')

# input:
# 0
# three
# 2
# -9
# end

# output:
# z
# v
# 10
# x
# OK
# 







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



