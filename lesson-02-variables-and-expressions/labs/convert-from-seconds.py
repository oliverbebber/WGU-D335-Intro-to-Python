# Read total number of seconds from user input
total_seconds = int(input())

# Calculate number of hours
hours = total_seconds // 3600

# Calculate remaining seconds after factoring out hours
remaining_seconds = total_seconds % 3600

# Calculate number of full minutes from remaining seconds
minutes = remaining_seconds // 60

# Calculate remaining seconds after removing full minutes
seconds = remaining_seconds % 60

# Output the results in specific format
print(f"Seconds: {seconds}")
print(f"Minutes: {minutes}")
print(f"Hours: {hours}")
