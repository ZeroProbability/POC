#!/usr/bin/env python
# encoding: utf-8
import functools
import itertools

cache = {1: 1}


def read_test_cases():
    number_of_tests=int(raw_input())
    for _ in xrange(number_of_tests):
        yield int(raw_input())

def f(n):
    if n % 2 == 0:
        return n/2
    return 3 * n + 1

def len_chain_f(n):
    if cache.get(n):
        return cache[n]
    next_n = f(n)
    if cache.get(next_n):
        cache[n] = 1 + cache[next_n]
        return cache[n]
    return 1 + len_chain_f(f(n))

def main():
    for c in read_test_cases():
        print len_chain_f(c)

if __name__ == '__main__':
    main()

#------------------------------------------------------------------------

def test_something():
    assert 1 == 2
