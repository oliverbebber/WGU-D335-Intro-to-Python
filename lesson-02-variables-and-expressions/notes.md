# Lesson 02 Variables and Expressions Notes

These are my notes for Lesson 02 of the Intro to Python course.

## Sections

### 1. Variables and Expressions

- **Variable**: a named placeholder that stores data a program can use and modify.
  - Examples
    ```python
    x = 3
    num_cats = 7
    ```

- **Assignment statement**: stores a value in a variable by using the ```=``` symbol.
  - Python evaluates the **expression on the right** and stores the result in the **variable on the left**.
 

📌 ```=``` is **not** equals
> Do not think of it in terms of math.
> ```python
> x = 3
> ```
> This is read as "x is assigned with 3."

  
- **Incrementing**: increasing a variable's value by 1; common operation used in loops or counters.
  - Example
      ```python
      x = 5
      x = x + 1
      ```
      - x is now 6

### 2. Identifiers

- **Identifier** aka **name**: the name given to variables, functions, or classes within code.
  - Names must follow these rules:
    - Must start with a letter or an underscore - not a number.
    - Can only include letters (**a-z, A-Z**), digits (**0-9**), and underscores ( **_** )
    - Cannot be the same as a Python **keyword**
  - Examples
  > Valid identifiers
  > ```python
  > first_name
  > _temp
  > street_address1
  > street_address2
  > state
  > zip_code
  > ```
  >
  > Invalid identifiers
  > ```python
  > 2name  # Starts with a digit
  > last-name  # Contains a hyphen
  > class  # Reserved word (keyword) in Python
  > ```

- **Reserved words** aka **keywords**: special words built into the Python language that hold specific meaning and purpose.
  - Cannot be used as variable or function names
  - Python 3 reserved words:
  > ```python
  > if
  > else
  > while
  > for
  > def
  > return
  > class
  > True
  > False
  > None
  > assert
  > as
  > async
  > await
  > except
  > import
  > pass
  > raise
  > in
  > is
  > return
  > try
  > lambda
  > nonlocal
  > with
  > yield
  > or
  > not
  > elif
  > del
  > continue
  > break
  > and
  > finally
  > for
  > from
  > global
  > ```
  > 📌 Some of these keywords are valid identifiers if the first letter is either capitalized or lowercase. 

- **PEP 8**: Python Enhancement Proposal 8; the official style guide for writing clean, readable, and consistent Python code.
  - Includes best practices for:
    - Naming variables & functions
    - Spacing & indentation
    - Organizing code for readability
   


### 3. Objects

- **Object**: a container representing a value in a Python program; automatically created when you assign a value to a variable.
  - Example
  > ```python
  > x = 42 # Creates an integer object
  > name = "Oliver" # Creates a string object
  > ```
  >
  > ```42``` and ```"Oliver"``` are objects (the values)
  > ```x``` and ```name``` are identifiers that refer to those objects

- **Garbage collection**: an automatic process Python uses to delete objects no longer needed by the program; frees up memory space to keep the program efficient
- **Name binding**: the process of associating an identifier with an object in memory. When a value is assigned to a variable, Python binds the name to the object holding the value.
  - Example
  > ```python
  > age = 25
  > ```
  > - The name ```age``` is **bound** to the integer object ```25```
  > - If you write ```age = 30```, the name is **re-bound** to a new object (```30```)
  
- **Value**: the actual data stored in an object
- **Type**: tells you what kind of value an object holds, like an integer, string, list, etc. which determines what operations can be performed on the object.
- **Identity**: a unique identifier for each object in memory.
- **type() function**: a built-in function that returns the **type** of an object, showing what kind of data it holds.
- **Mutability**: describes whether an object's value can be changed after it's created.
  - **Mutable** objects **can** be changed (lists, dictionaries)
  - **Immutable** objects **cannot** be changed (integers, strings)
- **id() function**: a built-in function that returns the unique identity of an object in memory; guaranteed to be unique and constant for the object during its lifetime.
  - Example
  > ```python
  > a = 1000
  > b = 1000
  > print(id(a))
  > print(id(b))
  > ```
  > Note: two different objects with the same value will always have different identities.
  > Think of it like two people sharing the same birthday - even if they are twins, both individuals will have different SSNs.
  >   - There is one exception to this due to Python interning small integers (-5 to 256) to optimize memory usage & performance.


