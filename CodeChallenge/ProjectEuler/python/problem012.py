#!/usr/bin/env python
# encoding: utf-8
from math import sqrt
from itertools import imap,count

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

global_cache = {}
def find_number_with(max_factor_count):
    if global_cache.get(max_factor_count):
        return global_cache[max_factor_count]

    for n in count(1):
        sum_n = sum_up_to(n)
        factors = list(generate_factors(sum_n))

        len_f = len(factors)
        print 'got here ', len_f-1, sum_n
        if not global_cache.get(len_f-1):
            mk  = max([0] + global_cache.keys())
            for k in set(range(len_f)) - set(global_cache.keys()):
                global_cache[k] = sum_n
            print global_cache

        #print global_cache

        if len(factors) > max_factor_count:
            return sum_n

if __name__ == '__main__':
    for c in read_test_cases():
        print find_number_with(c)

#------------------------------------------------------------------------

def test_something():
    assert list(generate_factors(1)) == [1]
    assert list(generate_factors(3)) == [1, 3]
    assert set(generate_factors(10)) == set([1, 2, 5, 10])
    assert set(generate_factors(12)) == set([1, 2, 3, 4, 6, 12])

