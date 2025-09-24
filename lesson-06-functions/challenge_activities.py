# 6.1.1
def get_pattern():
   return '*****'

# finish the program to get the following output:
# *****
# *****

print(get_pattern())
print(get_pattern())



# 6.5.1
def find_max(num_1, num_2):
   max_val = 0.0

   if (num_1 > num_2):  # if num1 is greater than num2,
      max_val = num_1   # then num1 is the maxVal.
   else:                # Otherwise,
      max_val = num_2   # num2 is the maxVal
   return max_val

max_sum = 0.0

num_a = float(input())
num_b = float(input())
num_y = float(input())
num_z = float(input())

# assign max_sum with the greater of num_a and num_b, PLUS the greater of num_y and num_z. 
# Use just one statement
max_sum = find_max(num_a, num_b) + find_max(num_y, num_z)

print(f'max_sum is: {max_sum}')


# 6.5.2
MILLILITERS_PER_TEASPOON = 4.92892
TEASPOONS_PER_TABLESPOON = 3

# define function convert_volume()
def convert_volume(tablespoons, teaspoons):
    # returns volume converted to milliliters
    total_teaspoons = tablespoons * TEASPOONS_PER_TABLESPOON + teaspoons
    result = total_teaspoons * MILLILITERS_PER_TEASPOON
    return result   # remember to always return the result at the end of a function
   
tablespoons = int(input())
teaspoons = int(input())

# Print with value rounded to 3 decimal places  
print(f'{convert_volume(tablespoons, teaspoons):.3f} milliliters')




# define find_base_area() with two params as a prism's base length & width
# the function returns the area of the prism's base
def find_base_area(base_length, base_width):
    area = base_length * base_width
    return area

# define find_vol() with three params as a prism's base length, width, and height
# the function returns the prism's volume and uses the find_base_area() function
# to calculate the prism's base area
def find_vol(base_length, base_width, height):
    base_area = find_base_area(base_length, base_width)   # area is not defined, requiring find_base_area() to be included
    volume = base_area * height
    return volume

base_length = float(input())
base_width = float(input())
height = float(input())

print(f'Base length: {base_length}')
print(f'Base width: {base_width}')
print(f'Height: {height}')
print(f'Base area: {find_base_area(base_length, base_width):.1f}')
print(f'Volume: {find_vol(base_length, base_width, height):.1f}')






# 6.7.2
# define function print_popcorn_time() with param bag_ounces
def print_popcorn_time(bag_ounces):
   # if bag_ounces is less than 3, print "Too small"
   if bag_ounces < 3:
      print('Too small')
   # if bag_ounces is greater than 10, print "Too large"
   elif bag_ounces > 10: 
      print('Too large')
   # otherwise, compute & print 6 * bag_ounces followed by " seconds"
   else:
      print(f'{bag_ounces * 6} seconds')

bag_ounces = int(input())
print_popcorn_time(bag_ounces)






# 6.7.3
# define function find_fee() with one parameter as person's age traveling by train
def find_fee(input_age):
   # returns ticket price
   # price is returned as follows:
   # if the person's age is less than 5 or more than 78, price is $5
   if input_age < 5 or input_age > 78:  # use OR
      return 5    # return val instead of price == val
   # if the person's age is no more than 56 and at least 17, price is $21
   elif 17 <= input_age <= 56: # 17 <= means age is greater than or equal to 17
      return 21
   # otherwise, price is $11
   else:
      return 11
    
input_age = int(input())

print(f'Testing 1: {find_fee(1)}')
print(f'Testing user input: {find_fee(input_age)}')






# define function output_sum() with two params
def output_sum(numberA, numberB):
    # outputs the sum of all integers starting with the 1st parameter, ending with the 2nd
    result = sum(range(numberA, numberB + 1))   # range(start, end +1)
    print(result)   # function does NOT return any value

numberA = int(input())
numberB = int(input())

print('Testing static input: ')
output_sum(4, 6)
print(f'\nTesting user input: ')
output_sum(numberA, numberB)







# 6.9.1
def celsius_to_kelvin(value_celsius):
    value_kelvin = 0.0

    value_kelvin = value_celsius + 273.15
    return value_kelvin

# using the celsisus_to_kelvin function
# create a new function kelvin_to_celsius
# modify the function accordingly
def kelvin_to_celsius(value_kelvin):
    value_celsius = 0.0
    
    value_celsius = value_kelvin - 273.15
    return value_celsius
    
value_c = 10.0
print(f'{value_c} C is {celsius_to_kelvin(value_c)} K')

value_k = float(input())
print(f'{value_k} K is {kelvin_to_celsius(value_k)} C')





# 6.12.1
# my_age and num_years are read from input
# calculate_future_age() has two params num_age and num_years
# outputs the sum of num_age and num_years
def calculate_future_age(num_age, years):
    print(f'Age in {years} years: {num_age + years}')

my_age = int(input())
num_years = int(input())

# call calculate_future_age() to output the sum of my_age and num_years without modifying my_age
calculate_future_age(my_age, num_years)

print(f'Age now: {my_age}')




# write a function set_elements() that assigns 'default' to the 
# last and 5th elements of a list param
def set_elements(number_list):
    # set the 5th element
    number_list[4] = 'default'
    # set the last element
    number_list[-1] = 'default'

number_list = input().split()

set_elements(number_list)
print(number_list)
