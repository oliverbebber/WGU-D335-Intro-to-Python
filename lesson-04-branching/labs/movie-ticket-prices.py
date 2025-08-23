# given a string to hold the value of "day" or "night" and an integer that holds a person's age
time_of_day = str(input())
age = int(input())

# movies are free for everyone under 4
if age < 4:
  price = "free"
else:
  # movies are $8 for everyone older than 4 during the day
  if time_of_day == "day":
    price = "$8"
  elif time_of_day == "night":
    # movies are $12 at night for ages 4-16
    if 4 <= age <=16:
      price = "$12"
    # movies are $15 for ages 17-54
    elif 17 <= age <= 54:
      price = "$15"
    # movies are $13 for ages 55+
    else: 
      price = "$13"
  # if time_of_day isn't day or night, output invalid input
  else:
    price = "Invalid input"

# output movie ticket prices
print(price)
