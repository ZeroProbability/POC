#!/usr/bin/env python
# encoding: utf-8

def find_max(n, k, big_int):
    big_int = str(big_int)
    n = int(n)
    k = int(k)

    max_p = 0
    for s in xrange(n - k + 1):
        v = list(big_int[s:s+k])
        v = [int(x) for x in v]
        m = reduce(lambda p, i: p * i, v, 1)
        if m > max_p:
            max_p = m

    print max_p

def read_test_cases():
    number_of_tests=int(raw_input())
    test_cases=[(raw_input().split(), raw_input()) for x in xrange(number_of_tests)]
    return test_cases

def main():
    for i in read_test_cases():
        ((n, k), big_int) = i
        find_max(n, k, big_int)

if __name__ == '__main__':
    main()
