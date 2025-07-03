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
