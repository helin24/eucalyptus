def sundays(beg_year, end_year):
    days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

    date = 1
    month = 1
    weekday = 1
    year = 1900

    max_months = 12
    max_weekday = 7

    first_sundays = 0

    while year <= end_year:
        max_days = days_in_month[month]
        if month == 2:
            if year % 4 == 0 and year % 100 > 0 or year % 400 == 0:
                max_days = 29

        if weekday == max_weekday:
            if date == 1 and year >= beg_year:
                first_sundays += 1
            weekday = 1
        else:
            weekday += 1
        
        if date == max_days:
            date = 1
            if month == max_months:
                month = 1
                year += 1
            else:
                month += 1
        else:
            date += 1

    return first_sundays


def simpler_sundays(beg_year, end_year):
    days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

    month = 1
    year = 1900
    days_passed = 1
    first_sundays = 0

    while year <= end_year:
        if days_passed % 7 == 0 and year >= beg_year:
            first_sundays += 1

        add_days = days_in_month[month]
        if month == 2 and (year % 4 == 0 and year % 100 > 0 or year % 400 == 0):
            add_days = 29

        days_passed += add_days

        if month == 12:
            month = 1
            year += 1
        else:
            month += 1

    return first_sundays


# print sundays(1901, 2000)
print simpler_sundays(1901, 2000)
