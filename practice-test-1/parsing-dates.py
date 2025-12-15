# write a program that reads dates from input, one date per line
# each date's format must be in the following format
  # March 1, 2025
# any date not folowing this format is incorrect and should be ignored

# input ends with -1 on a line by itself

# output each correct date as:
# 3/1/2025

# HINT: use string[start:end] to get a substring when parsing the string and extracting the date
# use split() to break the input into tokens

# test input:
# March 1, 1990
# April 2 1995
# 7/15/20
# December 13, 2003
# -1

# expected output:
# 3/1/1990
# 12/13/2003

def get_month_as_int(monthString):

    if monthString == 'January':
        month_int = 1
    elif monthString == 'February':
        month_int = 2
    elif monthString == 'March':
        month_int = 3
    elif monthString == 'April':
        month_int = 4
    elif monthString == 'May':
        month_int = 5
    elif monthString == 'June':
        month_int = 6
    elif monthString == 'July':
        month_int = 7
    elif monthString == 'August':
        month_int = 8
    elif monthString == 'September':
        month_int = 9
    elif monthString == 'October':
        month_int = 10
    elif monthString == 'November':
        month_int = 11
    elif monthString == 'December':
        month_int = 12
    else:
        month_int = 0  # returns 0 if invalid

    return month_int

while True:
    user_string = input()
    if user_string == "-1":
        exit()
        
    tokens = user_string.split()    # list = ['month', 'day_int,', 'year']
    if len(tokens) !=3: # skips over 7/15/20
        continue

# TODO: Read dates from input, parse the dates to find the one
#       in the correct format, and output in m/d/yyyy format
    
    month_int = get_month_as_int(tokens[0])
    
    if month_int == 0:
        continue
    
    # day_str = tokens[1][:-1]  # do not use as this will remove the last int, not just comma
    # if not day_str.isdigit():
        # continue
    
    day_str = tokens[1]
    if not day_str.endswith(','):   # skip over day_str lacking ','
        continue
    day_str = tokens[1][:-1]    # remove ',' from day_str
    if not day_str.isdigit():   # skip over day_str that isn't a digit
        continue
    
    day_int = int(day_str)  # convert str to int
    
    year_str = tokens[2]
    
    if not year_str.isdigit():
        continue
    
    year_int = int(year_str)  # convert str to int
    
    print(f'{month_int}/{day_int}/{year_int}')
