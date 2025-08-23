# 11.4.1 Reading files
# A file's name is read from input. 
# The file is opened and tie_file is assigned with the file object. 
# Each line in tie_file contains a name and a color, representing a person's name and the color of the person's tie.
# Complete the for loop to read each line, called line, from tie_file.

main.py
# The file is opened and tie_file is assigned with the file object. 
tie_file = open(input())

for line in tie_file:
    # Each line read from the file ends with a newline.
    print(line, end="")  # end="" prints each line without adding another newline.
print()

tie_file.close()



data1.txt
Meg gold
Guy red
Avi maroon
Mel teal



data2.txt
Jan brick
Abe sienna



data3.txt
Ben beige
Dax teal
Eli gray





# src_file_name is assigned with a file's name read from input. Perform the following tasks:

# Open the file named src_file_name, and assign a variable kiwi_file with the file object.
# Use kiwi_file's readlines() to read the contents of src_file_name and assign kiwi_data with the list of strings read.
# Close kiwi_file.

main.py
src_file_name = input()

# Open the file named src_file_name, and assign a variable kiwi_file with the file object.
kiwi_file = open(src_file_name)

# Use kiwi_file's readlines() to read the contents of src_file_name and assign kiwi_data with the list of strings read.
kiwi_data = kiwi_file.readlines()

# Close kiwi_file.
kiwi_file.close()

for line in kiwi_data:
    print(line, end="")
print()



data1.txt
Kim 4
Mel 2



data2.txt
Tia 14
Ada 32
Ani 35
Gus 27



data3.txt
Eli 9
Noa 27
Guy 31







# A file's name is read from input. 
# The file is opened and beet_file is assigned with the file object. 
# Each line in beet_file contains an integer representing the number of beets in a basket. 
# Use a loop to read each line of beet_file. 
# Inside the loop, if max_beets is less than the current integer, assign max_beets with the current integer.

main.py
max_beets = 0

# A file's name is read from input. 
# The file is opened and beet_file is assigned with the file object. 
beet_file = open(input())

# Each line in beet_file contains an integer representing the number of beets in a basket. 
# Use a loop to read each line of beet_file. 
for line in beet_file:  # iterates over each line of beet_file
  num_beets = int(line)
  # Inside the loop, if max_beets is less than the current integer, assign max_beets with the current integer.
  if num_beets > max_beets:  # for each line read, if max_beets is less than the int, max_beets is assigned with the int
    max_beets = num_beets

beet_file.close()

print(f'All baskets have at most {max_beets} beets.')



data1.txt
12
18



data2.txt
18
2
5



data3.txt
19
2
11
18
