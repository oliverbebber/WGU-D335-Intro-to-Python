# Define your function here 
def feet_to_steps(user_feet):
    # use float division, cast to int
    result = int(user_feet / 2.5)
    return result

if __name__ == '__main__':
    # Type your code here.
    user_feet = float(input())
    # call function and store result
    steps = feet_to_steps(user_feet)
    print(steps)
