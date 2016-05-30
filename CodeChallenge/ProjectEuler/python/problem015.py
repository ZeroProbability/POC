#!/usr/bin/env python
# encoding: utf-8

def read_test_cases():
    number_of_tests=int(raw_input())
    for _ in xrange(number_of_tests):
        yield [int(i) for i in  raw_input().split()]

mx = 10**9+7

def main():
    for case in read_test_cases():
        n = max(case)
        r = min(case)
        answer = n + r
        for i in xrange(1, r):
            answer = (answer * (n+r-i) / (i+1)) 
        print answer%mx

if __name__ == '__main__':
    main()
