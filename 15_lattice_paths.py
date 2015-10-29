import math

def lattice_paths(size):
    return math.factorial(size * 2) / (math.factorial(size)**2)

print lattice_paths(20)
