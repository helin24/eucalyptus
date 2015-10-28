def largest_palindrome_product(digits):
    factors = range(10 ** (digits - 1), 10 ** (digits))
    start = 10 ** digits - 1
    end = 10 ** (digits - 1)
    num = start
    second_num = start
    max_palindrome = 0
    
    while num >= end:
        while second_num >= max(max_palindrome / num, end):
            product = num * second_num
            if is_palindrome(product) and product > max_palindrome:
                max_palindrome = product
                break
            else:
                second_num -= 1
        num -= 1
        second_num = num

    return max_palindrome

    

def is_palindrome(num):
    num_str = str(num)
    index = 0

    while index <= len(num_str) / 2:
        if num_str[index] != num_str[(index + 1) * -1]:
            return False
        index += 1

    return True

print largest_palindrome_product(3)
