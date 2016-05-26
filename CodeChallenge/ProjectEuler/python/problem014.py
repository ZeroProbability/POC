#!/usr/bin/env python
# encoding: utf-8
import functools
import itertools

def memoize(obj):
    cache = obj.cache = {}

    @functools.wraps(obj)
    def memoizer(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = obj(*args, **kwargs)
        return cache[key]
    return memoizer

def f(n):
    if n % 2 == 0:
        return n/2
    return 3 * n + 1

@memoize
def chain_len_of(n):
    if n == 1:
        return (1, 1)
    return (n, 1 + chain_len_of(f(n))[1])

def read_test_cases():
    number_of_tests=int(raw_input())
    for _ in xrange(number_of_tests):
        yield int(raw_input())

@memoize
def max_len_under(n):
    if n == 1:
        return (1, 1)
    for i in xrange(1, n):
        max_len_under(i)
    if chain_len_of(n)[1] >= max_len_under(n-1)[1]:
        return chain_len_of(n)
    else:
        return max_len_under(n-1)

def main():
    for c in read_test_cases():
        print max_len_under(c)[0]

if __name__ == '__main__':
    main()

#------------------------------------------------------------------------

def test_something():
    assert 1 == 2
