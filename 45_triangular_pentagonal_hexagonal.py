import time

def matching():

  # all hexagonal numbers are triangular
  # h represents hexagonal index, t represents triangle index
  # h = 2t - 1
  # (2t - 1)(2t - 1 + 1) / 2
  # (2t - 1)(2t) / 2
  # t(2t - 1)

  pen_n = 166
  hex_n = 143

  pentagon = pentagonal(pen_n)
  hexagon = hexagonal(hex_n)

  while pentagon != hexagon:
    if pentagon <= hexagon:
      pen_n += 1
      pentagon = pentagonal(pen_n)
    else:
      hex_n += 1
      hexagon = hexagonal(hex_n)

  return pentagon


def pentagonal(n):
  return n * (3 * n - 1) / 2

def hexagonal(n):
  return n * (2 * n - 1)

start = time.time()
print matching()
print time.time() - start
