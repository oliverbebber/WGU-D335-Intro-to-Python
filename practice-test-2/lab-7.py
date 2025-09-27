# write a program that creates a login name for a user
# given the user's first name, last name, and 4 digit int as input
line = input()          # accept input on ONE line

parts = line.split()

first_name = parts[0]
last_name = parts[1]
four_digit = int(parts[2])

# first_name = input()      --> would have worked had the input been 3 lines 
# last_name = input()       --> would have worked had the input been 3 lines 
# four_digit = int(input()) --> would have worked had the input been 3 lines 

# output login name which is made up of the first 6 letters of the first name
# followed by the first letter of the last name, an underscore, and
# the last digit of the number (use the % operator)
last_digit = four_digit % 10
first_six = first_name[0:6]

# if the first name has less than 6 letters, use all letters of first name
if len(first_name) < 6:
    print(f'Your login name: {first_name}{last_name[0]}_{last_digit}')
else:
    print(f'Your login name: {first_six}{last_name[0]}_{last_digit}')
