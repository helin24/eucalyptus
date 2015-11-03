import time

def distinct_powers(max_num):
    distinct_powers = {}

    total_combinations = 0

    for num in range(2, max_num + 1):
        if num in distinct_powers:
            total_combinations += max_num - len(distinct_powers[num]) - 1
        else:
            total_combinations += max_num - 1

        power = num * num
        index = 2
        while power <= max_num:
            if power in distinct_powers:
                repeats = distinct_powers[power]
            else:
                repeats = {}
            for j in range(2, index + 1):
                exp = j - 1
                while exp <= max_num * (j - 1) / index:
                    if exp > 1:
                        repeats[exp] = True
                    exp += j - 1

            distinct_powers[power] = repeats
            power *= num
            index += 1

    return total_combinations

def brute_force(max_num):
    distinct = {}

    count = 0
    for num in range(2, max_num + 1):
        for power in range(2, max_num + 1):
            if num ** power not in distinct:
                distinct[num ** power] = True
                count += 1
    return count

start = time.time()
print distinct_powers(100)
print time.time() - start
start = time.time()
print brute_force(100)
print time.time() - start


