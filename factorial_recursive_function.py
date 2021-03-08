'''
Title: Factorial function (recursive)
Author: Ayan Ashkenov
Date: 07/03/2021
Description: This function calculates a factorial of a number.
'''

def calculate_factorial(number):
        if number >= 1:
                factorial = number * calculate_factorial(number - 1)
                return factorial
        elif number == 0:
                return 1
        else:
                return "Cannot calculate factorial of a negative number!"