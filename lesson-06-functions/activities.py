# 6.1.2

Main program  # Cluttered, repeated code
c1 = (f1 - 32.0) * (5.0 / 9.0)
c2 = (f2 - 32.0) * (5.0 / 9.0)
c3 = (f3 + 32.0) * (5.0 / 9.0)


F2C(f)
  c = (f - 32.0) * (5.0 / 9.0)  # calculation only written once
  return c


Main program  # Simpler
c1 = F2C(f1)
c2 = F2C(f2)
c3 = F2C(f3)


Main program
a = expression1
b = a + expression2
c = b * expression3
c = XYZ(a, b)

d = expression1
e = d + expression2
f = e * expression3
f = XYZ(d, e)


Main program
a = expression1
b = a + expression2
c = b * expression3
c = XYZ(a, b)

d = expression4
e = d * d * d
f = (e + 1) * 2
f = f / g
f = CalcPQR(d, e, g)

# In the orginal main program, the Fahrenheit to Celsius calculation appeared how many times?
# 3 times

# Along with yielding a simpler main program, using the predefined Fahrenheit to Celsius calculation prevented what error in the original program?
# Adding rather than subtracting 32.0

# In the last example, the main program was simplified by
# predefining operations for XYZ and CalcPQR



# 6.1.8
# What defines two params x and y for a function definition:
def calc_val(...):
# (x, y)

# What correctly passes two int arguments for the following function call:
calc_val(...)
# (99, 44 + 5)
calc_val(99, 44 + 5)
calc_val(99, 49)

# Given a function definition:
def calc_val(a, b, c):
# b is assigned with what value during this function call:
calc_val(42, 55, 77)
# 55

# given a function definition:
def calc_val(a, b, c):
# and given variables i, j, and k, what are valid arguments in the call?
# (k, i + j, 99)
a = k
b = i + j
c = 99
