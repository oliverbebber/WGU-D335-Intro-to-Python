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

- **with statement**: can be used to open a file, execute a block of statements, and automatically close the file when finished
  - Helpful to simplfy resources management
  - Example
  > ``` python
  > with open('myfile.txt', 'r') as myfile
  >     # Statement-1
  >     # Statement-2
  >     # ....
  >     # Statement-N
  > ```
  - Example: opening a file
  > ``` python
  > print("Opening myfile.txt")
  > # Open a file for reading and writing
  > with open("myfile.txt", "r+") as f:
  >     # Read in two integers
  >     num1 = int(f.readline())
  >     num2 = int(f.readline())
  >
  >     product = num1 * num2
  >
  >     # Write back result on own line
  >     f.write("\n")
  >     f.write(str(product))
  >
  > # No need to call f.close() - f closed automatically
  > print("Closed myfile.txt")
  > ```

- **context manager**: manages the use of a resource by performing setup and cleanup operations.

### 4. Reading files

- **open() function**: built-in Python function; used to open files and retrieve information from them

- **file.close() method**: closes a file; no more reads or writes to the file are allowed once it's closed

- **file.read() method**: returns the file contents as a string

- **file.readlines() method**: returns a *list* of strings; the first element is the information on the first line, the second is from the second line, etc.

Note: each method (```file.close()```, ```file.read()```, ```file.readlines()``` stops reading when it reaches the **end-of-file (EOF)** as it indicates the file has no additional data.

- **file.readline() method**: returns a single line at a time; beneficial when working with large files and the contents may not fit in the system memory


### 5. Writing files

### 6. Interacting with file systems

### 7. Command-line arguments and files

### 8. Comma-separated values files

### 9. Files practice


### References

[File Objects in Python](https://www.geeksforgeeks.org/python/file-objects-python/)

[csv - CSV File Reading and Writing - Python Documentation](https://docs.python.org/3/library/csv.html)

[readline() in Python](https://www.geeksforgeeks.org/python/readline-in-python/)

[with statement in Python](https://www.geeksforgeeks.org/python/with-statement-in-python/)

[27. Context Managers - Python Tips](https://book.pythontips.com/en/latest/context_managers.html)
