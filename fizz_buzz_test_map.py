'''
Title: Advanced Fizz Buzz Test
Sub-title: map()
Author: Ayan Ashkenov
Date: 18/01/2021
Description: The Fizz Buzz Test using map().
'''

list_1to100 = list(range(1,101))

# Version 1
fizz_buzz_forMap = lambda n: ("FizzBuzz" * (n/15==n//15)) or ("Buzz" * (n/5==n//5)) or ("Fizz" * (n/3==n//3)) or n
print(list(map(fizz_buzz_forMap, list_1to100)))

# Version 2
print(list(map(lambda n: ("FizzBuzz" * (n/15==n//15)) or ("Buzz" * (n/5==n//5)) or ("Fizz" * (n/3==n//3)) or n, list(range(1,101)))))