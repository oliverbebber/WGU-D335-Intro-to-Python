int1 = int(input())
int2 = int(input())

# determine max value
max_val = max(int1, int2)

# if int1 is greater than int2
if int1 > int2:
  # output max_val
  print(f'Max of {int1} and {int2} is {max_val}')
# elif int2 > int1:
#  print(f'Max of {int2} and {int1} is {max_val}')
else:  # int1 == int2
  print(f'Max of {int1} and {int2} is {max_val}')

# unsure if an elif statement is needed as the lab was passed with AND without it
