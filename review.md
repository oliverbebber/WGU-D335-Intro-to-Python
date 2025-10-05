# Review

## List Methods

- lists are ordered, **mutable**, and allows for duplicate values
  - Example
  > ``` python
  > cats = ['Phoenix', 'Dallas', 'Leo']
  > nums = [1, 2, 3, 4]
  > ```
  
- **.append(x)**: adds `x` value to the end of an existing list
  - Example
  > ``` python
  > cats.append('Miso')
  > ```
  > Result:
  > ['Phoenix', 'Dallas', 'Leo', 'Miso']
  
- **.insert(i, x)**: insert a value at index `i`
  - Example
  > ``` python
  > cats.insert(1, 'Apollo')
  > ```
  > Result:
  > ['Phoenix', 'Apollo', 'Dallas', 'Leo']
  
- **.remove(x)**: remove the first occurence of `x` value
  - Example
  > ``` python
  > cats.remove('Phoenix')
  > ```
  > Result:
  > ['Apollo', 'Dallas', 'Leo']
  
- **.pop(i)**: remove and return the item at index `i` (default: `.pop()` is the last index)
  - Example
  > ``` python
  > cats.pop()
  > ```
  > Result:
  > 'Leo'

- **.sort()**: sort existing list in place
  - Example
  > ``` python
  > nums.sort()
  > ```
  > Result:
  > [1, 2, 3, 4]
  
- **.reverse()**: reverse the list order in place
  - Example
  > ``` python
  > nums.reverse()
  > ```
  > Result:
  > [4, 3, 2, 1]
  
- **.count(x)**: count occurrences of `x` value
  - Example
  > ``` python
  > cats.count('Dallas')
  > ```
  > Result:
  > 1
  
- **.index(x)**: return the first index of `x` value
  - Example
  > ``` python
  > cats.index('Leo')
  > ```
  > Result:
  > 2
  
- **.copy()**: shallow copy (if list contains nested lists, the inner lists are still shared)
  - Example
  > ``` python
  > new_list = cats.copy()
  > ```
  
- **.clear()**: removes all items from an existing list
  - Example
  > ``` python
  > ```
  

## Loops

### `for` Loops

- used when you know how many times to repeat something
  - Example
  > ``` python
  > for i in range(3):
  >   print('Hello', i)
  > ```
  > Output: Hello 0
  > Hello 1
  > Hello 2
  
Note: `range(start, stop, step)`

### `while` Loops

- used when you **don't** know in how many times to repeat in advance
  - Example
  > ``` python
  > num = 5
  > while num > 6:
  >   print(num)
  >   num -= 1
  > ```
  > Output: 5
  > 4
  > 3
  > 2
  > 1

Common mistakes:

- forgetting to update the loop variable, resulting in an infinite loop
- using `=` instead of `==`
  - `=` is used to define variables
  - `==` is used for comparing
 
### Loop control

``` python
for i in range(5):
  if i == 2:
    continue
  if i == 4:
    break
  print(i)
```

> Output: `0 1 3`

### Practice

``` python
count = 0

while count < 3:
  for i in range(2):
    print(count,i)
  count += 1
```

> Output: 0 0
> 0 1
> 1 0
> 1 1
> 2 0
> 2 1

## Branching (if / elif / else)

``` python
x = 15

if x > 20:
  print('Large')
elif x > 10:
  print('Medium')
else:
  print('Small')
```

> Output: `Medium`

Note: Order matters in branching; python will check conditions from top to bottom, **until** one is true.

Common mistakes:

- forgetting colons (`:`)
- indentation errors

### Practice

``` python
x = 10
y = 20

if x > y:
  print('A')
elif x == 10:
  print('B')
else:
  print('C')
```

> Output: B

## Exceptions

- used to handle errors gracefully
  - Example
  > ``` python
  > try:
  >   num = int(input('Enter number: '))
  >   print(10 / num)
  > except ValueError:
  >   print('Not a number!')
  > except ZeroDivisionError:
  >   print('Can't divide by zero!')
  > finally:
  >   print('Done!')
  > ```
  >
  > Note: the `finally` block **always** runs
  
### Practice

``` python
try:
  x = int('abc')
  print('Converted!')
except ValueError:
  print('Error!')
finally:
  print('Finished.')
```

> Output: Error!
> Finished.

## File handling

### Reading files

``` python
with open('data.txt', 'r') as f:
  content = f.read()
  print(content)
```

### Writing files

``` python
with open('output.txt', 'w') as f:
  f.write('Hello world\n')
```

### Appending

``` python
with open('output.txt', 'a') as f:
  f.write('Another line\n')
```

Note: using `with` automatically closes the file - remember to do this as a best practice.

### Practice

if `notes.txt` contains:

```
cat
dog
fish
```

What does the following code print?

``` python
with open('notes.txt', 'r') as f:
  for line in f:
    print(line.strip().upper())
```

> Output: CAT
> DOG
> FISH
```
