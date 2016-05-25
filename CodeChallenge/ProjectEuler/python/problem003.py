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


def read_test_cases():
    number_of_tests=int(raw_input())
    test_cases=[int(raw_input()) for x in xrange(number_of_tests)]
    return test_cases

if __name__ == '__main__':
    for test_case in read_test_cases():
        print list(generate_prime_factors(test_case))[-1]

