def fibonacci_index(digits):
    min_num = 10**(digits - 1)

    first = 1
    current = 1
    index = 2

    while current < min_num:
        new = first + current
        first = current
        current = new
        index += 1

    return index

print fibonacci_index(1000)
