# 2.7.1
12 / 4 = 3.0     # remember, regular division yields a floating point
5 / 10 = 0.5
5.0 // 2 = 2.0   # remember, floor division with a floating point and an integer always returns a floating point
100 / 0 = Error  # division error

7 // 2 = 3      # Integer
7.0 // 2 = 3.0  # Float
7 // 2.0 = 3.0  # Float  
7.5 // 2 = 3.0  # Float

# 2.7.2 
50 % 2 = 0
# 50 / 2 = 25, no remainder

51 % 2 = 1
# 51 / 2 = 25.5 (don't include the decimal point and following numbers)
# 25 * 2 = 50
# Think of it as 50 + x = 51
# x = 1, so modulo is 1
# NOTE: any ODD number % 2 is 1
# NOTE: any EVEN number % 2 is 0

5 % 3 = 2
# 5 / 3 = 1.67 (1)
# 3 * 1 = 3
# 3 + x = 5
# x = 2, so modulo is 2

27 % 4 = 3  
# 27 / 4 = 6
# 4 * 6 = 24
# 24 + x = 27
# x = 3, so modulo is 3

596 % 10 = 6
# 596 / 10 = 59.6 (59)
# 10 * 59 = 590
# 590 + x = 596
# x = 6, so modulo is 6

100 % (1 // 2) = Error
# 1 // 2 = 0.5 (0)
# 100 % 0 = DivisionError



# 2.7.3
# Given a non-negative number x, which expression has the range of 5 to 10?
(x % 6) + 5   # x % 6 yields 0 to 5. Then + 5 yields 5 to 10.

# Given a non-negative number x, which expression has the range -10 to 10?
(x % 21) - 10  # x % 21 yields 0 to 20. Then - 10 yields -10 to 10.

# Which expression gets the tens digit of x? Ex: If x = 693, which expression yields 9?
(x // 10) % 10  
# x // 10 removes the rightmost digit, putting the tens digit in the ones place. 
# Then % 10 gets the (new) ones digit. 
# Ex: 693 / / 10 is 69, then 69 % 10 is 9.

# Given a 16-digit credit card number stored in x, which expression gets the rightmost four digits (assume the fourth digit from the right is non-zero)?
x % 10000   
# x % 10000 yields the rightmost four digits. 
# To get other digits like the next four digits, first divide to remove the rightmost digits, then use % to get just those digits.

