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


## IndexError and enumerate()
**Common error**: attempting to access a list with an index that is out of the list's index range
  - Example
    - `my_list[8]` when `my_list`'s indices are 0-7
    - The program will abort execution and display **IndexError**


## Built-in functions supporting list objects

| Function     | Description                                         | Example Code                             | Example Output |
|-------------|-----------------------------------------------------|-----------------------------------------|----------------|
| all(list)    | True if every element in list is True (!= 0), or if the list is empty. | `print(all([1, 2, 3]))`<br>`print(all([0, 1, 2]))` | True<br>False |
| any(list)    | True if any element in the list is True.           | `print(any([0, 2]))`<br>`print(any([0, 0]))`       | True<br>False |
| max(list)    | Get the maximum element in the list.              | `print(max([-3, 5, 25]))`                | 25             |
| min(list)    | Get the minimum element in the list.              | `print(min([-3, 5, 25]))`                | -3             |
| sum(list)    | Get the sum of all elements in the list.          | `print(sum([-3, 5, 25]))`                | 27             |



### 5. List games

### 6. List nesting

**list nesting**: embedding a list within another list
  - Example
  > ``` python
  > my_list = [[5, 6], [50, 60, 70]]
  > ```
  > This creates a list with two elements, each being lists

List nesting allows programmers to create a multi-dimensional data structure
- The simplest would be a two-dimensional table, which could be a tic-tac-toe board or spreadsheet

Multi-dimensional examples
> ``` python
> my_list = [[10, 20], [30, 40]]
> print(f'First nested list: {my_list[0]}')
> print(f'Second nested list: {my_list[1]}')
> print(f'Element 0 of first nested list: {my_list[0][0]}')
> ```
>
> Tic-tac-toe
> ``` python
> tic_tac_toe = [
>    ['X', 'O', 'X'],
>    [' ', 'X', ' '],
>    ['O', 'O', 'X']
> ]
> 
> print(tic_tac_toe[0][0], tic_tac_toe[0][1], tic_tac_toe[0][2])
> print(tic_tac_toe[1][0], tic_tac_toe[1][1], tic_tac_toe[1][2])
> print(tic_tac_toe[2][0], tic_tac_toe[2][1], tic_tac_toe[2][2])
> ```


### 7. List slicing

**slice notation**: used to read multiple elements from a list to create a new list that contains the desired elements
  - Example
  > `my_list[0:2]`
  - This indicates the start and end positions of a range of elements to retrieve
  -  0 is the position of the first element to read
  - 2 is the last element to read
  - All elements between 0 and 2 from my_list are added to the new list
  - However, 2 is *not* added to the new list 

## Common list slicing operations

| Operation                 | Description                                                     | Example code                                | Example output          |
|----------------------------|-----------------------------------------------------------------|---------------------------------------------|-------------------------|
| `my_list[start:end]`       | Get a list from start to end (minus 1).                        | `my_list = [5, 10, 20]`<br>`print(my_list[0:2])` | `[5, 10]`              |
| `my_list[start:end:stride]`| Get a list of every stride element from start to end (minus 1).| `my_list = [5, 10, 20, 40, 80]`<br>`print(my_list[0:5:3])` | `[5, 40]`              |
| `my_list[start:]`          | Get a list from start to end of the list.                      | `my_list = [5, 10, 20, 40, 80]`<br>`print(my_list[2:])` | `[20, 40, 80]`         |
| `my_list[:end]`            | Get a list from beginning of the list to the end (minus 1).    | `my_list = [5, 10, 20, 40, 80]`<br>`print(my_list[:4])` | `[5, 10, 20, 40]`      |
| `my_list[:]`               | Get a copy of the list.                                        | `my_list = [5, 10, 20, 40, 80]`<br>`print(my_list[:])` | `[5, 10, 20, 40, 80]`  |


### 8. Loops modifying lists

- **[:]**: copies a list
  - Example
  > ``` python
  > copy = my_list[:]:
  > ```

Example of modifying a list during iteration
> ``` python
> my_list = [1, 2, 3, 4]
>
> for i in range(len(my_list)):
>   my_list[i] =+ 5
>
> print(my_list)
> > ```
> Output: [5, 5, 5, 5]

**Common error**: adding or removing a list element while iterating over the list.


### 9. List comprehensions

A list comprehension has 3 parts:

1. An **expression component** to evaluate for each element in the iterable object
2. A **loop variable component** to bind the current iteration element
3. An **iterable object component** to iterate over (list, string, tuple, enumerate, etc)

Basic form:
> ``` python
> new_list = [expression for loop_variable_name in iterable]
> ```

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


## Conditional list comprehensions

Basic form:
> ``` python
> new_list = [expression for name in iterable if condition]
> ```

- Using this syntax will *only* add an element to the resulting list *if* the condition is True.

Conditional list comprehension example
> ``` python
> # get a list of integers from user input
> numbers = [int(i) for i in input('Enter numbers:').split()]
>
> # return a list of even numbers
> even_numbers = [i for i in numbers if (i % 2) == 0]
> print(f'Even numbers only: {even_numbers}'
> ```

### 10. Sorting lists

### 11. Command-line arguments

### 12. Additional practice: Engineering examples

### 13. Dictionaries

NOTE: Dictionaries are **mutable**, just like lists. This means they can be *modified in place*.

- **dict type**: the data type that implements a dictionary in Python; dictionaries associate keys with values
  - Example
  > ``` python
  > my_dict = {
  >   'Oliver': 'A+',
  >   'Thomas': '93',
  >    10: 5.0
  > }
  > ```

