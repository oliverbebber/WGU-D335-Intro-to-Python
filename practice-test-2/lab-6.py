# solution accepts a 9-digit int representing an unformatted student ID number (e.g.,"5417543010")
# solution outputs formatted student ID number as a string (e.g.,"541-75-3010")
# accept integer input
print("Enter Student Identification Number:")
identification_number = int(input())

id_str = str(identification_number).strip()

first = id_str[0:3]
second = id_str[3:5]
third = id_str[5:9]

print(f'{first}-{second}-{third}')
