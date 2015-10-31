import math
import time

def non_abundant_sums():
    abundants = abundant_numbers(28123)
    non_abundants = 0

    for num in range(1, 28124):
        add = True
        for component in range(12, num / 2 + 1):
            if component in abundants and num - component in abundants:
                add= False

        if add:
            non_abundants += num

    return non_abundants


def abundant_numbers(max_num):
    abundants = {}

    for number in range(12, max_num):
        if sum_of_divisors(number) > number:
            abundants[number] = True

    return abundants

def sum_of_divisors(num):
    factors = 1
    sqrt = math.sqrt(num)
    for divisor in range(2, int(sqrt) + 1):
        if num % divisor == 0:
            factors += divisor + num / divisor
    if sqrt == int(sqrt):
        factors -= sqrt

    return factors

def non_abundant_sums_faster():
    abundants = set()
    non_abundants = 0

    for num in range(1, 28124):
        if sum_of_divisors(num) > num:
            abundants.add(num)

        add = True
        for a in abundants:
            if num - a in abundants:
                add = False
                break

        if add:
            non_abundants += num

    return non_abundants

# start = time.time()
# print non_abundant_sums()
# print time.time() - start

start = time.time()
print non_abundant_sums_faster()
print time.time() - start