There are a few different approaches to create a dictionary:

- Using braces `{}` with key-value pairs
  - format: `{key: value, key: value, ...}`
  - Example
  > ``` python
  > {'Oliver': 'A+', 'Colton': 'C+'}
  > ```
  >
  > This creates a dictionary with 2 keys, 'Oliver' and 'Colton', that are associated with the grades 'A+' and 'C+'.

- Using disctionary comprehension
  - Uses a loop inside `{}` to build a new dictionary
  - Similar concept to list comprehension 

- Using the `dict()` built-in function:
  - Multiple ways to use it: 
    - Using keyword arguents
      > ``` python
      > dict(Bob='805-123-4567', John='954-123-4567')
      > ```
    - Using a list of tuple pairs
      > ``` python
      > dict([('Bob', '805-123-4567'), ('John', '954-123-4567')])
      > ```
  - Both examples produce equivalent dictionaries 

## Common dict operations

| Operation          | Description                                                        | Example code                       |
|--------------------|--------------------------------------------------------------------|-------------------------------------|
| `my_dict[key]`     | Indexing operation — retrieves the value associated with `key`.    | `jose_grade = my_dict['Jose']`      |
| `my_dict[key] = value` | Adds an entry if the entry does not exist, else modifies the existing entry. | `my_dict['Jose'] = 'B+'`            |
| `del my_dict[key]` | Deletes the key from a dict.                                       | `del my_dict['Jose']`               |
| `key in my_dict`   | Tests for existence of `key` in `my_dict`.                         | `if 'Jose' in my_dict: # ....`      |


### 14. Dictionary methods

| Dictionary method          | Description                                                                 | Code example                                                                 | Output                                   |
|----------------------------|-----------------------------------------------------------------------------|----------------------------------------------------------------------------|------------------------------------------|
| `my_dict.clear()`          | Removes all items from the dictionary.                                      | ```python my_dict = {'Ahmad': 1, 'Jane': 42}```<br>```my_dict.clear()```<br>```print(my_dict)``` | `{}`                                     |
| `my_dict.get(key, default)`| Reads the value of the key from the dictionary. If the key does not exist, returns default. | ```python my_dict = {'Ahmad': 1, 'Jane': 42}```<br>```print(my_dict.get('Jane', 'N/A'))```<br>```print(my_dict.get('Chad', 'N/A'))``` | `42`<br>`N/A`                            |
| `my_dict1.update(my_dict2)`| Merges dictionary `my_dict1` with another dictionary `my_dict2`. Existing entries are overwritten if the same keys exist. | ```python my_dict = {'Ahmad': 1, 'Jane': 42}```<br>```my_dict.update({'John': 50})```<br>```print(my_dict)``` | `{'Ahmad': 1, 'Jane': 42, 'John': 50}`   |
| `my_dict.pop(key, default)`| Removes and returns the key value from the dictionary. If key does not exist, returns default. | ```python my_dict = {'Ahmad': 1, 'Jane': 42}```<br>```val = my_dict.pop('Ahmad')```<br>```print(my_dict)``` | `{'Jane': 42}`                           |


### 15. Dictionary methods reference

| Method                 | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| `clear()`              | Removes all items from the dictionary.                                      |
| `copy()`               | Returns a shallow copy of the dictionary.                                   |
| `fromkeys(keys, value)`| Returns a new dictionary with specified keys and a default value.           |
| `get(key)`             | Returns the value for the specified key, or `None` if the key does not exist. |
| `items()`              | Returns a view object of the dictionary’s key-value pairs.                  |
| `keys()`               | Returns a view object of the dictionary's keys.                             |
| `pop(key)`             | Removes and returns the value for the specified key.                        |
| `popitem()`            | Removes and returns an arbitrary `(key, value)` pair from the dictionary.   |
| `setdefault(key, value)`| Returns the value of the specified key if it exists, otherwise sets it to the default value. |
| `update(other)`        | Updates the dictionary with key-value pairs from another dictionary or iterable. |
| `values()`             | Returns a view object of the dictionary's values.                           |


### 16. Iterating over a dictionary

Useful methods:

| Method        | Description                                             |
|---------------|---------------------------------------------------------|
| dict.items()  | Returns a view object that yields `(key, value)` tuples. |
| dict.keys()   | Returns a view object that yields dictionary keys.       |
| dict.values() | Returns a view object that yields dictionary values.     |


# Iterating over a Dictionary

## `dict.items()`

> ```python
> num_calories = dict(Coke=90, Coke_zero=0, Pepsi=94)
> for soda, calories in num_calories.items():
>    print(f'{soda}: {calories}')
> ```
> Output:
> 
> Coke: 90
> 
> Coke_zero: 0
> 
> Pepsi: 94

## `dict.keys()`

> ``` python
> num_calories = dict(Coke=90, Coke_zero=0, Pepsi=94)
> for soda in num_calories.keys():
>   print(soda)
> ```
> Output:
>
> Coke
>
> Coke_zero
>
> Pepsi

## `dict.values()`

> ``` python
> num_calories = dict(Coke=90, Coke_zero=0, Pepsi=94)
> for calories in num_calories.values():
>   print(calories)
> ```
>
> Output:
>
> 90
>
> 0
>
> 94





### 17. Dictionary nesting

### 18. Lists and dictionaries practice

### References

[Python Lists](https://www.geeksforgeeks.org/python/python-lists/)
