def largest_prime_factor(num):
    divide_by = 2
    last_factor = 1
    
    while num >= divide_by ** 2:
        if num % divide_by == 0:
            num = num / divide_by
            last_factor = divide_by
        else:
            divide_by += 1

    return num

print largest_prime_factor(13195)
print largest_prime_factor(600851475143)

