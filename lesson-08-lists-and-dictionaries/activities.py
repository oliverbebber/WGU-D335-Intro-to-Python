# 8.1.3
animals = ['cat', 'dog', 'bird', 'raptor']
print(animals[0])
# cat

print(animals[2])
# bird

print(animals[0 + 1])
# 0 + 1 = 1
# dog

i = 3
print(animals[i])
# raptor



# 8.2.2 
temps = [65, 67, 72, 75]
temps.append(77)
print(temps[-1])
# output: 77

actors = ['Pitt', 'Damon']
actors.insert(1, 'Affleck')
print(actors[0], actors[1], actors[2])
# output: Pitt Affleck Damon

# write the simplest two statements that first sort my_list
# then remove the largest value element from the list, using list methods
my_list.sort()
my_list.pop()

# write a statement that counts the number of elements of my_list that have the value 15
my_list.count(15)



# 8.4.2
# count how many odd numbers (cnt_odd) there are
cnt_odd = 0

for i in num:
    if i % 2 == 1:
        cnt_odd += 1


# count how many negative numbers (cnt_neg) there are
cnt_neg = 0
for i in num:
    if i < 0:
      cnt_neg += 1


# Determine the number of elements in the list that are divisible by 10. 
# (Hint: The number x is divisible by 10 if x % 10 is 0.)
div_ten = 0
for i in num:
    if i % 10 == 0:
        div_ten += 1
