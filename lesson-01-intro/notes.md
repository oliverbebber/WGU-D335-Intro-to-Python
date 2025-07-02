# Lesson 01 Intro Notes

These are my notes for Lesson 01 of the Intro to Python course.

## Overview

Introduction to programming concepts and Python basics. This lesson covers general programming ideas, Python-specific syntax, and development tools.

## Sections

### 1. Programming (General)

- **Program**: a set of instructions that execute one at a time.
- **Input**: data a program receives, whether from a file, peripheral (keyboard, mouse, touchscreen, etc.), network, or other sources.
  - Example
  ```python
  # Get user input
  name = input("Enter your name: ")
  ```

- **Process**: actions performed on the input, like adding or subtractiong two values.
- **Output**: data a program provides after processing input. Output can be to a file, displayed on a screen, or sent over a network.
  - Example
  ```python
  # Print a greeting
  print("Hello, " + name + "!")
  ```

- **Variables**: a named placeholder that stores data a program can use and modify.
    - Example
      ```python
      # Assign a value to a variable
      age = 25
      name = Oliver

      # Display variables
      print("Name:", name)
      print("Age:", age)
      ```
      
- **Computational thinking**: the process of creating clear, step-by-step instructions to solve a problem.
- **Algorithm**: a logical, ordered sequence of instructions used to solve a problem.


### 2. Programming Using Python

- **Python interpreter**: a program that reads and runs Python code. It translates code into actions the computer can perform.
- **Interactive interpreter**: a tool that allows you to type and run small pieces of Python code quickly, one line at a time.
- **Code**: the written text of a program - instructions written in a programming language such as Python.
- **Line**: a single row of code or text in a program.
- **Prompt**: the prompt within an ineractive interpreter is displayed as ```>>>```, and means Python is ready to accept user input.
- **Statement**: a single instruction within a program. Programs typically are made up of multiple statements, each written on its own line.
- **Expressions**: a piece of code that caluclates and returns a value.
  - Example
  ```python
  # Define variables: wage, hours, and weeks
  wage = 20
  hours = 40
  weeks = 52

  # Expression to calculate yearly salary
  salary = (wage * hours * weeks)
  ```
  
- **Assignment**: the ```=``` symbol assigns a value to a variable.
- **```print()``` function**: used to display information as output.
  - Example
  ```python
  # Display yearly salary
  print(salary)
  ```
  
- **Comments**: programmers can leave helpful notes that start with ```#``` within their code to explain what pieces of the program does. These are beneficial for others and for the programmer who wrote the code. Information starting with the ```#``` is ignored by Python.


### 3. Basic Input and Output

- **String**: a sequence of characters enclosed in quotes. Strings can include letters, numbers, spaces, **and** symbols.
  - Example
  ```python
  "Hello, world!"
  ```

Note: a single output line can include multiple strings and variables. These are separated by commas in the ```print()``` function and automatically have a space character between them.

> Example
>  ```python
>  wage = 160
>
>  # Display daily wage
>  print('Your daily wage is $', wage)
>
>  weekly_wage = 800
>
>  # Display daily wage and weekly wage
>  print('$', wage, 'per day is $', weekly_wage, 'per week')
>  ```

