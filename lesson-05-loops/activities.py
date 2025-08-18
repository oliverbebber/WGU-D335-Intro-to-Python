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
