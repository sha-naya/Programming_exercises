'''
Title: Advanced Fizz Buzz Test
Author: Ayan Ashkenov
Date: 18/01/2021
Description: The Fizz Buzz Test without if-else statements and for-loops.
'''

#No if-else statements
for n in range(1,101): print(("FizzBuzz" * (n/15==n//15)) or ("Buzz" * (n/5==n//5)) or ("Fizz" * (n/3==n//3)) or n)

#No if-else and no for-loops
iterable = list(range(1,101))
function = lambda n: ("FizzBuzz" * (n/15==n//15)) or ("Buzz" * (n/5==n//5)) or ("Fizz" * (n/3==n//3)) or n
print(list(map(function, iterable)))

#One line solution
print(list(map(lambda n: ("FizzBuzz" * (n/15==n//15)) or ("Buzz" * (n/5==n//5)) or ("Fizz" * (n/3==n//3)) or n, list(range(1,101)))))