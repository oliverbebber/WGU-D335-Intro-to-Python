# write a program that reads a char, then a list of words
# output is every word in the list that contains the char at least once
# assume at least one word in the list will contain the given char

letter = input()                # input: z
words = input()                 # input: hello zoo sleep drizzle

word_list = words.split()
# print(word)                   # ['hello', 'zoo', 'sleep', 'drizzle']

for w in word_list:
    if letter in w:
        print(w + ',', end='')  # output format: zoo,drizzle
