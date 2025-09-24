# Define your function here.
def swap_values(user_val1, user_val2, user_val3, user_val4):
    return user_val2, user_val1, user_val4, user_val3

if __name__ == '__main__': 
    # Type your code here. Your code must call the function.
    user_val1 = int(input())
    user_val2 = int(input())
    user_val3 = int(input())
    user_val4 = int(input())
    
    val1, val2, val3, val4 = swap_values(user_val1, user_val2, user_val3, user_val4)
    print(val1, val2, val3, val4)
