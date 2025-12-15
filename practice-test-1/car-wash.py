# write a program to calculate the total price for car wash services

# a base wash is $10

# a dictionary with each additional service and the corresponding cost has been provided
# two additional services can be selected
# a '-' signifies an additional service was not selected

# output all selected services, according to the input order, along with
# the corresponding costs and then the total price for all car wash services

# test input:
# Tire shine
# Wax

# expected output:
# ZyCar Wash
# Base car wash - $10
# Tire shine - $2
# Wax - $3
# -----
# Total price: $15

# test input v2:
# Rain repellent
# -

# expected output:
# ZyCar Wash
# Base car wash - $10
# Rain repellent - $2
# -----
# Total price: $12

services = { 'Air freshener' : 1 , 'Rain repellent': 2, 'Tire shine' : 2, 'Wax' : 3, 'Vacuum' : 5 }
base_wash = 10
total = 0

service_choice1 = input()
service_choice2 = input()

# add base_wash to total 
total += base_wash

# print header & base wash price
print('ZyCar Wash')
print(f'Base car wash - ${base_wash}')

if service_choice1 != '-':
    price = services[service_choice1]
    total += price
    print(f'{service_choice1} - ${price}')
    
if service_choice2 != '-':
    price = services[service_choice2]
    total += price
    print(f'{service_choice2} - ${price}')

# print separator & total
print('-----')
print(f'Total price: ${total}')
