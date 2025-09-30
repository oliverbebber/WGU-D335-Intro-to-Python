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
| **`my_list = [1, 2, 3]`** | Creates a list. | ```my_list = [1, 2, 3]``` <br> ```print(my_list)``` | `[1, 2, 3]` |
| **`list(iter)`** | Creates a list from an iterable. | ```my_list = list('123')``` <br> ```print(my_list)``` | `['1', '2', '3']` |
| **`my_list[index]`** | Gets an element from a list. | ```my_list = [1, 2, 3]``` <br> ```print(my_list[1])``` | `2` |
| **`my_list[start:end]`** | Gets a new list containing some of another list's elements. | ```my_list = [1, 2, 3]``` <br> ```print(my_list[1:3])``` | `[2, 3]` |
| **`my_list1 + my_list2`** | Gets a new list with elements of `my_list2` added to end of `my_list1`. | ```my_list = [1, 2] + [3]``` <br> ```print(my_list)``` | `[1, 2, 3]` |
| **`my_list[i] = x`** | Changes the value of the element at index `i` in-place. | ```my_list = [1, 2, 3]``` <br> ```my_list[2] = 9``` <br> ```print(my_list)``` | `[1, 2, 9]` |
| **`del my_list[i]`** | Deletes the element from index `i` from a list. | ```my_list = [1, 2, 3]``` <br> ```del my_list[1]``` <br> ```print(my_list)``` | `[1, 3]` |

- **in-place modification**: refers to changing the contents of a list **without** creating a new list



### 2. List methods

- **list method**: can perform useful operations on lists like adding or removing elements, sorting, reversing, etc.

| List method | Description | Code example | Final my_list value |
|-------------|-------------|--------------|-------------------|
| **`list.append(x)`** | Add an item to the end of list. | ```my_list = [5, 8]``` <br> ```my_list.append(16)``` | `[5, 8, 16]` |
| **`list.extend([x])`** | Add all items in `[x]` to list. | ```my_list = [5, 8]``` <br> ```my_list.extend([4, 12])``` | `[5, 8, 4, 12]` |
| **`list.insert(i, x)`** | Insert `x` into list before position `i`. | ```my_list = [5, 8]``` <br> ```my_list.insert(1, 1.7)``` | `[5, 1.7, 8]` |
| **`list.remove(x)`** | Remove first item from list with value `x`. | ```my_list = [5, 8, 14]``` <br> ```my_list.remove(8)``` | `[5, 14]` |
| **`list.pop()`** | Remove and return last item in list. | ```my_list = [5, 8, 14]``` <br> ```val = my_list.pop()``` | `[5, 8]` <br> `val` is `14` |
| **`list.pop(i)`** | Remove and return item at position `i` in list. | ```my_list = [5, 8, 14]``` <br> ```val = my_list.pop(0)``` | `[8, 14]` <br> `val` is `5` |
| **`list.sort()`** | Sort the items of list in-place. | ```my_list = [14, 5, 8]``` <br> ```my_list.sort()``` | `[5, 8, 14]` |
| **`list.reverse()`** | Reverse the elements of list in-place. | ```my_list = [14, 5, 8]``` <br> ```my_list.reverse()``` | `[8, 5, 14]` |
| **`list.index(x)`** | Return index of first item in list with value `x`. | ```my_list = [5, 8, 14]``` <br> ```print(my_list.index(14))``` | Prints `2` |
| **`list.count(x)`** | Count the number of times value `x` is in list. | ```my_list = [5, 8, 5, 5, 14]``` <br> ```print(my_list.count(5))``` | Prints `3` |

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

**Iterating through a list: finding the max even number**

  > ``` python
  > user_input = input('Enter numbers:')
  > tokens = user_input.split()  # Split into separate strings
  >
  > # Convert strings to integers
  > nums = []
  > for token in tokens:
  >   nums.append(int(token))
  >
  > # Print each position and number
  > print()  # Print a single newline
  > for index in range(len(nums)):
  >   value = nums[index]
  >
  > print(f'{index}: {value}')
  > # Determine maximum even number
  > max_num = None
  > for num in nums:
  >   if (max_num == None) and (num % 2 == 0):
  >     # First even number found
  >     max_num = num
  >   elif (max_num != None) and (num > max_num ) and (num % 2 == 0):
  >     # Larger even number found
  >     max_num = num
  >
  > print(f'Max even #: {max_num}')
  > ```


