# write a program whose input is a string containing a character and phrase
user_input = input()

char = user_input[0]     
# print(user_input[0:2])        # user_input[0:2] = n
phrase = user_input[2:]         # slice char off the string

# output indicates the number of times the character appears in the phrase
# print(phrase.count(char))       # returns the number of times char is found in phrase 

# output should include the input character and the use of the plural form, n's, if 
# the number of times the chars appears is not exactly 1
if phrase.count(char) == 1:
    print(f'{phrase.count(char)} {char}')
else:
    print(f'{phrase.count(char)} {char}\'s')
