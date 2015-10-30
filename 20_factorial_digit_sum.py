import math

def factorial_digit_sum(number):
    factorial = str(math.factorial(number))

    digits = list(factorial)

    return sum(int(x) for x in digits)


print factorial_digit_sum(100)
    
