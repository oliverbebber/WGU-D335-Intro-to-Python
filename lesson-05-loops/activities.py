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
