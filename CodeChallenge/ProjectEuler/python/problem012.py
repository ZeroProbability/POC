#!/usr/bin/env python
# encoding: utf-8
import math 
from collections import Counter

def read_test_cases():
    number_of_tests=int(raw_input())
    test_cases=[int(raw_input()) for x in xrange(number_of_tests)]
    return test_cases

def generate_prime_factors(n):
    while n % 2 == 0:
        yield 2
        n /= 2

    upto = int(math.sqrt(n)) + 1
    for i in xrange(3, upto, 2):
        while n % i == 0:
            yield i
            n /= i

    if n > 1:
        yield n

def factor_count(n):
    if n == 1:
        return 1
    exps = map(lambda x: x+1, Counter(generate_prime_factors(n)).values())
    return reduce(lambda x, v: x*v, exps, 1)

def sum_up_to(n):
    return n * (n+1) / 2

global_cache = {}

def answer_for(max_factor_count):
    if global_cache.get(max_factor_count):
        return global_cache.get(max_factor_count)

    i = max([1] + global_cache.keys())

    while True:
        sum_up = sum_up_to(i)
        factor_count_of_sum = factor_count(sum_up)

        if not global_cache.get(factor_count_of_sum-1):
            mk  = max([0] + global_cache.keys())
            for k in set(range(factor_count_of_sum)) - set(global_cache.keys()):
                global_cache[k] = sum_up
            #print global_cache
        
        if factor_count_of_sum > max_factor_count:
            return sum_up
        i += 1

if __name__ == '__main__':
    for c in read_test_cases():
        print answer_for(c)


#------------------------------------------------------------------------

def test_something():
    assert factor_count(1) == 1
    assert factor_count(2) == 2
    assert factor_count(3) == 2
    assert factor_count(10) == 4
    assert factor_count(72) == 12

