def sum_square_diff(max_num):
    all_nums = range(1, max_num + 1)

    sum_sq = sum(x**2 for x in all_nums)
    sq_sums = sum(all_nums)**2

    return sq_sums - sum_sq

print sum_square_diff(100)
