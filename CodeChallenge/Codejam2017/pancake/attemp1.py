#!/usr/bin/env python
# encoding: utf-8

from numba import jit

def single_line_tests():
    with open('testcase.txt', 'r') as test_file:
        lines=test_file.read().splitlines()
        number_of_tests=lines[0]
        individual_tests=lines[1:]
        return (number_of_tests, individual_tests)

@jit
def invert(inputStr, i, k):
    inputList = list(inputStr)
    for i1 in xrange(i, i + k):
        if inputList[i1] == '+':
            inputList[i1] = '-'
        else:
            inputList[i1] = '+'
    return ''.join(inputList)

def flip(inputStr, k):
    l = len(inputStr)
    count = 0
    for i in xrange(0, l - k + 1):
        if inputStr[i] == '-':
            count += 1
            inputStr = invert(inputStr, i, k)
            print inputStr
    return count


#------------------------------------------------------------------------

def test_invert():
    assert invert('+++', 0, 3) == '---'
    assert invert('+-++', 0, 3) == '-+-+'
    assert invert('---+++', 3, 3) == '------'
    assert invert('---+++', 4, 1) == '---+-+'

def test_something():
    res = flip('---+-++-', 3)
    assert res == 3
