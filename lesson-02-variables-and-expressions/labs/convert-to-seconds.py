seconds = int(input())
minutes = int(input())
hours = int(input())

# Convert hours and minutes to seconds, then add together for total seconds
total_seconds = seconds + (minutes * 60) + (hours * 3600)

# Output total number of seconds
print(f"{total_seconds} seconds")
