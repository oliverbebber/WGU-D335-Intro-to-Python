# 7.1.4
my_str = 'http://reddit.com/r/python'
print(my_str[17:])  # output: /r/python

my_str = 'http://reddit.com/r/python'
protocol = 'http://'
print(my_str[len(protocol):])  # len(protocol) = 7    my_str[7:]

# output: reddit.com/r/python
