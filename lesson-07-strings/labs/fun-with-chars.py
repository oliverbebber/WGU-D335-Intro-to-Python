# complete the check_character() function which has 2 params
# a string and a specified index
def check_character(word, index):
  # function checks the character at the specified index of the string param
  char = word[index]
  # returns a string based on the type of character at that location inidicating
  # if the character is a letter, digit, whitespace, or unknown character
  
  if char.isalpha():
    return f"Letter: '{char}'"
  elif char.isdigit():
    return f"Digit: '{char}'"
  elif char.isspace():
    return f"Whitespace: ' '"
  else:
    return f"Unknown: '{char}'"
  
if __name__ == '__main__': 
  print(check_character('happy birthday', 2))          # returns "Letter: 'p'"
  print(check_character('happy birthday', 5))          # returns "Whitespace: ' '"
  print(check_character('happy birthday 2 you', 15))   # returns "Digit: '2'"
  print(check_character('happy birthday!', 14))        # returns "Unknown: '!'"
