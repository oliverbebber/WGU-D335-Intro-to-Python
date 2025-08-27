# read integer from input
num = int(input())

# check if input is out of valid range (11-99)
if num < 11 or num > 99:
  print('Input must be 11-99')
else:
  # loop until both digits are the same
  while True:
    # print the current number in the countdown
    print(num)
    # determine the tens and ones digits
    tens = num // 10  # int division provides the tens place
    ones = num % 10  # modulo gives the ones place
    
    # if both digits are the same, stop the loop
    if tens == ones:
      break
      
    # otherwise, continue conuntdown
    num -= 1
