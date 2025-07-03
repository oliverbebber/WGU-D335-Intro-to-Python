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


### 5. Set basics


### 6. Dictionary basics


### 7. Common data types summary


### 8. Grade calculator: Average score on three exams


### 9. Type conversions


### 10. Binary numbers


### 11. String formatting



## References

[Python Docs: Text Sequence Type - str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
