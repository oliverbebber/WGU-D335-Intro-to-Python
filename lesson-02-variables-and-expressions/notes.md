# Lesson 02 Variables and Expressions Notes

These are my notes for Lesson 02 of the Intro to Python course.

## Sections

### 1. Variables and Expressions


### 2. Identifiers


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


### 10. Random numbers


### 11. Representing text
