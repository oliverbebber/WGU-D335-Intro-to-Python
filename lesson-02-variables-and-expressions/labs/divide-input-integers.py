# write a program that reads integers user_num & div_num as input
user_num = int(input())
div_num = int(input())

# calculate user_num divided by div_num (three times)
div1 = user_num // div_num
div2 = div1 // div_num
div3 = div2 // div_num

# output user_num divided by div_num three times using floor divisions 
# remember, floor division discards fractions
print(f'{div1} {div2} {div3}')
