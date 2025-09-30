# given a text file containing the availability of food items, write a program that reads
# the info from the text file and outputs the available food items
# 1.   the program first reads the name of the text file from a user
# 2.   then it reads the text file, stores the info into 4 separate lists
#         categories
#         names
#         descriptions
#         availability
#      and outputs the available food items in the following format 
#      name (category) -- description

# food.txt 
Sandwiches	Ham sandwich	Classic ham sandwich	Available
Sandwiches	Chicken salad sandwich	Chicken salad sandwich	Not available
Sandwiches	Cheeseburger	Classic cheeseburger	Not available
Salads	Caesar salad	Chunks of romaine heart lettuce dressed with lemon juice	Available
Salads	Asian salad	Mixed greens with ginger dressing, sprinkled with sesame	Not available
Beverages	Water	16oz bottled water	Available
Beverages	Coca-Cola	16oz Coca-Cola	Not available
Mexican food	Chicken tacos	Grilled chicken breast in freshly made tortillas	Not available
Mexican food	Beef tacos	Ground beef in freshly made tortillas	Available
Vegetarian	Avocado sandwich	Sliced avocado with fruity spread	Not available


# main.py
# Get the name of the text file from the user
filename = input()

# Initialize lists to store data
categories = []
names = []
descriptions = []
availability = []

# Read the file and store data into lists
with open(filename, 'r') as file:
  for line in file:
    # Remove any trailing newline characters and split by tab
    parts = line.strip().split('\t')
    if len(parts) == 4:
      category, name, description, avail = parts
      categories.append(category)
      names.append(name)
      descriptions.append(description)
      availability.append(avail)

# Output available food items
for i in range(len(names)):
  if availability[i].lower() == 'available':
    print(f'{names[i]} ({categories[i]}) -- {descriptions[i]}')
