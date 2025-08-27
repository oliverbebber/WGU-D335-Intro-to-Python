# given a line of text as input
user_text = input()

# def count as starting at 0
count = 0

# iterate through each character in user_text
for n in user_text:
    if n not in [' ', '.', '!', ',']:  # skip excluded characters
        count += 1

# output the number of characters excluding spaces, periods, commas, or exclamation points.
print(count)
