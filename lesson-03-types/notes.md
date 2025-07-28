# Lesson 03 Types Notes

These are my notes for Lesson 03 of the Intro to Python course.

## Sections

### 1. Introduction


### 2. String basics

- **String**: a sequence of characters used to represent text (names, sentences, labels, etc.); can be created from user input or written directly into the program.
  - Strings **can** include numbers, letters, symbols, and spaces.
- **String literal**: text that is **hard-coded** into the program using quotes (single or double)
  - Example
  > ```'Mary'```, ```"Hello!"```
  
- **Sequence type**: a string that stores a collection of items in a specific order: from first to last.
  - Each character has a **position** (called an **index**).
  - You can **access, slice, and iterate** over the characters using that order.

### 3. List basics

- **Container**: a data structure that holds & organizes multiple elements, allowing easy storage and retrieval
- **List**: a mutable, ordered collection of items that can hold elements of various data types
- **Element**: an individual item stored within a list
- **Index**: an integer that specifies the position of an element inside a list
- **Method**: a function that belongs to an object and performs an action on that object; use a method by typing the object name ```.``` method name.
  - **append() function**: adds a new element to the end of a list
    - Example
    > ```python
    > my_list = [1, 2, 3]
    > my_list.append(4)
    >
    > # my_list = [1, 2, 3, 4]
    > ```
  - **pop() function**: removes and returns the last item in the list (or item at a specified index)
    - Example
    > ```python
    > my_list.pop()    # Removes the last item (4)
    > my_list.pop(0)   # Removes the item at index 0 (1)
    > ```
  - **remove() function**: removes the first matching value from the list
    - Example
    > ```python
    > my_list.remove(2)  # Removes the first occurrence of 2 (originally my_list[1])
    > ```

📌 Updating an element in a list
> Assume the list cat_weights = [9.3, 10.1, 5.7]
> 
> Update the second item in cat_weights to 10.4
> ```python
> cat_weights[1]=10.4
> ```

- ** Sequence-type methods**: functions built into sequence objects, like strings or lists.
  - Methods can be called using **dot notation** to perform the action on the object.
  - These methods typically **change** the object or **return info** about it.
    - Examples
    > ```python
    > my_list.append()
    > my_list.pop()
    > my_list.remove()
    > ```
  
- **Sequence-type functions**: built-in functions that work with sequence types (like strings, lists, or tuples)
  - Not attached to any specific object, so no dot ( ```.``` ) is needed.
  - These functions take a **sequence** as an argument.
    - Examples
    > ```python
    > len()
    > sorted()
    > 
    > my_list = [1, 2, 3]
    > print(len(my_list))   # Function returns the length of the list
    > ```
    
Useful Functions and Methods Related to Lists
> ```python
> len(list)         # finds length of the list
> list1 + list2     # produces a new list by concatenating list2 to the end of list1
> min(list)         # finds the smallest value in the list; all elements must be the same type
> max(list)         # finds the largest value in the list; all element must be the same type
> sum(list)         # finds the sum of all elements in the list (only numbers)
> list.index(val)   # finds the index of the first element in the list whose value matches val
> list.count(val)   # counts the number of occurrences of the value val in the list
> ```


📌 Finding the average
> ```python
> avg = sum(list)/len(list)
> ```


### 4. Tuple basics

- **Tuple**: stores a collection of items, similar to a list, but tuples are **immutable** - their values **cannot** change after creation.
  - Tuples are typically surrounded by parentheses.
    - Example
    > ```python
    > wh_coordinates = (38.8977, 77.0366)
    > print(f'Coordinates: {wh_coordinates}')
    > print(f'Tuple length: {len(wh_coordinates)}')
    > 
    > # Access tuples via index
    > print(f'\nLatitude: {wh_coordinates[0]} north')
    > print(f'Longitude: {wh_coordinates[1]} west\n')
    > 
    > # Error. Tuples are immutable
    > wh_coordinates[1] = 50
    > ```
    >
    > ```python
    > # Create a new variable that is a tuple containing two strings
    > new_var = ('first string', 'second string')
    >
    > # Display length of new_var
    > len(new_var) # Outputs 2
    > ```
