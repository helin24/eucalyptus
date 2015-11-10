import time

# must have digits 1-9
# using some n.. 1, 2 .. n  where n > 1
# if n = 2 then number must be between 5000 and 10000
# if n = 3 then number must be between 100 and 333
# if n = 4 then number must be digits 2 2 2 3 between 25 - 33
# if n = 5 then number must be digits 1 2 2 2 2 .. between 5-10
# if n = 6 then number must be digits 1 1 2 2 2 2  between 1-4
# if n = 7 then number must be digits 1 1 1 1 1 2 2

def largest_in_range_with_n(lower, upper, n):
    largest_pan = 0
    for num in range(lower, upper + 1):
        digits = {}
        pan = True
        joined_number = ''
        for multiplier in range(1, n + 1):
            product = num * multiplier
            remaining = product
            while remaining > 0:
                remaining, d = divmod(remaining, 10)
                if d in digits or d == 0:
                    pan = False
                    break
                else:
                    digits[d] = True
            if not pan:
                break
            joined_number = joined_number + str(product)
        if pan and int(joined_number) > largest_pan:
            largest_pan = int(joined_number)

    return largest_pan

start = time.time()
print largest_in_range_with_n(5000, 9999, 2)
intermediate = time.time()
print intermediate - start
print largest_in_range_with_n(5, 9, 5)
print time.time() - start
print time.time() - intermediate

