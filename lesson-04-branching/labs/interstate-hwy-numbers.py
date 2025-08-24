highway_number = int(input())

# 1. Is it a primary or auxiliary hwy?
# 2. If auxiliary hwy, which primary hwy does it serve?
# 3. Whether the primary hwy, does it run n/s or e/w?

# Primary hwys = 1-99
# Odd numbers = N/S
# Even numbers = E/W
# Auxiliary hwys = 100-999 & service primary hwys (rightmost two digits indicate this)
# 200 is NOT a valid aux hwy

# invalid
if ((highway_number < 1) or (highway_number > 999) or ((highway_number % 100) == 0)):  # highway_number divided by 100 will help get the two right numbers
  print(f'{highway_number} is not a valid interstate highway number.')
else:  # valid
  if(highway_number > 99):  # auxiliary
    print(f'I-{highway_number} is auxiliary', end='')  # keep cursor on the same line for primary_hwy
    # get primary hwy
    primary_hwy = highway_number % 100  # gets rightmost two digits
    print(f', serving I-{primary_hwy}', end='')  # keep cursor on the same line for direction
  else:  # must be 1-99
    primary_hwy = highway_number
    print(f'I-{primary_hwy} is primary', end='')  # keep cursor on the same line for direction
  if ((primary_hwy % 2) == 0):  # even
    print(f', going east/west.')
  else:  # odd
    print(f', going north/south.')