- **Named Tuple**: similar to a regular tuple, but with **named fields**. Makes the data more readable and easier to access by name rather than by index.
  - These tuples are **immutable** and allow you to access elements using dot notation, like accessing attributes of an object.
  - namedtuple() does not create new data objects, it just creates the new, simple data type.
  - The container ```namedtiple``` must be imported to create a new named tuple, then it can be created.
    - Example
    > ```python
    > from collections import namedtuple
    >
    > # Define a named tuple called 'Cat' with fields for name, age, and breed
    > Cat = namedtuple('Cat', ['name', 'age', 'breed', 'weight'])
    >
    > # Create instances of Cat
    > cat_1 = Cat('Dallas', 11, 'DSH Tabby', 10.2)
    > cat_2 = Cat('Phoenix', 6, 'DSH Tabby', 10.1)
    > cat_3 = Cat('Miso', 3, 'DSH Tabby', 8.8)
    >
    > cats = [cat_1, cat_2. cat_3]
    >
    > # Access individual fields
    > print(cat_1.name)   # Outputs: Dallas
    > print(cat_1.age)    # Outputs: 11
    >
    > # Print the full named tuple
    > print(cat_1)  # Outputs: Cat(name='Dallas', age=11, breed='DSH Tabby')
    > print(cat_2)  # Outputs: Cat(name='Phoenix', age=6, breed='DSH Tabby')
    > print(cat_3)  # Outputs: Cat(name='Miso', age=3, breed='DSH Tabby')
    >
    > # Compute the total weight of all cats
    > total_weight = cat_1.weight + cat_2.weight + cat_3.weight
    >
    > # Display the result
    > print(f'Total weight of my cats: {total_weight} lbs')  # Outputs: Total weight of my cats: 29.1 lbs
    > ```
    >
    > ```cat_1```, ```cat_2```, and ```cat_3``` are instances of a ```Cat``` named tuple.
    > ```.weight``` allows us to access the age field of each tuple.
    > The sum is stored in ```total_weight``` and printed.


### 5. Set basics

- **Set**: a collection of elements where each element is unique and the order does not matter.
  - Sets do **not** support indexing or slicing because of the elements being unordered.
    - Example
    > ```python
    > my_set = {1, 2, 3, 3, 2}
    > print(my_set)  # Outputs: {1, 2, 3} - duplicates removed
    > ```
- **set() function**: a built-in Python function used to create a set.
  - It can convert other iterable types (lists or strings) into a set, removing duplicates automatically
    - Example
    > ```python
    > # From a list
    > numbers = [1, 2, 2, 3, 4, 4]
    > unique_nums = set(numbers)
    > print(unique_nums)  # Outputs: {1, 2, 3, 4}
    >
    > # From a string
    > letters = set("banana")
    > print(letters)  # Outputs: {'a', 'n', 'b'}
    > ```
