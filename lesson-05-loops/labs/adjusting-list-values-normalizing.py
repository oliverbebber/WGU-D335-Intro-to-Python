# when analyzing data sets, like human heights or weights, a common step
# is to adjust the data
# the adjustment can be done by normalizing two values between 0 and 1, or 
# throwing away outliers
# write a program that adjusts the values by dividing all values by the largest value
# the input begins with an integer indicating the number of floating-point
# values that follow
# assume that the list will always contain positive floating-point values
# output each floating-point value with 2 digits after the decimal
user_num = int(input())                    # input: 5

values = []
for i in range(user_num):
    values.append(float(input()))   # 30.0 50.0 10.0 100.0 65.0
    
max_val = max(values)
# print(max_val)                      # 100.0

for v in values:                    # for every value, 
    print(f'{v / max_val:.2f}')     # divide value by largest value
