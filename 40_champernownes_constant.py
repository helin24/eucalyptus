import time

def product_of_ns(n):
    # power of 1 starts at 1
    # power of 10 starts at 10 which is (10**1 - 10**0) * 1 + 1
    # power of 100 starts at (10**2 - 10**1) * 2 + 10

    # start with a count at 1 
    # beginning number is always 1
    product = 1
    while n > 0:
        product *= int(digit(10**n))
        n -= 1

    return product

def digit(n):
    previous_digit = 0
    digit = 1
    power = 0
    while n > digit:
        power += 1
        previous_digit = digit
        digit += (10**power - 10**(power - 1)) * power
    
    numbers_after_power, which_digit = divmod(n - previous_digit, power)
    return str(10**(power - 1) + numbers_after_power)[which_digit]

start = time.time()
print product_of_ns(6)
print time.time() - start
