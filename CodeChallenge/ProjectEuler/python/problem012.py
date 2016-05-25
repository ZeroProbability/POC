#!/usr/bin/env python
# encoding: utf-8
from math import sqrt


def read_test_cases():
    number_of_tests=int(raw_input())
    test_cases=[int(raw_input()) for x in xrange(number_of_tests)]
    return test_cases

def find_factors(n):
    sum_up=n*(n+1)/2
    for i in xrange(1, int(sqrt(sum_up))+1):
        if sum_up % i == 0:
            yield i
            if sum_up > 1: 
                yield sum_up/i

def check(n):
    i = 0
    while True:
        i += 1
        divisors=list(find_factors(i))
        if(len(divisors) > n):
            print max(divisors)
            break

def main():
    for n in read_test_cases():
        check(n)

if __name__ == '__main__':
    main()

#------------------------------------------------------------------------

def test_something():
    assert 1 == 2
