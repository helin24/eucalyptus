import time

def pandigital_products():
    check = range(1, 10)
    pandigitals = set()
    for smaller in range(2, 100):
        for larger in range(1000 / smaller, 10000 / smaller + 1):
            product = smaller * larger
            digits = sorted(int(x) for x in str(smaller) + str(larger) + str(product))
            if digits == check:
                pandigitals.add(product)

    return sum(x for x in pandigitals)


start = time.time()
print pandigital_products()
print time.time() - start

