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






# 5.3.1
curr_value = int(input())  # input: 6 7 4 9 2 0

max_value = curr_value

while curr_value > 0:
    if curr_value > max_value:
        max_value = curr_value
    curr_value = int(input())

print(f'Max value: {max_value}')
# output: Max value: 9
#


total_sum = 0

entered_value = int(input())  # input: 2 4 3 -1

while entered_value > 0:
    total_sum = total_sum + entered_value
    entered_value = int(input())

print(f'Sum: {total_sum}')
# output: Sum: 9
#


entered_age = int(input())  # input: 55 22

while (entered_age < 18 or entered_age > 60):
    if entered_age < 18:
        print('5% discount')
    else:
         print('15% discount')
    entered_age = int(input())

print('No discount')
# output: No discount
#


user_age = int(input())  # input: 65 35 22

while (user_age < 16 or user_age > 60):
    if user_age < 16:
        print('5% discount')
    else:
         print('15% discount')
    user_age = int(input())

print('No discount')
# output: 15% discount
# No discount
#

entered_age = int(input())  # input: 8 42 19

while (entered_age < 16 or entered_age > 65):
    if entered_age < 16:
        print('5% discount')
    else:
         print('10% discount')
    entered_age = int(input())

print('Regular ticket price')
# output: 5% discount
# Regular ticket price
#





# 5.3.2
# keep_bidding is initially assigned 'y'
# within the loop, keep_bidding is updated with the user's next input value
# complete the while loop's expression to terminate the loop is 'n' is entered
import random
random.seed(5)

keep_bidding = 'y'
next_bid = 0

while keep_bidding != 'n':  # remember, while loops are great to use until a specific condition is met
   next_bid = next_bid + random.randint(1, 10)
   print(f'I\'ll bid ${next_bid}!')
   print('Continue bidding? (y/n)', end=' ')
   keep_bidding = input()




# 5.3.3
# positive int num_insects is read from user input
num_insects = int(input())

# write a while loop that in each iteration first prints and then doubles num_insects
# the loop executes while values are less than or equal to 100
# output each number on a new line
while num_insects <= 100: 
  print(num_insects)
  num_insects = num_insects * 2




# 5.3.4 
# strings word_to_find and input_word are read from input
word_to_find = input()
input_word = input()

# int expected_count is initialized with 1
expected_count = 1

# write a loop that iterates while input_word is not equal to 'Completed'
while input_word != 'Completed':
  # each iteration increments expected_count if input_word is equal to word_to_find
  if input_word == word_to_find:  # don't get tricked nesting a while loop; use if statement instead to avoid an infinite loop
    expected_count += 1
  # reads string input_word from input
  input_word = input()

print(f'{word_to_find} occurs {expected_count} time(s).')




# string input_key is read from input
input_key = input()

# write a loop that iterates while_input is not equal to "Over"
while input_key != "Over":
  # each iteration reads int food_number from input
  food_number = int(input())
  # if food_number is less than 45
  if food_number < 45:
    # output the value of input_key followed by ': reorder soon' on one line
    print(f'{input_key}: reorder soon')
    # read str input_key from input
input_key = input()




# the first and second int in input are read as variables previous_val and current_val
previous_val = int(input())
current_val = int(input())
print(f'Sequence starts at {previous_val}.')

# write a loop that iterates while current_val is 10 + previous_val
while current_val == 10 + previous_val:
  # each iteration outputs current_val followed by 'is 10 plus previous_val, amd '. Sequence is increasing arithmetically.' on one line
  print(f'{current_val} is 10 plus {previous_val}. Sequence is increasing arithmetically.')
  # assign previous_val with current_val
  previous_val = current_val
  # read the next int from input and assign current_val with the int read
  current_val = int(input())





# 5.4.1 
n = 1
while n <= 3:
  print(n)
  n = n + 1

# output: 1
# 2
# 3
# 

n = 6
while n >= 0:
  print(n)
  n = n - 1

# output: 6
# 5
# 4
# 3
# 2
# 1
# 0
#

target = int(input())  # 6
n = int(input())       # 4
while n <= target:
  print(n * 2)
  n += 1

# output: 8
# 10
# 12
# 

target = int(input())  # 10
n = int(input())       # 6
while n <= target:
  print(n * 2)
  n += 1

# output: 12
# 14
# 16
# 18
# 20
# 

target = int(input())  # 12
n = int(input())       # 1
step = 4
while n <= target:
    print(n * 2)
    n += step

# output: 2
# 10
# 18
# 

target = int(input())  # 4
n = int(input())       # 6
step = 2
while n > target:
    print(n * 2)
    n -= step

# output: 12
# 





# 5.4.2
# integer num_threshold is read from input
num_threshold = int(input())

# integer i is initialized with 6
i = 6

# complete the while loop to perform the following tasks at each iteration
# until i is greater than num_threshold:
#   increment i
#   if i is divisible by 3, output value of i

while i <= num_threshold:
  i += 1
  if i % 3 == 0:
    print(i)



# integer input_num is read from input
input_num = int(input())

# initialize k with 25
k = 25

# write a while loop to perform the following tasks at each iteration until k is less than input_num
#  decrement k
#  if k is divisible by 2, then output the value of k
while k > input_num:
  k -= 1
  if k % 2 == 0:
    print(k)





# 5.5.1
colors = ['cyan', 'blue', 'grey']
for color in colors:
    print(color)

# output: cyan
# blue
# grey
# 

word = 'Memory'
for char in word:
    print(char, end=',')
print()

# output: M,e,m,o,r,y,
#


weights = [1, 3, 7, 6]
result = 0
for weight in weights:
    result += weight
print(result)

# output: 17
#


colors = ['red', 'tan', 'grey', 'gold']
for color in reversed(colors):
    print(color)

# output: gold
# grey
# tan
# red
#


cities = {
    'Montreal': 958,
    'Rome': 550,
    'Austin': 3435,
    'Toronto': 5259,
}

best = ''
distance = 0
for city in cities:
    if cities[city] > distance:
        best = city
        distance = cities[city]
print(best, distance)

# output: Toronto 5259


