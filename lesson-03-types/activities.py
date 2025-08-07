# 3.9.1
num_items = 5
item_weight = 0.5

num_items + num_items   # 10

item_weight * num_items  # 2.5

(num_items + num_items) * item_weight  # 5.0



# 3.9.2
int(1.55)
# truncates to 1

float("7.99")
# converts directly to the floating point 7.99

str(99)
# converts 99 to a string


# 3.11.4
num = 31
# value of num decimal base 10 int (31)
print(f'{num:d}')

num = 31
# value of num as a hexadecimal base 16 int (1f)
print(f'{num:x}')

num = 31
# value of num as a binary base 2 int (11111)
print(f'{num:b}')
