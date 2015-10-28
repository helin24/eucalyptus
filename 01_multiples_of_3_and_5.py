def multiple(num):
    total_sum = 0
    
    for n in range(1, num):
        if n % 3 == 0 or n % 5 == 0:
            total_sum += n

    return total_sum

print multiple(1000)
