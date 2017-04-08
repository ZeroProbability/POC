#!/usr/bin/env python
# encoding: utf-8

from numba import jit

def main():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        s = int(raw_input())
        print "Case #{}: {}".format(i, prevtidy(s))

@jit
def find_untidy_digit(n):
    if n < 10: return -1
    ns = str(n)
    l = len(ns)
    for i in xrange(l - 1):
        i1 = int(ns[i])
        i2 = int(ns[i+1])
        if i1 > i2:
            return i

    return -1

@jit
def prevtidy(n):
    ni = n
    while True:
        dl = find_untidy_digit(ni)
        if dl < 0:
            return ni
        ni = decrementdigit(n, dl)

def decrementdigit(n, i):
    ns = str(n)
    l = len(ns)
    nn = ns[:i] + str(int(ns[i]) - 1) + (l-i-1)*'9'
    return int(nn)

if __name__ == '__main__':
    main()

#------------------------------------------------------------------------

def test_find_untidy_digit():
    assert find_untidy_digit(7) < 0
    assert find_untidy_digit(17) < 0
    assert find_untidy_digit(71) == 0
    assert find_untidy_digit(123) < 0
    assert find_untidy_digit(555) < 0
    assert find_untidy_digit(224488) < 0
    assert find_untidy_digit(321) == 0
    assert find_untidy_digit(884422) == 1
    assert find_untidy_digit(112233445566778899) < 0
    assert find_untidy_digit(12340000) == 3

def test_decrementdigit():
    assert decrementdigit(110, 1) == 109
    assert decrementdigit(132, 1) == 129
    assert decrementdigit(109, 0) == 99

def test_prevtidy():
    assert prevtidy(7) == 7
    assert prevtidy(32) == 29
    assert prevtidy(132) == 129
    assert prevtidy(1000) == 999
    assert prevtidy(111111111111111110) == 99999999999999999
