#!/usr/bin/env python
# encoding: utf-8

from numba import jit
import heapq

def main():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        s = int(raw_input())
        print "Case #{}: {}".format(i, prevtidy(s))

def split_list(l):
    heapq.nlargest(1, l)

if __name__ == '__main__':
    main()

#------------------------------------------------------------------------

def test_find_untidy_digit():
    assert split_list() < 0

