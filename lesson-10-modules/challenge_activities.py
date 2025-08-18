# 10.1.1
main.py
import arithmetic

def calculate(number):
    return number * 2

print(calculate(4))
print(arithmetic.calculate(4))



arithmetic.py
def calculate(number):
    return number + 2	


# output: 8
# 6
#



main.py
import arithmetic

def calculate(number):
    return number - 4

print(arithmetic.calculate(5))
print(calculate(5))


arithmetic.py

def calculate(number):
    return number * 4


# output: 20
# 1
#


main.py
import arithmetic

def calculate(number):
    return number * 4   # 2 * 4 = 8 

print(arithmetic.calculate(2))  # -2
print(calculate(2))	  # 8



arithmetic.py
def calculate(number):
    return number - 4  # 2 - 4 = -2


# output: -2
# 8
# 





main.py
import arithmetic
import data

def calculate(number): 
    return number * 3  # 90 * 3 = 270

print(arithmetic.calculate(data.medium))  # 88
print(calculate(data.medium))  # 270


data.py
small = 7
medium = 90
large = 500


arithmetic.py
def calculate(number):
    return number - 2  # 90 - 2 = 88

# output: 88
# 270
#



main.py
import blue
import red

print(blue.dark)  # cerulean
print(red.dark)  # vermilion


blue.py
dark = 'cerulean'
bright = 'royal'
medium = 'steel'
dull = 'powder'


red.py
dark = 'vermilion'
bright = 'crimson'
medium = 'salmon'
dull = 'coral'

# output:  # cerulean
# vermilion
# 


main.py
import blue
import green

print(blue.dark)  # cerulean
print(green.dark)  # viridian


blue.py
dark = 'cerulean'
bright = 'royal'
medium = 'steel'
dull = 'powder'

green.py
dark = 'viridian'
bright = 'forest'
medium = 'chartreuse'
dull = 'olive'

# output: cerulean
# viridian
# 



main.py
import first

def fct_a(number):
    return number ** 2

def fct_b(number):
    return number * 6

def fct_c(number):
    return fct_a(number) - fct_b(number)  # 

print(fct_c(1))  # -5
print(first.fct_c(1))  # -27
print(first.fct_d(1))  # 9


first.py
import second

def fct_a(number):
    return number + 8  # 1 + 8 = 9

def fct_b(number):
    return number - 4  # 1 - 4 = -3

def fct_c(number):
    return fct_a(number) * fct_b(number)  # 9 * -3 = -27

def fct_d(number):
    return second.fct_c(number)  # 9
  

second.py
def fct_a(number):
    return number - 2

def fct_b(number):
    return number + 5

def fct_c(number):
    return number * 9  # 1 * 9 = 9


# output: -5
# -27
# 9
#


main.py
import first

def fct_a(number):
    return number ** 2  # 9 ** 2 = 81

def fct_b(number):
    return number * 2  # 9 * 2 = 18

def fct_c(number):
    return fct_a(number) - fct_b(number)  # 81 - 18 = 63

print(fct_c(9))  # 63
print(first.fct_c(9))  # 12
print(first.fct_d(9))  # 6


first.py
import second

def fct_a(number):
    return number * 1  # 9 * 1 = 9

def fct_b(number):
    return number - 6  # 9 - 6 = 3

def fct_c(number):
    return fct_a(number) + fct_b(number)   # 9 + 3 = 12

def fct_d(number):
    return second.fct_c(number)  # 6 


second.py
def fct_a(number):
    return number * 4

def fct_b(number):
    return number + 8

def fct_c(number):
    return number - 3  # 9 - 3 = 6

# output: 63
# 12
# 6 
# 






# 10.1.2
main.py
import airline_kiosk
import airline_luggage

# string traveler_name & integer num_luggages are read from input
traveler_name = input()
num_luggages = int(input())

airline_kiosk.check_in(traveler_name, num_luggages)
airline_luggage.check_bags(num_luggages)


airline_kiosk.py
def check_in(traveler_name, num_luggages):
	print(f'{num_luggages} pieces of luggage are checked by {traveler_name}.')


airline_luggage.py
def check_bags(num_luggages):
	charge = num_luggages * 30
	print(f'${charge} is charged for {num_luggages} pieces of luggage.')






main.py
import airline_kiosk
import airline_luggage

customer_name = input()
luggage_quantity = int(input())

# call airline_kiosk's check_in() with customer_name & luggage_quantity as arguments
airline_kiosk.check_in(customer_name, luggage_quantity)

# call airline_luggage's deposit() with luggage_quantity as the argument
airline_luggage.deposit(luggage_quantity)

# call airline_luggage's insure() with customer_name & luggage_quantity as the arguments, respectively
airline_luggage.insure(customer_name, luggage_quantity)


airline_kiosk.py
def check_in(customer_name, luggage_quantity):
	print(f'{customer_name} checks in with {luggage_quantity} pieces of luggage.')


airline_luggage.py
def deposit(luggage_quantity):
	charge = luggage_quantity * 35
	print(f'{luggage_quantity} pieces of luggage cost {charge} dollars.')

def insure(customer_name, luggage_quantity):
	print(f'$50 lost luggage insurance bought by {customer_name} to cover {luggage_quantity} pieces of luggage.')







main.py
import persons
import colors
import clothing
import search

one_sentence = input()

# assign has_color with the value returned by search's find() called with one_sentence and color's search_list as the arguments, respectively
has_color = search.find(one_sentence, colors.search_list)

# assign has_person_and_clothing with the value returned by combining the following using logical AND:
    # search's find() called with one_sentence & persons's search_list as the arguments, respectively
    # search's find() called with one_sentence & clothing's search_list as the arguments, respectively
has_person_and_clothing = (search.find(one_sentence, persons.search_list)) and (search.find(one_sentence, clothing.search_list))    
    # be sure to use 'and' vs 'AND' to prevent syntax errors

# could also be written as the following
# has_person_and_clothing = (
#    search.find(one_sentence, persons.search_list)
#    and search.find(one_sentence, clothing.search_list)
# )


if has_color:
	print('The sentence mentions a color.')

if has_person_and_clothing:
	print('The sentence mentions a person and a piece of clothing.')



persons.py
search_list = ['He', 'You', 'I']


colors.py
search_list = ['red', 'yellow', 'pink']


clothing.py
search_list = ['coat', 'hat', 'cap']


search.py
def find(one_sentence, search_list):
    words = one_sentence[:-1].split()
    for word in words:
        if word in search_list:
            return True
    return False
