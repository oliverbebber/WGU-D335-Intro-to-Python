# Open & read file, append sentence from contents of original file, read and display contents

# solution accepts file input to insert sentence composed of file content into text file on a new line
# solution outputs the text file contents including the new sentence
# accept input identifying filename
print("Enter the name of the input file:")
filename = input()

# 1. Read the words from a the file
with open(filename, 'r') as f:
    words = [line.strip() for line in f]

# 2. Construct a sentence from the contents of the file
sentence = ' '.join(words)

# 3. Append the sentence to the file on a new line
with open(filename, 'a') as f:
    f.write('\n' + sentence + '\n')
 
# 4. Display updated contents of the file
with open(filename, 'r') as f:
    for line in f:
        print(line, end='')
