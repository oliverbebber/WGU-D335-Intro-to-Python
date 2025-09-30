# write a program that calculates an adult's fat burning heart rate which is 70%
# of the diffrence between 220 and the person's age, respectively.
# 1.    complete fat_burning_heart_rate() to calculate the fat burning heart rate
#       the adult's age must be between 18 and 75, inclusive
# 2.    if the age entered is NOT in this range, raise a ValueError exception in get_age()
#       with the message "Invalid age"
# 3.    handle the exception in __main__ and prince the ValueError message along with
#       "Could not calculate heart rate info."
def get_age():
    age = int(input())
    # TODO: Raise exception for invalid ages
    if age < 18 or age > 75:    # remember age > or age, not age < or > 
        raise ValueError("Invalid age.")
    return age

# TODO: Complete fat_burning_heart_rate() function
def fat_burning_heart_rate(age):
    heart_rate = 0.7 * (220 - age)
    return heart_rate

if __name__ == "__main__":
    # TODO: Modify to call get_age() and fat_burning_heart_rate()
    #       and handle the exception
    try:
        age = get_age()
        heart_rate = fat_burning_heart_rate(age)
        print(f'Fat burning heart rate for a {age} year-old: {heart_rate} bpm')
    except ValueError as e:
        print(e)
        print('Could not calculate heart rate info.')
