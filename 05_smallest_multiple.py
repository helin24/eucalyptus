def smallest_multiple(max_num):
    factors = range(2, max_num + 1)

    index = 0

    while index < len(factors) / 2:
        check = index + 1
        while check < len(factors):
            if factors[check] % factors[index] == 0:
                factors[check] = factors[check] / factors[index]
            check += 1
        index += 1

    product = 1
    for num in factors:
        product = product * num
    return product

print smallest_multiple(10)
print smallest_multiple(20)
