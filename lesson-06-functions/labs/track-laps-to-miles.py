# one lap around a standard high-school track is exactly 0.25mi
# define a function laps_to_miles() that takes a number of laps as a param
# returns the number of miles
# then write a main program that takes a number of laps as input,
# calls laps_to_miles() to calculate the number of miles,
# and outputs the number of miles

# Define your function here 
def laps_to_miles(user_laps):
    miles = user_laps * 0.25
    return miles

if __name__ == '__main__':
    user_laps = float(input())        # accept user_laps as float from input
    miles = laps_to_miles(user_laps)  # define miles to function, passing user_laps as param
    print(f'{miles:.2f}')             # ensure miles is output showing 2 decimal places 
