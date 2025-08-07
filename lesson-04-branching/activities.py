# 4.2.2
# Organizing a search party to look for Phe
# If the urgency level equals 10, add 3 extra volunteers to the team
# Initially, only one volunteer signed up
search_urgency = 10
volunteers = 1

# After running the following code, how many volunteers will be on my team?
if search_urgency == 10:
  volunteers = volunteers + 3
# volunteers = 4


# Prepping supplies to search for Phe
# Add 3 extra treat bag if the search urgency is 10
# Start with 1 treat bag
# Urgency is currently level 0 due to no reported sightings but a new cat has been showing up every night
search_urgency = 0
treat_bags = 1

# After running the following code, how many treat bags will you need to take on your walk?
if search_urgency == 10:
  treat_bags = treat_bags + 3
# treat_bags = 1


# 4.2.3
phoenix_age == 6  # Assign age

if phoenix_age == 6:
  print("Phoenix is 6 years old.")
        

#4.2.4
num_cats == 2
num_dogs == 7
        
num_dogs != num_cats


# 4.2.6
# You base the number of flyers on how many cats have been seen and how big the area is. 
# More cats and a large area? Print a lot. 
# More cats in a small space? Fewer are needed. 
# Fewer cats overall? Print the minimum to stay efficient.

cats_spotted = 12
search_area = "large"  # could be "small"

# The 'and' operator means BOTH conditions must be True for the block to run
if cats_spotted >= 10 and search_area == "large":
  flyers_needed = 300
# if cats are >= 10 but the search area is smaller (BOTH conditions must be True)
elif cats_spotted >= 10 and search_area == "small":
  flyers_needed = 150
# cover all other cases (like fewer than 10 cats spotted)
else:
  flyers_needed = 75

# flyers_needed = 300


# Once 12 credible reports come in about the same cat, you’re confident enough to set up a humane trap. 
# Otherwise, you wait for more data.
reports_received = 12

if reports_received == 12:
  begin_trapping = True
else:
  begin_trapping = False

# begin_trapping = True


# You haven’t seen a cat in over two weeks.
# Depending on exactly how long it’s been, you increase food slightly or more significantly
# And always add a small buffer since the raccoons, opossums, and skunks swing by for snacks and you want to be sure some food is leftover
days_since_last_cat = 15
daily_food_grams = 44

if days_since_last_cat == 14:
  daily_food_grams = daily_food_grams + 3  # Slight increase
else:
  daily_food_grams = daily_food_grams + 6  # Larger increase due to long absence

daily_food_grams = daily_food_grams + 1  # Adding extra gram just in case

# daily_food_grams = 51


# 4.2.7 
# Organizing teams to hand out flyers for Phoenix
# If exactly 10 people show up, the group gets divided differently
num_volunteers = 10
flyer_group_size = 5

if num_volunteers == 10:
  flyer_group_size = 2 * flyer_group_size
else: 
  flyer_group_size = 3 * flyer_group_size
  num_volunteers = num_volunteers - 1  # Someone had to leave early


# Preparing for a search party
# I want at least 11 people, even if less show up
# After setting the minimum team size, double the size for night search teams
search_team_count = 9  # maybe only 9 showed up today

# If the team is smaller than 11, assign a minimum value
if search_team_count != 11:
  team_size = 11
else: 
  team_size = search_team_count

# Then double the size for night searches
team_size = 2 * team_size





# 4.5.6
# num_cats has a minimum of 2 and a maximum of 5
if (num_cats >= 2) and (num_cats <=5):

# wage is greater than 10 and less than 18
if (wage > 10) and (wage < 18):

# num is a 3-digit positive integer, compare the smallest and largest 3-digit number
if (num >= 100) and (num <= 999):





# 4.5.7
user_channel = int(input())  # Input is 300
   
if (user_channel >= 2) and (user_channel <= 499):
    channel_type = 's'  # Evaluates to True

elif (user_channel >= 1002) and (user_channel <= 1499):
    channel_type = 'h'

else:
    channel_type = 'e'

print(f'Channel type: {channel_type}')





# 4.5.9
if temp <= 0...
elif (temp > 0) and (temp < 100)...

if temp <= 0...
elif temp < 100...
# detects the same range as the first if-else statement as the ranges do not have gaps (low end can be implicit)

if systolic < 130: ...
elif (systolic >= 130) and (systolic <= 139): ...

if systolic < 130: ...
elif systolic >= 130: ...
# does NOT detect the same range since the first branch must be grater than or equal to 130
# the low end of the second range can be implicitly 130
# the second if-else statement EXPLICITLY defines the low end of the second range 
# lacks the high end of the range

if (year >= 1901) and (year <= 2000): ...
elif (year >= 2001) and (year <= 2100): ...

if year <= 2000: ...
elif year <= 2100: ...
# does NOT detect the same range since the first branch's low end is 1901 and must be explicit
# the low end of the second range is 2001 and can be implicit since there the range lacks a gap




# 4.6.2
if num_items <= 0: ...
elif num_items > 100: ...
else:   # Range: 1 - 100


if num_items < 50: ...
elif num_items > 50: ...
else:   # Range: 50
