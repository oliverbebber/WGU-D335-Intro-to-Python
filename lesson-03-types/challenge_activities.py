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



# 3.5.1
# Create an empty set
unique_cats = set()

# Read 3 strings from user input
cat1 = input()
cat2 = input()
cat3 = input()

# Add inputs to the set & handle duplicates automatically
unique_cats.add(cat1)
unique_cats.add(cat2)
unique_cats.add(cat3)

# Print the set contents as a sorted list
print(sorted(unique_cats))



# Create empty set to store cat names
cats = set()

# Accept 3 cat names from user input
cat1 = input()
cat2 = input()
cat3 = input()

# Add each cat name to the set
cats.add(cat1)
cats.add(cat2)
cats.add(cat3)

# Get the number of unique cats in the set
num_cats = len(cats)

# Clear the set
cats.clear()

# Print the total number of unique cats
print(f'Number of values picked: {num_cats}')

# Print contents of the set (now empty)
print(sorted(cats))



# Create sets
cats_set1 = {'Phoenix'}
cats_set2 = set()

# Read two colors from user input & add to set2
cats_set2.add(input())
cats_set2.add(input())

# Read next string from input and remove the string from cats_set1
remove_cat = (input)
cats_set1.remove(remove_cat)

# Read the next string from input and add the string to cats_set1
add_cat = input()
cats_set1.add(add_cat)

# Output the sets (sort for readability)
print(f'cats_set1: {sorted(cats_set1)}')
print(f'cats_set2: {sorted(cats_set2)}')




# Set my favorites to contain cat, opossum, shark
my_favorites = {'cat', 'opossum', 'shark'}

# Set Adam, Robert, and Haylee's favorites to contain one string from user input
adams_favorites = {input()}
roberts_favorites = {input()}
haylees_favorites = {input()}

# Assign likeable animals with the union of Adam, Robert, Haylee, and my favorites
likeable_animals = my_favorites.union(adams_favorites, roberts_favorites, haylees_favorites)

print(f'My favorite animals: {sorted(my_favorites)}')
print(f"Adam's favorite animals: {sorted(adams_favorites)}") 
print(f"Robert's favorite animals: {sorted(roberts_favorites)}") 
print(f"Haylee's favorite animals: {sorted(haylees_favorites)}") 
print(f'Likeable animals: {sorted(likeable_animals)}')




# 3.9.2
num_yards = float(input())

# convert num_yards to a string
str_yards = str(num_yards)

print('Number of yards: ' + str_yards)





total_cost = float(input())
tip_amount = int(input())

# Assign num_dollars with the sum of total_cost + tip_amount
num_dollars = total_cost + tip_amount

print(f'${num_dollars}')





num_stripes1 = int(input())
num_stripes2 = int(input())

# Assign avg_stripes_per_tiger with the avg stripes per tiger
avg_stripes_per_tiger = (num_stripes1 + num_stripes2) / 2

# convert avg_stripes_per_tiger to int
avg_stripes_per_tiger = int(avg_stripes_per_tiger)

print(avg_stripes_per_tiger)





# 3.11.1
number = 13

print(f'{number:d}, {number:03d}, {number:.2f}')
# Outputs:
# 13, 013, 13.00
#




# 3.11.2
num_students = 25
print(f'The math class has {num_students} students.')

loan_rate = 0.09
borrowers_name = 'Frank'
# Output Frank's loan rate is 9.0%
print(f'{borrowers_name}\'s loan rate is {loan_rate * 100:.1f}%.')

price = 10
num = 5
# Outout 5 tacos at $10 each costs $50.00
print(f'{num} tacos at ${price} each costs ${price * num:.2f}.')





# 3.11.3
user_value = int(input())
# Output user_value in fixed-point notation, with 6 places of precision
# user_value in exponent notation
print(f'{user_value:6f}\n{user_value:e}')
