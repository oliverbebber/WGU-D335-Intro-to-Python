# write a program that reads a person's name in the following format:
# firstName middleName lastName (on one line)
user_name = input()

token = user_name.split()   # stores name as a list

# test printing first, middle, and last name
# print(token)
# print(token[0])             # prints first name
# print(token[1])             # prints middle name
# print(token[2])             # prints last name; OR token[-1] - doesn't work when len(token) == 2

# test printing firstInitial & middleInitial
# print(token[0][0])
# print(token[1][0])

# output the person's name in the following format:
# lastName, firstInitial.middleInitial.
if len(token) == 2:
    print(f'{token[-1]}, {token[0][0]}.')
elif len(token) == 3:
    print(f'{token[-1]}, {token[0][0]}.{token[1][0]}.')
