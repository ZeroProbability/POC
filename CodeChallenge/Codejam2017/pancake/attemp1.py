#!/usr/bin/env python
# encoding: utf-8

from numba import jit

def main():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        s, k = raw_input().split(" ")
        print "Case #{}: {}".format(i, flip(s, int(k)))

@jit
def invert(inputStr, i, k):
    inputList = list(inputStr)
    for i1 in xrange(i, i + k):
        if inputList[i1] == '+':
            inputList[i1] = '-'
        else:
            inputList[i1] = '+'
    return ''.join(inputList)

@jit
def flip(inputStr, k):
    l = len(inputStr)
    count = 0
    for i in xrange(0, l - k + 1):
        if inputStr[i] == '-':
            count += 1
            inputStr = invert(inputStr, i, k)

    if '-' in inputStr:
        return "IMPOSSIBLE"
    return count

if __name__ == '__main__':
    main()

#------------------------------------------------------------------------

def test_invert():
    assert invert('+++', 0, 3) == '---'
    assert invert('+-++', 0, 3) == '-+-+'
    assert invert('---+++', 3, 3) == '------'
    assert invert('---+++', 4, 1) == '---+-+'

def test_something():
    res = flip('---+-++-', 3)
    assert res == 3
    res = flip('+++', 3)
    assert res == 0
    res = flip('-+-+-', 4)
    assert res == 'IMPOSSIBLE'
