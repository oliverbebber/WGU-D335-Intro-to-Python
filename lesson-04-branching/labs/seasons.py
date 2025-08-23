# write a program that takes a date as input
input_month = input()

try:
    input_day = int(input())
except ValueError:
    print('Invalid')
    exit()

# dict days in each month (ignore leap years) to define length of months
days_in_month = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

# validate input
if input_month not in days_in_month or not (1 <= input_day <= days_in_month[input_month]):
    print('Invalid')
    exit()

# spring: march 20 - june 20
if (input_month == "March" and input_day >= 20) or input_month in ["April", "May"] or (input_month == "June" and input_day <= 20):
    season = "Spring"
# summer: june 21 - september 21
elif (input_month == "June" and input_day >= 21) or input_month in ["July", "August"] or (input_month == "September" and input_day <= 21):
    season = "Summer"
# autumn: september 22 - deceomber 20
elif (input_month == "September" and input_day >= 22) or input_month in ["October", "November"] or (input_month == "December" and input_day <= 20):
    season = "Autumn"
# winter: december 21 - march 19
else:
    season = "Winter"

# output the date's season in the northern hemisphere
print(season)
