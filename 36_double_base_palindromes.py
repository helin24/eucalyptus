import math
import itertools
import time

def sum_palindromes(max_num):
    palindromes = [1, 3]

    for power in range(2, int(math.log(max_num, 2)) + 1):
        if power % 2 == 0:
            changeable_digits = power / 2
        else:
            changeable_digits = (power - 1) / 2

        permutations = itertools.product(['0','1'], repeat = changeable_digits)
        for p in permutations:
            if power % 2 == 0:
                bin_num = '1' + ''.join(p) + ''.join(reversed(p[:-1])) + '1'
            else:
                bin_num = '1' + ''.join(p) + ''.join(reversed(p)) + '1'

            if is_palindrome(str(int(bin_num, 2))) and int(bin_num, 2) < max_num:
                palindromes.append(int(bin_num, 2))

    return sum(palindromes)


def is_palindrome(string):
    p = True
    for index in range((len(string) - 1) / 2 + 1):
        if string[index] != string[-1 - index]:
            return False

    return p

start = time.time()
print sum_palindromes(1000000)
print time.time() - start




