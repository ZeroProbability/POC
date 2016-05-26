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


def main():
    for c in read_test_cases():
        chain_lens = itertools.imap(chain_len_of, xrange(c, 0, -1))
        print max([x[1] for x in chain_lens])


if __name__ == '__main__':
    main()

#------------------------------------------------------------------------

def test_something():
    assert 1 == 2
