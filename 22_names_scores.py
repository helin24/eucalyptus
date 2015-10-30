def total_names(txt_file):
    f = open(txt_file)
    names = f.read().split('","')
    names[0] = names[0][1:]
    names[-1] = names[-1][:-1]

    names.sort()
    ord_start = 64

    index = 0
    names_sum = 0
    while index < len(names):
        names_sum += (index + 1) * sum(ord(letter) - ord_start for letter in names[index])
        index += 1

    return names_sum


print total_names('p022_names.txt')
