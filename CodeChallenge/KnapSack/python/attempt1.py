#!/usr/bin/env python
# encoding: utf-8
import itertools

capacity = 10

weights = [1, 3, 4, 7, 9]

def possibilities():
    for itemcount in xrange(1, len(weights)+1):
        for i in itertools.combinations(weights, itemcount):
            yield sum(i), i

def filter_capacity(v):
    total, items = v
    #print total, items
    return total <= capacity

def main():
    dd = itertools.ifilter(filter_capacity, possibilities())
    print max(dd)

if __name__ == '__main__':
    main()
