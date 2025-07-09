# 3.2.1
print('Phoenix')
# Output: Phoenix


person = 'Oliver'
print(person)
# Output: Oliver


cat = 'Apollo'
cat = 'Leo'
print(cat)
# Output: Leo


print(len('Shadow'))
# Output: 6


cat = 'Phoenix'
print(cat[0])
# Output: P


cat = 'Apollo'
print(cat[-2])
# Output: l


cat1 = 'Dallas'
cat2 = 'Phoenix'
cat3 = cat1 + cat2
print(cat3)
# Output: DallasPhoenix



# 3.2.2
# Read string my_name from input
my_name = input()
# Input: 
# Oliver
# 12

# Read lemon_count from input, use int() to convert the input to an integer
lemon_count = int(input())

print(my_name, 'makes 5 lemons into lemonade, he now has', lemon_count - 5, 'lemons')
# Output: Oliver makes 5 lemons into lemonade, he now has 7 lemons 


# Read string fav_animal from input
fav_animal = input()
# Read string least_fav_animal from input
least_fav_animal = input()
# Input:
# Cat
# Ant

print('My favorite animal is a', fav_animal, 'and it has', len(fav_animal), 'characters')
# Output: My favorite animal is a cat and it has 3 characters.
print('My least favorite animal is a', least_fav_animal, 'and it has', len(least_fav_animal), 'characters')
# Output: My least favorite animal is a ant and it has 3 characters.


# Read string fav_animal from input
fav_animal = input()
# Input:
# Cheeta

print('The fourth character of', fav_animal, 'is', fav_animal[3])
# Output: The fourth character of Cheeta is e


# Read username from input
user_name = input()
# Read user address from input
user_address = input()

# Assign addresses_str with the concatenation of: user_name, 'lives on', user_address
addresses_str = user_name + ' lives on ' + user_address

print(addresses_str)



# 3.3.2
# Read three integers from input into variables 
datapoint1 = int(input())
datapoint2 = int(input())
datapoint3 = int(input())

# Create list named data_list to hold variables
data_list=[datapoint1, datapoint2, datapoint3]

print(data_list)


# Reads four values from input into names_list
names_list = [input(), input(), input(), input()]

# Print the 2nd element on one line, the 3rd element on another, and the 1st element on the last line, followed by 'is my sibling.'
print(names_list[1], 'is my sibling.')
print(names_list[2], 'is my sibling.')
print(names_list[0], 'is my sibling.')

# Originally tried using one print statement with \n for each new line. 
# print(names_list[1], 'is my sibling.'\n names_list[2], 'is my sibling.'\n names_list[0], 'is my sibling.')

# It's important to remember \n only works within strings and each print statement must be written separately
# or inside a single properly formatted string.

print(
    names_list[1] + ' is my sibling.\n' +
    names_list[2] + ' is my sibling.\n' +
    names_list[0] + ' is my sibling.'
)
# This is an additional way the answer could have been written without rewriting each individual print function.
# However, this option may not follow best practices for readability.


# Reads four values from input into years_list
years_list = [int(input()), int(input()), int(input()), int(input())]

# Remove the second element
years_list.pop(1)

# Read another int from input and append to years_list
years_list.append(int(input()))

print(years_list)


# Reads four values from input into state_codes_list
state_codes_list = [input(), input(), input(), input()]

len_value = len(state_codes_list)
index_value = state_codes_list.index('TX')

print(f'List length: {len_value}')
print(f'TX is found at index {index_value} of {state_codes_list}')



# 3.4.1
from collections import namedtuple

# Named tuple with the fields first name, last name, and birthday
Person = namedtuple('Person', ['first_name', 'last_name', 'birthday'])

# Person object with three strings read from input as attributes
person_data = Person(input(), input(), input())

# Output each field, ending with a newline
print(f'First name: {person_data.first_name}')
print(f'Last name: {person_data.last_name}')
print(f'Birthday: {person_data.birthday}')


# Four values get read from input and stored into variables
color_name = input()
red_channel = int(input())
green_channel = int(input())
blue_channel = int(input())

# Initalize color named tuple to store variables in a specific order
color = (color_name, red_channel, green_channel, blue_channel)

print(f'Color name: {color[0]}, R: {color[1]}, G: {color[2]}, B: {color[3]}')


# Import namedtuple container from collections container
from collections import namedtuple

# Define a named tuple called City with the following fields: name, state, population, in this order
City = namedtuple('City', ['name', 'state', 'population'])

city_name = input()
state_located = input()
population_count = int(input())

city = City(city_name, state_located, population_count)

print(f'City name: {city.name}, State: {city.state}, Population: {city.population}')


from collections import namedtuple

Color = namedtuple('Color', ['name', 'R', 'G', 'B'])

# Read inputs
color_name = input()
red_channel = input()
green_channel = input()
blue_channel = input()

# Create color_data tuple with input values
color_data = Color(color_name, red_channel, green_channel, blue_channel)

print(f'Color name: {color_data.name}, R: {color_data.R}, G: {color_data.G}, B: {color_data.B}')
