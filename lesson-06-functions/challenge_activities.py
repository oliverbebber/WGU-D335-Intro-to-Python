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
