# 4.2.2
# We set up a feeding station to scan for cats' microchips to see if Phe comes by the porch
# Phoenix's microchip end in 5
# If it's not a match, assign to general review group (10)
# If it's a match, assign to urgent review group (5)

chip_last_digit = int(input())  # Program will be tested with values: 5, 6, 7, 8.

if chip_last_digit != 5:
  group_id = 10  # Not Phoenix, assign to general review group
else:
  group_id = chip_last_digit  # Possibly Phoenix, assign to urgent review group & review logs

print(group_id)



# Phoenix has been missing for 523 days as of 7/29/2025
# I want to build a tool to check if a reported sighting date aligns with the timeframe he has been missing for.

# If someone claims to have seen him more than 523 days ago, the reported sighting should be labled invalid (since that would have been before he escaped)
# If the number of days this person claims to have seen him, the sighting should be labeled valid and worth checking into.
# Write an if-else statement to evaluate a reported number of days since seen.
# If the report is not valid, set lead_status = "invalid"
# Otherwise, set lead_status = "valid"

# Valid range is still 0–523 days.
# Reports older than 400 days may be valid but treated with caution (harder to confirm).

if num_days_ago_seen > 523:
    lead_status = "invalid"
elif num_days_ago_seen > 400:
    lead_status = "caution"
else:
    lead_status = "priority"

print(f"Lead status: {lead_status}")

# I will be expanding upon this in another repo as I want to add input validation on parts of the form I created when I launched the website for findingphe
# Additionally, I want to ensure that the days since I last seen him can be flexible as each day, that number increases.




# 4.4.2
# user_grade is read from user input
user_grade = int(input())

# value of user_grade is between 9 and 12 (both inclusive) then print 'in high school'
if 9 <= user_grade <=12:
  print('in high school')
# otherwise, 'not in high school'
else:
  print('not in high school')




# 4.4.3
input_val = int(input())

# value of input_val is less than 90
if input_val < 90:
  print('Less than 90')
# otherwise, '90 or more'
else:
  print('90 or more')



in_val = int(input())

if in_val <= -21:
  print('-21 or less')
else: 
  print('More than -21')



        
