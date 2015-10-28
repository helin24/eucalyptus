def sum_primes(max_num):
    sieve = range(0, max_num)
    index = 2
    total_sum = 0

    while index < max_num:
        if sieve[index] == None:
            index += 1
            continue

        total_sum += index
        delete = index * 2

        while delete < max_num:
            sieve[delete] = None
            delete += index

        index += 1

    return total_sum

print sum_primes(2000000)


