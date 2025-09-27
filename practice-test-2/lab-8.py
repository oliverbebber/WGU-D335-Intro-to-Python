# given a string representing a 10-digit phone number
# output the area code, prefix, and line number
# following the format (800) 555-1212
phone_number = str(input())

phone_str = str(phone_number).strip()

area_code = phone_str[0:3]
prefix = phone_str[3:6]
suffix = phone_str[6:]

print(f'({area_code}) {prefix}-{suffix}')
