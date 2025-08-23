# Lesson 05 Loops Notes

These are my notes for Lesson 05 of the Intro to Python course.

## Sections

### 1. Loops

- **Loop**: a program construct that performs the same check, or action, while the expression is true; once the expression is false, the loop ends.
  - Example
  > ``` python
  > count = 1
  > while count <= 3:  # Loop runs while the condition is true
  >     print("Hello") # Loop body
  >     count += 1
  > ```
 
- **iteration**: one complete execution of the loop body.
  - Example
    - Using the same loop above:
      - 1st iteration: count = 1, prints "Hello", increments to 2
      - 2nd iteration: count = 2, prints "Hello", increments to 3
      - 3rd iteration: count = 3, prints "Hello", increments to 4 --> condition is now false, loop stops

### 2. While loops

- **while loop**: repeatedly executes a block of code as long as a given condition evalues to ```True```
  - Example
  > ``` python
  > while condition:
  >   # loop body
  > ```
  
- **loop body**: the indented block if code that runs each time the loop condition is checked and determined to be ```True```
  - Example
  > ``` python
  > count = 0
  > while count < 3:
  >   print("Hello!")  # loop body
  >   count += 1
  > ```
  
- **sentinel value**: a special value used to signal the end of input, or to stop a loop.
  - Example
  > ``` python
  > sentinel = -1
  > num = int(input('Enter a number (-1 to quit): '))
  > while num != sentinel:
  >     print(num)
  >     num = int(input('Enter a number (-1 to quit): '))
  > print('goodbye!')
  > ```
  
- **infinite loop**: a loop that never ends because its conditional always evaluates as ```True``` (or there isn't a condition to stop the loop).

### 3. More while examples

- **docstring**: a special type of string used to document Python functions, classes, or modules; written inside triple quotes (```''' '''```) at the beginning of the function/class/module.

- **randint() function**: part of Python's ```random``` module; returns a random integer within a specified range (inclusive)
  - Example
  > ``` python
  > import random
  >
  > # generate a random number between 1 and 37
  > num = random.randint(1, 37)
  > print(num)
  > ```  

### 4. Counting

- **loop variable**: keeps track of each repetition of a loop; usually changes value each time the loop runs and helps control how many times it is executed.
  - Example
  > ``` python
  > # Iterating N times using a loop variable
  > i = 1
  > while i <= N:
  >   # Loop body statesments go here
  >   i = i + 1
  > ```

📌 Note: it's a common error to forget to include a loop variable update at the end of a loop which causes an *unintended* infinite loop.

**Other forms of counting**

- While loop with loop variable that counts down: 

  > ``` python
  > i = 5
  > while i >= 1:
  >   i = i - 1  # loop body will execute when i = 5, 4, 3, 2, 1 but does NOT execute when it reaches 0
  > ```
  
- Loop variable increased by 2 per iteration

  > ``` python
  > i = 0
  > while i <= 100:
  >   i = i + 2
  > ```

### 5. For loops


### 6. Counting using the range() function


### 7. While vs. for loops


### 8. Nested loops


### 9. Developing programs incrementally


### 10. Break and continue


### 11. Getting both index and value when looping: enumerate()


### References

[Loops - Learn Python](https://www.learnpython.org/en/Loops)

[Chapter 4: Loop - Professional Python Programming](https://pythonbook.org/ch04_loop/notes/loop/)

[Iteration in Python: A Comprehensive Guide](https://coderivers.org/blog/iteration-in-python/)

[Python While Loops](https://www.w3schools.com/python/python_while_loops.asp)

[Sentinel Value And Its Uses in Python](https://www.pythonpool.com/sentinel-value-python/)

[Python Infinite Loop](https://unstop.com/blog/python-infinite-loop)

[Python Docstrings](https://www.geeksforgeeks.org/python/python-docstrings/)

[randint() Function in Python](https://www.geeksforgeeks.org/python/python-randint-function/)

[Python for Loops](https://realpython.com/python-for-loop/)
