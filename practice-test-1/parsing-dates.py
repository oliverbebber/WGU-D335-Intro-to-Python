# write a program that reads dates from input, one date per line
# each date's format must be in the following format
  # March 1, 2025
# any date not folowing this format is incorrect and should be ignored
# input ends with -1 on a line by itself
# output each correct date as:
# 3/1/2025
# HINT: use string[start:end] to get a substring when parsing the string and extracting the date
# use split() to break the input into tokens
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
        month_int = 0

    return month_int

user_string = input()

# TODO: Read dates from input, parse the dates to find the one
#       in the correct format, and output in m/d/yyyy format
