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


### 10. Random numbers


### 11. Representing text
