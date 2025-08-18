# 5.2.1
g = 0

while g <= 2:
  print(g)
  g += 1

# output: 
# 0
# 1
# 2
#

g = 0

while g <=5:
  print(g)
  g += 2

# output:
# 0
# 2
# 4
#

g = 0

while g >= -3:
  print(g)
  g -= 1

# output:
# 0
# -1
# -2
# -3
#

g = 0

while g >= -4:
  print(g)
  g -= 2

# output
# 0
# -2
# -4
#

g = 4

while g <= 7:
  print(g)
  g += 1

# output:
# 4
# 5
# 6
# 7
# 





# 5.2.2
input_val = float(input())
while input_val < 1.0:  # executes while loop when input_val is less than -1.0
    print(f'User entered {input_val}')
    input_val = float(input())

print('Loop terminated')




sum_chars = 0
char_input = input()

while char_input != 's':  # executes while loop without reading 's'
  sum_chars += 1  # updates sum_chars with the sum of sum_chars +1
  char_input = input()  # read next character from input into char_input
  
print(sum_chars)




result = 0
user_num = int(input())

while user_num >= 0:  # while user_num is non-negative
  if user_num % 4 != 0:  # if user_num is not divisible by 4
    result += user_num # add user_num to result
  else:  # otherwise
    result -= user_num  # subtract user_num from result
    
  user_num = int(input())  # read next int from input
    
print(f'Result is {result}')

