# write a program that takes a string and int as input
# outputs a sentence using the input values as shown in the following example
    # Eating {num} {word} a day keeps you happy and healthy.
# the program repeats until the input string is quit and disregards the int input after

while True:
  user_input = input().strip()        # format of user_input: apples 5

  # split into word and number
  word, num = user_input.split()  
  # print(word, num)                  # returns apples 5
  
  # check for quit condition
  if word == 'quit':
    exit()
  
  print(f'Eating {num} {word} a day keeps you happy and healthy.')