- **Set literal**: a way to create a set using curly braces ```{}``` with comma-separated values (CSV) inside.
  - An empty set **cannot** be created this way, because it creates an empty dictionary instead.
    - To create an empty set, use ```set()```
      - Example
      > ```python
      > colors = {'red', 'blue', 'green'}
      > print(colors)  # Outputs: {'green', 'red', 'blue'}
      >
      > # Creating an empty set
      > empty_set = set()
      > print(type(empty_set))  # Outputs: <class 'set'>
      >
      > # Using {} by itself, creating a dictionary vs a set
      > not_a_set = {}
      > print(type(not_a_set))  # Outputs: <class 'dict'>
      > ```

  ### Modifying Sets

  - **add() method**: adds a single new element to a set.
    - If an element already exists, nothing happens.
      - Example
      > ```python
      > fruits = {'apple', 'banana'}
      > fruits.add('orange')
      > print(fruits)  # Outputs: {'apple', 'banana', 'orange'}
      > ```
  - **remove() method**: removes a specific element from a set.
    - Raises a ```KeyError``` if the element is not found.
      - Example
      > ```python
      > numbers = {1, 2, 3}
      > numbers.remove(2)
      > print(numbers)  # Output: {1, 3}
      > ```
  - **pop() method**: removes and returns a random element from the set.
    - Raises a ```KeyError``` if the set is empty.
      - Example
      > ```python
      > colors = {'red', 'green', 'bluee'}
      > removed_color = colors.pop()
      > print(removed_color)  # Outputs: could be 'red', 'green', or 'blue'
      > print(colors)   # The set now contains the original colors, minus the color that was removed 
      > ```
  - **clear() method**: removes all elements from a set, leaving it empty - the length will be 0 after using.
    - Example
    > ```python
    > cats = {'Phoenix', 'Dallas', 'Leo'}
    > cats.clear()
    > print(cats)  # Outputs: set()
    > ```
  - **update() method**: adds the elements from another set, list, or tuple, to the current set.
    - Duplicate values are ignored.
    - Example
    > ```python
    > colors = {'red', 'green'}
    > new_colors = ['blue', 'yellow']
    > colors.update(new_colors)
    > print(colors)  # Outputs: {'red', 'yellow', 'blue', 'green'}
    > ```
  - **len(set) function**: returns the number of elements within a specific set.
    - Example
    > ```python
    > cats = {'Phoenix', 'Dallas', 'Leo'}
    > print(len(cats))  # Outputs: 3
    > ```

  ### Set Operations

  - **set.intersection() method**: returns a new set with elements common between all sets (can be two or more sets)
    - Example
    > ```python
    > a = {1, 2, 3, 4}
    > b = {3, 4, 5. 6}
    >
    > common = a.intersection(b)
    > print(common)  # Outputs: {3, 4}
    > ```
  - **set.union() method**: returns a new set with all elements from each set (duplicates are removed)
    - Example
    > ```python
    > a = {1, 2, 3, 4, 5}
    > b = {3, 4, 5}
    > united = a.union(b)
    > print(united)  # Outputs: {1, 2, 3, 4, 5}
    > ```
  - **set.difference() method**: returns a new set containing elements in each the set being compared that are **not** in any other the other sets
    - Example
    > ```python
    > a = {1, 2, 3, 4, 5}
    > b = {3, 4}
    > c = {5, 6}
    > result = a.difference(b, c)
    > print(result)  # Outputs: {1, 2}
    > ```
  - **set.symmetric_difference() method**: returns a set containing elements from the sets compared
    - Example
    > ```python
    > a = {1, 2, 3}
    > b = {3, 4, 5}
    > sym_diff = a.symmetric_difference(b)
    > print(sym_diff)  # Outputs: {1, 2, 4, 5}
    > ```

### 6. Dictionary basics

- **Dictionary**: a Python container used to represent associative relationships by linking keys to pairs.
  - Dictionary items **can** be removed after creating the dictionary, however, two keys **cannot** share the same name.
  - Example
  > ```python
  > animal_sounds = {
  >   "cat": "meow",
  >   "dog": "bark",
  >   "cow": "moo"
  > }
  > ```
- **Dict object type**: the specific object type Python uses to create dictionaries.
  - Example
  > ``` python
  > print(type(animal_sounds))  # Outputs: <class 'dict'>
  > ```
- **Key**: used to uniquely identify a value in a dictionary.
- **Value**: the data used to describe a given key in a dictionary.
  - Example
    In the animal_sounds dictionary, ```{"cat": "meow"}```
    - ```cat``` is the key
    - ```meow``` is the value

### 7. Common data types summary


### 8. Grade calculator: Average score on three exams


### 9. Type conversions


### 10. Binary numbers


### 11. String formatting



## References

[Python Docs: Text Sequence Type - str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)

[Python Docs: collections - Container datatypes](https://docs.python.org/3/library/collections.html)

[set() Function in python](https://www.geeksforgeeks.org/python/python-set-function/)

[Python Sets](https://www.geeksforgeeks.org/python/python-sets/)

[Python Set add() Method](https://www.w3schools.com/python/ref_set_add.asp)

[Python Set remove() Method]([https://www.w3schools.com/python/ref_list_remove.asp](https://www.w3schools.com/PYTHON/ref_set_remove.asp))

[Python Set pop() Method](https://www.geeksforgeeks.org/python/python-set-pop-method/)

[Find the length of a set in Python](https://www.geeksforgeeks.org/python/find-the-length-of-a-set-in-python/)

[Python Set intersection() method](https://www.w3schools.com/python/ref_set_intersection.asp)

[Python Set union() method](https://www.w3schools.com/python/ref_set_union.asp)

[Python Set difference() method](https://www.w3schools.com/python/ref_set_difference.asp)

[Python Set symmetric_difference() method](https://www.w3schools.com/python/ref_set_symmetric_difference.asp)

[Python Dictionaries](https://www.w3schools.com/python/python_dictionaries.asp)

[Python Dictionary keys() method](https://www.geeksforgeeks.org/python/python-dictionary-keys-method/)
