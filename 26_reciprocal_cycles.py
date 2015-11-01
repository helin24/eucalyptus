import time

def longest_cycle(max_num):
    longest = 0
    for num in range(2, max_num):

        remainders = {}
        numerator = 10
        digit = 1
        rem = num

        while rem not in remainders:
            remainders[rem] = digit
            rem = numerator % num
            if rem == 0:
                break

            numerator = rem * 10
            digit += 1

        if rem == 0:
            cycle = 0
        else:
            cycle = digit - remainders[rem]

        if cycle > longest:
            max_num = num
            longest = cycle

    return max_num, longest

start = time.time()
print longest_cycle(1000)
print time.time() - start
