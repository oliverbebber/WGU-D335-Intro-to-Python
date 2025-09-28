# write a program that removes all non-alpha chars from input
a = input()             # input: -Hello, 1 world$!

b = a.replace('-', '')  # removes - from original string
print(b)                # Hello, 1 world$!
c = b.replace(',', '')
print(c)                # Hello 1 world$!
d = c.replace('1 ', '')
print(d)                # Hello world$!
e = d.replace('$', '')
print(e)                # Hello world!
f = e.replace('!', '')
print(f)

# program can be simplified / less redundant by using the following:
phrase = input()

result = ''.join([char for char in phrase if char.isalpha()])
# for char in phrase looks at each character one by one
# if char.isalpha() will keep *only* alpha chars
# char for char in phrase with the if statement makes a new list with only letters
# finally, all characters are joined together to make one string
print(result)
