def spiral_sum(sq_size):
    total = 1
    start = 3
    additional = 12
    inc = 2

    # for size - 1 boxes
        # add is 2 * size
        # add 4 numbers each increasing by add

    for n in range(1, (sq_size) / 2 + 1):
        total += start * 4 + additional * n
        inc += 8
        start += inc

    return total

print spiral_sum(1001)
