# write a program that accepts a string representing an integer as input
user_string = input()

# outputs "Yes" if the char is a digit 0-9
if user_string.isdigit():  # .isdigit() returns Trye if all chars are numbers 0-9
    print('Yes')
# otherwise
else:
# outputs "No"
    print('No')
