def distinct_powers(max_num):
    distinct_powers = {}

    total_combinations = 0

    for num in range(2, max_num + 1):
        if num in distinct_powers:
            total_combinations += max_num - distinct_powers[num]
        else:
            total_combinations += max_num - 2 + 1

        power = num * num
        index = 2
        while power <= max_num:
            if index % 2 == 0:
                distinct_powers[power] = max_num / index
            # don't kno whow to account for every other power of 8 covered by 8 (e.g.) programmatically
            distinct_powers[power] = max_num / index
            power *= num
            index += 1

    print distinct_powers
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

print distinct_powers(100)
print brute_force(100)


