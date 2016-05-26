#!/usr/bin/env python
# encoding: utf-8
import functools

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
def chain_f(n):
    if n == 1:
        return [1]
    return [n] + chain_f(f(n))

def max_chain_len_under(n):
    for i in xrange(n+1):
        chain = chain_f(i)



def read_test_cases():
    number_of_tests=int(raw_input())
    for _ in xrange(number_of_tests):
        yield int(raw_input())


def main():
    for c in read_test_cases():
        chain = chain_f(c)
        len_c = len(chain)


if __name__ == '__main__':
    main()

#------------------------------------------------------------------------

def test_something():
    assert 1 == 2
