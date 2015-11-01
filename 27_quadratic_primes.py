import time

cache = {}
non_primes = {}

def best_coefficients(limit):
    max_count, max_a, max_b = 0, 0, 0
    for a in range(-limit, limit):
        for b in range(0, limit):
            if not is_prime(abs(b)):
                continue
            count = 0
            num = 0
            while True:
                if is_prime(num * num + a * num + b):
                    count += 1
                    num += 1
                else:
                    break
            if count > max_count:
                max_count, max_a, max_b = count, a, b

    return max_a * max_b, max_a, max_b

def is_prime(num):
    factor = 2
    if num < 0:
        return False
    if num in cache:
        return cache[num]
    while factor**2 <= num:
        if num % factor == 0:
            cache[num] = False
            return False
        factor += 1

    cache[num] = True
    return True

start = time.time()
print best_coefficients(1000)
print time.time() - start
