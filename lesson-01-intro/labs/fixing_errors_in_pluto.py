int proportion = 6

print("Is Pluto a planet?")
print("Some people think so, ")
print("but others don't.")
print("The Moon's mass is " + proportion + " times Pluto's.")  # first syntax error
print("Not much of a planet, is it.")

# Resolved errors
proportion = 6

print("Is Pluto a planet?")
print("Some people think so, but others don't.")
print(f'The Moon\'s mass is {proportion} times Pluto\'s.')
print("Not much of a planet, is it?")
