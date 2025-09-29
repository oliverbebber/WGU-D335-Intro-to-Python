# write a program whose input is a phrase
# output is an acronym of the input
# append a period (.) after each letter in the acronym
# if a word begins with a lowercase letter, do NOT include that letter in the acronym
# assume the input has at least one uppercase letter
phrase = input()            # Institute of Electrical and Electronics Engineers

words = phrase.split()      # ['Institute', 'of', 'Electrical', 'and', 'Electronics', 'Engineers']

acronym = ''                # create empty string to hold acronym

for word in words:
  if word[0].isupper():    # if first letter of each word is uppercase
    acronym += word[0] + '.'  # add 1st letter with a period following to build the acronym
        
print(acronym)
