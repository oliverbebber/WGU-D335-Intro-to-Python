import math

# given a piano key frequency f0
frequency = int(input())

# each higher key (black or white) has a frequency: fn = f0 * r ** n
# where n is the number of keys above f0, and r is 2 ** (1/12) (use math.pow)
r = math.pow(2, 1/12)

# compute the next 3 higher key frequencies (n = 1, 2, 3)
for n in range(0,4):  # including 0 to print 440.00 Hz
  next_freq = frequency * (r ** n)
  # output each frequency with 2 decimal places, followed by "Hz"
  print(f'{next_freq:.2f} Hz')

# range(1,4) will only output 466.16 Hz - 523.25 Hz
