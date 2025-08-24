# Lesson 07 Strings Notes

These are my notes for Lesson 07 of the Intro to Python course.

## Sections

### 1. Strng slicing

- **index**: an integer matching a specific position in a string's sequence of characters

- **Slice notation**: general form ```my_str[start:end]```
  - This creates a new string containing the characters of ```my_str``` starting at index ```start``` (inclusive) to, but not including, index ```end```
  - Example
  > ``` python
  > my_str = 'Boogle'
  > my_str[0:3]  # output: Bog
  > ```
  
**Slicing and slicing operations**

| Syntax        | Result                          | Description                                                   |
|---------------|---------------------------------|---------------------------------------------------------------|
| my_str[10:19] | wikipedia                       | Returns the characters in indices 10–18.                      |
| my_str[10:-5] | wikipedia.org/wiki/             | Returns the characters in indices 10–28.                      |
| my_str[8:]    | n.wikipedia.org/wiki/Nasa/      | Returns all characters from index 8 until the end of the string. |
| my_str[:23]   | http://en.wikipedia.org         | Returns every character up to index 23, but not including `my_str[23]`. |
| my_str[:-1]   | http://en.wikipedia.org/wiki/Nasa | Returns all but the last character.                          |


### 2. Advanced string formatting

### 3. String methods

### 4. String methods reference

### 5. Splitting and joining strings

### 6. Strings practice

### References
