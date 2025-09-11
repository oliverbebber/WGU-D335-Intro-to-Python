# accept integer from user input
num = int(input())

# initiate empty list to store num if greater than 0
my_list = []

# loop while num is greater than 0
while num > 0:
    # only store num in my_list if greater than 0
    my_list.append(num)
    # accept next number from input
    num = int(input())

# output smallest and largest number in list
print(f'{min(my_list)} and {max(my_list)}')  

# reminder: min and max are function*
# syntax is minx() and max()
