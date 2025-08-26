# Lesson 07 Strings Notes

These are my notes for Lesson 07 of the Intro to Python course.

## Sections

### 1. String slicing

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

| Method              | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| capitalize()        | Converts the first character of the string to uppercase.                   |
| casefold()          | Converts the string to lowercase, more aggressive than lower().             |
| center(width)       | Centers the string within a given width, padding with spaces.               |
| count(sub)          | Counts the occurrences of a substring in the string.                        |
| encode(encoding)    | Encodes the string into bytes using the specified encoding.                  |
| expandtabs(tabsize) | Expands tabs in the string into spaces.                                     |
| find(sub)           | Returns the lowest index where the substring is found, or -1 if not found.  |
| format(*args, **kwargs) | Performs string formatting by replacing placeholders in the string.    |
| format_map(mapping) | Similar to format(), but takes a dictionary as input.                       |
| index(sub)          | Returns the lowest index of the substring, raises ValueError if not found.  |
| isalnum()           | Returns True if all characters are alphanumeric.                            |
| isalpha()           | Returns True if all characters are alphabetic.                              |
| isascii()           | Returns True if all characters are ASCII.                                   |
| isdecimal()         | Returns True if all characters are decimal digits.                          |
| isdigit()           | Returns True if all characters are digits.                                  |
| isidentifier()      | Returns True if the string is a valid Python identifier.                    |
| islower()           | Returns True if all characters are lowercase.                               |
| isnumeric()         | Returns True if all characters are numeric.                                 |
| isprintable()       | Returns True if all characters are printable.                               |
| isspace()           | Returns True if all characters are whitespace.                              |
| istitle()           | Returns True if the string is in title case.                                |
| isupper()           | Returns True if all characters are uppercase.                               |
| join(iterable)      | Concatenates elements of an iterable with the string as a separator.         |
| ljust(width)        | Left-justifies the string within a given width, padding with spaces.         |
| lower()             | Converts the string to lowercase.                                           |
| lstrip()            | Removes leading whitespace from the string.                                 |
| partition(sep)      | Splits the string into a 3-tuple at the first occurrence of the separator.   |
| replace(old, new)   | Replaces occurrences of a substring with a new substring.                   |
| removeprefix(prefix)| Removes the specified prefix if it exists.                                  |
| removesuffix(suffix)| Removes the specified suffix if it exists.                                  |
| rfind(sub)          | Returns the highest index where the substring is found, or -1 if not found. |
| rindex(sub)         | Returns the highest index of the substring, raises ValueError if not found. |
| rjust(width)        | Right-justifies the string within a given width, padding with spaces.        |
| rpartition(sep)     | Splits the string into a 3-tuple at the last occurrence of the separator.    |
| rsplit(sep)         | Splits the string at each occurrence of the separator from the right.        |
| rstrip()            | Removes trailing whitespace from the string.                                |
| split(sep)          | Splits the string at each occurrence of the separator.                      |
| splitlines()        | Splits the string into a list of lines.                                     |
| swapcase()          | Swaps case, converting uppercase to lowercase and vice versa.               |
| translate(table)    | Translates characters using the given translation table.                    |
| upper()             | Converts the string to uppercase.                                           |
| zfill(width)        | Pads the string with zeroes to the left to fill a given width.               |


### 5. Splitting and joining strings

### 6. Strings practice

### References

[Python String Interpolation](https://www.geeksforgeeks.org/python/python-string-interpolation/)
