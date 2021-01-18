'''
Title: Fibonacci Sequence Function
Author: Ayan Ashkenov
Date 18/01/2021

Description: A function that produces the Fibonacci sequence of
desired length.
Example - Fibonacci sequence of length 10 is [0 1 1 2 3 5 8 13 21 34].

Note: Fibonacci sequence always starts with 0 and 1.
'''

def fibonacci_simple(length):

        sequence_list = [0, 1]

        while len(sequence_list) < length:

                sequence_list.append((sequence_list[-2] + sequence_list[-1]))

        return sequence_list