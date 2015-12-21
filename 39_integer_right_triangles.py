import math

def max_triangles(max_num):
    max_triangles = 0
    max_p = 0
    for p in range(1, max_num + 1):
        num_triangles = 0
        for i in range(1, p / 3 + 1):
            for j in range(i, (p - i) / 2 + 1):
                if math.sqrt(i*i + j*j) == p - i - j:
#                    print "%s and %s and %s makes right triangle" % (i, j, p - i - j)
                    num_triangles += 1
                else:
                    pass
#                    print "%s and %s and %s not right triangle" % (i, j, p - i - j)
        if num_triangles > max_triangles:
            max_triangles, max_p = num_triangles, p

    return max_triangles, max_p
    # for each perimeter from 1 to max_num:
        # for each first side (i) from 1 to 1/3 of max num:
            # for each second side from i to 1/3 of max num:
                # find what i^2 + j^2 would mean for third side. 
                # if sqrt of squares is max_num - i - j
                    # increment number of triangles


print max_triangles(1000)
