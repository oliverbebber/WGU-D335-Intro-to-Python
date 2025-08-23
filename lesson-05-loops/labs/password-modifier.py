# write a program that takes a simple password and makes it strong
# by replacing chars using the following key and appending "!" at 
# the end of the input string

# i becomes 1
# a becomes @
# m becomes M
# B becomes 8
# s becomes $

word = input()
password = ""

# create dict to define modifiers
modifiers = {
  'i': '1',
  'a': '@',
  'm': 'M',
  'B': '8',
  's': '$'
}


# alternatively we could use .replace() instead of creating a dict
# however, this lab is part of the loops lesson and tests knowledge on programming with loops

# password = word.replace('i', '1') \
#               .replace('a', '@') \
#               .replace('m', 'M') \
#               .replace('B', '8') \
#               .replace('s', '$')


# loop through each character & replace if in modification mapping
for char in word:
  if char in modifiers:
    password += modifiers[char]
  else: 
    password += char

# append "!" at the end of the input string
password += '!'

print(password)

