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

| Method             | Description                                                                                       |
|-------------------|---------------------------------------------------------------------------------------------------|
| close()            | Closes the file. Once closed, the file cannot be read or written to.                              |
| flush()            | Forces the file’s internal buffer to be written to disk.                                          |
| read(size=-1)      | Reads up to the specified number of bytes from the file. If no size is given, reads the entire file. |
| readline(size=-1)  | Reads one line from the file. If size is specified, it reads at most that many bytes.            |
| readlines(hint=-1) | Reads all lines from the file and returns them as a list of strings. If hint is given, reads that many bytes. |
| seek(offset, whence=0) | Moves the file pointer to a specified position. The whence parameter defines the starting point. |
| tell()             | Returns the current position of the file pointer.                                                |
| truncate(size=None)| Truncates the file to the specified size. If no size is specified, it truncates to the current position. |
| write(string)      | Writes the specified string to the file.                                                         |
| writelines(lines)  | Writes a list of strings to the file.                                                            |

- File Objects as a Data Type
  - File objects are treated as a distinct data type
    - Managed by the ```TextIOWrapper``` class
    - Specific methods to interact with them
  - Important: think about file objects like an object with associated methods - similar to strings or lists

- Iterators and File Methods
  - ```f.readline()``` method: iterator function which reads one line at a time from a file.
    - Useful when dealing with large files (processes the file incrementally - doesn't load full file into memory)
    - Example
    > ``` python
    > with open('file.txt', 'r') as f:
    >   line = f.readline()
    >   print(line) # prints the first line
    > ```
  - ```csv.reader()``` function: specialized iterator that reads CSV files
    - Able to parse rows and return the data as a list
    - Processes files incrementally
    - Example
    > ``` python
    > import csv
    >
    > with open('file.csv', newline='') as f:
    >   reader = csv.reader(f)
    >   for row in reader:
    >     print(row)  # prints each row as a list of values
    > ```
    
- Key Differences from Other Iterators
  - ```f.readline()``` and ```csv.reader()``` require careful attention since file objects maintain their own internal state
  - ```readline()``` can cause the file pointer to move forward through the file

### 3. The 'with' statement

### 4. Reading files

### 5. Writing files

### 6. Interacting with file systems

### 7. Command-line arguments and files

### 8. Comma-separated values files

### 9. Files practice


### References