By default, every ```print()``` function outputs on a new line; however, to continue printing on the same line, you can use ```end=' '```. This adds a single space instead of moving to the next line.
> Example
> ```python
> # Including end=' ' keeps output on the same line
> print('Hello there.', end=' ')
> print('My name is...', end=' ')
> print('Oliver.')

- **Escape sequence**: a combination of characters used inside a string that starts with a backslash {```\```) which tells Python to do something special - like add a line break, tab, or a special symbol.
  - ```\n```: moves text to a new line
  - ```\t```: indent text horizontally
  - ```\\```: prints a backslash
  
  
- **Newline character (```\n```)**: a specific type of escape sequence that moves the output onto the next line. Commonly used in strings to format output across multiple lines.
  - Example
   ```python
   print("Line1\nLine2\nLine3")

   # Output:
   # Line 1
   # Line 2
   # Line 3
   ```
  
- **Whitespace**: Any space, tab, or newline character; often used to separate words and format code clearly.
- **```input()``` function**: a built-in Python function that pauses the program to accept user input. It returns the input as a string.
  - Example
  ```python
  name = input("Enter your name: ")
  print("Hello, " + name)
  ```
  
- **Type**: the kind of data a value represents.
 
  ```int```: integer (whole number; ex: ... -100, -1, 0, 1, 100, ...)

  ```float```: decimal number
  
  ```str```: string of characters
 
- **```int()``` function**: a built-in Python function that converts a string or number into an integer
- **Whole numbers**: numbers **without** fractions or decimals; includes 0 and all **positive** integers.
- **Integers**: numbers that include all whole numbers, plus their negative counterparts


### 4. Errors

- **SyntaxError**: occurs when the code breaks the rules of the programming language and usually the result of something being written incorrectly. Python will not understand the instruction, so it won't run the program.
  - Examples:
    - Missing parentheses
    - Misspelled keywords
    - Incorrect indentation
    - Incorrect symbols (```( )``` instead of ```{ }```)
    - Using multiple ```print()``` functions on the same line without proper formatting
   
    ```python
    print('My name is Oliver") # Syntax error caused by mismatching quotes (single vs double)
    ```

Note: Executing code frequently is a best practice that is helpful to avoid continually hitting error messages. 

> For beginners:
> 
> Write 3-5 lines at a time before executing to determine if there are any errors needing resolution before moving onto the next part of the program.

- **Runtime error**: occurs after the code is executed, usually because the program attempts to do something that is impossible - such as dividing by zero or using a variable that has not been defined.
  - Example
    ```python
    x = 10
    y = 0

    # Divide by zero
    print(x / y) # RuntimeError: division by zero
    ```
    
- **IndentationError**: occurs when lines of code are not properly indented. Indentation is critical in Python as it defines the structure of the code (especially in blocks like ```if```, ```for```, ```while```, etc.).
  - Example
    > ```python
    > def greeting():
    > print("Hello, world!") # IndentationError: expected an indented block
    > ```
    >
    > ```python
    > def greeting():
    >   print("Hello, world!") # Correctly indented
    > ```
    >
    > IndentationErrors can occur whether the indentation is missing or simply inconsistent.


- **ValueError**: occurs when you attempt to use the correct type of data but the value doesn't make sense for the operation you're trying to perform.
  - Example
    > ```python
    > # Attempting to convert a non-numeric string to an integer
    > age = int("twenty-five") # ValueError: invalid literal for int() with base 10
    > ```
    >
    > ```python
    > import math
    > # Asking for the square root of a negative number
    > print(math.sqrt(-1)) # ValueError: math domain error
    > ```

- **NameError**: occurs when Python cannot recognize a name because it has not been defined in the current program. This is usually because you have forgotten to define it, made a typo, or used it before assigning it to a variable.
  - Example
    > ```python
    > print(age) # NameError: name 'age' is not defined
    > ```
    >
    > ```python
    > username = "Oliver"
    > print(usernme) # NameError: name 'usernme' is not defined
    > ```
    >
    > Pay special attention to the error messages as these will assist you in resolving the problem that caused the error.


- **TypeError**: occurs when an operation is performed on a value of the wrong data type.
  - Example
    > ```python
    > import math
    > print(math.pi(-1)) # TypeError: 'float' object is not callable
    > ```
    >
    > This error occurs due to math.pi being a float constant (3.14159...) vs a function.
    >
    > ```python
    > age = 25
    > print("You are " + age) # TypeError: can only concatenate str (not "int") to str
    > ```
    >
    > The resolution:
    > ```python
    > print*"You are " + str(age)) # Converts int to str before combining
    > ```

- **Crash**: when a program abruptly and unintentionally gets terminated.
- **Logic error**: occurs when a program runs without any syntax or runtime errors, but it produces the wrong result because the code doesn't follow the correct steps to solve the problem; aka bug.
  - Example
    > ```python
    > price = 100
    > tax_rate = 0.0925
    > total = price - (price * tax_rate) # Logic error: subtracting tax instead of adding
    >
    > print(total)
    > ```
    >
    > The resolution:
    > ```python
    > total = price + (price * tax_rate)
    > ```
    >
    > ```python
    > current_salary = int(input('Enter current salary: '))
    >
    > raise_percentage = 10 # Logic error gives a 1000% raise instead of 10%
    > new_salary = current_salary + (current_salary * raise_percentage)
    > print('New salary:', new_salary)
    > ```


