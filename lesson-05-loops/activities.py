# 5.1.7
# count ends having the number of negative values in an input list of values (list ends with 0)
# if input is -1 -5 9 3 0, then count should end with 2
count = 0
val = Get next input

while val is not 0
  if __(A)___  # val < 0
     __(B)___  # count = count + 1

  val = Get next input

# if input value is 0, the loop body will NOT execute



# 5.1.9
# max ends having the maximum value in an input list of positive values (list ends with 0)
# if input is 22 5 99 3 0, then max should end as 99
max = -1
val = get next input

while val is not 0
  if __(A)__  # val > max
     __(B)__  # max = val

  val = get next input

# final value of max does NOT depend on the order of inputs

max = -1
val = get next input

while val is not 0
  if val > max
     max = val

  val = get next input

# values 5 10 7 20 8 0
max = -1, 5, 10, 20

# first value is 5 > -1
# second value is 10 > -1
# third value is 7 > 10 --- FALSE
# fourth value is 20 > 10 
# fifth value is 8 > 20 --- FALSE
# sixth value is 0 > 20 --- FALSE



# 5.2.2
x = 3
while x >= 1:
  # Do something
  x = x - 1

# loop will execute 3 times
# 3 >= 1 --- TRUE
# 2 >= 1 --- TRUE
# 1 >= 1 --- TRUE
# 0 >= 1 --- FALSE



# Get character from user here   --- input will be 'n', 'n', 'y'
while user_char != 'n':
  # do something
  # get character from user here

# loop will never execute because the first evaluation is FALSE
# 'n' != 'n' --- FALSE



# get character from user here  --- input will be 'a', 'b', 'n'
while user_char != 'n':
  # do something
  # get character from user here

# loop will execute 2 times
# 'a' != 'n' --- TRUE
# 'b' != 'n' --- TRUE
# 'n' != 'n' --- FALSE



# 5.2.3
# iterate while x is less than 100
while x < 100

# iterate while x is greater than or equal to 0
while x >= 0

# iterate while c equals 'g'
while c == 'g'

# iterate until c equals 'z'
while c != 'z'




# 5.2.5
x = 0
while x > 0:  # x == 0; loop never executes
  print(x, end=' ')
  x = x - 1
print('Bye')
# Output: Bye


x = 5
y = 18
while y >= x:
  print(y, end=' ')
  y = y - x
# Output: 18 13 8 
# Space after each number, including the last number


x = 10
while x != 3:
  print(x, end=' ')
  x = x / 2
# Infinite loops


x = 1
y = 3
z = 5
while (not (y < x < z)):
  # y < x and x < z
  # 3 < 1 and 1 < 5 
  # False and True ---> False
  # not False ---> True, loop executes
  print(x, end=' ')
  x = x + 1
# Output: 1 2 3 
# Space afer each number, including the last number





# 5.3.1
num_a = int(input('Enter first positive integer: '))  # 15
print()

num_b = int(input('Enter second positive integer: '))  # 10
print()

while num_a != num_b:
    if num_a > num_b:
        num_a = num_a - num_b  # num_a = 15 - 10 = 5 ---- (num_a = 5)
    else:
        num_b = num_b - num_a  # num_b = 10 - 5 = 5 ----- (num_b = 5)

print(f'GCD is {num_a}')   # ouput: GCD is 5

# this program will execute two loop iterations given num_a = 15 and num_b = 10





# 5.4.1
'''Program that calculates savings and interest'''

initial_savings = 10000
interest_rate = 0.05

print(f'Initial savings of ${initial_savings}')
print(f'at {interest_rate*100:.0f}% yearly interest.\n')

years = int(input('Enter years: '))
print()

savings = initial_savings
i = 1  # Loop variable
while i <= years:  # Loop condition
    print(f' Savings at beginning of year {i}: ${savings:.2f}')
    savings = savings + (savings*interest_rate)
    i = i + 1  # Increment loop variable

print('\n')

# beginning of year 4: $11576




'''Program that calculates savings and interest'''

initial_savings = 5000
interest_rate = 0.03

print(f'Initial savings of ${initial_savings}')
print(f'at {interest_rate*100:.0f}% yearly interest.\n')

years = int(input('Enter years: '))
print()

savings = initial_savings
i = 1  # Loop variable
while i <= years:  # Loop condition
    print(f' Savings at beginning of year {i}: ${savings:.2f}')
    savings = savings + (savings*interest_rate)
    i = i + 1  # Increment loop variable

print('\n')

# savings will be greater than $7500 after how many iterations? 14




# 5.4.2
# loop iterates 10 times
i = 1
while i <= 10:
  i = i + 1

# loop iterates 99 times
i = 1
while i <= 99:
  i = i + 1

# loop iterates 2 times
i = 1
while i <= 2:
  i = i + 1




# 5.4.3
# loop iterates over odd integers from 1 to 9 (inclusive)
i = 1
while i <= 9:
  i = i + 2

# loop iterates over multiples of 5 from 0 to 1000 (inclusive)
i = 0
while i <= 1000:
  i = i + 5

# loop iterates over odd integers from 211 down to 31 (inclusive)
i = 211
while i >= 31:
  i = i - 2

# loop iterates from -100 to 65
i = -100
while i <= 65:
  i = i + 1
