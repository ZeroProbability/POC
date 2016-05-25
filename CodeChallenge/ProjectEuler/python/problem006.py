#!/usr/bin/env python
# encoding: utf-8

def sum_of_squares(n):
    return reduce(lambda x, y: y*y + x, xrange(1, n+1), 0)

def square_of_sum(n):
    return sum(xrange(1, n+1))**2


def read_test_cases():
    number_of_tests=int(raw_input())
    test_cases=[int(raw_input()) for x in xrange(number_of_tests)]
    return test_cases

if __name__ == '__main__':
    for n in read_test_cases():
        print square_of_sum(n)-sum_of_squares(n)
