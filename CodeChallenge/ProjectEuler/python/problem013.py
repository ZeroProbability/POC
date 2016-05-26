#!/usr/bin/env python
# encoding: utf-8

def read_test_cases():
    number_of_tests=int(raw_input())
    for _ in xrange(number_of_tests):
        yield int(raw_input())

if __name__ == '__main__':
    print str(sum(read_test_cases()))[:10]


