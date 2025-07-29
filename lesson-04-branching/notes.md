# Lesson 04 Branching Notes

These are my notes for Lesson 04 of the Intro to Python course.

## Sections

### 1. If-else branches (general)

- **Branch**: part of a program that executes only if a certain condition is met.  
- **if branch**: a branch that runs **only** when a specific condition evaluates to ```True```.
  - Remember to use a colon after the ```if``` statement
  - Example
  > ```python
  > if age > 21:
  >   print("Drinks can be served")
  > ```
- **if-else branch**: a decision structure with **two** branches.
  - The ```if``` branch runs if the condition is ```True```.
  - The ```else``` branch runs if the condition is ```False```.
  - Example
  > ```python
  > if age > 21:
  >   print("Drinks can be served")
  > else:
  >   print("Sorry, you are not old enough to drink")
  > ```

### 2. Detecting equal values with branches

- **if statement**: executes a group of statements *only if* a condition is ```True```.
  - Statements within the ```if``` block must be indented (typically using 4 spaces)
- **equality operator (==)**: checks if two values are equal.
  - Returns ```True``` if the values are the same, otherwise returns ```False```.
  - Example
  > ```python
  > if cat == "Phoenix":
  >   print("You found my cat, Phoenix!")
  > ```
- **inequality operator (!=)**: checks if two values are *not* equal.
  - Returns ```True``` if the values are different
  - Example
  > ```python
  > if cat != "Phoenix":
  >   print("This is not my cat.")
  > ```
- **Boolean**: a data type that represents 2 values: ```True``` or ```False```.
  - Used to control the flow of programs through conditions
- **elif keyword**: short for "else if".
  - Used to check *multiple* conditions in sequence.
    - The first condition that is ```True``` will run; all others are skipped.
    - If none are ```True```, the optional ```else``` block will run.
  - Example
  > ```python
  > if cat == "Phoenix":
  >   print("You found Phe!")
  > elif cat == "Whiskers":
  >   print("That's my neighbor's cat.)
  > elif cat == "Sparky":
  >   print("That's a stray that is taken care of by a lady down the street.")
  > else:
  >   print("I don't recognize this cat.")
  > ```

### 3. Detecting ranges with branches (general)


### 4. Detecting ranges with branches


### 5. Detecting ranges using logical operators


### 6. Detecting ranges with gaps


### 7. Detecting multiple features with branches


### 8. Comparing data types and common errors


### 9. Membership and identity operators


### 10. Order of evaluation


### 11. Code blocks and indentation


### 12. Conditional expressions


## References

[Chapter 3: Branch - Professional Python Programming](https://pythonbook.org/ch03_branch/notes/branch/)

[Branching: Learn If, Else, and Elif in Python - Raspberry Pi Official Magazine](https://magazine.raspberrypi.com/articles/branching-if-else-python)

[Python If Else](https://www.w3schools.com/python/gloss_python_else.asp)

[4. More Control Flow Tools - Python 3.13.5 documentation](https://docs.python.org/3/tutorial/controlflow.html)

[If Statements Explained - Python Tutorial](https://pythonbasics.org/if-statements/)

[Python Comparison Operators](https://www.w3schools.com/python/gloss_python_comparison_operators.asp)

[Python Booleans](https://www.w3schools.com/python/python_booleans.asp)
