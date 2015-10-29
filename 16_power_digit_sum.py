import time

def sum_of_digits(power):
    x = 2**power
    xlist = str(x)
    return sum(int(x) for x in xlist)

start = time.time()
print sum_of_digits(1000)
print time.time() - start
