import time

def sum_of_fifth_powers():
    # max number is less than 999999 because 9**5 * 6 is less than that number
    total = 0
    for num in range(2, 300000):
        digits = [int(x) for x in list(str(num))]
        if sum(x**5 for x in digits) == num:
            total += num

    return total

start = time.time()
print sum_of_fifth_powers()
print time.time() - start
