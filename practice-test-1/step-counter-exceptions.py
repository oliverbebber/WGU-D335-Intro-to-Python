# a pedometer treats walking 2000 steps as walking 1 mile
# write a steps_to_miles() function that takes the number of steps as a paramenter and
# returns the miles walked
# the steps_to_miles() function raises a ValueError object with the message
# "Exception: Negative step count entered." when the number of steps is Negative
# complete the main() program tha treads the number of steps from a user, calls the 
# steps_to_miles() function, and outputs the returned value from the steps_to_miles() function.

# use a try-except block to catch any ValueError object raised by the steps_to_miles() function
# and output the exception message

# output each floating-point value with 2 digits after the decimal, using:
# print(f'{your_val:.2f}')

# test input:
# 5345

# expected output:
# 2.67

# test input v2:
# -3850

# expected output:
# Exception: Negative step count entered.

def steps_to_miles(num_steps):
    if num_steps < 0:
        raise ValueError("Exception: Negative step count entered.")
        
    miles_walked = num_steps / 2000
    return miles_walked

if __name__ == '__main__':
    try:
        steps = int(input())
        
        miles = steps_to_miles(steps)
        
        print(f'{miles:.2f}')
        
    except ValueError as e:
        print(e)
