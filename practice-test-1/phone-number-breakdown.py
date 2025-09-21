# given an integer representing a 10-digit phone number (1234567890)
phone_number = int(input())

# convert to string, to slice digits easily
phone_str = str(phone_number).strip()  # .strip() before slicing to remove leading whitespace

# output the area code, prefix, and line number
area_code = phone_str[0:3]    # list position (0:2)  - 123
prefix = phone_str[3:6]       # list position (3:5)  - 456
line = phone_str[6:10]        # list position (6:10) - 7890

# use the format: (800) 123-123
print(f'({area_code}) {prefix}-{line}')
