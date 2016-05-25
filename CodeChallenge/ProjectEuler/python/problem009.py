#!/usr/bin/env python
# encoding: utf-8

def find_result(n):
    max_p = -1
    for a in xrange(1, n/3):
        b = int((n*n/2 - n * a ) / (n - a))
        if a * a + b * b == (n-a-b)**2:
            new_v = a * b * (n - a - b)
            if new_v > max_p:
                max_p = new_v
    return max_p

def read_test_cases():
    number_of_tests=int(raw_input())
    test_cases=[int(raw_input()) for x in xrange(number_of_tests)]
    return test_cases

def main():
    for tc in read_test_cases():
        print find_result(tc)

if __name__ == '__main__':
    main()
