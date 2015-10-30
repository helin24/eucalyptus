import math
import time

def amicable_sum(num):
    checked = {}
    total_sum = 0

    for current in range(2, num):
        if current in checked:
            continue

        self_d = prime_divisors_sum(current) - current
        if current == prime_divisors_sum(self_d) - self_d and current > 1 and current < num and self_d > 1 and self_d < num and self_d != current:
            print "pair of %s and %s" % (current, self_d)
            checked[self_d] = True
            checked[current] = True
            total_sum += self_d + current

        else:
            checked[self_d] = False
            checked[current] = False

    return total_sum


def divisors(num):
    factors = [1]
    sqrt = math.sqrt(num)
    if sqrt == int(sqrt):
        factors.append(int(sqrt))
        sqrt -= 1
    for divisor in range(2, int(sqrt) + 1):
        if num % divisor == 0:
            factors.extend([divisor, num / divisor])

    return factors


def prime_divisors_sum(num):
    check = 2

    instances = 0
    total_sum = 1
    while check <= num and num > 1:
        if num % check == 0:
            instances += 1
            num = num / check
        else:
            if instances > 0:
                total_sum *= ((check**(instances + 1) -1) / (check - 1))
            instances = 0
            check += 1

    if instances > 0:
        total_sum *= ((check**(instances + 1) - 1) / (check - 1))

    return total_sum


# print prime_divisors_sum(24)
start = time.time()
print amicable_sum(10000)
print time.time() - start

start = time.time()
for num in range(1, 10000):
    sum(divisors(num))
print time.time() - start

start = time.time()
for num in range(1, 10000):
    prime_divisors_sum(num)
print time.time() - start
