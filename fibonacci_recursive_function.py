'''
Title: Factorial function (recursive)
Author: Ayan Ashkenov
Date: 08/03/2021
Description: This function returns the nth number in a fibonacci sequence.
'''

def fibonacci_recursive(nth_number):
        if nth_number >= 4:
                return fibonacci_recursive(nth_number - 1) + fibonacci_recursive(nth_number - 2)
        elif nth_number == 1:
                return 0
        else:
                return 1