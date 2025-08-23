# ex: 
# 8x + 7y = 38
# and
# 3x - 5y = -1
# both have a solution x = 3, y = 2

# given integer coefficients (a, b, c, d, e, and f) of two linear equations
# with variables x and y listed below use brute force to find an integer solution 
# for x and y in the range -10 to 10

# ax + by = c 
# dx + ey = f

''' Read in first equation, ax + by = c '''
a = int(input())
b = int(input())
c = int(input())

''' Read in second equation, dx + ey = f '''
d = int(input())
e = int(input())
f = int(input())

# define range for x and y
r = range(-10, 11)

# flag to determine if solution is found
solution_found = False

# brute force approach:
# for every value of x from -10 to 10
#  for every value of y from -10 to 10
#    check if the current x and y satisfy both equations. if so, output the solution and finish

# loop through all possible x values in the range
for x in r:
  # loop through all possible y values in the range
  for y in r:
    # check if the current x and y satisfy both equations
    if a*x + b*y == c and d*x + e*y == f:
      # print the solution
      print(f'x = {x} , y = {y}')
      # change flag to indicate a solution has been found
      solution_found = True
      # exit inner loop after finding solution
      break
  # exit outer loop if solution has been found
  if solution_found:
    break

# otherwise, if no solution is found
if not solution_found:
  # output "There is no solution"
  print('There is no solution')
