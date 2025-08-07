# 11.6.3
import os
p = 'C:\\Programs\\Microsoft\\msword.exe'
print(os.path.split(p))
# Output: ('C:\\Programs\\Microsoft', 'msword.exe')

os.path.isfile('C:\\Program Files\\')
# Output: False

os.path.getsize(path_str)
# returns the size in bytes of the file at path_str
