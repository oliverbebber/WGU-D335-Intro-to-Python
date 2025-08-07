# 4.2.2
# We set up a feeding station to scan for cats' microchips to see if Phe comes by the porch
# Phoenix's microchip end in 5
# If it's not a match, assign to general review group (10)
# If it's a match, assign to urgent review group (5)

chip_last_digit = int(input())  # Program will be tested with values: 5, 6, 7, 8.

if chip_last_digit != 5:
  group_id = 10  # Not Phoenix, assign to general review group
else:
  group_id = chip_last_digit  # Possibly Phoenix, assign to urgent review group & review logs

print(group_id)



# Phoenix has been missing for 523 days as of 7/29/2025
# I want to build a tool to check if a reported sighting date aligns with the timeframe he has been missing for.

# If someone claims to have seen him more than 523 days ago, the reported sighting should be labled invalid (since that would have been before he escaped)
# If the number of days this person claims to have seen him, the sighting should be labeled valid and worth checking into.
# Write an if-else statement to evaluate a reported number of days since seen.
# If the report is not valid, set lead_status = "invalid"
# Otherwise, set lead_status = "valid"

# Valid range is still 0–523 days.
# Reports older than 400 days may be valid but treated with caution (harder to confirm).

if num_days_ago_seen > 523:
    lead_status = "invalid"
elif num_days_ago_seen > 400:
    lead_status = "caution"
else:
    lead_status = "priority"

print(f"Lead status: {lead_status}")

# I will be expanding upon this in another repo as I want to add input validation on parts of the form I created when I launched the website for findingphe
# Additionally, I want to ensure that the days since I last seen him can be flexible as each day, that number increases.




# 4.4.2
# user_grade is read from user input
user_grade = int(input())

# value of user_grade is between 9 and 12 (both inclusive) then print 'in high school'
if 9 <= user_grade <=12:
  print('in high school')
# otherwise, 'not in high school'
else:
  print('not in high school')




# 4.4.3
input_val = int(input())

# value of input_val is less than 90
if input_val < 90:
  print('Less than 90')
# otherwise, '90 or more'
else:
  print('90 or more')



in_val = int(input())

if in_val <= -21:
  print('-21 or less')
else: 
  print('More than -21')



        
# 4.4.4
number_of_cats = int(input())

if number_of_cats > 17:
  print('Enough cats')




user_val = int(input())
new_val = int(input())

# assign new_val with 1000 if user_val is less than or equal to 1000
if user_val <= 1000:
  new_val = 1000

print(new_val)




num_chairs = int(input())

if num_chairs > 10:
  print('A fine number of chairs')
else:
  print('Not many chairs')




num_tasks = int(input())
accepted_groups = int(input())
remaining_groups = int(input())

if num_tasks <= 23:
  accepted_groups = accepted_groups - 2  # Remember to reassign the variable before performing equation
else:
  remaining_groups = remaining_groups + 1  # Remember to reassign the variable before performing equation

print(accepted_groups)
print(remaining_groups)




# 4.4.5
suitcase_volume = int(input())

# if value of suitcase_volume is less than or equal to 46, output 'Too light'
if suitcase_volume <= 46:
  print('Too light')
# if value of suitcase_volume is between 46 (exclusive) and 124, output 'Checkable'
elif 46 < suitcase_volume <= 124:
  print('Checkable')
# if value of suitcase_volume is greater than 124, output 'Too big'
else:
  print('Too big')





number_of_fish = int(input())


# if value of number_of_fish is greater than 12, output 'Multiple aquariums needed'
if number_of_fish > 12:
  print('Multiple aquariums needed')
# if value of number_of_fish is between 6 (inclusive) and 12 (inclusive), output 'Jumbo aquarium'
elif 6 <= number_of_fish <=12:
  print('Jumbo aquarium')
# if value of number_of_fish is between 0 (exclusive) and 5 (inclusive), output 'Mid-sized aquarium'
elif 0 < number_of_fish <= 5:
  print('Mid-sized aquarium')
# if value of number_of_fish is less than or equal to 0, output 'Invalid input'
else:
  print('Invalid input')





# 4.5.1
user_age = int(input())

# Modify the following line so 'Not currently a teenager' is output if user_age is outside the range 13-19 (inclusive).
if (user_age >= 13) or (user_age <= 19):
    print('Not currently a teenager')
else:
    print('Currently a teenager')

# modified 
if (user_age < 13) or (user_age > 19):
  print('Not currently a teenager')




zip_code = int(input())

# valid zip codes range: 10000 - 99950 (inclusive)
if (zip_code >= 10000) and (zip_code <= 99950):
  print('Valid ZIP code')
else:
  print('Invalid ZIP code')




degree_val = int(input())

if (degree_val <= 232):
  print('New state: solid')
elif (degree_val > 232) and (degree_val < 2500):
  print('New state: liquid')
else:
    print('New state: gas')




salary_num = int(input())

# salary_num is in the inclusive ranges
# range: 0 - 47000
if (salary_num >= 0) and (salary_num <= 47000):
  print('15% income tax bracket')
# range: 47001 - 76000
elif (salary_num >= 47001) and (salary_num <= 76000):
  print('21% income tax bracket')
# range: 76001 - 250000
elif (salary_num >= 76001) and (salary_num <= 250000):
  print('35% income tax bracket')
else:
  print('Invalid input')






# 4.6.1
x = 4

if (x < 8) and (x > 3):
  print('a')
else: 
  print('b')

# Outputs: 
# a
# 

x = 6

if (x > 7) or (x < 4):
  print('a')
else:
  print('b')

# Outputs: 
# b
#

x = 5

if not (x < 6):
  print('a')
if not (x == 3):
  print('b')
print('c')

# Outputs: 
# b
# c
#

x = 5

if (x > 6) and not (x <= 6):
  print('a')
if (x < 7) and not (x >= 1):
  print('b')
print('c')

# Outputs:
# c
# 

x = 7

if not((x > 6) or (x < 2)):
  print('a')
if (x > 2) and (x < 9):
  print('b')
print('c')

# Outputs:
# b
# c
#
