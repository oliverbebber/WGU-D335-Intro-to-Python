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
