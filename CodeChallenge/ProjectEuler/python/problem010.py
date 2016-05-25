#!/usr/bin/env python
# encoding: utf-8
import random

def primes_sieve(limit):
    a = range(limit)                          # Initialize the primality list
    sum_so_far = 0

    a[0] = a[1] = 0

    for (i, isprime) in enumerate(a):
        if isprime:
            leng=len(a[i*i::i])
            a[i*i::i] = [0]*leng
            sum_so_far += i
        a[i] = sum_so_far

    return a


def read_test_cases():
    number_of_tests=int(raw_input())
    test_cases=[int(raw_input()) for x in xrange(number_of_tests)]
    return test_cases

def random_test_cases():
    return [random.randint(3, 1000000) for r in xrange(1000)]

def main():
    tcs = read_test_cases()
    max_tcs=max(tcs) + 1
    ps = primes_sieve(max_tcs)
    for tc in tcs:
        print ps[tc]

if __name__ == '__main__':
    main()
