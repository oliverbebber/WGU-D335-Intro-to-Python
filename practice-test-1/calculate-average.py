def calc_average(nums):
  # complete the function that has an int list param
  average = sum(nums) / len(nums)
  # returns the average value of elements in the list as a float
  return average
    
if __name__ == '__main__':
  nums = [1, 2, 3, 4, 5]
  print(calc_average(nums))   # calc_average() should return 3.0