### 4. Numeric Types: Floating-point

- **Floating-point number**: a real number that can include a fractional part, like '100.3', '2.384', or '-123.45'
- **Float**: the *datatype* to use for floating-point numbers
- **Floating-point literal**: a number explicitly written with a decimal point, even if the fractional part is '0', like '100.0', '0.0', '-13.0'

  - Example
  > ```python
  > temperature = 98.6  # variable bound to a float value
  > balance = 0.0  # fractional part '0'
  > negative = -123.45  # negative float
  > ```

- **Scientific notation**: a way to represent extremely large or small floating-point numbers
  - Uses an `e` or `E` to indicate the power-of-10 exponent and is often used in scientific or engineering contexts
  - Example
  > ```python
  > avogadro_number = 6.02e23  # 6.02 * 10^23
  > small_value = 1.0e-3  # 0.001
  > ```


Note: Python does have float range limitations. 
- Standard 32-bit Python install is limited to the following:
  - Max: ~`1.8e308`
  - Min: ~`2.2e308`

- **OverflowError aka overflow**: occurs when a value is too large for Python to store in memory allocated for a float
  - Example
  > ```python
  > large_number = 1.8e300  # within the float range  
  > too_large = 1.8e309   # OverflowError
  > ```

Note: Some floating-point numbers have a repeating decimals and some have an infinite number after the decimal
- Most programming langauges output at least 5 digits past the decimal point by default
- To output a floating-point number with specific number of digits after the decimal:
  - `print(f'{my_float:.2f}')` --> this syntax `:.2f` prints two digits after the decimal
 

### 5. Arithmetic expressions

- **Expression**: a combo of items (variables, literals, operators, and parentheses) that evaluate to a value. Typically, the expression is on the right-hand side of the assignment statement.
  - Example
  > ```python
  > x = 3
  > y = 2 * (x + 1)  # 2 * (x + 1) is the expression
  > ```
  > This expression evaluates to `8` and assigns it to `y`

- **Literal**: a fixed value written directly in code
  - Examples: `1` (integer), `3.14` (float), `'hello'` (string)

- **Operator**: a symbol that instructs Python to perform a specific operation on one or more values
  - Examples: `+` (addition), `-` (subtraction), `*` (multiplication)


Arithmetic Operators

| Operator | Description |
|----------|-------------|
| `+`  | **Addition** operator, as in `x + y` |
| `-`  | **Subtraction** operator, as in `x - y`.<br>Also used for negation, as in `-x + y` or `x + -y` |
| `*`  | **Multiplication** operator, as in `x * y` |
| `/`  | **Division operator**, as in `x / y` |
| `**` | **Exponent operator**, as in `x ** y` (`x` to the power of `y`) |

- **Evaluates**: when Python processes an expression, it produces or *evaluates to* a value that replaces the expression
  - Example  
  > ```python
  > x = 5
  > y = x + 1  # evaluates to 6
  > ```

- **Precedence rules**: the order in which Python evaluates operators in an expression, following standard math rules
  - Example  
  > ```python
  > result = 2 + 3 * 4  # evaluates to 14
  > ```


Precedence Rules for Arithmetic Operators

| Operator / Convention | Description | Example / Explanation |
|----------------------|-------------|---------------------|
| `( )` | Items within parentheses are evaluated first | `2 * (x + 1)` → `x + 1` is evaluated first, then multiplied by 2 |
| Exponent `**` | Exponentiation is evaluated next | `x**y * 3` → `x**y` is computed first, then multiplied by 3 |
| Unary `-` | Negation (unary minus) is next | `2 * -x` → `-x` is evaluated first, then multiplied by 2 |
| `* / %` | Multiplication, division, and modulo have equal precedence | `%` is discussed elsewhere |
| `+ -` | Addition and subtraction have equal precedence | `y = 3 + 2 * x` → `2 * x` is evaluated first, then added to 3 |
| Left-to-right | Operators of equal precedence are evaluated left to right (except `**`, which is right-to-left) | `y = x * 2 / 3` → `x * 2` is evaluated first, then divided by 3 |


### 6. Python expressions

- **Unary minus (-)**: the minus sign is used to indicate a negative value instead of subtraction
  - Example
  > ```python
  > x_coordinate = -y_coordinate  # the - is a unary minus
  > ```


Compound Operators

