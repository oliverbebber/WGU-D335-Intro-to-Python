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

Multiple exception handlers can be added to a try block by adding in additional except blocks & specifying the type of exception each block handles.
  
  - Example
  > ``` python
  > try:
  >   # normal code
  > except TypeError:
  >   # code that handles TypeErrors
  > except ValueError:
  >   # code that handles ValueErorrs
  > except:
  >   # code that handles other exception types
  > ```

Note: if no exception handler exists for an error type, an unhandled exception *may* occur. This will cause the interpreter to print the exception that occurred and halt the program.

Multiple exception types can sometimes be handled by the same exception handler. A tuple can be used to specify all of the exception types a handler's code should execute.
  - Example
  > ``` python
  > try:
  >   # ...
  > except (ValueError, TypeError):
  >   # Exception handler for any ValueError or TypeError that occurs.
  > except (NameError, AttributeError):
  >   # A different handler for NameError and AttributeError exceptions.
  > except:
  >   # A different handler for any other exception type.
  > ```

### 3. Raising exceptions

Code that finds errors can execute a *raise* statement, which causes the program to exit from the try block and the execution of an exception handler.
  - The exception handler prints the argument passed by the raise statement that triggered the execution


### 4. Exceptions with functions

### 5. Using finally to clean up

### 6. Custom exception types

### References

[Python: Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)

[Python Try Except](https://www.w3schools.com/python/python_try_except.asp)

[Python's raise: Effectively Raising Exceptions in Your Code](https://realpython.com/python-raise-exception/)
