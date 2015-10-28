def even_fib(max_num):
    even_sum = 0

    prev_num = 1
    num = 1
    while num < max_num:
        new_num = prev_num + num
        num, prev_num = new_num, num
        
        if num % 2 == 0:
            even_sum += num

    return even_sum

print even_fib(4000000)
        
