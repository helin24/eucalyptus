import math

def nth_prime(n):
    max_bound = (n + 1) * (math.log(n + 1) + math.log(math.log(n + 1)))
    index = 3
    last_prime = 2
    prime_n = 1
    all_nums = range(0, int(max_bound) + 1)
    
    while prime_n <= n:
        if all_nums[index] == None:
            index += 1
            continue

        prime_n += 1
        last_prime = index
        delete = index * 2

        while delete <= max_bound:
            all_nums[delete] = None
            delete += index

        index += 1

    return last_prime


print nth_prime(10001)
