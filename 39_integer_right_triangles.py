import math
import time

def max_triangles(max_num):
    max_triangles = 0
    max_p = 0
    perimeters = {}
    
    for i in range(1, max_num / 3 + 1):
        for j in range(i, (max_num - i) / 2 + 1):
            hyp = math.sqrt(i * i + j * j)
            if hyp == math.floor(hyp):
                perim = i + j + int(hyp)
                if perim in perimeters:
                    perimeters[perim] += 1
                else:
                    perimeters[perim] = 1
                if perimeters[perim] > max_triangles:
                    max_p = perim
                    max_triangles = perimeters[perim]

    return max_triangles, max_p

start = time.time()
print max_triangles(1000)
print time.time() - start
