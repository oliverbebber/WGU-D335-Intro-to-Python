# write a program to calculate the total price for car wash services
# a base wash is $10
# a dictionary with each additional service and the corresponding cost
# has been provided
# two additional services can be selected
# a '-' signifies an additional service was not selected
# output all selected services, according to the input order, along with
# the corresponding costs and then the total price for all car wash services
services = { 'Air freshener' : 1 , 'Rain repellent': 2, 'Tire shine' : 2, 'Wax' : 3, 'Vacuum' : 5 }
base_wash = 10
total = 0

service_choice1 = input()
service_choice2 = input()


# output format:
  # ZyCar Wash
  # Base car wash - $10
  # Tire shine - $2
  # Wax - $3
  # -----
  # Total price: $15
