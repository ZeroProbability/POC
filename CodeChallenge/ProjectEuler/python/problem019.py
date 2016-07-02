#!/usr/bin/env python
# encoding: utf-8
from datetime import date

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
    """ start_date and end_date as (yyyy, mm, dd) """
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
    else:
        for m in xrange(month1 + 2, month2):
            days_count += days_in_month(m, year2)

    days_count += days_in_month(month1, year1) - day1 + 1
    days_count += day2 

    return days_count

def main():
    for start_date, end_date in read_test_cases():
        print days_between(start_date, end_date)

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
    assert days_between((1900, 1, 1), (1900, 1, 1)) == 0
