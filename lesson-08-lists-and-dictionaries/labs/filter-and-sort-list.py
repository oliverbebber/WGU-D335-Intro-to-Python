# write a program that gets a list of integers from input & outputs negative integers
# in descending order (highest to lowest)

my_list = [int(x) for x in input().split()]

negatives = [x for x in my_list if x < 0]

negatives.sort(reverse=True)

for num in negatives:
    print(num, end=' ')
