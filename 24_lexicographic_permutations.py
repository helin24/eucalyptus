# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 9 8 
# 0 1 2 3 4 5 6 8 7 9
# 0 1 2 3 4 5 6 8 9 7
# 0 1 2 3 4 5 6 9 7 8
# 0 1 2 3 4 5 6 9 8 7
# 0 1 2 3 4 5 7 6 8 9
# 0 1 2 3 4 5 7 6 9 8
# 0 1 2 3 4 5 7 8 6 9
# 0 1 2 3 4 5 7 8 9 6
# 0 1 2 3 4 5 7 9 6 8
# 0 1 2 3 4 5 7 9 8 6
# 
# 10th digit changes every 1
# 9th digit changes every 1
# 8th digit changes every 2 (2!)
# 7th digit changes every 6 (3!)
# 6th digit changes every 24 (4!)
# 5th digit changes every 120 (5!)
# 4th digit changes every 6!
# 3rd digit changes every 7!
# 2nd digit changes every 8!
# 1st digit changes every 9!
import math
import time

def nth_permutation(digits, num):
    size = len(digits)
    permutation = ''

    for place in range(1, size + 1):
        switches_every = math.factorial(size - place)
        current_digit_index = (num - 1) / switches_every
        if current_digit_index < 0:
            current_digit_index += len(digits)
        permutation = permutation + str(digits[current_digit_index])
        num = num % switches_every
        digits = digits[:current_digit_index] + digits[current_digit_index + 1:]

    return permutation

start = time.time()
print nth_permutation([0,1,2,3,4,5,6,7,8,9], 1000000)
print time.time() - start




