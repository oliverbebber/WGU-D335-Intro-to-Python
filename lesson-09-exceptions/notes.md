# Lesson 09 Exceptions Notes

These are my notes for Lesson 09 of the Intro to Python course.

## Sections

### 1. Handling exceptions using try and except

- **Error-checking code**: code programmers use to detect & handle errors that occur while a program executes

- **try block**: used to test code for errors

- **except block**: used to handle the error
  - Statements in the try block that are not executed before the except block are skipped
  - If no errors occur, the except block is skipped


## Basic exception-handling constructs

> ``` python
> try:
>   # code that may produce errors
> except:  # initiates the following if any error occurs in the try block
>   # exception handling code
> ```

## Common exception types

| Type             | Reason exception is raised                                           |
|------------------|----------------------------------------------------------------------|
| [EOFError](https://docs.python.org/3/library/exceptions.html#EOFError)         | `input()` hits an end-of-file condition (EOF) without reading input. |
| [KeyError](https://docs.python.org/3/library/exceptions.html#KeyError)         | A dictionary key is not found in the set of keys.                    |
| [ZeroDivisionError](https://docs.python.org/3/library/exceptions.html#ZeroDivisionError)| Divide by zero error                                                 |
| [ValueError](https://docs.python.org/3/library/exceptions.html#ValueError)       | Invalid value (e.g., input mismatch)                                 |
| [IndexError](https://docs.python.org/3/library/exceptions.html#IndexError)       | Index is out of bounds.                                              |


### 2. Multiple exception handlers

### 3. Raising exceptions

### 4. Exceptions with functions

### 5. Using finally to clean up

### 6. Custom exception types

### References

[Python: Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)

[Python Try Except](https://www.w3schools.com/python/python_try_except.asp)
