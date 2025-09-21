# write a program to take line of text as input
while True:
  text = input()
  if text in ('Done', 'done', 'd'):   # stop condition
    break
    print(text[::-1])  # output the text in reverse



# the solution could also be the following
text = input()
while text not in ('Done', 'done', 'd'):  # stop condition
  print(text[::-1])  # output the text in reverse
  text = input()
