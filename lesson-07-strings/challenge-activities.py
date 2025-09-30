# 7.1.1
city = 'Khartoum'
city_slice = city[0:3]
print(city_slice)
# output: Kha
#

color = 'verdant'
color_slice = color[:4]
print(color_slice)
# output: verd
#

city = 'Beirut'
city_slice = city[:2]
print(city_slice)
# output: Be
#

state = 'Wyoming'
my_slice = state[4:6]
print(my_slice)
# output: in
# 

color = 'violet'
my_slice = color[4:6]
print(my_slice)
# output: et
# 

city = 'Quito'
my_slice = city[0:4:2] # yields every second element of state from indices 0 to 4
print(my_slice)
# output: Qi
# 

state = 'Vermont'
my_slice = state[0:4:3]  # yields every third element of state from indices 0 to 3
print(my_slice)
# output: Ver
# 

color = 'silver'
my_slice = color[0:4:3]  # yields every third element of state from indices 0 to 3
print(my_slice)
# output: sv
# 

city = 'Algiers'
my_slice = city[0:5:2]  # yields every second element of city from indices 0 to 4
print(my_slice)
# output: Age
#

state = 'Idaho'
my_slice = state[0:-2]  # yields the chars from indices 0 to -2; -2 refers to the second-from-last char 'h' at index 3
print(my_slice)
# output: Ida
#

city = 'Cairo'
my_slice = city[0:-2]  # yields the chars from indices 0 to -2; -2 refers to the second-from-last char 'r' at index 3
print(my_slice)
# output: Cai
# 




# 7.2.1
name = 'Sadio'
print(f'{name:8}')  # total characters, including white space is 8

# output: Sadio   
# 

name = 'Jack'
points = 11
print(f'{name:6}{points:5}')  # points:5 will include white space = 3 then the remaining 2 would be 11

# output: Jack     11
#

name = 'Jane'
matches = 21
points = 8
print(f'{name:6}{points:3}{matches:5}')  # matches:5 will be similar to points:5 - white space = 3 then the remaining 2 will be 21

# output: Jane    8   21
# 





# 7.2.2
# string food_name & int food_quantity are read from user input
food_name = input()
food_quantity = int(input())

# use one print(f'') statement to output the following on one line:
# food_name with a width of 13 chars, left-aligned, and with the fill char '+'
# the pound sign '#'
# food_quantity with a width of 13 chars, right-aligned, and with the fill char '+'
print(f'{food_name:+<13}#{food_quantity:+>13}')  # be sure to put the plus signs before the alignment and no space between #





# floating-point num location_size is accepted from user input
location_size = float(input())

# use one print(f'') statement to output 'Square Feet: ', followed by location_size to decimal places
print(f'Square Feet: {location_size:.2f}')




# three strings are read from user input & stored into list plants
plants = input().split()
# three more strings are read from user input & stored into list colors
colors = input().split()
# string separator_char is read from user input
separator_char = input()

# use five print(f'') statements to output the following 5 lines:
# "Plants", with a field width of 21, centered. Then "Colors", with a field width of 21, centered.
print(f'{"Plants":^21}{"Colors":^21}')    # do NOT put a space between the two curly braces
# 42 instances of separator_char
print(f'{separator_char*42}')
# plants[0], with a field width of 21, left-aligned.
print(f'{plants[0]:<21}{colors[0]:>21}')
# plants[1], with a field width of 21, left-aligned. Then colors[1] with a field width of 21, right-aligned
print(f'{plants[1]:<21}{colors[1]:>21}')
# plants[2], with a field width of 21, left-aligned. Then colors[2] with a field width of 21, right-aligned
print(f'{plants[2]:<21}{colors[2]:>21}')






# 7.3.1
vowel_letters = input()

if 'i' in vowel_letters:
    index = vowel_letters.rfind('i')    # find last occurence of i
    print(f'Found at index: {index}')
    new_string = vowel_letters.replace('i', '+')    # replace all 'i' with '+'
    print(new_string)
else:
    print('No results')



my_name = input()
your_name = input()

# write an if-else statement that compares the strings:
# if my_name and your_name have exactly the same chars
if my_name == your_name:
    # output "Same inputs"
    print('Same inputs')
# otherwise
else: 
    # output the string with the smaller ASCII value
    if my_name < your_name:
        print(my_name)
    else:
        print(your_name)




string_data = input()

# if all chars in my_string are numbers, output "All numbers"
# otherwise, if all chars in my_string are uppercase, output "All uppercase"
# if none of the above are true, output "No condition fits"
#while True:
if string_data.islower():
    print('All lowercase')
elif string_data.isnumeric():
    print('All numbers')
else:
    print('No condition fits')



# 7.5.2
key_value = input()

key_value_tokens = key_value.split(' => ')

print(key_value_tokens)
