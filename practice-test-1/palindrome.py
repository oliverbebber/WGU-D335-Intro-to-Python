# a palindrome is a word or phrase that is the same read forward and backward
# ex: "bob", "sees", "never odd or even" (ignores spaces)

# write a program whose input is a word or phrase
# outputs whether the input is a palindrome
# start by removing spaces
# then check if the string equals itself in reverse
word = input()

# remove spaces
remove_spaces = word.replace(' ', '')

if remove_spaces == remove_spaces[::-1]:  # [::-1] reverses the entire string; [:-1] slices the last char
    print(f'palindrome: {word}')
else:
    print(f'not a palindrome: {word}')
