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
