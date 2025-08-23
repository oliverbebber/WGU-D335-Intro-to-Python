# 11.4.2
# write a statement to open the file "readme.txt" for reading
my_file = open("readme.txt")

# write a statement to read up to 500 bytes from "readme.txt" into the contents variable
my_file = open("readme.txt")
contents = my_file.read(500)  # optional argument to lmit the number of bytes read

# write a program to print the second line of "readme.txt"
my_file = open("readne,txt")
lines = my_file.readlines()
print(lines[1])


# 11.6.3
import os
p = 'C:\\Programs\\Microsoft\\msword.exe'
print(os.path.split(p))
# Output: ('C:\\Programs\\Microsoft', 'msword.exe')

os.path.isfile('C:\\Program Files\\')
# Output: False

os.path.getsize(path_str)
# returns the size in bytes of the file at path_str


# 11.8.1
# myfile.csv contains the following

# Airline,Destination,Departure time,Plane
# Southwest,Phoenix,615,B747
# Alitalia,Milan,1545,B757
# British Airways,London,1230,A380

# create a csv module reader object to read myfile.csv
import csv
with open('myfile.csv', 'r') as myfile:
  csv_reader = csv.reader(myfile)



# print the destination of each flight in myfile.csv
import csv
with open('myfile.csv', 'r') as myfile:
  csv_reader = csv.reader(myfile)
  for row in csv_reader:
    print(row[1])  # iterating over the reader object provides each row of the file as a list of the fields 

# Airline = [0]
# Destination = [1]
