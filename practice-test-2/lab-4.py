# solution accepts three integer values
# representing base and height measurements of a trapezoid
# first and second integers represent base 1 and base 2
# third integer represents height 
# solution outputs the trapezoid area in square meters 
# using formula A = ((b1 + b2) * h) / 2)
print("Enter base 1: ")
base_1 = int(input())
print("Enter base 2: ")
base_2 = int(input())
print("Enter height: ")
height = int(input())

# calculate the area of a trapezoid
area = ((base_1 + base_2) * height) / 2

#ouput exact trapezoid area based on input dimensions
print(f'Trapezoid area: {area:.1f} square meters')
