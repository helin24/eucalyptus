import math

def first_with_n_divisors(n):
    triangular = 0
    num = 1

    while True:
        triangular += num
        if triangular % 2 != 0 or triangular % 3 != 0 or triangular % 5 != 0:
            num += 1
            continue
        factors = 0

        factor = 1
        sqrt = math.sqrt(triangular)
        while factor < int(sqrt) + 1:
            if triangular % factor == 0:
                factors += 2
            factor += 1
            if sqrt == int(sqrt):
                factors -= 1
            
#        print "number %s has %s factors" % (triangular, factors)
        if factors >= n:
            break

        num += 1

    return triangular

# better answer would use http://mathforum.org/library/drmath/view/55843.html

print first_with_n_divisors(500)
