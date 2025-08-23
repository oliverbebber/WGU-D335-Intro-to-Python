# Prompt the user to enter a chord name
user_chord = input()

# The chord can be "G", "C", or "D"

# If the chord is "G":
if user_chord == "G":
  # Output the corresponding tab using print()
  # Use \n to include multiple lines in a single string
  # Each line represents a string on the guitar, from highest (e) to lowest (E)
  # Numbers indicate which fret to press; 0 means open string
  print('e|-3-\nB|-0-\nG|-0-\nD|-0-\nA|-2-\nE|-3-')

# If the chord is "C":
elif user_chord == "C":
  # Output the tab for C chord similarly
  # strings that should not be played (represented by ---)
  print('e|-0-\nB|-1-\nG|-0-\nD|-2-\nA|-3-\nE|---')

# If the chord is "D":
elif user_chord == "D":
  # Output the tab for D chord
  # strings that should not be played (represented by ---)
  print('e|-2-\nB|-3-\nG|-2-\nD|-0-\nA|---\nE|---')

# Use an else branch to handle unrecognized chord names
else:
  # print a message like "{chord} is not a supported chord."
  print(f'{user_chord} is not a supported chord.')   # be sure to enter output messages EXACTLY as required by the problem
