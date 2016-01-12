import math
import time
import itertools

def largest_pandigital_prime():
    digits = '7654321'
    for start in range(0, len(digits)):
        for permutation in itertools.permutations(digits[start:]):
            test = int(''.join(permutation))
            if is_prime(test):
                return test


def is_prime(num):
    if num % 2 == 0:
        return False
    sqrt = int(math.ceil(math.sqrt(num)))
    for factor in range(2, sqrt + 1):
        if num % factor == 0:
            return False

    return True

start = time.time()
print largest_pandigital_prime()
print time.time() - start