def lowest_denominator():
    numerator, denominator = 1, 1
    for i in range(10, 100):
        if i % 10 == 0:
            continue
        for j in range(i + 1, 100):
            if j % 10 == 0:
                continue
            if str(i)[0] == str(j)[1]:
                if 1.0 * i / j == 1.0 * (i % 10) / (j / 10):
                    numerator *= i % 10
                    denominator *= j / 10
            elif str(i)[1] == str(j)[0]:
                if 1.0 * i / j == 1.0 * (i / 10) / (j % 10):
                    numerator *= i / 10
                    denominator *= j % 10

    common_factor = lcf(numerator, denominator)
    return numerator / common_factor, denominator / common_factor

def lcf(a, b):
    lcf = 1
    largest_possible = min(a, b)
    i = 2
    while i <= largest_possible:
        if a % i == 0 and b % i == 0:
            a /= i
            b /= i
            lcf *= i
        else:
            i += 1

    return lcf

    

print lowest_denominator()

