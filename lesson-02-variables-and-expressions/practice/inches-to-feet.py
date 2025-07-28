# Read total inches from user input
total_inches = int(input())

# Divide total inches by 12 to get the number of feet (12in = 1ft)
feet = total_inches // 12 

# Calculate remaining inches using modulus operator
inches = total_inches % 12

# Print the result in feet and inches format (e.g., 5'5")
print(f"{feet}'{inches}\"")
