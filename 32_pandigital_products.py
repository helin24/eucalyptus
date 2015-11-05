def pandigital_products():
    check = range(1, 10)
    pandigitals = set()
    for smaller in range(2, 100):
        for larger in range(1000 / smaller, 10000 / smaller + 1):
            product = smaller * larger
            digits = sorted([int(x) for x in list(str(smaller))] + [int(x) for x in list(str(larger))] + [int(x) for x in list(str(product))])
            if digits == check:
                pandigitals.add(product)

    return sum(x for x in pandigitals)



print pandigital_products()

