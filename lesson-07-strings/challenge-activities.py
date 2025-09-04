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
