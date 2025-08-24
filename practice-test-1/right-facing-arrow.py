# given input characters for an arrowhead and arrowbody
base_char = input()
head_char = input()

row1 = '      ' + head_char
row2 = base_char + base_char + base_char + base_char + base_char + base_char + head_char + head_char
row3 = base_char + base_char + base_char + base_char + base_char + base_char + head_char + head_char + head_char

# output a right-facing arrow
print(row1)
print(row2)
print(row3)
print(row2)
print(row1)


# this program could also be written in a cleaner manner as follows
# given input characters for an arrowhead and arrowbody
base_char = input()
head_char = input()

row1 = '      ' + head_char
row2 = (base_char * 6) + (head_char * 2)
row3 = (base_char * 6) + (head_char * 3)

# output a right-facing arrow
print(row1)
print(row2)
print(row3)
print(row2)
print(row1)
