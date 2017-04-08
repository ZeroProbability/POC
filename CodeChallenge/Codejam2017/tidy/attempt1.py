#!/usr/bin/env python
# encoding: utf-8

from numba import jit


def main():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        s = int(raw_input())
        print "Case #{}: {}".format(i, prevtidy(s))

@jit
def istidy(n):
    if n < 10: return True
    ns = str(n)
    i1 = int(ns[0])
    i2 = int(ns[1])
    if n < 100:
        return i1 <= i2
    if i1 <= i2:
        return istidy(int(ns[1:]))

    return False

@jit
def prevtidy(n):
    ni = n
    while True:
        if istidy(ni):
            return ni
        ni -= 1

if __name__ == '__main__':
    main()

#------------------------------------------------------------------------

def test_istidy():
    assert istidy(7) 
    assert istidy(17) 
    assert not istidy(71) 
    assert istidy(123) 
    assert istidy(555) 
    assert istidy(224488) 
    assert not istidy(321) 
    assert not istidy(884422) 
    assert istidy(112233445566778899) 

def test_prevtidy():
    assert prevtidy(7) == 7
    assert prevtidy(32) == 29
    assert prevtidy(132) == 129
    assert prevtidy(1000) == 999
    assert prevtidy(111111111111111110) == 99999999999999999
