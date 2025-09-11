# accept two strings from  user input
str1 = input()
str2 = input()

# output the two strings followed by "are the same length" if they are the same length
if len(str1) == len(str2):
  print(f'{str1} and {str2} are the same length')
# output string is longer than the shorter string
elif len(str1) > len(str2):
  print(f'{str1} is longer than {str2}')
else:
  print(f'{str2} is longer than {str1}')



# could also be written differently
str1 = input()
str2 = input()

if len(str1) > len(str2):
  print(f'{str1} is longer than {str2}')
elif len(str1) < len(str2):
  print(f'{str2} is longer than {str1}')
  # otherwise, output str1 and str2 are the same length
else:
  print(f'{str1} and {str2} are the same length')  
