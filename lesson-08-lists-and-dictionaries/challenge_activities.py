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



# SOLVE LATER
m = int(input())
customer_line = input().split()

# write multi-branch if-else statements
# if m == 1
    # assign suffix with 'st'

# if m == 2
    # assign suffix with 'nd'
    
# if m == 3
    # assign suffix with 'rd'
    
# otherwise
    # assign suffix with 'th'
    
# output the mth element of customer_line
# output 'is the '
# m and suffix
# ' customer in line.'



# 8.2.1
# int num_students is read from input
num_students = int(input())

students_list = []

# read the remaining strings from input and insert each string at the front of students_list at position 0
for i in range(num_students):
  student = input()
  students_list.insert(0, student)

print(students_list)





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
