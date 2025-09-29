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

**Shorthand operators**

| Operator | Meaning                         | Example           | Equivalent To       |
|----------|---------------------------------|-------------------|---------------------|
| +=       | Add and assign                  | x += 5            | x = x + 5           |
| -=       | Subtract and assign             | x -= 3            | x = x - 3           |
| *=       | Multiply and assign             | x *= 2            | x = x * 2           |
| /=       | Divide and assign (float)       | x /= 4            | x = x / 4           |
| //=      | Floor divide and assign         | x //= 4           | x = x // 4          |
| %=       | Modulo and assign               | x %= 2            | x = x % 2           |
| **=      | Exponent and assign             | x **= 3           | x = x ** 3          |


### 5. For loops

- **for loop**: each item in a sequence is processed in order. The loop will temporarily assign each item to a variable, which is then available for use within the loop body
  - Example
  > ``` python
  > numbers = [2, 4, 6, 8]
  > 
  > for num in numbers:  # num is the variable, numbers is the container
  >   # Loop body: goes through each item in numbers
  >   print(f'The square of {num} is {num ** 2}'}
  >
  > # Statements to execute after the for loop is complete
  > print('Done looping!')
  > ```


### 6. Counting using the range() function

- **range() function**: allows counting in *for* loops; creates a sequence of integers between a starting integer that's included within the range, an ending integer that isn't included in the range, and an integer step value. 

| Range            | Generated sequence | Explanation                   |
|------------------|--------------------|-------------------------------|
| `range(5)`       | 0 1 2 3 4          | Every integer from 0 to 4     |
| `range(0, 5)`    | 0 1 2 3 4          | Every integer from 0 to 4     |
| `range(3, 7)`    | 3 4 5 6            | Every integer from 3 to 6     |
| `range(10, 13)`  | 10 11 12           | Every integer from 10 to 12   |
| `range(0, 5, 1)` | 0 1 2 3 4          | Every 1 integer from 0 to 4   |
| `range(0, 5, 2)` | 0 2 4              | Every 2nd integer from 0 to 4 |
| `range(5, 0, -1)`| 5 4 3 2 1          | Every 1 integer from 5 to 1   |
| `range(5, 0, -2)`| 5 3 1              | Every 2nd integer from 5 to 1 |




### 7. While vs. for loops







### 8. Nested loops

- **Nested loop**: a loop that exists within another loop; often used when working with multi-dimensional data or repeating a set of actions multiple times for each iteration of an outer loop
- **Outer loop**: the loop that contains the nested (*inner*) loop
- **Inner loop**: the loop that is nested inside the outer loop
  - Example
  > ```python
  > for i in range(3):         # outer loop
  >     for j in range(2):     # inner loop
  >         print(i, j)
  > ```
  > - The **outer loop** iterates over `i`  
  > - For each iteration of `i`, the **inner loop** iterates over `j`



NOTE: Nested loops are tricky because it feels like the outer loop does something, but it *only controls how many times the inner loop runs*. Track the inner loop as this is what increments the counter. 

> ``` python
> count = 0
> for i in range(5):        # outer loop; i = 0, 1, 2, 3, 4
>   for j in range(4, 8):   # inner loop; j = 4, 5, 6, 7
>     count += 1            # increment count each time inner loop runs
> print(count)	
> ```
> 1. Outer loop (i):
>   - Iterates **5** times --> 0, 1, 2, 3, 4
> 2. Inner loop (j):
>   - Iterates **4** times --> 4, 5, 6, 7; stops at 7 as 8 is not inclusive as range(start, stop) includes the start number but NOT the stop number
>   - `count += 1` occurs here, increasing the count each time
> 4. Count iterations:
>   - Outer x inner = 5 * 4 = 20 --> final `count` = 20


## Trace Table

I felt using a trace table helped me grasp this concept best.

> ``` python
> count = 0
> for i in range(5):                              # outer loop; i = 0, 1, 2, 3, 4
>   for j in range(4, 8):                         # inner loop; j = 4, 5, 6, 7
>     count += 1                                  # increment count each time inner loop runs
>         print(f"i={i}, j={j}, count={count}")   # Trace output
>
> print("Final count:", count)
> ```
> | i | j | count |
> |---|---|-------|
> | i=0 | j=4 | count=1     |
> | i=0 | j=5 | count=2     |
> | i=0 | j=6 | count=3     |
> | i=0 | j=7 | count=4     |
> | i=1 | j=4 | count=5     |
> | i=1 | j=5 | count=6     |
> | i=1 | j=6 | count=7     |
> | i=1 | j=7 | count=8     |
> | i=2 | j=4 | count=9     |
> | i=2 | j=5 | count=10    |
> | i=2 | j=6 | count=11    |
> | i=2 | j=7 | count=12    |
> | i=3 | j=4 | count=13    |
> | i=3 | j=5 | count=14    |
> | i=3 | j=6 | count=15    |
> | i=3 | j=7 | count=16    |
> | i=4 | j=4 | count=17    |
> | i=4 | j=5 | count=18    |
> | i=4 | j=6 | count=19    |
> | i=4 | j=7 | count=20    |
> **Final count:** 20




### 9. Developing programs incrementally


### 10. Break and continue


### 11. Getting both index and value when looping: enumerate()

- **enumerate() function**: gets both the index and corresponding element value at the same time
  - Example
  > ``` python
  > # using range() & len() to iterate over a seq
  > origins = [4, 8, 10]
  >
  > for index in range(len(origins)):
  >     value = origins[index]      # Retrieve value of element in list.
  > print(f'Element {index}: {value}')
  > ```
  > This generates a position index but requires additional code to get the value
  >
  > ``` python
  > # using list.index() to find the index of each element
  > origins = [4, 8, 10]
  >
  > for value in origins:
  >   index = origins.index(value)  # Retrieve index of value in list
  >   print(f'Element {index}: {value}')
  > ```
  > The for loop interates over a container and obtains the value directly, but it must look up the index using a function call
  >
  > ``` python
  > # using enumerate()
  > origins = [4, 8, 10]
  >
  > for (index, value) in enumerate(origins):
  >   print(f'Element {index}: {value}')
  > ```
  > This provides a much cleaner and easier to read solution
  > The enumerate() function produces a new tuple each time it passes through the loop. The new tuple contains the current index and the element value.
  
- **Unpacking**: a process that performs multiple assignments at one time; binds comma separated values on the left to the elements of a seq on the right
  - Example
  > ``` python
  > num1, num2 = [350, 400]
  > # the above is equivalent to the following:
  > num1 = 350
  > num2 = 400
  > ```


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

[Python Operators](https://www.w3schools.com/python/python_operators.asp)

[Python range() Function: How-To Tutorial With Examples](https://python.land/deep-dives/python-range)

<!-- 5.7 --> 

<!-- 5.8 -->
[Python Nested Loops](https://www.geeksforgeeks.org/python/python-nested-loops/)

[Nested Loops in Python - Real Python](https://realpython.com/nested-loops-python/)

[trace - Trace or track Python statement execution - Python 3.13.7 documentation](https://docs.python.org/3/library/trace.html)

<!-- 5.9 -->

<!-- 5.10 -->

<!-- 5.11 -->
[Enumerate() in Python](https://www.geeksforgeeks.org/python/enumerate-in-python/)

[Enumerate Explained with Examples](https://pythonbasics.org/enumerate/)
