import time

def circular_primes(max_num):
    primes_hash = get_possible_primes(max_num)
    circulars = [2, 5]

    for prime in primes_hash.keys():
        digits = []
        remaining = prime
        circular = True
        
        while remaining > 0:
            remaining, digit = divmod(remaining, 10)
            if digit % 2 == 0 or digit % 5 == 0:
                circular = False
                break
            digits.append(digit)
        if not circular:
            continue

        index = len(digits) - 2
        while index >= 0:
            multiplier = 1
            num = 0 # 1 + 70 + 300  # 3 + 10 + 700
            for d in digits[index + 1:]:
                num += d * multiplier
                multiplier *= 10
            for d in digits[0:index + 1]:
                num += d * multiplier
                multiplier *= 10
#            print "checking num %s" % (num)
            if num not in primes_hash:
                circular = False
                break
            index -= 1

        if circular:
            circulars.append(prime)
        
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
