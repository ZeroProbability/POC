#!/usr/bin/env python
# encoding: utf-8
from math import sqrt
from itertools import imap

def read_test_cases():
    number_of_tests=int(raw_input())
    test_cases=[int(raw_input()) for x in xrange(number_of_tests)]
    return test_cases

def generate_factors(n):
    if n == 1:
        yield 1
    else:
        for i in xrange(1, int(sqrt(n))+1):
            if n % i == 0:
                yield i
                if n/i > i : 
                    yield n/i

def sum_up_to(n):
    return n * (n + 1) / 2

def main():
    for n in count(1):
        sum = sum_up_to(n)
        factors = imap(generate_factors, sums)
        collected_factors = imap(list, factors)
        print map(len, list(collected_factors))

if __name__ == '__main__':
    main()

#------------------------------------------------------------------------

def test_something():
    assert list(generate_factors(1)) == [1]
    assert list(generate_factors(3)) == [1, 3]
    assert set(generate_factors(10)) == set([1, 2, 5, 10])
    assert set(generate_factors(12)) == set([1, 2, 3, 4, 6, 12])

