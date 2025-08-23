# write a program that takes 3 integers
a = int(input())  # 7
b = int(input())  # 1
c = int(input())  # 4

# a is greatern than or equal to b and a is less than or equal to c, OR a is less than or equal to b and a is greater than or equal to c
if (a >= b and a <= c) or (a <= b and a >= c):
  median = a
# b is greatern than or equal to a and b is less than or equal to c, OR b is less than or equal to a and b is greater than or equal to c
elif (b >= a and b <= c) or (b <= a and b >= c):
  median = b
else:
  median = c

# output the median value
print(median)


# eval inputs
# (7 >= 1 and 7 <= 4) or (7 <= 1 and 7 >= 4)
# (TRUE and FALSE) or (FALSE and TRUE)
# FALSE or FALSE -> FALSE

# (1 >= 7 and 1 <= 4) or (1 <= 7 and 1 >= 4)
# (FALSE and TRUE) or (TRUE and FALSE)
# FALSE or FALSE -> FALSE

# median = 4
