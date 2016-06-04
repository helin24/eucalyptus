import time

def matching():
  tri_n = 286
  pen_n = 165
  hex_n = 143

  triangle = triangular(tri_n)
  pentagon = pentagonal(pen_n)
  hexagon = hexagonal(hex_n)

  while triangle != pentagon or triangle != hexagon:
    if triangle <= pentagon and triangle <= hexagon:
      tri_n += 1
      triangle = triangular(tri_n)
    elif pentagon <= triangle and pentagon <= hexagon:
      pen_n += 1
      pentagon = pentagonal(pen_n)
    else:
      hex_n += 1
      hexagon = hexagonal(hex_n)

  return triangle


def triangular(n):
  return n * (n + 1) / 2

def pentagonal(n):
  return n * (3 * n - 1) / 2

def hexagonal(n):
  return n * (2 * n - 1)

start = time.time()
print matching()
print time.time() - start