| Compound Operator | Expression with Compound Operator | Equivalent Expression |
|------------------|---------------------------------|---------------------|
| Addition assignment | `age += 1` | `age = age + 1` |
| Subtraction assignment | `age -= 1` | `age = age - 1` |
| Multiplication assignment | `age *= 1` | `age = age * 1` |
| Division assignment | `age /= 1` | `age = age / 1` |
| Modulo assignment | `age %= 1` | `age = age % 1` |


### 7.  Division and modulo

- **Division (/)**: performs division and always returns a floating-point number.  
  - Example  
  > ```python
  > 15 / 3   # 5.0
  > 7 / 2   # 3.5
  > 9 / 4    # 2.25
  > ```

- **Floor division (//)**: divides and rounds **down** to the nearest smaller whole number.  
  - Returns an **integer** if both operands are integers; returns a **float** if either operand is a float.  
  - Example  
  > ```python
  > 15 // 3   # 5
  > 7 // 2   # 3
  > 9 // 4    # 2
  > 9.0 // 4   # 2.0
  > ```

- **Division by zero**: the second operand of `/` or `//` must **never** be `0`.  
  - Example  
  > ```python
  > 10 / 0      # ZeroDivisionError
  > 10 // 0     # ZeroDivisionError
  > ```

- **Modulo (%)**: evaluates the **remainder** after dividing one number by another  
  - Example  
  > ```python
  > 23 % 10   # 3
  > ```
  > `23 ÷ 10` equals `2` with a remainder of `3`, modulo returns `3`

- More examples:  
  > ```python
  > 9 % 5     # 4   (9 = 5 * 1 + 4)
  > 70 % 7    # 0   (70 = 7 * 10 + 0)
  > 1 % 2     # 1   (1 = 2 * 0 + 1)
  > ```
  > The modulo operator gives the leftover part after **floor division** (`//`)


### 8. Module basics

- **Interactive Python interpreter**: executes code one line at a time; extremely useful for testing small snippets, experimenting, and/or practicing Python syntax
 
- **Script**: a file containing code which executes every line at one time by the interpreter; common workflow with larger programs

- **Import**: the statement to use to bring a module, or specific items (functions, variables, classes) from a module, into a script
  - Example  
  > ```python
  > import math
  > print(math.sqrt(16))  # 4.0
  > ```

- **Dot notation**: a way to access objects within a module once it's been imported; the **module name** comes first, followed by a `.`, then the **object name**
  - Example
  > ```python
  > import universe
  > print(universe.speed_of_light)  # speed_of_light is accessed once the universe module is imported
  > ```

- **Module**: a Python file that contains code which can be **reused in other scripts or modules**, which helps organize code into separate, logical pieces
  - Modules are made accessible using the `import` statement
  - Example  
  > File `universe.py` defines:  
  > ```python
  > speed_of_light = 299792458  # meters per second
  > ```  
  >
  > Another script can use this value:  
  > ```python
  > import universe
  > print(universe.speed_of_light)  # 299792458
  > ```
  > After importing, any item in the module is accessed with **dot notation**

**Importing modules and executing scripts**
- When a module is imported, all of its top-level code runs *immediately*. Python provides a special variable `__name__` to check whether a file is being run directly as a script or imported as a module
  - If `__name__` is `'__main__'`, the file is being executed directly by the interpreter
  - Example
    > `pet_names.py` defines some variables and may print statistics in an `if __name__ == '__main__'` block
    > `favorite_pet.py` imports `pet_names.py` to use the variables
    > 
    > Running `python pet_names.py` executes all code, including the `if __name__ == '__main__'` block
    > Running `favorite_pet.py` imports `pet_names.py`, but the `if __name__ == '__main__'` block does **not** execute, so favorite pets aren't printed

Note: code inside `if __name__ == '__main__':` only runs when the file is executed directly, **not when imported**


### 9. Math module

- **Module**: a separate file that contains code that you can reuse in your own programs.
- **Function**: a reusable block of code that performs a specific task. 
  - Example
    ```python
    import math

    print(math.sqrt(25)) # Outputs: 5.0
    ```

    - ```math``` is a module
    - ```sqrt()``` is a function within the ```math``` module
  
- **Function call**: when you activate a function by using a function's name followed by parentheses. Function calls tell Python to execute the code within the function.
- **Argument**: the value or data provided to a function when calling it. The function uses the argument to complete its task.
  - Example
    ```python
    print("Hello")
    ```

    - ```print()``` is the function call
    - ```"Hello"``` is the argument that is passed to the function

Common functions

| Function                  | Description                                   |
|:--------------------------|:----------------------------------------------|
| **Number representation and theoretic functions**                         |
| ceil(x)                   | Round-up value                                |
| factorial(x)              | factorial (3! = 3 * 2 * 1)                    |
| fmod(x, y)                | Remainder of division                         | 
| fabs(x)                   | Absolute value                                |
| floor(x)                  | Round-down value                              |
| fsum(x)                   | Floating-point sum of a range, list, or array |
| **Power, expotential, and logarithmic functions**                         |
| exp(x)                    | Exponential function e<sup>x</sup>            |
| pow(x, y)                 | Raise x to power y                            |
| log(x, (base))            | Natural logrithm; base is optional            |
| sqrt(x)                   | Square root                                   |
| **Trigonometric functions**                                               |
| acos(x)                   | Arc cosine                                    |
| atan(x)                   | Arc tangent                                   |
| cos(x)                    | Cosine                                        |
| hypot(x1, x2, x3, ..., xn | Length of vector from origin                  |
| radians(x)                | Convert degrees to radians                    |
| cosh(x)                   | Hyperbolic cosine                             |
| asin(x)                   | Arc sine                                      |
| atan2(y, x)               | Arc tangent with two parameters               |
| sin(x)                    | Sine                                          |
| degrees(x)                | Convert from radians to degrees               |
| tan(x)                    | Tangent                                       |
| sinh(x)                   | Hyperbolic sine                               |
| **Complex number functions**                                              |
| gamma(x)                  | Gamma function                                |
| erf(x)                    | Error function                                |
| **Mathematical constants**                                                |
| pi (constant)             | Mathematical constant 3.141592...             |
| e (constant)              | Mathematical constant 2.718281...             |


Math function examples

```python
import math

x = math.sqrt(25.0)
print(x)
```

  - Output: ```5.0```
    - The ```math.sqrt()``` function calculates the square root of a number.
    - Since the input is ```25.0``` (a float), the result is also a float.

```python
import math

x = math.fabs(3.1)
print(x)
```

  - Output: ```3.1```
    - The ```math.fabs()``` function returns the **absolute value** of a number.
    - It always returns a **positive float**.

```python
import math

x = math.pow(2.0, 5.0)
print(x)
```

- Output: ```32.0```
  - The ```math.pow()``` function raises the first number to the power of the second: 2<sup>5</sup> = 32.
  - Both inputs and the result are floats.

```python
import math

x = math.fabs(-10.0 + 5.0)
print(x)
```

  - Output: ```5.0```
    - The expression ```-10.0 + 5.0``` evaluates to ```-5.0```. and ```math.fabs()``` returns the absolute value: ```5.0```.

```python
import math

x = math.pow(5.0, math.sqrt(25.0))
print(x)
```

  - Output: ```3125.0```
    - The innermost expression ```math.sqrt(25.0)``` evaluates to ```5.0```.
    - Then ```math.pow(5.0, 5.0)``` calcuates 5<sup>5</sup> = ```3125```.
    - Both inputs and the result are floats.


📌 Exponents in Python

  > **Reminder**: In Python, ```^``` does **not** mean exponent (power).
  > Instead, it's the **bitwise XOR operator**.
  > To raise a number to a power, use ```**```.
  >
  > Incorrect
  > ```python
  >   x = 5 ^ 2 # Result is 7
  > ```
  >
  > Correct
  > ```python
  >   x = 5 ** 2 # Result is 25
  > ```




### 10. Random numbers

- **Random module**: part of the Python Standard Library, the ```random``` module provides tools for generating random values.
  - **random() function**: returns a random floating-point number between ```0.0``` (inclusive) and ```1.0``` (exclusive).
  - Example
  > ```python
  > import random
  >
  > # Store a random number in a variable
  > x = random.random()
  > print(x)
  >
  > # Print random numbers directly
  > print("Another random number:", random.random())
  > print("And another:", random.random())
  > ```

- **randrange(min, max)**: generates a random integer within a specified range; returns an integer between min (inclusive) and max (exclusive).
  - Example
  > ```python
  > import random
  >
  > # Returns a random integer from 1 (inclusive) up to 10 (exclusive)
  > num = random.randrange(1, 10)
  > print(num)
  >
  ># Returns random integers with 5 possible values
  > print(random.randrange(5))
  > print(random.randrange(5))
  > print(random.randrange(5))
  > print(random.randrange(5))
  > print(random.randrange(5))
  > ```
  
- **randint(min, max)**: returns a random integer between min (inclusive) and max (inclusive).
  - Example
  > ```python
  > # Returns a random integer between 23 and 50 inclusive
  > print(random.randint(23, 50))
  > ```

- **Psuedo-random**: numbers created by the ```random``` module aren't truly random, they simply **look** random, but they're calculated using a formula behind the scenes.
  - Python's random number generator works by:
  >  - Starting with a special value (**seed**), oftened based on the current time.
  >  - Using a formula to produce a sequence of random-looking numbers.
  >  - Each new number is bsed on the one coming before it.
  


### 11. Representing text

- **Unicode**:
- **Code point**: 

Common escape sequences

| Escape Sequence | Explanation      | Example code                                               | Output                   |
|:----------------|:-----------------|:-----------------------------------------------------------|:-------------------------|
| \\              | Backslash (\)    | ```python print('\\home\\users\\')```                      | \home\users\             |
| \'              | Single quote (') | ```python print('Name: John O\'Donald'```                  | Name: John O'Donald      |
| \"              | Double quote (") | ```python print("He said, \"Hello friend!\"")```           | He said, "Hello friend!" |
| \n              | Newline          | ```python print('My name...\nIs John...')```               | My name...<br>Is John... |
| \t              | Tab (indent)     | ```python print('1. Back cookies\n\t1.1. Preheat oven')``` | 1. Bake cookies<br>&nbsp;&nbsp;&nbsp;&nbsp;1.1 Preheat oven |

