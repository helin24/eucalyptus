import itertools
import math
import time

def factorial_digit_sum():
    possibilities = itertools.combinations_with_replacement(range(10),7)
    sum_factorials = 0
    next(possibilities)
    next(possibilities)
    next(possibilities) # skip 0, 1, 2
    for digits in possibilities:
        factorial_sum = sum(math.factorial(digit) for digit in digits)
        zeroes = 7 - len(str(factorial_sum))
        factorial_sum -= zeroes
        if factorial_sum == sum(math.factorial(int(x)) for x in str(factorial_sum)):
            sum_factorials += factorial_sum

    return sum_factorials 

start = time.time()
print factorial_digit_sum()
print time.time() - start
