# encoding: utf-8

def read_test_cases():
    number_of_tests=int(raw_input())
    for _ in xrange(number_of_tests):
        start_date = map(int, raw_input().split())
        end_date = map(int, raw_input().split())
        yield start_date, end_date

def is_leap_year(year):
    if year % 4 != 0:
        return False
    if year % 100 == 0:
        return year % 400 == 0
    return True

def days_in_month(month, year):
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    if month == 2:
        return 29 if is_leap_year(year) else 28
    return 30

def days_between(start_date, end_date):
    """ start_date and end_date as (year, month, date) """
    year1, month1, day1 = start_date
    year2, month2, day2 = end_date

    days_count = 0

    for y in xrange(year1 + 1, year2):
        days_count += 366 if is_leap_year(y) else 365

    if year2 > year1:
        for m in xrange(month1 + 1, 13):
            days_count += days_in_month(m, year1)

        for m in xrange(1, month2):
            days_count += days_in_month(m, year2)

        days_count += days_in_month(month1, year1) - day1 + 1
        days_count += day2 
    else:
        if month2 > month1:
            for m in xrange(month1 + 1, month2):
                days_count += days_in_month(m, year2)

            days_count += days_in_month(month1, year1) - day1 + 1
            days_count += day2 
        elif day2 >= day1:
            days_count += (day2 - day1) + 1

    return days_count

def find_weekday(year, month, day):
    weekday_on_first_jan = 1
    for y in xrange(1901, year + 1):
        weekday_on_first_jan += 2 if is_leap_year(y-1) else 1

    days_in_that_year = 0
    for m in xrange(1, month):
        days_in_that_year += days_in_month(m, year)

    days_in_that_year += (day - 1)

    weekday = (days_in_that_year + weekday_on_first_jan) % 7

    return weekday

def first_of_each_month(start_date, end_date):
    year1, month1, day1 = start_date
    year2, month2, day2 = end_date

    start_month = month1 if day1 == 1 else month1 + 1
    end_month = month2 

    if year1 == year2:
        for m in xrange(month1+1, month2):
            yield (year1, m, 1)
    else:
        start_month = month1 if day1 == 1 else month1 + 1

        for m in xrange(start_month, 13):
            yield(year1, m, 1)

        for y in xrange(year1+1, year2):
            for m in xrange(1, 13):
                yield(y, m, 1)

        for m in xrange(1, month2+1):
            yield(year2, m, 1)

def main():
    def is_a_sunday(dt):
        v = 1 if find_weekday(*dt) == 0 else 0
        return v

    for start_date, end_date in read_test_cases():
        print sum(map(is_a_sunday, first_of_each_month(start_date, end_date)))

if __name__ == '__main__':
    main()

#-------------------------------------------------------------------------------

def test_leap_year():
    assert is_leap_year(2000)
    assert not is_leap_year(1900)
    assert not is_leap_year(1903)
    assert is_leap_year(1908)

def test_days_in_month():
    assert days_in_month(1, 2001) == 31
    assert days_in_month(2, 2001) == 28
    assert days_in_month(2, 2000) == 29
    assert days_in_month(7, 2000) == 31
    assert days_in_month(8, 2000) == 31

def test_date_diff():
    assert days_between((1900, 1, 1), (1901, 1, 1)) == 366
    assert days_between((1900, 1, 1), (1902, 1, 1)) == 366 + 365
    assert days_between((1900, 1, 1), (1903, 1, 1)) == 366 + 365 * 2
    assert days_between((1900, 1, 1), (1904, 1, 1)) == 366 + 365 * 3
    assert days_between((1900, 1, 1), (1905, 1, 1)) == 366 * 2 + 365 * 3
    assert days_between((1900, 1, 1), (1900, 2, 1)) == 32
    assert days_between((1900, 1, 1), (1900, 1, 1)) == 1

def test_weekday_on_first_jan():
    assert find_weekday(1909, 2, 1) == 1
    assert find_weekday(1900, 1, 1) == 1
    assert find_weekday(1901, 1, 1) == 2
    assert find_weekday(1902, 1, 1) == 3
    assert find_weekday(1903, 1, 1) == 4
    assert find_weekday(1904, 1, 1) == 5
    assert find_weekday(1905, 1, 1) == 0
    assert find_weekday(1900, 1, 2) == 2
    assert find_weekday(2016, 7, 2) == 6
    assert find_weekday(2000, 1, 1) == 6
