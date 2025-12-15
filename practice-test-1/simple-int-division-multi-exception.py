
# write a program that reads integers user_num and div_num as input
# output the integer quotient (user_num divided by div_num)
# use a try block to perform all the statements
# use an except block to catch any ZeroDivisionError as a variable & output 
# "Zero Division Exception: " followed by the exception message from the variable
# use another except block to catch any ValueError caused by invalid input as a variable
# and output "Input Exception: " followed by the exception message from the variable

# note: ZeroDivisionError is raised when a division by zero occurs
# ValueError is raised when a user enters a value of different data type than what is 
# defined in the program
# do not include code to raise any exception in the program

# test input:
# 15
# 3

# expected output:
# 15

# test input v2:
# 10
# 0

# expected output: 
# Zero Division Exception: integer division or modulo by zero

# test input v3:
# 15.5
# 5

# expected output:
# Input Exception: invalid literal for int() with base 10: '15.5'

try:  # placing the input statements in the try block ensures the errors will be caught
    user_num = int(input())
    div_num = int(input())

    print(user_num // div_num)
    
except ZeroDivisionError as err1:
    print(f'Zero Division Exception: {err1}')
    
except ValueError as err2:
    print(f'Input Exception: {err2}')
