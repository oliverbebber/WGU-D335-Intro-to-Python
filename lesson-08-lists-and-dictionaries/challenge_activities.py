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
