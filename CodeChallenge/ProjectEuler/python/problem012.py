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

global_cache = {}

def check(n):
    i = 1
    if global_cache.get(n):
        return global_cache.get(n)[1]
    else:
        i = max([0]+ map(lambda x: x[0], global_cache.values())) 
    while True:
        divisors=list(find_factors(i))
        if(len(divisors) > n):
            global_cache[n] = (i, max(divisors))
            print global_cache[n][1]
            break
        i += 1

def main():
    for n in read_test_cases():
        check(n)

if __name__ == '__main__':
    main()

#------------------------------------------------------------------------

def test_something():
    assert 1 == 2
