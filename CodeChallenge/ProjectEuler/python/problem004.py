#!/usr/bin/env python
# encoding: utf-8
import math

def is_palindrome(n):
    reversed_str=list(str(n))
    reversed_str.reverse()
    reversed_str=''.join(reversed_str)

    return str(n) == reversed_str

def three_digit_divisors(n):
    for i in xrange(100, 1000):
        if n % i == 0:
            yield i

def evaluate(n):
    if is_palindrome(n):
        for d in three_digit_divisors(n):
            other_factor = n / d
            if other_factor > 99 and other_factor < 1000:
                return n


def read_test_cases():
    number_of_tests=int(raw_input())
    test_cases=[int(raw_input()) for x in xrange(number_of_tests)]
    return test_cases

if __name__ == '__main__':
    for test_case in read_test_cases():
        for n in xrange(test_case, 1000, -1):
            v = evaluate(n)
            if v != None:
                print v
                break



