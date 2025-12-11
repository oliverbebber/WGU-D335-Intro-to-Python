# Given a list of 10 names, complete the program that outputs the name specified by the list index
# entered by the user. Use a try block to output the name and an except block to catch any 
# IndexError exception as a variable. Output "Exception! " followed by the message from the 
# exception variable. Output also the first element in the list if the invalid index is negative or
# the last element if the invalid index is positive.

# Note: Python allows using a negative index to access a list, as long as the magnitude of the 
# index is smaller than the size of the list.

# test input:
# 5

# expected output:
# Name: Jane

# test input:
# 12

# expected output: 
# Exception! list index out of range 
# The closest name is: Johnny

# test input:
# -2

# expected output:
# Name: Tyrese

# test input:
# -15

# expected output:
# Exception! list index out of range
# The closest name is: Ryley
names = ['Ryley', 'Edan', 'Reagan', 'Henry', 'Caius', 'Jane', 'Guto', 'Sonya', 'Tyrese', 'Johnny']
index = int(input())

# 1. use a try block to output the name
# 2. use an except block to catch an IndexError exception as a variable
# 3. output "Exception!" followed by the message from the exception variable
# 4. output the first element in the list if the invalid index is negative or the last
# element if the invalid index is positive

try:
    print(f'Name: {names[index]}')
    
except IndexError as error:
    print(f'Exception! {error}')
    if index < 0:
        print(f'The closest name is: {names[0]}')
    else:
        print(f'The closest name is: {names[-1]}')
