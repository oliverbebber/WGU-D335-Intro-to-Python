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

- **relational operator**: compares two values or expressions and returns a Boolean result (```True``` or ```False```)

Common Relational Operators in Python

| Operator | Meaning                | Example   | Result |
|----------|------------------------|-----------|--------|
| `<`      | Less than              | `3 < 5`   | `True` |
| `<=`     | Less than or equal to  | `3 <= 3`  | `True` |
| `>`      | Greater than           | `10 > 7`  | `True` |
| `>=`     | Greater than or equal  | `8 >= 9`  | `False`|
| `==`     | Equal to               | `4 == 4`  | `True` |
| `!=`     | Not equal to           | `6 != 2`  | `True` |

- **operator chaining**: allows linking multiple relational comparisons in a single expression.
  - Python will evaluate these from left to right and **all** conditions must be ```True``` for the entire expression to be ```True```.

### 5. Detecting ranges using logical operators

- **logical operator**: treats operands as being `True` or `False`, and evaluates to a `True` or `False` result. Logical operators are used to combine or modify boolean expressions.

  **Common logical operators:**

  | Expression | Description                                       |
  |------------|---------------------------------------------------|
  | `a AND b`  | Logical AND: True when **both** operands are True |
  | `a OR b`   | Logical OR: True when **at least one** is True    |
  | `NOT a`    | Logical NOT: True when operand is **False**       |

  - Example
  > ```python
  > cat_seen_today = True
  >   cat_looks_like_phe = False
  >
  >   if cat_seen_today and cat_looks_like_phe:
  >     print("Possible Phoenix sighting!")
  >   else:
  >     print("No match today.")
  > ```

  ### Detecting Ranges Implicitly vs. Explicitly

  When writing conditionals that check if a value falls within a specific range, programmers can explicitly or implicitly detect the range.

  - **Explicit ranges**: uses logical operators (```and```, ```or```, ```<```, ```<=```, etc.) to state each end of the range.
    - Example
    > ``` python
    > if x < 0:
    >   # Negative
    > elif (x >= 0) and (x <= 10):  # x >= 0 is implicit
    >   # 0 through 10
    > elif (x >= 11) and (x <= 20):
    >   # 11 through 20
    > else:
    >   # 21 and above
    > ```
    
  - **Implicit ranges**: relies on the structure of the conditional branches to define boundaries. In a multi-branch ```if-elif-else``` chain, the lower end of a range is implied if the previous conditions weren't met.
    - Example
    > ``` python
    > if x < 0:
    >   # Negative
    > elif (x <= 10):
    >   # 0 through 10
    > elif (x <= 20):
    >   # 11 through 20)
    > else:
    >   # 21 and above
    > ```

### 6. Detecting ranges with gaps

- **See activities & challenges sections**

### 7. Detecting multiple features with branches

- **See activities & challenges sections**

### 8. Comparing data types and common errors

Python uses different rules to compare values, depending on the data types.

- **Numbers**: if both values are numbers, they are compared using standard arthimetic rules
  - Example
  > ``` python
  > 5 < 2  # False
  > ```

- **Strings**: compared by converting each character to a numeric value (ASCII or unicode) before comparing each character in order
  - Example
  > ``` python
  > 'abc' >= 'ABCDEF'
  > ```
    - Most string comparisons use **equality operators** (`==` or `!=`)
      - Example: `today == 'Friday'`

- **Lists and Tuples**: compared by evaluating each element, in order.
  - Using equality (`==`), each element *must* match
    - For relational operators (`<`, `>`, etc.):
      - Comparisons stop at the *first* mismatching element.
  - Example
  > ``` python
  > x = [1, 5, 2]
  > y = [1, 4, 3]
  > print(x < y)  # 5 < 4 is False
  > ```

- **Dictionaries**: can only be compared using `==` or `!=`
  - Two dictionaries are *if* they have the same set of keys **and** the same value for each key

- **Type mismatch**: comparisons that make **no sense**, like comparing a number to a string (`1 < 'abc'`), will result in a **TypeError**


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

[Python Relational Operators](https://pythonexamples.org/python-relational-operators/)

[Chaining comparison operators in Python](https://www.geeksforgeeks.org/python/chaining-comparison-operators-python/)

[Python Logical Operators](https://www.w3schools.com/python/gloss_python_logical_operators.asp)
