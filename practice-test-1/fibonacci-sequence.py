# the fibonacci sequence begins with 0, then 1 follows
# all subsequent values are the sum of the previous two
# complete the fibonacci() function, which has an index n (starting at 0) as a param
# returns the nth value in the sequence
# any negative index values should return -1
# use a for loop
# Do NOT use recursion

def fibonacci(n):
  if n < 0:
    return -1  # negative index case
  elif n == 0:
    return 0  # base case: fibonacci[0]
  elif n == 1:
    return 1  # base case: fibonacci[1]

  # initialize first 2 fibonacci numbers
  a = 0   # first number: fibonacci(0)
  b = 1   # second number: fibonacci(1)
  
  # loop to compute fibonacci numbers from index 2 up to n
  # range starts at 2 because 0 and 1 are already handled
  # range ends at n + 1 because range(start, stop) excludes the stop value
  for i in range(2, n + 1):
    c = a + b  # next fibonacci number
    a = b      # move previous number forward
    b = c      # update current number
    
    return b  # holds nth number in sequence

if __name__ == '__main__':
  start_num = int(input())
  print(f'fibonacci({start_num}) is {fibonacci(start_num)}')
