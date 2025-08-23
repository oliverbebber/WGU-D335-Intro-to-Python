''' calories = (age x 0.2757 + weight x 0.03295 + heartrate x 1.0781 - 75.4991) x time / 8.368 '''
# write a program using inputs age (in years), weight (in pounds), heartrate (BPM), and time (mins) respectively.
age = int(input())
weight = int(input())
heartrate = int(input())
time = int(input())

# output the avgerage calories burned for a person
calories = (age * 0.2757 + weight * 0.03295 + heartrate * 1.0781 - 75.4991) * time / 8.368
  # 49 * 0.2757 = 13.5093
  # 155 * 0.03295 = 5.10725
  # 148 * 1.0781 = 159.5588
  # 13.5093 + 5.10725 + 159.5588 = 178.17535
  # 178.17535 - 75.4991 = 102.67625
  # 102.67625 * 60 = 6160.575
  # 6160.575 // 8.368 = 736.2063814531549
    # round the result to the second decimal point --- don't use floor division (//)

# each floating-point value should have 2 digits after the decimal point
print(f'Calories: {calories:.2f} calories')
