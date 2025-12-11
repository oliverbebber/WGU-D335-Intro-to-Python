# the given program reads a list of single-word first names and ages (ending with -1), and outputs
# that list with the age incremented. the program fails and raises an exception if the second input
# on a line is a string rather than an integer.
# at FIXME in the code, add try and except blocks to catch the ValueError exception and output 0 for
# the age

# test input:
# Lee 18
# Lua 21
# Mary Beth 19
# Stu 33
# -1

# expected output:
# Lee 19
# Lua 22
# Mary 0
# Stu 34

# Split input into 2 parts: name and age
parts = input().split()
name = parts[0]
while name != '-1':
    # FIXME: The following line will raise ValueError exception.
    #        Insert try/except blocks to catch the exception.
    try:
        age = int(parts[1]) + 1
        print(f'{name} {age}')
    
    except ValueError:
        print(f'{name} 0')
    # Get next line
    parts = input().split()
    name = parts[0]
