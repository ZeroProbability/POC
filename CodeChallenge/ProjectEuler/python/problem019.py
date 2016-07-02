#!/usr/bin/env python
# encoding: utf-8
from datetime import date

def read_test_cases():
    number_of_tests=int(raw_input())
    for _ in xrange(number_of_tests):
        start_date = map(int, raw_input().split())
        end_date = map(int, raw_input().split())
        yield start_date, end_date

def days_between(start_date, end_date):
    """ start_date and end_date as (yyyy, mm, dd) """
    year1, month1, day1 = start_date
    year2, month2, day2 = end_date

    return 10

def main():
    for start_date, end_date in read_test_cases():
        print days_between(start_date, end_date)


if __name__ == '__main__':
    main()

#-------------------------------------------------------------------------------

def test_date_diff():
    assert days_between((1900, 1, 1), (1901, 1, 1)) == 365
