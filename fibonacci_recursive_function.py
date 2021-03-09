'''
Title: Factorial function (recursive)
Author: Ayan Ashkenov
Date: 08/03/2021
Description: This function returns the nth number in a fibonacci sequence.
'''

def fibonacci_recursive(nth_number, value_holder):
        if nth_number in value_holder:
                return value_holder[nth_number]
        elif nth_number >= 4:
                return fibonacci_recursive(nth_number - 1, value_holder) + fibonacci_recursive(nth_number - 2, value_holder)
        elif nth_number == 1:
                value_holder[nth_number] = 0
                return 0
        else:
                value_holder[nth_number] = 1
                return 1

value_holder = {}
print(fibonacci_recursive(7, value_holder))