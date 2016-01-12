import time
import math

def triangle_count(filename):
    f = open(filename)
    long_str = f.read()
    triangles = 0
    for word in long_str.split(','):
        if quadratic_is_triangle(word_value(word[1:-1])):
            triangles += 1
    return triangles

def quadratic_is_triangle(value):
    n = (math.sqrt(1 + 8 * value) - 1) / 2
    return int(n) == n

def word_value(word):
    value = 0
    for char in word:
        value += ord(char) - ord('A') + 1

    return value

start = time.time()
print triangle_count('p042_words.txt')
print time.time() - start
