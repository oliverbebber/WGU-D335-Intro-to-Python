# write a program that takes in a positive integer as input
x = int(input())  

# define reverse_binary, default should be blank/empty
reverse_binary = ""

# algorithm to return 0's and 1's in reverse order:
# as long as x is greater than 0
  # output x modulo 2 (remainder is either 0 or 1)
  # assign x with x divided by 2

while x > 0:  # be sure to use while vs if
    reverse_binary += str(x % 2)  # get remainder and append to string
    x = x // 2  # be sure to use floor division since working with integers

# output a string of 1's and 0's representing the integer in reverse binary
print(reverse_binary)
