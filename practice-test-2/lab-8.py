# create a solution that accepts one integer input representing the index value for any
# of the string elements in the frameworks list
# output the string element of the index value entered
# place the solution in a try block and implement an exception of "Error" if an incompatible int 
# input is provided
# the solution output should be in the following format:
# frameworks_element

frameworks = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]

#try-block to determine value
try:
  print("Enter the index of the element that you want to extract from the list:")  
  index = int(input())             #accept integer input
  print(frameworks[index])

except:
  print("Error")