### 5. List games

### 6. List nesting

### 7. List slicing

## Common list slicing operations

| Operation                 | Description                                                     | Example code                                | Example output          |
|----------------------------|-----------------------------------------------------------------|---------------------------------------------|-------------------------|
| `my_list[start:end]`       | Get a list from start to end (minus 1).                        | `my_list = [5, 10, 20]`<br>`print(my_list[0:2])` | `[5, 10]`              |
| `my_list[start:end:stride]`| Get a list of every stride element from start to end (minus 1).| `my_list = [5, 10, 20, 40, 80]`<br>`print(my_list[0:5:3])` | `[5, 40]`              |
| `my_list[start:]`          | Get a list from start to end of the list.                      | `my_list = [5, 10, 20, 40, 80]`<br>`print(my_list[2:])` | `[20, 40, 80]`         |
| `my_list[:end]`            | Get a list from beginning of the list to the end (minus 1).    | `my_list = [5, 10, 20, 40, 80]`<br>`print(my_list[:4])` | `[5, 10, 20, 40]`      |
| `my_list[:]`               | Get a copy of the list.                                        | `my_list = [5, 10, 20, 40, 80]`<br>`print(my_list[:])` | `[5, 10, 20, 40, 80]`  |


### 8. Loops modifying lists

### 9. List comprehensions

A list comprehension has 3 parts:

1. An **expression component** to evaluate for each element in the iterable object
2. A **loop variable component** to bind the current iteration element
3. An **iterable object component** to iterate over (list, string, tuple, enumerate, etc)

Note: list comprehensions are *always* surrounded by brackets; it builds and returns a **new** list object. 

  - Example
  > ``` python
  > my_list = [10, 20, 30]
  > list_plus_5 = [(i + 5) for i in my_list]
  >
  > print(f'New list contains: {list_plus_5}')   
  > ```

List comprehensions can replace *some* for loops

| Num | Description                                         | For loop                                                                 | Equivalent list comprehension                            | Output of both programs |
|-----|-----------------------------------------------------|-------------------------------------------------------------------------|---------------------------------------------------------|------------------------|
| 1   | Add 10 to every element.                           | my_list = [5, 20, 50]  <br>for i in range(len(my_list)):  <br>my_list[i] += 10  <br>print(my_list) | my_list = [5, 20, 50]  <br>my_list = [(i+10) for i in my_list]  <br>print(my_list) | [15, 30, 60]           |
| 2   | Convert every element to a string.                 | my_list = [5, 20, 50]  <br>for i in range(len(my_list)):  <br>my_list[i] = str(my_list[i])  <br>print(my_list) | my_list = [5, 20, 50]  <br>my_list = [str(i) for i in my_list]  <br>print(my_list) | ['5', '20', '50']      |
| 3   | Convert user input to a list of integers.          | inp = input('Enter numbers:')  <br>my_list = []  <br>for i in inp.split():  <br>my_list.append(int(i))  <br>print(my_list) | inp = input('Enter numbers:')  <br>my_list = [int(i) for i in inp.split()]  <br>print(my_list) | Enter numbers: 7 9 3 <br>[7, 9, 3] |
| 4   | Find the sum of each row in a two-dimensional list. | my_list = [[5, 10, 15], [2, 3, 16], [100]]  <br>sum_list = []  <br>for row in my_list:  <br>sum_list.append(sum(row))  <br>print(sum_list) | my_list = [[5, 10, 15], [2, 3, 16], [100]]  <br>sum_list = [sum(row) for row in my_list]  <br>print(sum_list) | [30, 21, 100]         |
| 5   | Find the sum of the row with the smallest sum in a two-dimensional table. | my_list = [[5, 10, 15], [2, 3, 16], [100]]  <br>sum_list = []  <br>for row in my_list:  <br>sum_list.append(sum(row))  <br>min_row = min(sum_list)  <br>print(min_row) | my_list = [[5, 10, 15], [2, 3, 16], [100]]  <br>min_row = min([sum(row) for row in my_list])  <br>print(min_row) | 21                     |



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
