a = int(input())
b = int(input())

# output the first int and subsequent increments of 5 
# if value is less than or equal to the second integer
if a <= b:
  for i in range(a, b + 1, 5):
    print(i, end=' ')     # end=' ' prints output with space in between each i
    print()   # end output with a new line
else:
  # output "Second integer can't be less than the first."
  print('Second integer can\'t be less than the first.')
