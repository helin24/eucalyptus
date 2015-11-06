import math
import itertools

def sum_palindromes(max_num):
    # 0         0
    # 1         1
    # 11        3       2^1 + 1
    # 101       5       2^2 + 1
    # 111       7       2^3 - 1
    # 1001      9       2^3 + 1
    # 1111      15      2^4 - 1
    # 10001     17      2^4 + 1
    # 10101     21      2^4 + 2^2 + 1
    # 11011     27      2^4 + 2^3 + 2^2 - 1
    # 11111     31      2^5 - 1
    # 100001    33      2^5 + 1
    # 101101    45      2^5 + 2^3 + 2^2 + 2^0
    # 110011    51      2^5 + 2^4 + 2^1 + 2^0

    palindromes = [1, 3]

    for power in range(2, int(math.log(max_num, 2)) + 1):
        print "power of 2 is now %s" % (power)
        digits = power + 1
        if digits % 2 == 0:
            changeable_digits = max(digits / 2 -1, 0)
        else:
            changeable_digits = digits / 2

        permutations = itertools.product(['0','1'], repeat = changeable_digits)
        for p in permutations:
            if digits % 2 == 0:
                bin_num = '1' + ''.join(p) + ''.join(reversed(p)) + '1'
            else:
                bin_num = '1' + ''.join(p) + ''.join(reversed(p[:-1])) + '1'

            if is_palindrome(str(int(bin_num, 2))) and int(bin_num, 2) < max_num:
                print bin_num
                print int(bin_num, 2)
                palindromes.append(int(bin_num, 2))

    return sum(palindromes)


def is_palindrome(string):
    p = True
    for index in range((len(string) - 1) / 2 + 1):
        if string[index] != string[-1 - index]:
            return False

    return p

print sum_palindromes(1000000)




