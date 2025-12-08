# 8.1.1
user_values = [1, 4, 8]

print(user_values)
# output: [1, 4, 8]
#

user_values = [2, 5, 9]
user_values[0] = user_values[0] + 1  # increments the first element in user_values by 1

print(user_values)
# output: [3, 5, 9]
#

user_values = [3, 5, 8]
user_values[2] = user_values[2] + 1
user_values[1] = user_values[1] + 2

print(user_values)
# output: [3, 7, 9]
# 

user_values = [1, 5, 9]
user_values[1] = user_values[0]

print(user_values)
# output: [1, 1, 9]
# 

user_values = [2, 6, 7]
user_values[0] = user_values[2]
user_values[2] = user_values[1]

print(user_values)
# output: [7, 6, 6]
# 


# 8.1.2
# int n is read from user input and 7 strings are read and stored in the list country_data
n = int(input())
country_data = input().split()

# output "Jan's favorite country: " followed by the nth element of country_data
print(f'Jan\'s favorite country: {country_data[n - 1]}')  # n needs to be reduced to match indices across various tests




m = int(input())
customer_line = input().split()

if m == 1:
    # assign suffix with 'st'
    suffix = 'st'
elif m == 2:
    # assign suffix with 'nd'
    suffix = 'nd'
elif m == 3:
    # assign suffix with 'rd'
    suffix = 'rd'
else:
    # assign suffix with 'th'
    suffix = 'th'
    
# output the mth element of customer_line
print(f'{customer_line[m - 1]} is the {m}{suffix} customer in line.')





n = int(input())
new_color = input()
paint_colors = input().split()

# delete second element in paint_colors
del paint_colors[1]

# replace nth element of paint_colors with new_color
paint_colors[n - 1] = new_color

print(f'My favorite colors: {paint_colors}')





paint_colors = input().split()
new_colors = input().split()

# create a new list updated_colors that 
# contains elements of new_colors and paint_colors, in that order
updated_colors = new_colors + paint_colors

print(f'Resulting data: {updated_colors}')




# 8.2.1
# int num_students is read from input
num_students = int(input())

students_list = []

# read the remaining strings from input and insert each string at the front of students_list at position 0
for i in range(num_students):
  student = input()
  students_list.insert(0, student)

print(students_list)




not_on_board = input().split()
on_board_bus = input().split()

print(f'Passengers waiting at a bus stop: {not_on_board}')
print(f'Passengers on board: {on_board_bus}')

# remove the last element from not_on_board 
passenger_left = not_on_board.pop()

# output "Passenger left bus stop: " followed by the element
print(f'Passenger left bus stop: {passenger_left}')

# add all remaining elements of not_on_board to the end of on_board_bus
on_board_bus.extend(not_on_board)

print(f'Updated passengers on board: {on_board_bus}')




tokens = input().split()
values_list = []
for token in tokens:
    values_list.append(int(token))

# sort values_list in-place
values_list.sort()

# assign median_index with the size of values_list divided by 2 using floor division
median_index = len(values_list) // 2 # be sure to use len(values_list) before dividing

# assign middle_value with the value at median_index in values_list
middle_value = values_list[median_index]

print(f'Sorted data: {values_list}')
print(f'Median: {middle_value}')





# 8.4.1
# assign sum_extra with the total extra credit received given the list
# test_grades. Iterate through the list with for grade in test_grades:
# the code uses the split() method to split a string at each space into
# a list of string values & the map() function to convert each string value
# to an integer.
# full credit is 100, so anything over 100 is extra credit
user_input = input()
test_grades = list(map(int, user_input.split())) # test_grades is an integer list of test scores

sum_extra = 0 # Initialize 0 before your loop

for grade in test_grades:
    if grade > 100:
        sum_extra += grade - 100
        
print(f'Sum extra: {sum_extra}')






# 8.4.2
# Read input and split input into tokens
tokens = input().split()

values_list = []
for token in tokens:
    values_list.append(int(token))

print(f'Raw samples: {values_list}')

count_good = 0

