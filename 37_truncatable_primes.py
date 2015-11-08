def sum_truncatables():
    primes, truncatables = {}, {}
    numbers = range(2,1000000)
    index = 0
    count = 0

    while index < 999998 and count < 14:
        current_num = numbers[index]
        if not current_num:
            index += 1
            continue

        primes[current_num] = True
        j = index + current_num
        while j < 999998:
            numbers[j] = None
            j += current_num

        if current_num < 10:
            index += 1
            continue

        truncatable = True
        remove_from_left = 0
        multiplier = 1
        test_num = current_num
        while test_num > 10:
            test_num, remainder = divmod(test_num, 10)
            remove_from_right = test_num
            remove_from_left = remainder * multiplier + remove_from_left


            if remove_from_right not in primes or remove_from_left not in primes:
                truncatable = False
                break

            multiplier *= 10

        if truncatable:
            truncatables[current_num] = True
            count += 1
            
        index += 1

    return sum(truncatables.keys())




        
print sum_truncatables()
