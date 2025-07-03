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


### 4. Numeric Types: Floating-point


### 5. Arithmetic expressions


### 6. Python expressions


### 7.  Division and modulo


### 8. Module basics


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


### 11. Representing text
