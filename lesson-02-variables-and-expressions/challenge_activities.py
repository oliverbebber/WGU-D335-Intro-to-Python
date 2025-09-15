# 2.7.2 
# convert total_years to millennia, decades, and years
# finding the max number of millenia, then decades, then years
total_years = int(input())  # input is 8018

num_millennia = total_years // 1000  # 8018 // 1000 = 8 --> integer (floor) division
remaining_years_after_millennia = total_years % 1000  # 8018 % 1000 = 8 --> 8 * 1000 = 8000 --> 8000 + x = 8018 --> x = 18, modulo 18

num_decades = remaining_years_after_millennia // 10  # 18 // 10 = 1; num_decades is 1, num_years is the remainder; use modulo to solve
num_years = remaining_years_after_millennia % 10  # 18 % 10 = 1 --> 1 * 10 = 10 --> 10 + x = 18 --> x = 8, modulo 8 

# output
print('Millennia:', num_millennia)  # 8
print('Decades:', num_decades)  # 1
print('Years:', num_years)  # 8


# 2.11.2
# q1 
name1_input = input()

my_str = "picked the \"freshest\" dates"

# Output name1_input followed by my_str, separated by a space
print(name1_input, my_str) 



#2.11.2 
# q2
folder_input = input()

# Output folder names on new line after accepting input
computer_folders = "\nSystem\nAppData\nContacts\nBackup"

print(folder_input, end="")
print(computer_folders)



#2.11.2
# q3
vegetable_input = input()

# Output vegetables on a new line with indentations between each
my_list = "Finn\'s vegetables:\nCorn\tPeas\t"

print(my_list, end="")
print(vegetable_input)
