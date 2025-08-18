is_leap_year = False

# read input year from user
input_year = int(input())

# if year is divisible by 100, then check if it is divisible by 400
# divisible by 400 = leap year
if input_year % 400 == 0:
  is_leap_year = True
# not divisible by 400 = not a leap year
elif input_year % 100 == 0:
  is_leap_year = False
# must be divisible by 4 to be a leap year
elif input_year % 4 == 0:
  is_leap_year = True
# otherwise, not leap year
else:
  is_leap_year = False

# print the result in the format "year - leap year" 
if is_leap_year:
  print(f'{input_year} - leap year')
# or "year - not a leap year"
else: 
  print(f'{input_year} - not a leap year')
