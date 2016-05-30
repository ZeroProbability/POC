#!/usr/bin/env python
# encoding: utf-8

def read_test_cases():
    number_of_tests=int(raw_input())
    for _ in xrange(number_of_tests):
        yield int(raw_input())

def sum_digits(n):
    q = 0
    while n > 0:
        q += (n%10)
        n = n // 10
    return q

def main():
    for c in read_test_cases():
        print sum_digits(2 ** c)

if __name__ == '__main__':
    main()
