'''
Title: Advanced Fizz Buzz Test
Sub-title: reduce()
Author: Ayan Ashkenov
Date: 23/02/2021
Description: The Fizz Buzz Test using reduce().
'''

import functools

def fizz_buzz_forReduce(x, y):
        print(("FizzBuzz" * (y/15==y//15)) or ("Buzz" * (y/5==y//5)) or ("Fizz" * (y/3==y//3)) or y)
        if y == 100:
                return "Done"
        else:
                return (y*1) + (x*0)

list_0to100 = list(range(101))

print(functools.reduce(fizz_buzz_forReduce, list_0to100))