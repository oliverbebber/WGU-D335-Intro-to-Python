# Lesson 11 Files Notes

These are my notes for Lesson 11 of the Intro to Python course.

## Sections

### 1. What is a file?

- Text-based
  - Python files are plain text files containing Python code
  - Can be opened & edited in any text editor or IDE that can support Python

- Execution
  - Run ```python filename.py``` from the CLI / terminal
  - Python interpreter reads and executes code line by line

- File types
  -   ```.py```: most common type of Python file; contains standard Python code
  -   ```.pyc```: compiled Python files (bytecode); generated when a ```.py``` file is executed, allowing for faster execution
  -   ```.pyo```: optimized Python files; generated when the ```python -o``` command is used

- Files and File Objects
  - File objects are often used to read from or write to files
  - **File Objects**: instances of classes that allow interaction with files on your system
    - Most common operations:
      - Opening files
      - Reading files
      - Writing to files
  - Example
  > ``` python
  > with open('example.txt', 'r') as file:  # creates a file object allowing you to read the contents of the file specified
  >   content = file.read()
  >   print(content)
  > ```


### 2. File Objects Methods Reference

### 3. The 'with' statement

### 4. Reading files

### 5. Writing files

### 6. Interacting with file systems

### 7. Command-line arguments and files

### 8. Comma-separated values files

### 9. Files practice


### References