for index, value in enumerate(values_list):    # 
    # if element's value is less than 45
    if value < 45:
        # print the value followed by ' at index' with the index
        # and 'needs attention'
        print(f'{value} at index {index} needs attention'
    # otherwise 
    else:
        # increment count_good
        count_good += 1
        # output the value followed by ' at index' with the index
        # and ' is good'
        print(f'{value} at index {index} is good')

print(f'Total good samples: {count_good}')





# data_list contains integers read from input, representing data samples from an experiment

# 1.    initialize var sum_good with 0, 
# 2.    for each element in data_list that is at an odd-numbered index 
#       AND greater than or equal to 60:
# 3.    output 'Index ', the element's index, ': ' and the element's value
# 4.    increase sum_good by each such element's value

# Read input and split input into tokens
tokens = input().split()

data_list = []  # initialize data_list to store integers
for token in tokens:
    data_list.append(int(token))

print(f'All data: {data_list}')

sum_good = 0    # initialize sum as 0 before loop

for position, data in enumerate(data_list): # use enumerate() with looking for 2 criteria
    if position % 2 == 1 and data >= 60:
        print(f'Index {position}: {data}')
        sum_good += data

print(f'Sum of selected elements is: {sum_good}')




# data_list contains integers read from input, representing an increasing sequence of 
# data values. 

# max_diff measures the max difference between 2 neighboring values in the sequence 
# and is initialized with None

# 1.    for each index i of data_list from 1 through the last index (range)
# 2.    compute var neighbor_diff as the element at index i minus the element
#       at index i - 1
# 3.    output the element at index i, followed by '-', the element at index i - 1,
#       '=', and the value of neighbor_diff
# assign max_diff with the max value of neighbor_diff computed in all iterations

# Read input and split input into tokens
tokens = input().split()

data_list = []
for token in tokens:
    data_list.append(int(token))

print(f'Sequence: {data_list}')

max_diff = None

for i in range(1, len(data_list)):
    neighbor_diff = data_list[i] - data_list[i - 1]
    print(f'{data_list[i]} - {data_list[i - 1]} = {neighbor_diff}')
    if max_diff is None or neighbor_diff > max_diff:
        max_diff = neighbor_diff

print(f'The maximum difference between two neighboring values is {max_diff}')





# 8.6.1 
# two-dimensional list three_drinks consists of 3 lists
# list new_drink is read from input
# replace the element at index 2 of list three_drinks with new_drink
three_drinks = [
	['t', 'e', 'a'],
	['m', 'i', 'l', 'k'],
	['m', 'o', 'c', 'h', 'a']
]

new_drink = input().split()

three_drinks[2] = new_drink

print(three_drinks[0])
print(three_drinks[1])
print(three_drinks[2])




# two-dimensional list game_board represents a 3x3 tic-tac-toe game board from input
# list game_board contains 3 lists, each representing a row
# each list has 3 elements representing the 3 columns on the board
# each element in the tic-tac-toe game board is 'x', 'o', or '-'

# TODO: if all the elements at column index 2 are 'x', output 'A win at column 2.'
# TODO: otherwise, output 'No win at column 2'
# NOTE: a == 'x' and b == 'x' and c == 'x' returns True if a, b, and c are equal to 'x'
#       returns False otherwise
game_board = [
  input().split(),
  input().split(),
  input().split()
]

# print(game_board)   # v1: [['-', 'o', 'x'], ['o', '-', 'x'], ['-', '-', 'x']]
    # A win at column (index) 2

# print(game_board)   # v2: [['x', 'o', 'o'], ['-', '-', 'x'], ['-', '-', 'x']]
    # No win at column (index) 2

# print(game_board[2][2]) # v1: x; use format for loop

if (game_board[0][2] == 'x' and
    game_board[1][2] == 'x' and
    game_board[2][2] == 'x'):
        print('A win at column 2.')
else:
    print('No win at column 2.')



# integer num_lines is read from input, representing the number of rows of data
# remaining in the input
# two-dimensional list vals_2d consists of data read from the remaining input
# output each row of numbers in vals_2d on one line, ending each number with a space
num_lines = int(input())

vals_2d = []

for row_index in range(num_lines):  # ensures only num_lines rows of input is read
    row_elements = []
    for x in input().split():
        row_elements.append(int(x))
    vals_2d.append(row_elements)
# print(row_elements)

for row in vals_2d:
    for val in row:
        print(val, end=' ')
    print()



# integer grid_size is read from input representing the number of rows & columns of a 
# two-dimensional list. 
# list pattern_grid is created with zeros, 0, as the initial values
# for each element at row index i and column index j of pattern_grid, assign the 
# element with the value of j minus is
grid_size = int(input())

pattern_grid = []

for i in range(grid_size):
    row = []
    for j in range(grid_size):
        row.append(0)
    pattern_grid.append(row)
# print(row)          # returns [0, 0, 0, 0]

# fill in values with column[j] - row[i]
for i in range(grid_size):
    for j in range(grid_size):
        pattern_grid[i][j] = j - i
# print(row)          # returns [-3, -2, -1, 0]

for row in pattern_grid:
    for cell in row:
        print(cell, end=' ')
    print()






# 8.7.1 Enter the output of the sliced list
my_list = [13, 14, 15, 16, 17, 18, 19]
new_list = my_list[0:3]
print(new_list)

# output: [13, 14, 15]
#


my_list = [13, 14, 15, 16, 17, 18, 19]
new_list = my_list[0:7:3]
print(new_list)

# output: [13, 16, 19]
# 



my_list = [13, 14, 15, 16, 17, 18, 19]
new_list = my_list[3:4]
print(new_list)

# output: [16]
# 


my_list = [13, 14, 15, 16, 17]
new_list = my_list[-5:-2]
print(new_list)

# output: [13, 14, 15]
#

my_list = [13, 14, 15, 16, 17]
new_list = my_list[-3:-2]
print(new_list)

# output: [15]
#


my_list = [13, 14, 15, 16, 17]
new_list = my_list[-3:-1]
print(new_list)

# output: [15, 16]
#

my_list = [13, 14, 15, 16, 17]
new_list = my_list[0:-3]
print(new_list)

# output: [13, 14]
# 



# 8.7.2 List slicing
# list locations_list is read from input
# assign selected_locations with a slice of locations_list from the 3rd element
# up to and excluding the last two element
locations_list = input().split()

selected_locations = locations_list[2:-2]

print(f'Original list of locations: {locations_list}')
print(f'Selected list of locations: {selected_locations}')




# list experimental_data is read from input
# the elements of experimental_data are separated into thirds
# the first third of the data is collected in the beginning of a month
# the second third in the middle of a month
# and the last third in the end of the month
# integer slice_size represents the number of data in each third
# 1.    Assign slice_size with len(experimental_data) // 3
# 2.    Assign early_group with a slice of experimental_data from the beginning up to
#       and excluding index slice_size
# 3.    Assign mid_group with a slice of experimental_data from index slice_size up to
#       and excluding index (2 * slice_size)
# 4.    Assign late_group with a slice of experimental_data from index (2 * slice_size)
#       up to and including the end
experimental_data = []
for token in input().split():
	experimental_data.append(int(token))

slice_size = len(experimental_data) // 3
early_group = experimental_data[:slice_size]    # {} and () are not needed
mid_group = experimental_data[slice_size:2*slice_size]
late_group = experimental_data[2*slice_size:]

print(f'Number of data in each third: {slice_size}')
print(f'Complete data list: {experimental_data}')
print(f'Early group: {early_group}')
print(f'Mid group: {mid_group}')
print(f'Late group: {late_group}')







# 8.8.1 Iterating through a list using range()
user_values = [3, 6, 7]

for n in range(len(user_values)):
   print(user_values[n])

# output: 3
# 6
# 7
#


user_values = [1, 4, 9]
sum_value = 0

for pos in range(len(user_values)):
  sum_value += user_values[pos]

print(sum_value)

# output: 14
#


user_values = [1, 4, 7]
sum_value = 0

for i in range(len(user_values)):
  sum_value += user_values[i]

print(sum_value)

# output: 12
#


user_values = [-2, 3, 6, -8]

for i in range(len(user_values)):
  if user_values[i] < 0:
    print(user_values[i])

# output: -2
# -8
#


user_values = [-2, 3, -6, 8]

for i in range(len(user_values)):
  if user_values[i] < 0:
    user_values[i] = -1 * user_values[i]
  print(user_values[i])

# output: 2
# 3
# 6
# 8
#


user_values = [-2, 4, -5, 8]

for i in range(len(user_values)):
  if user_values[i] < 0:
    user_values[i] = -1 * user_values[i]
  print(user_values[i])

# output: 2
# 4
# 5
# 8
#


user_values = [1, 6, 7, 4]

max_value = user_values[0]
for i in range(len(user_values)):
  if user_values[i] >= max_value:
    max_value = user_values[i]
    print(max_value)

# output: 1
# 6
# 7
#


user_values = [1, 6, 7, 4]

max_value = user_values[0]
for pos in range(len(user_values)):
  if user_values[pos] >= max_value:
    max_value = user_values[pos]
    print(max_value)

# output: 1
# 6
# 7
#




# 8.7.2
# list countries_list is read from input
countries_list = input().split()

# assign backup_copy with a copy of countries_list using [:]
backup_copy = countries_list[:]

# assign selected_countries with a slice of countries_list that includes the
# elements at the odd indices of countries_list
selected_countries = countries_list[1::2]

countries_list.clear()
print(f'Backup list of countries: {backup_copy}')
print(f'Selected list of countries: {selected_countries}')





# 8.8.2 
# list scores_list contains integers read from input
# each int represents a student's score on a test
# test input: -84 67 56 79

scores_list = []

tokens = input().split()
	# print(tokens)     # prints ['-84', '67', '56', '79']
for token in tokens:
	# print(token)        # prints each element on new line
	scores_list.append(int(token))
	# print(scores_list)  # prints [-84] [-84, 67] [-84, 67, 56] [-84, 67, 56, 79]
  
print('Original scores:', end=' ')
for score in scores_list:
    # print(score)        # prints each element on new line
    print(score, end=' ')
print()                 # prints each element on same line

# write a loop to update all negative elements in scores_list with the negation
# of the element's current value
for i in range(len(scores_list)):
    if scores_list[i] < 0:
        scores_list[i] = -scores_list[i]
        # print(scores_list[i])   # prints 84
    # print(scores_list[i])   # prints 84 67 56 79, each on their own line
# print(scores_list[i])   # prints 79

print('Corrected scores:', end=' ')
for score in scores_list:
    print(score, end=' ')
print()




# list data_samples contains integers read from input
# each int represents a random data sample in an experiment
# test input: 48 80 28 70

data_samples = []

tokens = input().split()
for token in tokens:
    data_samples.append(int(token))
  
print('Original samples:', end=' ')
for samples in data_samples:
    print(samples, end=' ')
print()

# write a loop to remove every element from data_samples that is greater than or 
# equal to 70 and output the removed element, followed by 'dropped'
# iterate over a copy of the list using slice notation (data_samples[start:end])
for sample in data_samples[:]:
    if sample >= 70:
        print(sample, 'dropped')
        data_samples.remove(sample)

print('Filtered samples:', end=' ')
for samples in data_samples:
    print(samples, end=' ')
print()




# list colors_list contains words read from the first line of input
# list favorite_colors contains words read from the second line of input
# test input: 
    # bronze violet tan purple
    # cyan bronze tan

colors_list = input().split()
favorite_colors = input().split()
  
print('Available colors:', end=' ')
for color in colors_list:
    print(color, end=' ')
print()

print('Favorite colors:', end=' ')
for color in favorite_colors:
    print(color, end=' ')
print()

# for each element in colors_list that is not in favorite_colors:
    # output the element, followed by 'not wanted'
    # remove the element from colors_list
for color in colors_list[:]:       # remember to use a copy of a list to iterate safely
    if color not in favorite_colors:
        print(color, 'not wanted')
        colors_list.remove(color)

print('Remaining colors:', end=' ')
for color in colors_list:
    print(color, end=' ')
print()




# 8.9.1
my_list = [-1, 0, 1, 2]
new_list = [ number + 4 for number in my_list ]
print(new_list)
# Output: [3, 4, 5, 6]
#

my_list = [-3, -2, -1, 0, 1, 2, 3]
new_list = [ number for number in my_list if number > 0 ]
print(new_list)
# Output: [1, 2, 3]
#

my_list = [-3, -2, -1, 0, 1, 2, 3]
new_list = [ number + 4 for number in my_list if number <= 2 ]
print(new_list)
# Output: [1, 2, 3, 4, 5, 6]
#

my_list = [-3, -2, -1, 0, 1, 2, 3]
new_list = [ number * 5 for number in my_list if (number < -1) and (number % 2 == 1) ]
print(new_list)
# Output: [-15]
#




# 8.9.2
# list samples_list contains integers read from input
# assign processed_list with a new list where each element is 3x the corresponding
# element in samples_list minus one
# test input: 19 0 5 10

samples_list = []

# Read input
tokens = input().split()
for token in tokens:
    print(token)    # print 19 0 5 10 on individual lines
    samples_list.append(int(token))

processed_list = [3 * token - 1 for token in samples_list]  # expression loopvar iterable

print(f'Original: {samples_list}')
print(f'Processed: {processed_list}')





# list raw_list contains integers read from input
# assign filtered_list with the new list containing all the odd numbers in raw_list,
# in that order
# test input: 23 48 14 13

# Read input
raw_list = [int(x) for x in input().split()]

filtered_list = [x for x in raw_list if (x % 2 == 1)]

print(f'All numbers: {raw_list}')
print(f'Odd numbers: {filtered_list}')





# integer num_rows is read from input representing the numbers of rows in a 
# two-dimensional list
# list raw_list is a two-dimensional list containing the remaining integers from input
# assign computed_list with the new list containing True for each row in raw_list
# that has all non-zero values, and False otherwise
# test input: 
# 3
# 0 28
# 8 3
# 0 0 0

# Read input
num_rows = int(input())
raw_list = []
for i in range(num_rows):
    raw_list.append([int(x) for x in input().split()])

computed_list = [all(row) for row in raw_list]

print(f'All numbers: {raw_list}')
print(f'Row has no zeros: {computed_list}')





# 8.13.2

# create a dictionary named color_dict containing key-value pairs 
# 'R': 255, 'G': 99, and 'B': 71
# read strings new_key and new_value from input
# add new_key and new_value as a new key-value pair to color_dict with 
# new_key as the key and new_value as the value

# test input:
# note
# my favorite color

# expected output:
# R: 255
# G: 99
# B: 71
# note: my favorite color

color_dict = {'R': 255, 'G': 99, 'B': 71}

new_key = input()
new_value = input()

color_dict[new_key] = new_value

print(f'R: {color_dict["R"]}')
print(f'G: {color_dict["G"]}')
print(f'B: {color_dict["B"]}')
print(f'{new_key}: {color_dict[new_key]}')





# read string athlete_name from input
# create a list containing values 55, 100, and 85, in this order
# add a new key-value pair to three_attempts with athlete_name as the key
# and the list as the value

# test input:
# Aya

# Expected output:
# Aya: [55, 100, 85]

three_attempts = {} # creates empty dictionary

athlete_name = input() 

my_list = [55, 100, 85]

# add new key-value pair
three_attempts[athlete_name] = my_list

print(f'{athlete_name}: {three_attempts[athlete_name]}')




# integer num_data is read from input, representing the number of remaining strings
# in the input
# use a for loop to read the remaining strings from input
# each string consists of a key string and a value string, separated by a space
# add each key-value pair into the dictionary favorite_food

# test input:
# 3
# Eli peach
# Tia berry
# Mai oatmeal

# expected output:
# Favorite food:
# {'Eli': 'peach', 'Tia': 'berry', 'Mai': 'oatmeal'}

favorite_food = {}
num_data = int(input())

for food in range(num_data):    # loop through favorite_food num_data times
    input_key = input()
    name, food = input_key.split()
    favorite_food[name] = food

print('Favorite food:')
print(favorite_food)



# read strings from input until 'done' is read. for each string read:
# if the string is a key in dictionary users_record, delete the key from users_record
# otherwise, output the string followed by ' not in dict'

# test input:
# Kai
# Ina
# done

# expected output:
# Kai not in dict
# Updated users record:
# {'Gus': 'gushed@orange.com'}

users_record = {'Ina': 'ina@corn.com', 'Gus': 'gus@orange.com'}

user_input = input()

while user_input != 'done':
    if user_input in users_record:
        del users_record[user_input]
    else:
        print(f'{user_input} not in dict')
    user_input = input()

print('Updated users record:')
print(users_record)




# 8.14.2

# multiple key-value pairs, each representing a room number and name, are read from input
# and added to room_records1
# first, merge room_records2 with room_records1
# then, merge room_records3 with room_records2
# last, clear room_records1

# test input:
# 533 Ada
# 877 Jen
# exit

# expected output:
# Room records 1:
# {}
# Room records 2:
# {'761': 'Del', '380': 'Ani', '533': 'Ada', '877': 'Jen'}
# Room records 3:
# {'875': 'Ava', '761': 'Del', '380': 'Ani', '533': 'Ada', '877': 'Jen'}

room_records1 = {'380': 'Ani'}
room_records2 = {'761': 'Del'}
room_records3 = {'875': 'Ava'}
ref_record1 = room_records1  # For testing purposes, ref_record1 references room_records1
ref_record2 = room_records2  # For testing purposes, ref_record2 references room_records2
ref_record3 = room_records3  # For testing purposes, ref_record3 references room_records3

input_line = input()

while input_line != 'exit':
	room, name = input_line.split()
	room_records1[room] = name
	input_line = input()

# org output:
# Room records 1:
# {'380': 'Ani', '533': 'Ada', '877': 'Jen'}
# Room records 2:
# {'761': 'Del'}
# Room records 3:
# {'875': 'Ava'}

room_records2.update(room_records1) # merge room_records2 with room_records1
room_records3.update(room_records2) # merge room_records3 with room_records2
room_records1.clear() # clear room_records1

print('Room records 1:')
print(room_records1)
print('Room records 2:')
print(room_records2)
print('Room records 3:')
print(str(room_records3))



# dictionary doctors_location contains key-value pairs that represent the room number
# of each doctor
# dictionary patient_directory contains key-value pairs that represent the patient in each
# room
# string doctor_name is read from input

# complete the following tasks:
# 1. assign room_num with the value associated with key doctor_name in doctors_location.
# any string that is not a key in doctors_location has a default value -99
# 2. use pop() to remove room_num from patient_directory and assign patient_name with the
# value returned. any number that is not a key in patient_directory has the default value
# 'nobody'

# test input:
# Kim

# expected output:
# Kim (room 174) is seeing Meg.
# Remaining patients:
# {189: 'Taj', 247: 'Jan', 913: 'Ada'}

# test input:
# Hall

# expected output:
# Hall (room -99) is seeing nobody.
# Remaining patients:
# {174: 'Meg', 189: 'Taj', 247: 'Jan', 913: 'Ada'}

doctors_location = {'Kato': 913, 'Lee': 189, 'Kim': 174, 'Sims': 247}
patient_directory = {174: 'Meg', 189: 'Taj', 247: 'Jan', 913: 'Ada'}

doctor_name = input()

room_num = doctors_location.get(doctor_name, -99) # assign value in dict
patient_name = patient_directory.pop(room_num, 'nobody') # remove value in dict

print(f'{doctor_name} (room {room_num}) is seeing {patient_name}.')
print('Remaining patients:')
print(patient_directory)




# 8.16.1
# multiple key-value pairs, each representing a person's name & email address, are read
# from input and added to contact_dict
# convert contact_dict's items into a list, then sort the list
# assign sorted_items with the sorted list

# test input:
# Mai stork3@lemon.com
# Aya aya8@milk.com
# Ana ana7@cream.com
# done

# expected output:
# [('Ana', 'ana7@cream.com'), ('Aya', 'aya8@milk.com'), ('Mai', 'stork3@lemon.com')]

contact_dict = {}

input_line = input()
while input_line != 'done':
    name, email = input_line.split()
    contact_dict[name] = email
    input_line = input()

items_list = list(contact_dict.items())

sorted_items = sorted(items_list)

print(sorted_items)






# multiple key-value pairs, each representing a hotel room number and the guest's
# name, are read from input and added to room_data
# output each key-value pair in sorted order of the keys, separating each key and value
# by a space on a new line

# test input:
# 303 Bob
# 167 Ani
# quit

# expected output:
# 167 Ani
# 303 Bob

room_data = {}

input_line = input()
while input_line != 'quit':
    room_number, guest = input_line.split()
    room_data[int(room_number)] = guest
    input_line = input()

sorted_list = sorted(room_data) # sort the room_numbers (key)

# print(sorted_list)    # returns [167, 303]

for room_number in sorted_list:
    print(room_number, room_data[room_number])  # print the key, plus access dict values
