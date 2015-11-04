import time
import itertools

def sum_of_fifth_powers():
    # max number is less than 999999 because 9**5 * 6 is less than that number
    total = 0
    combinations = itertools.combinations_with_replacement(range(10), 6)
    for c in combinations:
        fifth_sum = sum(x**5 for x in c)
        ordered_digits = sorted([int(x) for x in '0' * (6 - len(str(fifth_sum))) + str(fifth_sum)])
        if list(c) == ordered_digits:
            total += fifth_sum

    return total - 1

start = time.time()
print sum_of_fifth_powers()
print time.time() - start
