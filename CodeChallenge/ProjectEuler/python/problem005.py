#!/usr/bin/env python
# encoding: utf-8
import math

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

def factors_dict(n):
    factors_dict = {}
    prime_factors = list(generate_prime_factors(n))
    for f in prime_factors:
        if factors_dict.has_key(f):
            factors_dict[f] += 1 
        else:
            factors_dict[f] = 1
    return factors_dict

def add_factors(previous_factors_dict, new_factors_dict):
    for key in new_factors_dict.keys():
        if previous_factors_dict.has_key(key):
            previous_factors_dict[key] = max(previous_factors_dict[key], new_factors_dict[key])
        else:
            previous_factors_dict[key] = new_factors_dict[key]

    return previous_factors_dict


def read_test_cases():
    number_of_tests=int(raw_input())
    test_cases=[int(raw_input()) for x in xrange(number_of_tests)]
    return test_cases

if __name__ == '__main__':
    for test_case in read_test_cases():
        full_factors_dict={}
        for i in xrange(2, test_case+1):
            full_factors_dict = add_factors(full_factors_dict, factors_dict(i))
        print reduce(lambda y, x: x[0]**x[1] * y, full_factors_dict.items(), 1)

