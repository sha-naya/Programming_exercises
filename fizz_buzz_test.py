'''
Title: Attempt at the Fizz Buzz Test
Author: sha-naya
Date: 12/10/2020
'''
#This problem was not as straight forward as I originally thought.
#Since division always results in a float, my first idea was quickly
#scrambled.
#Instead, I set the initial conditions, using them to filter through
#numbers. When they were met, the 'for' loop changed them accordingly. This
#works because once the initial condition is met (index "i" in the 'for' loop
#is 3, so "Fizz" needs to be printed), that same condition can no longer
#occur again.
#This is definitely not the 'cleanest' solution, but one that
#I came up with myself without outside help.

#First, I tried to accomplish the task on a smaller range of 1-20 instead of
#1-100.
def fizz_buzz_test_small():

    cond_3 = 3
    cond_5 = 5
    cond_3_5 = 15

    for i in range(1,21):
        if i == cond_3_5:
            print('FizzBuzz')
            cond_3_5 += 15
        elif i == cond_5: #if i is 10, then cond_5 = 15 now
            print('Buzz')
            cond_5 += 5
        elif i == cond_3:
            print('Fizz')
            cond_3 += 3 #if i is 12, then cond_3 = 15 now
        else:
            print(i)

        #the following code is necessary because at some point, cond_3 and
        #cond_5 would come to equal cond_3_5. As a result, the 'for' loop
        #would stop performing as intended. When cond_3 and cond_5 come to
        #equal cond_3_5, they need to be shifted forward.
        if cond_3 == cond_3_5:
            cond_3 += 3
        if cond_5 == cond_3_5:
            cond_5 += 5
###fizz_buzz_test_small()


#Now, I will try a slightly bigger fizz buzz range, 1-50.
def fizz_buzz_test_medium():

    cond_3 = 3
    cond_5 = 5
    cond_3_5 = 15

    for i in range(1,51):
        if i == cond_3_5:
            print('FizzBuzz')
            cond_3_5 += 15
        elif i == cond_5: #if i is 10, then cond_5 = 15 now
            print('Buzz')
            cond_5 += 5
        elif i == cond_3:
            print('Fizz')
            cond_3 += 3 #if i is 12, then cond_3 = 15 now
        else:
            print(i)

        if cond_3 == cond_3_5:
            cond_3 += 3
        if cond_5 == cond_3_5:
            cond_5 += 5
###fizz_buzz_test_medium()

#Since both tests were successful, the full fizz buzz should be correct.
def fizz_buzz_test():

    cond_3 = 3
    cond_5 = 5
    cond_3_5 = 15

    for i in range(1,101):
        if i == cond_3_5:
            print('FizzBuzz')
            cond_3_5 += 15
        elif i == cond_5: #if i is 10, then cond_5 = 15 now
            print('Buzz')
            cond_5 += 5
        elif i == cond_3:
            print('Fizz')
            cond_3 += 3 #if i is 12, then cond_3 = 15 now
        else:
            print(i)

        if cond_3 == cond_3_5:
            cond_3 += 3
        if cond_5 == cond_3_5:
            cond_5 += 5
fizz_buzz_test()

#On second thought, I completely forgot about the '%' operator.
#Here is another solution. First, a small range test to confirm the result.
def fizz_buzz_test_small_alt():

    for i in range(1,21):
        if (i % 15) == 0:
            print('FizzBuzz')
        elif (i % 3) == 0:
            print('Fizz')
        elif (i % 5) == 0:
            print('Buzz')
        else:
            print(i)
#fizz_buzz_test_small_alt()

#Now, the full alternative version.
def fizz_buzz_test_alt():

    for i in range(1,101):
        if (i % 15) == 0:
            print('FizzBuzz')
        elif (i % 3) == 0:
            print('Fizz')
        elif (i % 5) == 0:
            print('Buzz')
        else:
            print(i)
fizz_buzz_test_alt()
