# write a program that accepts 3 integers 
value_1 = int(input())
value_2 = int(input())
value_3 = int(input())

# determine largest value
if value_1 >= value_2 and value_1 >= value_3:
    max_val = value_1
elif value_2 >= value_1 and value_2 >= value_3:
    max_val = value_2
else:
    max_val = value_3

# output the largest value
print(f'Max of [{value_1}, {value_2}, {value_3}] is {max_val}')
