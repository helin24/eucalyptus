def letter_count(max_num):
    translate = {1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8, 20:6, 30:6, 40:5, 50:5, 60:5, 70:7, 80:6, 90:6, 100:7, 1000:8}

    total = 0

    for num in range(1, max_num + 1):
        value = 0
        thousands = num / 1000
        remainder = num % 1000
        if thousands > 0:
            value += translate[1000] + translate[thousands]

        hundreds = remainder / 100
        remainder = remainder % 100

        if hundreds > 0:
            value += translate[100] + translate[hundreds]
            if remainder > 0:
                value += 3 # for 'and'

        tens = remainder / 10

        if tens > 1:
            value += translate[tens * 10]
            remainder = remainder % 10
            if remainder > 0:
                value += translate[remainder]
        else:
            if remainder > 0:
                value += translate[remainder]

        print "total value of num %s is %s" % (num, value)
        total += value

    return total


print letter_count(1000)
