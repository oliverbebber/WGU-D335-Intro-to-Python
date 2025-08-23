# Lesson 08 Lists and Dictionaries Notes

These are my notes for Lesson 08 of the Intro to Python course.

## Sections

### 1. Lists

- **Container**: an object that groups related objects together

- **List**: a mutable container; the size of the list can grow or shrink, elements can be changed within the list; also a sequence

- **list() function**: accepts a single iterable object argument (string, list, tuple) and returns a new list object
  - Example
  > ``` python
  > letters = list('abc')
  > print(letters)  # output: ['a', 'b', 'c']
  > ```

- **index**: a zero-based integer matching to a specific position in a list's sequence of elements
  - Example
  > ``` python
  > fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
  >
  > # Accessing an element using a fixed integer index
  > print(fruits[2])  # output: 'cherry' (3rd element, index 2)
  >
  > # Using a variable as an index
  > i = 4
  > print(fruits[i])  # output: 'elderberry' (5th element, index 4)
  >
  > # Using an expression as an index
  > print(fruits[i - 2])  # output: 'cherry' (index 2)
  > ```

**Common list operators and in-place list modification**

| Operation | Description | Example code | Example output |
|-----------|-------------|--------------|----------------|
| **`my_list = [1, 2, 3]`** | Creates a list. | ```python\nmy_list = [1, 2, 3]\nprint(my_list)``` | `[1, 2, 3]` |
| **`list(iter)`** | Creates a list from an iterable. | ```python\nmy_list = list('123')\nprint(my_list)``` | `['1', '2', '3']` |
| **`my_list[index]`** | Gets an element from a list. | ```python\nmy_list = [1, 2, 3]\nprint(my_list[1])``` | `2` |
| **`my_list[start:end]`** | Gets a new list containing some of another list's elements. | ```python\nmy_list = [1, 2, 3]\nprint(my_list[1:3])``` | `[2, 3]` |
| **`my_list1 + my_list2`** | Gets a new list with elements of `my_list2` added to end of `my_list1`. | ```python\nmy_list = [1, 2] + [3]\nprint(my_list)``` | `[1, 2, 3]` |
| **`my_list[i] = x`** | Changes the value of the element at index `i` in-place. | ```python\nmy_list = [1, 2, 3]\nmy_list[2] = 9\nprint(my_list)``` | `[1, 2, 9]` |
| **`del my_list[i]`** | Deletes the element from index `i` from a list. | ```python\nmy_list = [1, 2, 3]\ndel my_list[1]\nprint(my_list)``` | `[1, 3]` |

- **in-place modification**: refers to changing the contents of a list **without** creating a new list



### 2. List methods

### 3. List methods and functions reference

### 4. Using built-in functions with lists

### 5. List games

### 6. List nesting

### 7. List slicing

### 8. Loops modifying lists

### 9. List comprehensions

### 10. Sorting lists

### 11. Command-line arguments

### 12. Additional practice: Engineering examples

### 13. Dictionaries

### 14. Dictionary methods

### 15. Dictionary methods reference

### 16. Iterating over a dictionary

### 17. Dictionary nesting

### 18. Lists and dictionaries practice

### References

[Python Lists](https://www.geeksforgeeks.org/python/python-lists/)
