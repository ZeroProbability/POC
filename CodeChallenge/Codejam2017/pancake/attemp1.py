#!/usr/bin/env python
# encoding: utf-8

def single_line_tests():
    with open('testcase.txt', 'r') as test_file:
        lines=test_file.read().splitlines()
        number_of_tests=lines[0]
        individual_tests=lines[1:]
        return (number_of_tests, individual_tests)

def flip(inputStr, k):
    l = len(inputStr)
    for i in xrange(l - k):
        if(l == 

#------------------------------------------------------------------------

def test_something():
    res = flip('---+-++-', 3)
    assert res == 3
