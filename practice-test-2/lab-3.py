# create a solution that accepts an integer input representing the 
# index value for any of the seven elements in the following list:
# data_mixture = ["Python is fun", 2024, 5.67, ["apple", "banana", 
# "coconut"], None,{"name": "John", "age": 25}]

# the solution should perform:
# 1. retrieve the elemt at the given index
# 2. determine its data type using the tyoe() function and its .name attr
# 3. check if the element belongs to one of the following categories:
  # if the element is iterable (list, str, dict), output "This element is iterable."
  # if the element is numeric (int, float), output "This element is numeric."
# 4. for other data types not in these categories, output "This is a different data type."

# the solution must be in the following format:
# Element: [element_value], Type: [data_type], Message: [category_message]
#list of mixed data elements
data_mixture = ["Python is fun", 2024, 5.67, ["apple", "banana", "coconut"], None, {"name": "John", "age": 25}]

#input for index
print("Enter index:")
index = int(input())

# Finish later
print(f'Element: {element}, Type: {data_type}, Message: {message}')
