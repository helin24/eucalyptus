def longest_under(n):
    max_count = 0
    max_num = 0
    known_counts = {1:1}

    for num in range(2, n):
        attempt = num
        count = 0
        while True:
            if attempt in known_counts:
                count += known_counts[attempt]
                break
            count += 1
            attempt = collatz(attempt)

        known_counts[num] = count

        if count > max_count:
            max_count = count
            max_num = num

    return max_count, max_num

def collatz(num):
    if num % 2 == 0:
        return num / 2
    else:
        return num * 3 + 1

print longest_under(1000000)
