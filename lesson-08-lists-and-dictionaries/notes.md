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

- **list method**: can perform useful operations on lists like adding or removing elements, sorting, reversing, etc.

| List method | Description | Code example | Final my_list value |
|-------------|-------------|--------------|-------------------|
| **`list.append(x)`** | Add an item to the end of list. | ```python\nmy_list = [5, 8]\nmy_list.append(16)``` | `[5, 8, 16]` |
| **`list.extend([x])`** | Add all items in `[x]` to list. | ```python\nmy_list = [5, 8]\nmy_list.extend([4, 12])``` | `[5, 8, 4, 12]` |
| **`list.insert(i, x)`** | Insert `x` into list before position `i`. | ```python\nmy_list = [5, 8]\nmy_list.insert(1, 1.7)``` | `[5, 1.7, 8]` |
| **`list.remove(x)`** | Remove first item from list with value `x`. | ```python\nmy_list = [5, 8, 14]\nmy_list.remove(8)``` | `[5, 14]` |
| **`list.pop()`** | Remove and return last item in list. | ```python\nmy_list = [5, 8, 14]\nval = my_list.pop()``` | `[5, 8]` <br> `val` is `14` |
| **`list.pop(i)`** | Remove and return item at position `i` in list. | ```python\nmy_list = [5, 8, 14]\nval = my_list.pop(0)``` | `[8, 14]` <br> `val` is `5` |
| **`list.sort()`** | Sort the items of list in-place. | ```python\nmy_list = [14, 5, 8]\nmy_list.sort()``` | `[5, 8, 14]` |
| **`list.reverse()`** | Reverse the elements of list in-place. | ```python\nmy_list = [14, 5, 8]\nmy_list.reverse()``` | `[8, 5, 14]` |
| **`list.index(x)`** | Return index of first item in list with value `x`. | ```python\nmy_list = [5, 8, 14]\nprint(my_list.index(14))``` | Prints `2` |
| **`list.count(x)`** | Count the number of times value `x` is in list. | ```python\nmy_list = [5, 8, 5, 5, 14]\nprint(my_list.count(5))``` | Prints `3` |

Important: It's a good practice to use methods to add and delete list elements vs alternative add and delete methods 
- Alternative approaches:
  > ```python
  > my_list[len(my_list):] = [val]  # to add a list
  >
  > del my_list[0]  # to remove from a list
  > ```



### 3. List methods and functions reference

| Method            | Description                                                     |
|-------------------|-----------------------------------------------------------------|
| append(item)      | Adds an item to the end of the list.                            |
| clear()           | Removes all items from the list.                                |
| copy()            | Returns a shallow copy of the list.                             |
| count(item)       | Returns the number of occurrences of the specified item.        |
| extend(iterable)  | Extends the list by appending all items from an iterable.        |
| index(item)       | Returns the index of the first occurrence of the specified item. |
| insert(index, item)| Inserts an item at the specified index in the list.             |
| pop(index)        | Removes and returns the item at the specified index.            |
| remove(item)      | Removes the first occurrence of the specified item.             |
| reverse()         | Reverses the elements of the list in place.                     |
| sort()            | Sorts the list in place.                                        |


**Additional List Methods**

- Use ```help(list)``` and ```print(dir(list))``` to see more about lists & their methods; provide detailed info and a list of available list methods

**Built-in Functions for List Reference**

| Function       | Description                                                               |
|----------------|---------------------------------------------------------------------------|
| len(list)      | Returns the number of items in the list.                                  |
| min(list)      | Returns the smallest item in the list.                                    |
| max(list)      | Returns the largest item in the list.                                     |
| sum(list)      | Returns the sum of all items in the list (requires numeric items).        |
| sorted(list)   | Returns a new sorted list from the items in the original list.            |
| reversed(list) | Returns an iterator that accesses the elements of the list in reverse order. |


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
