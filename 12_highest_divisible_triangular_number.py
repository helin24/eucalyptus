import math

def first_with_n_divisors(n):
    triangular = 0
    num = 1

    while True:
        triangular += num
        factors = 0

        factor = 1
        sqrt = math.sqrt(triangular)
        while factor < int(sqrt) + 1:
            if triangular % factor == 0:
                factors += 2
            factor += 1
            if sqrt == int(sqrt):
                factors -= 1
            

        if factors >= n:
            break

        num += 1

    return triangular

# better answer would use http://mathforum.org/library/drmath/view/55843.html

print first_with_n_divisors(500)
