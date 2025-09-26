# write a program that reads a positive int from input and outputs a string of 1's & 0's
# representing the int in binary
# for an int x, use the following algorithm:
# as long as x is greater than 0
  # output x % 2 (remainder is either 0 or 1)
  # x = x // 2
# this algorithm outputs the 0's and 1's in reverse order
# write a helper function to reverse the string

# define two functions: 
# int_to_reverse_binary() that takes an int as a param
def int_to_reverse_binary(integer_value):
  input_string = ""
  while integer_value > 0:
    remainder = integer_value % 2
    input_string += str(remainder)    # append remainder as a string
    integer_value = integer_value // 2
  return input_string                # returns a string of 1's & 0's (in reverse)

# string_reverse() that takes an input string as a param 
def string_reverse(input_string):          # helper function to reverse binary string
  return input_string[::-1]          # returns a string representing the input string in reverse

if __name__ == '__main__':
  integer_value = int(input())    # 6
  reverse_binary = int_to_reverse_binary(integer_value)
  # print(reverse_binary)   
  # testing program:           returns 011 --> needs to be reversed w/helper function
  binary = string_reverse(reverse_binary)
  print(binary)                # returns 110
