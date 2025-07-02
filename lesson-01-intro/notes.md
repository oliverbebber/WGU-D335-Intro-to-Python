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
