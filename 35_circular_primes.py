import time

def circular_primes(max_num):
    primes_hash = get_possible_primes(max_num)
    circulars = []

    for prime in primes_hash.keys():
        digits = []
        circular = True
        
        size = len(str(prime))
        remaining = prime
        for _ in range(size - 1):
            remaining, digit = divmod(remaining, 10)
            remaining = remaining + digit * 10 ** (size - 1)
            if remaining not in primes_hash:
                circular = False
                break

        if circular:
            circulars.append(prime)

    print circulars
    return len(circulars)


def get_possible_primes(max_num):
    possible = range(2, max_num)
    primes = {}
    index = 0
    while index < max_num - 2:
        current_num = possible[index]
        if current_num:
            delete = index + current_num
            while delete < max_num - 2:
                possible[delete] = None
                delete += current_num
            primes[current_num] = True
        index += 1

    return primes

start = time.time()
print circular_primes(1000000)
print time.time() - start
