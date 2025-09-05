# 8.1.1
user_values = [1, 4, 8]

print(user_values)
# output: [1, 4, 8]
#

user_values = [2, 5, 9]
user_values[0] = user_values[0] + 1  # increments the first element in user_values by 1

print(user_values)
# output: [3, 5, 9]
#

user_values = [3, 5, 8]
user_values[2] = user_values[2] + 1
user_values[1] = user_values[1] + 2

print(user_values)
# output: [3, 7, 9]
# 

user_values = [1, 5, 9]
user_values[1] = user_values[0]

print(user_values)
# output: [1, 1, 9]
# 

user_values = [2, 6, 7]
user_values[0] = user_values[2]
user_values[2] = user_values[1]

print(user_values)
# output: [7, 6, 6]
# 
