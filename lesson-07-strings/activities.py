# 7.1.2
my_str = 'The cat in the hat'
print(my_str[0:3])
# output: The 
# no space before or after 'The'


my_str = 'The cat in the hat'
print(my_str[3:7])
# output: cat
# space before ' cat'



# 7.1.4
my_str = 'http://reddit.com/r/python'
print(my_str[17:])  # output: /r/python

my_str = 'http://reddit.com/r/python'
protocol = 'http://'
print(my_str[len(protocol):])  # len(protocol) = 7    my_str[7:]

# output: reddit.com/r/python



# 7.1.5
my_str = 'Agt2t3afc2kjMhagrds!'
print(my_str[0:5:1])  

# output: Agt2t 
# reads the first FIVE characters, adding a stride of 1 to the index to find each new element to read

my_str = 'Agt2t3afc2kjMhagrds!'
print(my_str[::2])

# output: AttackMars


# 7.2.2
# complete the format specification to assign a field width of 10 chars
{name:10}

# write a complete replacement field that assigns a field with named value "count" and a field width of 5
{count:5}
