# 10.1.2
# write a statement that imports the content of tools.py into the interpreter
>>> import tools

# 10.1.5
shapes.py

cr = '#'

def draw_square(size):
    for h in range(size):
        for w in range(size):
            print(cr, end='')
        print() 

def draw_rect(height, width):
    for h in range(height):
        for w in range(width):
            print(cr, end='')
        print()


# write an import statement to import shapes.py
import shapes
# write a statement to call the draw_square function from the shapes module, passing an argument of 3
shapes.draw_square(3)
# change output to use '$" instead of '#' when drawing shapes
shapes.cr = '$'