- **Raw string**: a special type of string where Python does **not** process escape sequences such as ```\n``` or ```\t```. To create a raw string, place an ```r``` before the opening quote: ```r'text'```.
  - Example
  > ```python
  > # Prints out the text exactly as it is within the single quote
  > print(r'This is a raw string\nIt will print the backslash and n literally')
  >
  > # Creates a string that be processed by the escape sequences, creating text on a new line (\n)
  > my_string = 'This is a \n \'normal\' string\n'
  > # Creates a string that will **not** be processed by the escape sequences,
  > # creating a string that is exactly as it is within the single quotes
  > raw_string = r'This is a \n \'raw\' string'
  >
  > print(my_string)
  > print(raw_string)
  > ```
  
- **ord() function**: takes a single character and returns its Unicode (integer) code.
  - Example
  > ```ord('A')``` returns ```65```
  > ```ord('b')``` returns ```98```
- **chr() function**: takes an integer Unicode point and returns the corresponding character as a string.
  - Example
  > ```chr(65)``` returns ```A```
  > ```chr(52)``` returns ```4```
  

  
## References

[Object Interning in Python](https://www.geeksforgeeks.org/python/object-interning-in-python/)

[Python Bitwise Operators](https://www.geeksforgeeks.org/python/python-bitwise-operators/)

[randrange in Python](https://www.geeksforgeeks.org/python/randrange-in-python/)

[Range Function](https://pythonbasics.org/range-function/)

[Floor Division in Python](https://www.geeksforgeeks.org/python/floor-division-in-python/)

[15. Floating-Point Arithmetic: Issues and Limitations](https://docs.python.org/3/tutorial/floatingpoint.html)

[Python Floating-Point Numbers](https://coderivers.org/blog/python-floating-number/)

[Python Arithmetic Operators](https://www.w3schools.com/python/gloss_python_arithmetic_operators.asp)

[Operator Precedence in Python](https://pythongeeks.org/python-operator-precedence/)

[6. Modules - Python 3.13.7 documentation](https://docs.python.org/3/tutorial/modules.html)

[Absolute vs Relative Imports in Python - Real Python](https://realpython.com/absolute-vs-relative-python-imports/)

[Module execution in Python: Import, python -m script.py, and python script.py](https://alberto-agudo.github.io/posts/03-python-m-flag/index.html)

[Python Modules](https://www.geeksforgeeks.org/python/python-modules/)

[What does the if __name__ == "__main__ ": do?](https://www.geeksforgeeks.org/python/what-does-the-if-__name__-__main__-do/)

[__main__ - Top-level code enviroment - Python 3.13.7 documentation](https://docs.python.org/3/library/__main__.html)
