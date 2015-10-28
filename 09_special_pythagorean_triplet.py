import math

def triplet_product():
    for a in range(1, 999):
        found = False
        for b in range(1, 1000 - a):
            sum_sq = a**2 + b**2
            c = math.sqrt(sum_sq)
            if c == int(c):
                if a + b + c == 1000:
                    found = True
                    break

        if found:
            break
    
    return a * b * c, a, b, c

print triplet_product()

