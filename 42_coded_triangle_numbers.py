import time
import math

def triangle_count(filename):
    f = open(filename)
    long_str = f.read()
    triangles = 0
    for word in long_str.split(','):
        if is_triangle(word_value(word[1:-1])):
            triangles += 1
    return triangles

def is_triangle(value):
    n = int(math.floor(math.sqrt(value)))
    while True:
        test = n * (n + 1) / 2
        if test == value:
            return True
        elif test > value:
            return False
        n += 1
    

def word_value(word):
    value = 0
    for char in word:
        value += ord(char) - ord('A') + 1

    return value

print triangle_count('p042_words.txt')
