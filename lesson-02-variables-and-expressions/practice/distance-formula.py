import math

# given two points
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

''' distance formula: d = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) '''

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# output the distance between the two points
# round the distance to 2 decimal places

print(round(distance, 2))  

# originally tried print(f'{distance:.2f}')
# this didn't work as it prints 5.00 instead of 5.0
# while this works mathematically, it doesn't match the formatting required by this coding practice 
# it will ALWAYS print two decimal places yet the required format prints as many as needed 
# since we're working with floats in this problem, we would only need x.0
# if we were needing to return 5.05 as the output, then my original format would have been appropriate to use
